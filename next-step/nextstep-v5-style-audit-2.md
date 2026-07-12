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
