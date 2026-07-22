# Edit Rights V2 — Parallel Audit + Rewrite Brief

## Your Job

**Phase 1: Structured Audit.** Read the v1 parallel draft. Score it. Identify what works, what's weak, what's missing. Apply the audit framework below.

**Phase 2: V2 Rewrite.** Based on your audit, produce a NEW v2 version: full lyrics + vocal tags + Suno style prompt. Do NOT copy v1 lines — write your own alternative that addresses audit findings.

## Source Materials (READ THESE FIRST)

| File | What |
|---|---|
| `01-source/raw-notes-liz.txt` | Liz's field notes on class, housing, environment, 熵减, social observation (46KB) |
| `01-source/raw-chat-ccy.txt` | Chat with friend ccy about wealth, 配得感 vs 匮乏感, "why not me", the auntie with two flats, the Toronto-bound student, KFC coupons next to luxury cabinets (14KB) |
| `01-source/raw-sleep-experiment.txt` | Liz's obsessive sleep-experiment log — another angle on the scarcity/abundance theme: someone who CAN'T edit their environment, fighting for basic comfort (36KB) |
| `01-source/image-analysis.md` | Analysis of 3 photos from a high-end compound: "rich = edit rights over what you see", frontstage/backstage, friction deletion, the fake vine on the pipe (4KB) |

## v1 Reference (READ THIS)

`02-current/edit-rights-v1-parallel.txt` — dual-version comparison file containing:
- **Version A** (Lyric): ABABCB + Outro, 82 lines, male vocal, Alt R&B / lo-fi hip-hop, 92 BPM D minor
- **Version B** (Grok 4.5 via Cursor): ABABCB, 53 lines, female vocal, dark indie-electronic art-pop, 98 BPM A minor
- Comparison table (hook, structure, bridge, best lines, ending)
- Suno style prompts + vocal tags for both versions

## Core Theme

The narrator spends 90 yuan for one night in a high-end residential compound and experiences "edit rights" — the wealthy's ability to delete friction from their visible world. The song explores the tension between 匮乏感 (scarcity mindset) and 配得感 (entitlement/deservingness), ending not with envy but with ignition: "why not me?"

Key images from source: magnetic door closures, balance-board security guard, green-plate cars, fake vines on basement pipes, trash sorting in B1, the auntie who bought a first-floor flat for her parents, the Toronto-bound student with broken English, KFC coupons next to luxury cabinets, the night market as contrast.

## Audit Framework (Verbatim from Liz)

> 希望你动用最大的思考能力，深入推理，大胆想象，考究取证，直击本质。拒绝平庸的正确和无聊的平衡，只求新的，有趣、有用的洞见。理性、客观、科学、专业。
>
> 作为专家，全面而结构化的赏析，打分，该份歌词。
>
> what why how？属于哪一类？
>
> 如要进一步优化，无论是 lyric，又或是 style prompt、vocal tag 等，进一步纠偏和延展，要做出新的一版，要做些什么？
>
> 还是说已经完全没必要了？因为艺术本来就偏主观，再多做很容易陷入完美主义的过度优化陷阱？
>
> 最要避免的情况：又臭又长又无聊。曲高和寡、孤芳自赏、闭门造车、自以为是也需避免。尊重市场，因此尽可能与更广大的受众产生尽可能大的共鸣。我的野心比较大，想做到"有用且有趣"。
>
> 有野心的艺术品应该在"文学性"与"听觉成瘾性"之间找到张力，不想沦为只有少数人自嗨的"小众白噪音"。
>
> "有用且有趣"：
> - 有用：触动情绪。让听众在通勤、深夜、或者感到虚无时，听这首歌能产生生理上的"安定感"或"释怀感"（解决数字化焦虑）。
> - 有趣：听觉上有意外之喜。不能是一成不变的平铺直叙，必须有抓耳的、可哼唱的旋律线（即使是在很低的音域内）。
> - 防止"清汤寡水"和"Sheeran mean"（工业化流行套路），同时避免"无聊的平淡"

### Audit must explicitly answer:
1. **What** is the song doing? **Why** does (or doesn't) it work? **How** does it achieve its effects?
2. **分类**: What genre/mechanism class does this belong to?
3. **Iterate vs stop verdict**: 继续磨还是完全没必要? Name the marginal-return inflection point.
4. **Market resonance**: Will this connect beyond niche listeners?

## V2 Requirements

Based on your audit, produce ONE complete v2 version:

### Lyrics
- Structure: invent your own section architecture (not locked to ABABCB)
- Use concrete images from source materials — don't invent generic wealth imagery
- Emotional arc: observation → overwhelm → analysis → ignition
- The hook must be singable and memorable
- Bridge: one emotional core + one central question (no inventory dump)
- Final section should show transformation from the opening
- **Literariness + auditory addictiveness** — the tension

### Vocal Tags (inline metatags for each section)
- 3-5 tags per section max
- Include vocal performance, dynamics, atmosphere
- Match your lyric's energy

### Suno Style Prompt
- Genre + mood + BPM + key + instruments + vocal style + production + dynamics
- Describe the dynamic ARC, not just genre labels
- Build a vocal PERSONA, not just a gender
- No artist names or trademarks
- **Exclude Styles field**: what you DON'T want, specific to this prompt
- ~500-800 chars for the style field

## Output Format

Write your complete v2 to: `/home/ubuntu/music/07-17-edit-rights/03-archive/v2/[your-model-name]-v2.txt`

Use this exact format:
```
EDIT RIGHTS — v2 ([model name], 2026-07-22)

[AUDIT SECTION — your full structured audit here, answering all framework questions]

---

[FULL LYRICS with section tags and inline vocal tags]

---

SUNO STYLE PROMPT

Style:
<your style prompt>

Exclude:
<your exclude list>

Vocal Tags (inline):
  [Section] — <tags>
  ...
```

## Constraints
- Write REAL lyrics, not an outline or analysis
- Do NOT copy v1 lines verbatim — write your own
- Kill on sight: 清汤寡水, Sheeran-mean industrial pop, boring flatness
- Kill on sight: 曲高和寡, 孤芳自赏, 闭门造车, 自以为是
- Target: widest possible resonance while maintaining artistic integrity
- Lyric total: aim for 40-60 lines (not counting tags)
