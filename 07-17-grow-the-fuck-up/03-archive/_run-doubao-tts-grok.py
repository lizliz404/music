#!/usr/bin/env python3
"""Doubao V3 TTS for Grok 4.5 output — strip MD tables, plain speakable text"""
import os, json, base64, re, sys, urllib.request, uuid

TEXT_PATH = "/home/ubuntu/music/07-17-grow-the-fuck-up/2026-07-17-grow-the-fuck-up-grok-4.5.txt"
OUT_PATH  = "/home/ubuntu/music/07-17-grow-the-fuck-up/2026-07-17-grow-the-fuck-up-grok-4.5.mp3"
API_URL   = "https://openspeech.bytedance.com/api/v3/tts/unidirectional"
VOICE     = "zh_female_vv_uranus_bigtts"

# Load env
env_path = os.path.expanduser("~/.hermes/.env")
if os.path.exists(env_path):
    for line in open(env_path):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ[k] = v.strip('"').strip("'")

API_KEY = os.environ.get("DOUBAO_TTS2_API_KEY")
if not API_KEY:
    print("ERROR: DOUBAO_TTS2_API_KEY not found", file=sys.stderr)
    sys.exit(1)

# ---- Load + Clean ----
raw = open(TEXT_PATH).read()

# Fix broken English words across lines (e.g. "c\nontingent")
raw = re.sub(r'([a-z])[\s\n]+([a-z])', r'\1\2', raw)

# ---- Strip MD table formatting ----
# Remove separator rows: lines that are only |, -, :, spaces
raw = re.sub(r'\n\|[-:| \t]+\|\n', '\n', raw)
# Also handle variant patterns
raw = re.sub(r'\n\|[-:\s|]+\|\n', '\n', raw)

# Now convert remaining table rows to plain text:
# "| col1 | col2 |" → "col1, col2"
def strip_table_row(line):
    line = line.strip()
    if line.startswith('|') and line.endswith('|'):
        # Split by |, strip each cell, filter empties, join with comma
        cells = [c.strip() for c in line.split('|')]
        cells = [c for c in cells if c]
        return ', '.join(cells)
    return line

lines = raw.split('\n')
cleaned_lines = []
for line in lines:
    cleaned = strip_table_row(line)
    # Skip horizontal rules (--- by itself)
    if re.match(r'^[-]{3,}$', cleaned.strip()):
        continue
    cleaned_lines.append(cleaned)

clean = '\n'.join(cleaned_lines)

# Collapse excessive newlines
clean = re.sub(r'\n{3,}', '\n\n', clean)
clean = clean.strip()

# ---- Chunk ----
paragraphs = [p.strip() for p in clean.split('\n\n') if p.strip()]
MAX_CHUNK = 2000
chunks = []
current = ""
for p in paragraphs:
    if len(current) + len(p) + 2 > MAX_CHUNK and current:
        chunks.append(current)
        current = p
    else:
        current = (current + "\n\n" + p) if current else p
if current:
    chunks.append(current)

print(f"Total chars: {len(clean)}, paragraphs: {len(paragraphs)}, chunks: {len(chunks)}")
for i, c in enumerate(chunks):
    print(f"  chunk {i+1}: {len(c)} chars")

# ---- Generate ----
all_audio = b""
for i, text in enumerate(chunks):
    req_id = str(uuid.uuid4())
    body = {
        "user": {"uid": "hermes-lyric-tts"},
        "req_params": {
            "text": text,
            "speaker": VOICE,
            "audio_params": {
                "format": "mp3",
                "sample_rate": 24000,
                "bit_rate": 160000
            },
            "additions": json.dumps({
                "disable_markdown_filter": True,
                "cache_config": {"text_type": 1, "use_cache": True}
            })
        }
    }
    
    data = json.dumps(body).encode('utf-8')
    headers = {
        "X-Api-Key": API_KEY,
        "X-Api-Resource-Id": "seed-tts-2.0",
        "X-Api-Request-Id": req_id,
        "Content-Type": "application/json"
    }
    
    print(f"Chunk {i+1}/{len(chunks)}: sending {len(text)} chars...", flush=True)
    req = urllib.request.Request(API_URL, data=data, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            resp_text = resp.read().decode('utf-8')
    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    
    chunk_audio = b""
    for line in resp_text.split('\n'):
        line = line.strip()
        if not line:
            continue
        try:
            evt = json.loads(line)
        except json.JSONDecodeError:
            continue
        code = evt.get("code")
        if code == 0:
            data_b64 = evt.get("data", "")
            if data_b64:
                chunk_audio += base64.b64decode(data_b64)
        elif code == 20000000:
            print(f"  chunk {i+1} done: {len(chunk_audio)} bytes audio")
            break
        else:
            msg = evt.get("message", "")
            print(f"  WARN: code={code} msg={msg}", file=sys.stderr)
    
    if not chunk_audio:
        print(f"  ERROR: no audio data in chunk {i+1}", file=sys.stderr)
        sys.exit(1)
    all_audio += chunk_audio

with open(OUT_PATH, "wb") as f:
    f.write(all_audio)
print(f"\nTotal audio: {len(all_audio)} bytes → {OUT_PATH}")

# Verify
import subprocess
result = subprocess.run(
    ["ffprobe", "-hide_banner", "-show_entries", "format=duration,size,bit_rate",
     "-of", "json", OUT_PATH],
    capture_output=True, text=True, timeout=10
)
if result.returncode == 0:
    info = json.loads(result.stdout).get("format", {})
    dur = float(info.get("duration", 0))
    size = int(info.get("size", 0))
    print(f"Verified: {dur:.1f}s, {size} bytes, {info.get('bit_rate', '?')} bps")
else:
    print(f"ffprobe failed: {result.stderr[:200]}")
