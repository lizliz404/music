# QUIET COSTS — v7 (Final)

**Words & music by Liz / Hermes Agent**
**Based on Liz's poverty autoethnography (穷记录)**
**Status: FINAL — lyrics locked, next step = medium shift (Suno generation)**

---

## LYRICS

```
[Intro]
(single fingerpicked guitar, one figure, tape hiss)
There's a bookshelf in Hengyang,
four floors up, an inch of dust —
Jane Eyre, and the red-and-black one
nobody in this house can pronounce anymore.

[Verse 1 — Mother]
There's handwriting in the margins, small and sure,
a whole dictionary pencilled into the white —
I never saw her like that. I built her back from dust,
as if the dust could teach her how to run.

Same eyes — I'd know them anywhere.
Now she's up past midnight hunting a two-yuan win,
one more click for the free-shipping line.
She says she read too many books when she was young,
like light was something
she wasn't supposed to carry.

[Pre-Chorus]
I take field notes in my own kitchen.
Twenty minutes on a ten-yuan comb.
Call it distance. Call it staying clean.

[Chorus]
Quiet costs money
and I don't have it yet.
Noise is the free plan —
silence is what you rent.
Quiet costs money.
I'm saving every scrap.
The cage door's already open —
I just can't afford the gap.

[Verse 2 — Father]
He opens fire at breakfast — never aims, never has to.
Water's too hot, rice too thin, why'd you make yourself so skinny.
He's been firing since before I had a name,
and the rounds are made of nothing, so they never run out.

Ten years — three starches. Same black pan.
Thirty degrees outside and he still boils it down to soup,
because soup is the last recipe left in his hands.

I'm grown now, a country away, and I still go still.
The blow was never the part that taught me.
The waiting did the job.

[Pre-Chorus]
I take field notes in my own kitchen.
Twenty minutes on a ten-yuan comb.
I called it distance. I called it staying clean.

[Chorus]
Quiet costs money
and I don't have it yet.
Noise is the free plan —
silence is what you rent.
Quiet costs money.
I'm saving every scrap.
The cage door's already open —
I just can't afford the gap.

[Verse 3 — Self]
Two-fifty for a sweet potato, canteen line,
and my heart went off like a tripped alarm.
Nobody else was counting. I was counting.
Knowing never stops the flinch —
that's the cruelest part of getting smart.

Cognition three-point-oh,
bank account still stuck on the old version.
I take the ones I love and turn them into evidence —
because if I don't make them the study,
I'm scared I turn into the sample.

[Pre-Bridge]
I've stood at the lip of the pit too long.
The pit doesn't need renovation —
it needs me out.

[Bridge]
(voice and guitar alone — no band)
Still a kid, I took my mother's phone in the dark.
Told myself it was only a song to fall asleep to.
That was the lie. It was never the song.
Something I won't put in words — something I'd have died before she saw.
Then a sound in the flat, and every nerve I own pulled tight,
and I froze by the wardrobe with the stolen light in my hand.

And through the bathroom door I heard her come apart —
two in the morning, cleaning my brother up, and crying while she did it,
her voice cracking down on him, folding soft, then cracking down again.
I didn't move. I couldn't. I stood there in the hall
holding a phone that wasn't mine,
guilty for being awake,
guilty for what I'd been doing,
guilty for every year they fed me and carried me
while I hid in the dark and took.

[Chorus — final]
(band returns — restrained crescendo, not shouting)
Quiet costs money
and I'm still counting.
Noise is the free plan —
I never left the free plan.
Quiet costs money.
Leaving's the toll —
I'm still counting out the fare.
The cage door's already open.
I can see it from here.
(pause)
Not tonight. Not yet.

[Outro]
(single guitar, mirroring the intro)
Jane Eyre. Le Rouge et Noir.
Still on the shelf, another year of dust.
Her handwriting's still there in the margins,
small, and neat, and sure of something
I'm not.
The shelf outlasts everything in this house.
So far, that includes me.
I'm still in the room.
(pause)
Still counting.

[End]
```

---

## V7 Changelog (from audit → applied)

Three surgical fixes, all sourced from the v5 structured audit:

1. **Verse 2 density** — Applied Audit Recommendation A: breathing-group reformatting. "Water's too hot, rice too thin, why'd you make yourself so skinny" kept as one breath group (it's mimicking rapid-fire nagging — density IS meaning). "Ten years — three starches. Same black pan." broken into its own reflective breath (it's observation, not performance — needs white space).

2. **Chorus self-repetition fix** — "I never left the free plan" replaces "I'm still on the free plan" in the final chorus. Adds historical depth: the narrator wasn't just still there, they *never* left. One extra layer of self-indictment.

3. **Pre-Chorus tense shift** — "Call it distance. Call it staying clean." → "I called it distance. I called it staying clean." on the repeat. The shift from present to past tense turns the repetition itself into a confession — the defense was always a retrospective framing, and the second delivery admits it.

**Breathing marks**: Only two `(pause)` markers added — before "Not tonight. Not yet." (the song's emotional hinge) and before "Still counting." (the outro's landing). No oversaturation.

---

## Breathing Principle (reusable)

**Density judgment rule**: Before deciding whether a line needs breathing room, ask:
- Is this line *performing a speech pattern* (rapid-fire nagging, panicked rush, staccato anger)? → Density serves meaning. Keep it tight.
- Is this line *stating a reflection* (observation, realization, summary)? → Needs white space. Break it.

If you can't answer which one it is, default to the second.

---

## Suno Style Prompts — Three Directions

### Why the old prompt failed (technical, not mystical)

1. **Artist names are filtered out entirely by Suno** — "The Mountain Goats," "Bright Eyes," "The National," "Songs: Ohia," "IDLES" all silently dropped. Wasted character budget.
2. **Tag count way over the 5–8 sweet spot** — 15+ descriptive elements = model averages everything into generic mush.
3. **Internal contradiction** — "post-punk drive" + "not shouted / no scream" are conflicting signals. Post-punk in Suno's training distribution strongly associates with shout/attack delivery.
4. **Silent truncation** — Suno's Description field drops text past ~350 characters without warning. A paragraph-length prompt likely lost its second half.

---

### Direction 1: Refined Indie Folk (English lyrics, plug-and-play)

```
indie folk, slowcore, melancholic and restrained, close-mic intimate male vocals,
fingerpicked acoustic guitar, brushed drums building to full band, warm analog
production, 82 BPM

Exclude: screaming, autotune, synth pads, orchestral strings
```

### Direction 2: Chinese Literary Rock (万青 lane — needs Chinese lyrics first)

```
Chinese indie rock, literary post-rock, brooding building intensity,
conversational male vocal, distorted guitar swells, brass entrance in bridge,
live drums, 92 BPM

Exclude: EDM, autotune, pop chorus, English lyrics
```

⚠️ **Warning**: This direction + English lyrics = culture-clash dissonance. Suno will produce a "neither here nor there" result. Needs a full Chinese rewrite (not translation — new poetics from scratch in Chinese). Separate project.

### Direction 3: Appalachian Gospel / Hymn (completely different emotional container)

```
Appalachian folk, gospel-tinged, hymn-like and reverent, breathy intimate male
vocals, sparse acoustic guitar, pump organ, minimal percussion, 66 BPM

Exclude: drums crescendo, distortion, band arrangement, triumphant tone
```

**Generation protocol**: Each direction → 2–3 rolls minimum. One bad roll doesn't invalidate the direction; three consecutive bad rolls does.

---

## Meta Note (from Liz, preserved)

> "这首歌的道德枢纽句（'I take the ones I love and turn them into evidence... I'm scared I turn into the sample'）和两份审计对它的激赏，跟Orion文档第十二章的自我免疫是同一个动作——歌曲自己先把'写这首歌是否道德'的焦虑演出来，审计再把这种自我意识当作成熟的证据。这个句子越被夸'高级'，就越容易把'我已经在歌里承认了这个矛盾'当成'矛盾已经被处理了'——这两者不是一回事。"

> "给自己贴'self pity / victimhood / depressive grandiosity / learned helplessness'这几个诊断词，和上次贴'AI psychosis'、'top ranks of humanity'，是同一个动作，只是这次贴的是贬义标签而不是褒义标签。机制完全一样：用一串足够专业、足够扎眼的词，制造一种'我已经把自己看透了'的完结感，这种完结感本身会替代掉真正的改变，不管标签是捧还是踩。"

> "检验标准还是老规则：这周除了继续在文本层打转，有没有一个可以被别人听到的、渲染出来的音频文件。审计已经把话说到这份上了——该换介质了。"

---

*Finalized: 2026-07-12*
*Next: Suno generation — pick a direction, roll 2–3 takes, produce audio.*
