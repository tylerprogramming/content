# Thumbnail brief

## Reference: Chase AI, "How I Turned Claude Into My Personal Assistant"

![reference](reference-thumbnails/chase-personal-assistant.png)

**Layout.** Centered, single column. Text stacked above and below one graphic.
Enormous empty margins, maybe 70% of the frame is background.

**Colour.** Off-white, very light warm grey, with visible paper grain and a few
scuff marks. One accent: terracotta orange, roughly `#D2694A`. No third colour.

**Typography.** Black, lowercase, geometric sans, fairly light weight. "it
does" on top, "everything" below, both centred. Text is small relative to the
frame, which is unusual and is the whole point.

**Visual elements.** A single terracotta asterisk or starburst, hand-drawn
feel, uneven arms, with a soft drop shadow. Nothing else.

**Face.** None.

**Composition.** Extremely minimal, deliberately anti-thumbnail. It reads as an
editorial print ad rather than a YouTube tile.

**Why it gets clicked.** Pattern interrupt. In a browse row of loud, red-arrow,
shocked-face thumbnails, near-white and near-empty stops the scroll. The claim
is also maximally broad, which is the weakness we can exploit.

**What it gives up.** No product shot, because his system is invisible: skills
and an Obsidian vault do not photograph. And "it does everything" is vague, so
it promises nothing specific.

---

## Our advantage

The HUD is genuinely photogenic. Dark background, cyan lines, particle brain, a
ring of agents. **No competitor in this lane has an artifact worth showing.**
So where Chase went minimal out of necessity, we can go specific out of
strength.

The title carries "learns from its own mistakes," so the thumbnail should carry
the *thing*, not repeat the words.

---

## Three concepts

### A. The HUD, hero shot (differentiator play)
Dark navy, almost black. The Jarvis interface at a slight three-quarter angle
so it reads as a screen rather than a screenshot, cyan glow spilling onto the
background, particle brain visible at centre. Deep empty space in the left
third for text overlay. High contrast, small-size legible.

Text later: **IT LEARNS** or **IT REWROTE ITS OWN RULES**

*Why:* leads with the thing nobody else can show.

### B. Tyler plus the HUD (channel consistency)
Tyler on the right third, lit cool, looking at a large dark screen showing the
Jarvis interface on the left. Cyan rim light on his face from the monitor.
Background falls off to near black. Left third of the frame kept clear.

Use `--reference-images ~/content/youtube/tyler-reference-images/tylerai.png`

*Why:* faces still outperform on browse for a channel this size, and the cyan
rim light ties it to the product.

### C. The quiet counter (steal his move, aim it better)
Near-black instead of near-white, same restraint. One small cyan glowing node
with two or three lines radiating into a loop that returns to itself. Vast
empty space. Feels like a diagram, not a dashboard.

Text later: **THE PART EVERYONE SKIPS**

*Why:* same pattern-interrupt logic as the reference, inverted to our palette,
and the closed loop is a literal picture of the differentiator.

---

## Prompt notes

- No text in the generated image. Overlay is added afterward.
- Keep one focal point and leave a third of the frame clear.
- Cyan on near-black is the palette. Avoid the terracotta-and-cream look, it is
  Chase's and it is also the current AI-default house style.
- Test every candidate at 20% size before choosing.

## Generate with

```bash
python3 ~/.claude/skills/yt-thumbnail/generate_thumbnail.py "<prompt>" \
  --count 1 --resolution 2K --slug 043-jarvis-that-learns --aspect-ratio 16:9
```

Roughly $0.09 per image at 2K. Three concepts is about $0.27.
