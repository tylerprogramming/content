# Instagram Carousel Styles

Three carousel looks worth stealing from, pulled off the feed 2026-08-12/13.
Swipe files: `platform/instagram/swipe/2026-08-13/`.

Every hex below was **sampled from the pixels**, not eyeballed off a screenshot.

## Handle [confirmed 2026-08-13]

Every carousel, every platform: **@tylerreedai**. The older decks print
`@tylerai_dev`, which is not the account anything posts to. Fix it in the deck
data before rendering; leave already-published archives as they went out.

## Captions [confirmed 2026-08-13]

- **Under 40 words**, then five hashtags. The carousel is the content; the
  caption's only job is to get the comment.
- The two references that out-saved us both run 5 to 6 word captions.
  @ibraviz.ai's is literally "Comment JARVIS for the setup!" against 4,026
  comments and 10.4K saves. Ours have been 180 to 197 words.
- Reach explains part of that gap, so this is a strong prior rather than a
  proven cause. It costs nothing to test and the direction is one way.
- Tags in slots, three fixed and two per post:
  `#claudecode #aiagents #ai #<topic> #carousel`

  The topic slot is copied from @ibraviz.ai, the only reference whose tags were
  visible (`#claude #claudecode #ai #jarvis #reel`). Four of their five name the
  tool or the category; the fifth names the subject, which is the one reaching
  people searching for the thing rather than the software. Swap it every post:
  `#mcp`, `#arcade`, `#claudeskills`, `#obsidian`.

  `#aiagents` is a deliberate bet, not an observation - it appeared on no
  screenshot. It is there because it is the category to be found in. If a post
  is not about agents, swap it rather than leaving it in out of habit.

## The natural experiment sitting in here [confirmed 2026-08-13]

Two of these three are the *same carousel*. @ibraviz.ai and @theromanknox both
posted a "JARVIS OS" build, days apart, with the same slide order (What This Is
→ Why It Works → The 4 Parts You Need), the same four components (Claude Code =
engine, Obsidian = memory, local voice, the HUD), and in places the same
sentences: "One voice. Every workflow. Zero tabs." / "No context switching, no
lost notes, no database, just markdown." / "Focus on wiring, not busywork."

Same content, same week, same comment-gated CTA. The results were not close:

| | ibraviz.ai | theromanknox |
|---|---|---|
| Likes | 7,254 | 337 |
| Comments | 4,026 | 225 |
| Saves | **10.4K** | 270 |
| Saves per like | **1.43** | 0.80 |

**Read this carefully rather than as proof.** I do not have follower counts for
either account, and ibraviz appeared as "Suggested for you", meaning Instagram
was actively pushing it. Most of a 21x like gap is probably reach, not craft.

The number that survives that objection is **saves per like**: 1.43 vs 0.80.
That ratio is roughly reach-independent, and it says people who saw the blue
version were nearly twice as likely to file it away. A carousel is judged on
saves. That is the metric to copy toward.

**Sharper point for us:** this format is already being cloned in the wild, on
our exact topic, while our own Jarvis video is unshot. The topic is proven and
contested. Being late to it is the risk, not being unoriginal.

---

## Style A — "Electric" (@ibraviz.ai) [confirmed 2026-08-13]

The one Tyler picked. Product-documentation look: it reads like a spec sheet
someone spent money on.

**Palette (sampled)**

| Role | Hex |
|---|---|
| Background | `#FCFCFC` near-white, with a faint `#F0F0F6` graph-paper grid |
| Ink | `#0A0A0A` |
| Accent | `#2454F0` electric royal blue |

**Type**
- Headline: heavy grotesque, ALL CAPS, tight tracking, **two-tone across two
  lines** - line 1 ink, line 2 accent blue. "BUILD YOUR / **JARVIS OS**",
  "WHAT / **THIS IS.**", "WHY IT / **WORKS.**". The full stop is part of it.
- Chrome: letterspaced monospace, grey. Top rail reads
  `01 / 10 · JARVIS OS · THE 4-STEP BUILD · swipe →`.
- Asides: blue handwritten script, used sparingly, always as commentary rather
  than information - "by the last step, it runs your whole day →".

**Furniture**
- Rounded pill for the slide counter, blue outline.
- Sticky note top-right: pale blue, tape strip, handwritten. Carries the
  one-line thesis for that slide.
- White rounded-square icon tiles with a soft shadow, line glyphs inside, real
  brand marks where relevant (Claude sunburst, Obsidian gem).
- Real dark terminal/product screenshots with traffic-light dots. **This is the
  credibility move** - it is showing the thing running, not describing it.
- Footer rail, mono: handle left, `SPEAK · ROUTE · REMEMBER · REPEAT` centre
  with the current step highlighted blue, slide number right.
- 10 slides. CTA: "Comment JARVIS for the setup!"

**Why it works:** restraint. One accent colour, one script font, everything
else greyscale. The blue only ever marks the thing that matters on that slide,
so the eye is told where to go. The grid and mono chrome do the "engineered"
work without a single decorative element.

## Style C — "Pixel" (@albert.olgaard) [confirmed 2026-08-13]

The other one Tyler picked. Warm, personable, scrappy - the opposite read from
A, and it is *not* the palette doing the work.

**Palette (sampled)**

| Role | Hex |
|---|---|
| Background | `#F0EAE4` warm cream, over a heavily washed-out photo of a real desk |
| Ink | `#140A14` near-black with a faint purple cast |
| Accent | `#D85424` burnt orange |

**Type**
- Headline: very heavy **condensed** caps (Anton/Druk class), two lines,
  numbered - "1. FAMOUS / **IG CAROUSEL**". Line 2 in orange with a hand-drawn
  double-underline swoosh.
- Body: **monospace, centred, three short lines**, inside a white rounded card
  with a thick orange border. Mono as *body copy* rather than chrome is the
  signature.
- Annotations: black handwritten script with curved arrows pointing at objects.

**Furniture**
- A pixel-art mascot in an orange hoodie, holding a different prop each slide
  (clapperboard, camera, paint roller, trophy), plus a pixel dog.
- Orange asterisk/sparkle motif top-centre.
- Footer: `@handle` bottom-left, `save for later` in script bottom-right - a
  direct instruction for the metric that matters.
- 8 slides, last one pure CTA: "COMMENT "FAMOUS" FOR ALL 5 SKILLS" +
  "100% free of course :)".

**Note before copying this:** our existing `cream` theme is `#F5F0EB` bg /
`#E07355` accent. Style C is `#F0EAE4` / `#D85424`. Those are near-identical.
**We already have this palette.** What is missing is the treatment - condensed
caps, mono body in a bordered card, script-with-arrows, and a mascot. Changing
the hex will achieve nothing; the character does the work.

## Style B — "Copper" (@theromanknox) — recorded, not recommended

Cream over a hex pattern, brown-copper gradient (`#CC8454`), 3D rounded icon
tiles, pinned notes with red pushpins, hand-drawn ellipses circling phrases, a
3D mascot on every slide. Title Case headlines with a ghosted "Step 1:"
watermark behind them.

It is competent and it lost badly to A on identical content. The likely reason
is legibility: a mid-tone copper gradient on cream gives weak contrast at
thumbnail size, and gradients on both the icons and the table make the slide
busy without making it clearer. Kept in the swipe file as the control case.

---

## Rules that fall out of all three [confirmed 2026-08-13]

- **One accent colour.** All three winners use exactly one, and the strongest
  uses it only to mark the important thing.
- **Two-tone two-line headline.** Ink on top, accent underneath. Every slide in
  A and C does this; it is the most portable single element here.
- **Handwritten script for asides only.** Never for information. It signals "a
  person made this" without costing legibility.
- **A card carries the thesis.** Sticky note (A) or bordered mono card (C) -
  one boxed sentence per slide that stands alone if the rest is skimmed.
- **Show the thing running.** A's real terminal screenshots are the difference
  between claiming and demonstrating. We have a HUD that looks better than both
  of theirs and it is the easiest advantage to take.
- **Ask for the save out loud.** "save for later" printed in the footer, every
  slide.
- **Comment-gate the payoff.** All three do it. It is the whole comment count.
- **8 to 10 slides**, last slide a dedicated CTA.

## Where these live in the tooling

- `~/social-studio/themes/*.json` - the real theme system. One JSON per look;
  drop a file in and it appears as a swatch. `electric.json` and `pixel.json`
  added 2026-08-13.
- `~/.claude/skills/instagram-writer/instagram_writer.py` - **has its own
  hardcoded palette** (`#F5F0E8` / `#1C1C1C` / `#C4713A`) and does not read the
  themes folder. It has already drifted from `cream.json` by a few points per
  channel. Fix that before adding a fourth place for colours to live.
