# "Next Step" v5 — Style Audit #2
## Diagnosis: D/E/F strategy error — decoupling genre from vocal constraint
## 2026-07-12

## 问题诊断

shoegaze/post-rock/electroacoustic 这条链路是把"如何避免belting"这个约束和"选什么genre"这个决定捆在一起解决——只有让整个声音场景变得陌生化(墙式混响、无释放的ostinato、颗粒噪声),belting才"自然地"消失。代价是陌生的声音表层会在听众听清歌词之前就先过滤掉大部分人。

## 正确解法:解耦

genre 选主流、旋律性强、有大范围听感基础的类型,"人声克制"这个约束单独靠 delivery descriptor 和分段 tag 去锁,不靠换掉整个声音世界。坐标:Tracy Chapman《Fast Car》、赵雷《成都》、Jason Isbell、The National——离乡叙事+克制人声+完全主流可听的编曲。

---

## Style G: The Long Walk Home — Heartland Folk-Rock

Concept:真乐队编制(木吉他+干净电吉他+贝斯+鼓+管风琴暖色),叙事直给,情绪推进靠编曲层叠而不是人声音量。坐标:Jason Isbell 式白描叙事 + The National 式低音域冷静男声 + 《Fast Car》式普世离乡叙事。

Warm heartland folk-rock, full live band, acoustic and clean electric guitar interplay, driving brushed drums, upright-leaning bass, subtle Hammond organ warmth, plainspoken low-register male lead, conversational unaffected delivery, steady narrow melodic range, arrangement builds through layering not vocal volume, genuinely melodic memorable chorus line, 92 BPM D minor

分段人声标签:
[Verse 1: dry conversational low vocal, guitar and voice only, unhurried]
[Pre-Chorus: band enters gently, steady vocal, same quiet intensity]
[Chorus: full band lifts, vocal stays level and plainspoken, no swell, melody carries the weight]
[Verse 2: pared back again, intimate, documentary tone]
[Bridge: half-time, hushed, instruments thin out, vocal nearly spoken]
[Interlude: spoken-sung, breathy, no drums, near-ASMR]
[Final Chorus: full band warmest and fullest, vocal still restrained, unison double allowed, no belting]
[Outro: band falls away instrument by instrument, dry vocal last, single guitar chord fades]

Production: Interlude——鼓和贝斯完全退出,一把干净吉他持续一个和弦垫在气声人声下面。Outro——管风琴先褪,贝斯再褪,最后剩一把木吉他和干声人声,渐入寂静。

Excludes: shoegaze wall-of-sound, post-rock ostinato, ambient/electroacoustic texture, glitch, industrial, EDM, arena rock, belting, shouting, screaming, roaring, vocal crescendo, falsetto runs, gospel choir, arena singalong

Sliders: Weirdness 15-25 · Style Influence 70-80

---

## Style H: Warm Chamber Folk-Pop

Concept:更偏"好听优先"——钢琴+弦乐+轻打击乐的暖色,旋律性和 hook 感优先于叙事骨感。坐标:Gregory Alan Isakov / Ben Howard / Novo Amor 一类拥有广泛流媒体听众基础的"美但不炫技"民谣。

Warm acoustic chamber folk-pop, soft piano and light string pads, gentle brushed percussion, warm double bass, restrained tenor male lead, tender unaffected delivery, genuinely melodic hook-driven chorus, soft dynamic swell through strings not vocal, intimate but polished production, 92 BPM D minor

分段人声标签:
[Verse 1: bare piano and voice, close-mic, plainspoken melody]
[Pre-Chorus: strings enter softly, vocal steady and warm]
[Chorus: full arrangement blooms, vocal stays tender and level, melody is the hook, no belting]
[Verse 2: pulled back to piano and voice, documentary calm]
[Bridge: strings hold a suspended chord, vocal hushed, near-spoken]
[Interlude: spoken-sung, breathy, no drums, near-ASMR]
[Final Chorus: warmest full bloom, vocal restrained but present, gentle unison double, no crescendo]
[Outro: strings fade first, then percussion, piano and voice alone, final note unresolved]

Production: Interlude——弦乐和打击乐消失,只剩持续的钢琴垫音托着气声人声。Outro——弦乐垫先溶解,打击乐停止,最后只剩钢琴和干声,落入室内空气声。

Excludes: shoegaze, post-rock, ambient/electroacoustic texture, glitch, minimalism-for-its-own-sake, industrial, EDM, arena rock, orchestral bombast, belting, shouting, screaming, power ballad crescendo, gospel choir, cinematic triumph

Sliders: Weirdness 15-25 · Style Influence 68-78

---

## 与之前版本的差异

G/H 都不引入舞曲/Cantopop 的能量向量,也不依赖用户自己判断"哪一半在起作用"——genre 本身是内部一致的(不会有两个互相拉扯的风格向量)。如果两版都试了还是不满意,大概率问题就不在 style prompt 层面了,而是要回到 melody seed 本身或者用 Voices 功能录一遍想要的确切语气。

---

## Style I: California Hills — Eagles × 李宗盛
## 2026-07-13

### Concept
取《Hotel California》的加州暖调摇滚骨架——双吉他交织对话、模拟录音的宽阔声场、不急于进副歌的叙事型结构；取《山丘》念白式的低沉男声、留白大于填充的吐字节奏、将情感重量交给语气而非音量的克制。

### I-v1 问题诊断（Liz 快速诊断）

第一版 prompt 犯了关键错误：**只改了"演唱风格"（vocal delivery），没碰"混音平衡"（mix level）。**

实证：
- Hotel California 人声和主奏吉他在混音里刻意压得很低，鼓是 bone dry（极干、紧而克制）。真正情绪爆发点是结尾 2分12秒 双吉他 solo，不是人声
- 山丘 李宗盛嗓音带金属感、称不上优美、唱功也不算一流，制胜靠的是本色口语化，情绪高点交给编曲不是人声
- 两首歌共同点：**"克制到近乎业余的真实感，情绪高点交给编曲/器乐，不交给人声"**

I-v1 的问题："70s California rock"打头 + "dual guitars soar" + "brushed drums"，把 mix 往"满、前、响"拉。之前七八版全在"演唱风格"这一个杠杆上反复试，从没碰过"混音平衡"这个完全不同的杠杆。

另一个风险：AI 合成人声没有李宗盛 55 岁人生的天然背书，纯念白/纯平铺直叙容易显得"僵"而不是"真"。"口语化"要保留旋律轮廓，不是彻底降级成 spoken word。

### I-v2 修正版

**关键改动逻辑**：把"别喊"从"演唱指令"挪到"混音指令"——vocal mixed low and blended 描述最终成品里人声和乐队的相对音量关系，全新杠杆。鼓从 "brushed" 改成 "dry, no crashes, no fills"。贝斯首次明确要求 "subdued, not driving"。Style Influence 从 75 拉到 78-88——之前几版反复被拉回通用摇滚，可能是 style 权重不够压住模型默认倾向。

Weathered 70s Laurel Canyon folk-rock, aged husky low baritone lead vocal mixed low and blended into the band — never forward, never dominant in the mix, dry tight acoustic drum kit with no crash cymbals and no fills, subdued melodic bass sitting under the arrangement not driving it, dual clean electric guitars weaving warm interlocking harmonies, sparse Hammond organ pad, unhurried phrasing that stays melodic — conversational singing, not flat spoken word, instruments layer in gradually to build the swell, vocal intensity stays level and unchanged throughout

Excludes: pop, pop-punk, emo, radio polish, autotune, trap, EDM, synth-pop, dream-pop, belting, shouting, screaming, powerful vocal, vocal crescendo, lo-fi, garage rock, excessive distortion, guitar shredding, arena rock, hard rock, prominent bass, driving aggressive bassline, crash cymbals, heavy drum fills, cinematic climax

Sliders: Weirdness 20-30 · Style Influence 78-88

分段人声标签:
[Verse 1: aged husky low baritone, mixed low and blended with the guitars, conversational but melodic, single voice, no forward presence]
[Pre-Chorus: same weathered texture, guitars widen slightly, vocal stays blended not forward]
[Chorus: full band lifts through guitar harmonies and organ, vocal stays low in the mix and level — the guitars carry the lift, not the voice]
[Verse 2: pulled back, intimate, husky and unpolished, documentary tone]
[Bridge: half-time, hushed, nearly spoken but still melodic, single guitar underneath]
[Interlude: spoken-sung, breathy, no drums, near-ASMR]
[Final Chorus: fullest band moment, dual guitars soar and carry the emotional peak, vocal remains weathered, low in the mix, intensity unchanged]
[Outro: band falls away instrument by instrument, dry weathered vocal last, single guitar chord fades]

如果这版还是被拉回"响、满、喊"，问题大概率不在 prompt 文字本身——用 Voices 录一段确切语气锁定，不再纯文字试第十版。

---

## Style I-v3: ROCK-FREE REFINEMENT
## 2026-07-13

### 问题诊断（I-v2 反馈）

I-v2 加了 "vocal mixed low," "dry drums no crashes," "subdued bass" —— 仍然被 Suno 拉回摇滚模式。鼓还在砸，贝斯还在吼。**根本原因："rock" 这个词只要出现在 genre 里，整个 mix 就被拖向攻击性。** 任何文字约束都压不过这个词的权重。

### I-v3 改动清单（外科手术级）

每个改动只针对一个 Suno 触发词，其余保留：

| 触发词 | 位置 | 替换 | 原因 |
|--------|------|------|------|
| **"rock"** | Style Prompt genre: "Laurel Canyon folk-rock" | → "Laurel Canyon **folk**" | "rock" 是唯一的元凶——它把鼓、贝斯、人声全拉向攻击性。去掉后整个声场自然回到 warm/spacious/intimate |
| **"tight"** | Style Prompt: "dry tight acoustic drum kit" | → "dry acoustic drum kit" | "tight" 暗示张力/驱动感，可能触发鼓的 attack 增强 |
| **"build the swell"** | Style Prompt: "instruments layer in gradually to build the swell" | → "instruments layer in gradually, **arrangement deepens naturally**" | "build" + "swell" 双触发音量爬升。新表述只描述编曲层次增加，不承诺音量变化 |
| **"soar"** | Final Chorus tag: "dual guitars soar and carry the emotional peak" | → "dual guitars **at their warmest and most present** carry the emotional peak" | "soar" 触发 Suno 的 epic-rock 模式——即便修饰 guitars，也会把整个 mix 拉向宏大/轰鸣 |

### 新增 Excludes

- `forward vocal` — 补刀：即使 style prompt 写了 "mixed low"，排除词也明确拒绝人声前置
- `loud mix` — 直接拒绝混音层面的响度竞争
- `driving drums` — 在已有 "crash cymbals" / "heavy drum fills" 基础上再加一层鼓的推力封锁
- `epic build` — 防止编曲层叠被误解为 epic crescendo

### 新 Genre Anchor 选择

**"Weathered 70s Laurel Canyon folk"** 而非其他候选：

- ❌ "Laurel Canyon folk-rock" — 含 "rock"，已证实失败
- ❌ "70s singer-songwriter" — 太泛，可能偏钢琴 ballad 或 James Taylor 式轻民谣，丢失双吉他纹理
- ❌ "acoustic atmospheric" — 太模糊，可能触发 ambient/new-age
- ✅ **"Laurel Canyon folk"** — 精准锁定 Joni Mitchell / CSN / 早期 Jackson Browne 的声学传统：温暖、宽阔、双吉他、不着急、模拟录音质感。"Folk" 在 Laurel Canyon 语境下自带电吉他但不带摇滚侵略性

### Sliders 调整

Style Influence 从 **78-88 → 70-78**。理由：去掉 "rock" 后，模型没有摇滚默认倾向需要对抗——不需要那么高的 style 权重去压制。如果实际生成偏软/偏 generic folk，可回调到 75-85。

### 歌词同步

歌词已更新为 Liz 最新编辑稿（V1 精简版）：
- 移除 Verse 1 中 "Jets crossed the roof" / "From six until ten" / "I zipped the bag" / "Took the elevator down" / "Wheels on tile" 五句
- 移除 Pre-Chorus 中 "A VIP lane glows" / "The ad walls burn brighter" 两句
- Verse 2: `"Homework" moves from balcony to balcony` → `Through the window, "homework" moves balcony to balcony`
- Bridge: `Was it ever the room, or was it standing still?` → `Thin walls still ringing in my ears`
- Final Chorus: 移除开头第一个 `I don't even know`，直接从第二个进入

---

## Style I-v4: ANTI-BORING REFINEMENT — Tension Architecture
## 2026-07-14

### Core Diagnosis: Why All 8+ Previous Attempts Failed

"Boring" was never a prompt problem — it was a **length + tension-structure problem.** All previous prompts described the surface perfectly (warm, husky, folk, guitar harmonies), but every element aligned toward comfort/pleasantness. What makes Hotel California and 山丘 compelling is the **tension between surface calm and underlying dread/urgency.** Previous prompts described the surface; none described the undertow.

### Primary Lever: Lyric Cut (155 → 62 lines)

**Community-verified Suno fact**: Prompt adherence is tight for the first 60-90 seconds, then decays exponentially. After decay, Suno repeats motifs, simplifies, falls back to statistical mean = generic patterns. ~3:00-3:30 runtime keeps the entire song inside the high-adherence window. 155-line lyrics = 5+ minutes = guaranteed boring second half with 50%+ on autopilot.

**What was cut and why (from Liz's latest edit as starting point):**

| Section | Before | After | Cut | Rationale |
|---------|--------|-------|-----|-----------|
| Verse 1 | 10 | 10 | 0 | Already tight from Liz's edit — no further cuts |
| Pre-Chorus | 5 | 5 | 0 | Already tight |
| Chorus | 7 | 7 | 0 | Hook — must stay identical on repeats |
| **Verse 2** | 13 | **10** | -3 | Removed: "At dusk, the river singer reaches the roof" (one too many scene details), "The muddy lake road from the house I knew" ("childhood clay" already carries this), "I sit between them like I'm barely there" (tells rather than shows — the blankness is already shown through father/brother images) |
| **Bridge** | 9 | **8** | -1 | Removed: "Maybe it was the ceiling that forgot" (weaker echo of "Something tore" — doesn't earn its space) |
| **Interlude** | 13 | **8** | -5 | Cut redundant murmured repetitions ("I don't even know how," "oh," "yeah," "hmm — yeah," one extra "I don't even know"). Murmured repetition is the point, but shorter — still reads as fragmented, incomplete, unresolved |
| Final Chorus | 7 | 7 | 0 | Hook variant — preserved |
| **Outro** | 10 | **7** | -3 | Cut: duplicate "One step more," duplicate "I don't even know," duplicate "and that's enough." Final "and that's enough" kept as closer per Liz directive |

**Total**: 77 → 62 content lines. At 82 BPM with slow, spacious delivery, this lands at ~3:00-3:30 — the entire song inside Suno's high-adherence window.

### Style Prompt Changes: The Anti-Boring Architecture

Every change targets a specific failure mode from the accumulated 8+ failed attempts:

| Failure Mode | Root Cause | I-v4 Fix |
|-------------|-----------|----------|
| "Laurel Canyon folk" → sunny cowboy default | "Laurel Canyon" triggers the sunny half of its semantic field; "folk" without dark modifiers defaults pleasant | **Removed entirely.** Replaced with "brooding tense unresolved slow-burn noir folk" — mood FIRST, genre second |
| 92 BPM → inherent cowboy-sway feel | Steady mid-tempo with folk = campfire rhythm | **82 BPM** — slower = more weight, less sway |
| All elements aligned toward comfort | "Warm" used 3x, zero words for tension/urgency | "Warm" used 0x. Replaced with: **tense, unresolved, haunted, weight.** Descending bassline that never resolves |
| No melodic identity — nothing to remember | No recurring motif = nothing for the ear to grab | **Recurring 3-note clean guitar motif hook** — every non-boring song has one. Hotel California has the 12-string intro. This song gets its own |
| "Folk-rock" → rock triggers aggression, folk triggers pleasant | Two opposing vectors in genre tag | Genre anchor: **"noir folk"** — dark, cinematic, never sunny |
| No arrangement dynamics | All instruments present throughout = flat | **Strings enter only at Final Chorus** (李健版山丘先例: strings lift spoken delivery into poetry without changing vocal). **Bass is descending and unresolved** — never lands |

### Backup Vocals: Anti-Comfort Design

- **Female backing vocals**: YES, but only as **distant, wordless hum** — not harmonies, not "companion" presence. The song is about being alone. A distant female voice is a memory, not a person in the room. Enters only at Final Chorus.
- **Male unison double on chorus**: YES — **"his own voice" layered from a distance**, not a choir. The effect is isolation echoing back at itself, not community.

### Section Vocal Tags: From Constraint to Direction

Previous tags only said what NOT to do ("no belting"). I-v4 tags tell the model what TO do:

| Section | Delivery Direction | Arrangement Cue |
|---------|-------------------|-----------------|
| Verse 1 | Conversational but **weighted** | Guitar motif underneath |
| Pre-Chorus | Vocal stays **buried** | Bass descends, motif continues |
| Chorus | Male unison double, vocal stays **low** | Lift from **texture not volume** |
| Verse 2 | Intimate, husky, **documentary tone** | Motif sparse underneath |
| Bridge | Hushed, nearly spoken, **still melodic** | Single clean guitar, bass holds unresolved note |
| Interlude | Spoken-sung, breathy, **near-ASMR** | Motif distant and fragmented |
| Final Chorus | Vocal stays **buried and level** | **Strings enter — tense, not warm.** Female hum distant. Motif locks in |
| Outro | Dry vocal last | Strings fade → drums fade → guitar motif alone → unresolved chord |

### The Tension Philosophy

**Surface restraint + underlying dread = Hotel California / 山丘 magic.**

Previous prompts described Hotel California's surface: warm guitars, clean production, conversational delivery. None described its engine: the descending bassline that never resolves, the lyrics about being trapped while the music sounds free, the dual-guitar climax that arrives not through vocal power but through arrangement.

This song's engine: a man walking away from everything, unsure if he's moving toward something or just not going back — and the music should feel like it could collapse into silence at any moment. That's the undertow. That's what makes it not boring.

### Exclude Styles — Additions

New exclusions targeting the "pleasant-default" gravity well:
- `country rock` — blocks Eagles-lite cowboy drift
- `cheerful, breezy, campfire, singalong, uplifting` — blocks the folk-comfort zone
- `major-key resolution` — forces the model to stay in unresolved harmonic territory
- `female lead vocal, choir` — prevents model from misinterpreting "female hum" as lead/choir

### Sliders Rationale

- **Weirdness: 25-35** (up from 20-30) — slightly higher to create the dissonant/tense space. The model's comfort zone IS the boring zone. Need to push slightly into unfamiliar territory.
- **Style Influence: 78-88** (up from 70-78) — "rock" is gone from genre, but "noir folk" is a non-standard anchor. Higher influence locks the anti-boring direction tight. If output drifts generic, nudge to 82-90.

### Metrics

- Lyric content lines: 77 → **62** (19.5% cut)
- Target runtime: **~3:00-3:30** (entire song inside Suno's high-adherence window)
- Style prompt: ~315 chars, 5 distinct mood tags before genre tag, 0 artist names
- BPM: 92 → **82** (10.9% slower = more weight, less cowboy sway)
