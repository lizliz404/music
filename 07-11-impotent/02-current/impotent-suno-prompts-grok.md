# IMPOTENT — Suno Style Prompts (Grok 4.5)

**Generated**: 2026-07-12
**Model**: Grok 4.5 (Cursor Agent)
**Based on**: v4 Final lyrics + Kenshi Yonezu production DNA analysis
**Rules**: 5-8 tags, genre-first, no artist names, <350 chars, strong Exclude

---

## Lane A — Art-Rock Precision (Kenshi-core, FINAL)

**Style:**
```
Melodic art-rock, bassline-hook groove, tight drums, male vocals rhythmic precise controlled sung not shouted, abrupt hard section cuts, cold digital synths warm guitars in tension, idiosyncratic constructed structure, clean polished punchy mix, 92 BPM D minor
```
(~250 chars · 8 tags)

**Exclude:**
```
pop-punk, emo, grunge, screamo, metal, belting, raspy vocals, blues rock, stadium anthem, trap, lo-fi, garage rock, anime cheese
```

**Kenshi DNA mapped:**
| Element | Source | Tag |
|---------|--------|-----|
| Bassline IS the hook | Loser (bass enters before vocal) | `bassline-hook groove` |
| Tight propulsive drums | All four tracks | `tight drums` |
| Vocal rhythm as percussion | Loser, Flamingo | `vocals rhythmic precise` |
| Zero transitional smoothing | Loser, KICK BACK, Flamingo | `abrupt hard section cuts` |
| Cold digital + warm organic in conflict | M78, all four | `cold digital synths warm guitars in tension` |
| Sections feel built, not blended | Flamingo, KICK BACK | `idiosyncratic constructed structure` |
| Controlled intensity, never shouted | All four | `controlled sung not shouted` |
| Clean polished production | M78, KICK BACK | `clean polished punchy mix` |

---

## Lane B — Guitar-Forward Alt-Rock (band-room door)

**Style:**
```
Driving alt-rock, guitar-forward groove, male vocals controlled intense sung not shouted, tight dry drums, dense layered chorus, dry stacked doubles, punchy live-band mix, 92 BPM D minor
```
(~185 chars · 8 tags)

**Exclude:**
```
pop-punk, emo, grunge, screamo, metal, shoegaze wash, electronic pop, whisper vocals, blues solo, arena rock
```

**Rationale:** Same song through a rehearsal-room door — guitars and drums carry the charge, doubles thicken the chorus, still no shout. Physical rock energy for "I know the cost, and still I pay it" without emo/grunge defaults.

---

## Lane C — Coldwave / Synth-Noir Post-Punk

**Style:**
```
Coldwave post-punk, sparse synth bass pulse, male vocals close-mic melodic controlled, nocturnal digital atmosphere, sudden full-band locks, dry reverb vocals, idiosyncratic production, 92 BPM D minor
```
(~205 chars · 8 tags)

**Exclude:**
```
pop-punk, emo, grunge, new wave nostalgia, dance-punk shout, industrial metal, trap, soft acoustic folk, arena rock
```

**Rationale:** Phone glow and cold water as the container — sparse pulse, close-mic calm, sudden band lock on the decision line. Replaces rock-band defaults with nocturnal electronic atmosphere. Recognizably different from A and B on first listen.

---

## Reference: Kenshi Yonezu (米津玄師) Production DNA

Tracks analyzed: Loser, KICK BACK, M78, Flamingo

| Signature | Translation for Suno |
|-----------|---------------------|
| Bassline as primary melodic engine | `bassline-hook groove` |
| Tight propulsive drums | `tight drums` |
| Vocal rhythm as percussion | `vocals rhythmic precise` |
| Sudden section cuts, no smoothing | `abrupt hard section cuts` |
| Cold synth + warm organic in tension | `cold digital synths warm guitars in tension` |
| Constructed, section-distinct structure | `idiosyncratic constructed structure` |
| Intensity from arrangement, not force | `controlled sung not shouted` |
| Clean polished production | `clean polished punchy mix` |

**Not used (would overfit to specific tracks):**
- Staccato / syllable-dense → locks into Loser verse mode, fights IMPOTENT's hushed verses
- Chainsaw bass → KICK BACK-specific, too narrow
- Anime-OP → triggers cheese defaults; `tight drums` + `bassline-hook groove` gets the energy without the genre baggage
