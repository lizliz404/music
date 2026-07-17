# AGENTS.md — music repo conventions for AI agents

## 0. Absolute rules

- **All lowercase paths.** Never `~/Music/` — only `~/music/`.
- **Only `~/music/`.** No other music directories exist.
- **Git push = HTTPS only.** Repo: `github.com/lizliz404/music`. Credentials in `~/.git-credentials`.
- **Never create uppercase dirs, spaces in filenames, or Title_Case slugs.**

## 1. Project directory convention

```
~/music/MM-DD-slug/
```

- `MM-DD` = creation date (month-day, zero-padded). Example: `07-16-ml-self-refactor`
- `slug` = short hyphenated English identifier. No spaces, no underscores, no Chinese.
- Exception: `fuzzy/` for multi-song seed material that hasn't been split into dated projects yet.

## 2. Within-project structure

```
MM-DD-slug/
  00-看这里-CURRENT.txt   ← navigation / "read this first" pointer
  01-source/              ← raw intake, reference material, research
  02-current/             ← frozen/current final versions
  03-archive/             ← old versions, prompts, logs, intermediate artifacts
    v1/                   ← all v1 drafts
    v2-backups/           ← surgical/backup versions
    prompts-logs/         ← delegation prompts, stderr/stdout
    tts-chunks/           ← intermediate TTS audio chunks
    cover-prompts/        ← intermediate cover generation prompts
```

- Only `00-看这里-CURRENT.txt` belongs at project root (plus files actively being worked).
- Everything else goes into one of the three numbered subdirs.
- Intermediate artifacts (prompts, logs, TTS chunks) go straight to `03-archive/`.

## 3. File naming convention

**The base pattern is the project slug.** Everything derives from it:

```
# Primary: date-prefixed (for AI-generated output, audio, cross-project files)
YYYY-MM-DD-[slug]-[descriptor].ext   e.g. 2026-07-17-grow-the-fuck-up-grok-4.5.txt

# Shorthand: slug-only (for versioned drafts, finals, audits within a project)
[slug]-[descriptor].ext              e.g. all-beings-v1.txt, poverty-audit-v2.txt
```

Common descriptors: `v1`, `v2-final`, `opus`, `suno-paste-only`, `audit-v2`, `style-c`, etc.

### Special cases

**LRC** — `[slug]-[linecount]-[lang]-primary.lrc` + `.lrc.txt` copy (Telegram-compatible).
  Lang = `en` / `cn`. Linecount for version tracking (e.g. 344, 518).

**Source/raw** — `raw-[desc].txt` or `source-[desc].md`. Standard intake = `raw-material.txt`.

**Audio** — `YYYY-MM-DD-[slug]-[source].mp3`. Source = model or TTS engine.

**Intermediate** — `_` prefix (e.g. `_delegation-*.txt`, `_cursor-*.txt`, `_run-*.py`).
  These go in `03-archive/`, never at project root.

## 4. Version soup convention

```
01-source/   → raw materials, research, intake
02-current/  → FROZEN current version (one per language)
03-archive/  → everything else: old drafts, prompts, logs, intermediate
```

- **Never auto-promote a candidate to `02-current/`.** Liz decides.
- When in doubt, put new output at project root with a note in `00-看这里-CURRENT.txt`.

## 5. Song identification

When Liz says "second-last song" or "near-title" or uses a non-exact title:
- Resolve via `git log --oneline` + folder creation timeline, NOT from chat context.
- Check `00-看这里-CURRENT.txt` in the candidate folder.
- The song being discussed may not be the one open in the current chat.

## 6. Multi-model / delegation workflow

Typical creative flow:
1. Raw intake → `01-source/raw-material.txt`
2. Multi-model delegation (Opus, Grok, Sol, Sonnet) via Cursor / Hermes sub-agents
3. Outputs land at project root as `[model-name]-output.txt`
4. Lyric (this agent) or Liz audits, selects, integrates
5. Final version → `02-current/`
6. Intermediate prompts/logs → `03-archive/prompts-logs/`

## 7. Suno production

- Suno accepts paste-only (3 fields). Use `[slug]-suno-paste-only.txt`.
- MP3 naming: Artist = model ID, Title = `YYYY-MM-DD-[long-slug]`.
- Full-listen MP3s go in `audio/` subfolder.
- Duration estimation: words vs BPM + rests. If still 5 min after cut, fix style absorption, not more lyric cutting.

## 8. LRC / cover / TTS

- **LRC**: dual canons (EN-outer & CN-outer). Pair lines, don't re-translate. Telegram = `.lrc.txt`.
- **Cover**: 1:1 square only. Semantic domain first. Liz audits, then Cursor continues with her verbatim.
- **TTS**: Doubao V3 → zh_female_vv_uranus_bigtts, seed-tts-2.0, chunk ≤2000 chars. Use stdlib urllib (PEP 668 blocks pip).

## 9. Don't do

- Never create `~/Music/` (uppercase).
- Never leave `_`-prefixed files at project root.
- Never auto-promote to `02-current/`.
- Never rename files referenced by `00-看这里-CURRENT.txt` without updating the pointer.
- Never push via SSH — HTTPS only.
