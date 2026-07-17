#!/usr/bin/env python3
"""Doubao V3 TTS for claude-sonnet-5.0-output.txt (stdlib only)"""
import os, json, base64, re, sys, urllib.request, uuid

# ---- Config ----
TEXT_PATH = "/home/ubuntu/music/07-17-grow-the-fuck-up/claude-sonnet-5.0-output.txt"
OUT_PATH = "/home/ubuntu/music/07-17-grow-the-fuck-up/claude-sonnet-5.0-tts.mp3"
API_URL = "https://openspeech.bytedance.com/api/v3/tts/unidirectional"
VOICE = "zh_female_vv_uranus_bigtts"  # known-good

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

# ---- Load + Clean Text ----
raw = open(TEXT_PATH).read()

# Fix the weird line-break artifacts from the model output
raw = re.sub(r'([a-z])[\s\n]+([a-z])', r'\1\2', raw)  # fix broken English words like "c\nontingent"
raw = re.sub(r'\n{3,}', '\n\n', raw)  # collapse excessive newlines
raw = raw.strip()

# Split into paragraphs for chunking
paragraphs = [p.strip() for p in raw.split('\n\n') if p.strip()]

# Group paragraphs into chunks ≤ 2000 chars (safe for API)
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

print(f"Total chars: {len(raw)}, paragraphs: {len(paragraphs)}, chunks: {len(chunks)}")
for i, c in enumerate(chunks):
    print(f"  chunk {i+1}: {len(c)} chars")

# ---- Generate Audio ----
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
    
    # Parse SSE/chunked response (lines of JSON)
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

# ---- Write Output ----
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
