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
