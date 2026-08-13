# Packaging rules — titles and thumbnails

**Read this before writing any title or thumbnail brief.** It is the operational
checklist. The reasoning behind each rule lives in `brain.md` and in
`youtube/analytics/2026-08-13-*`; this file is just the rules.

Every rule here is measured on **Tyler's own channel** or on the six-channel
competitor pull (180 videos), not borrowed from general YouTube advice.

---

## TITLES

### The gate — check this before anything else

**Does the head term have search demand?**

Course framing is a wrapper. The searched term is the engine. Same title shape,
two outcomes:

| | Impressions |
|---|---:|
| Firecrawl Full Beginner Course | 30,981 |
| Claude Cowork Full Course | 4,588 |

Impressions are served *before* anyone clicks, so a 6.8x gap is demand, not CTR.
If nobody searches the head term, the video will not be shown, and no amount of
title craft fixes that.

**How to check:** search YouTube for `<term> course` / `<term> tutorial`. If
established channels have built content on it, the demand is real. If the results
are thin, put a searched term in front instead and move the tool name into the
description.

Contested is fine. Empty is not.

### Then apply, in priority order

1. **Second person, not first.** "How to" / "Full Course" / "For Beginners".
   Seven "I ..." long-form videos: 37,004 impressions, **15 subs**. Zero of the
   four best videos on the channel start with "I".
   - **"I" is allowed only** when attached to an external subject or a stake:
     *I Tested X vs Y* (3.30x), *I asked Claude Code to make me as much money as
     possible* (2.93x). Attached to a personal workflow it dies — *I Built an AI
     Agent That Works While I Sleep* did **0.27x on a 253K channel**.
2. **Transformation verb, not description.** `Turn X into Y`, never `X Explained`.
   This is the single biggest lever in the competitor set: Chase AI does 31% of
   his subscriber count per video and his best is *Turn Claude Into A Design
   GENIUS In 3 Simple Steps* (5.10x, 256,518 views). His channel contains no
   "X Explained" video at all.
   - Compare: his *Turn Claude Into A Design GENIUS* = 256,518 views.
     Ours *Claude Design is Incredible* = 521. Same topic, same lane.
3. **Ease qualifier with a small number.** `In 3 Simple Steps`. The number caps
   the perceived effort — it does not describe the content. Small beats accurate.
4. **One caps word, placed late**, so it lands as the payoff. GENIUS, HUGE,
   INSANE, SOLVED. Note: ALL-CAPS on its own does nothing (1.01x vs 1.00x across
   36 videos). It is table stakes, not an edge — do not count it as the hook.
5. **Second-person accusation** is unused and it works. *You're Paying Anthropic
   20x MORE Than You Need To.* Try it at least once per quarter.
6. **Replacement framing** for anything where we have standing: `FORGET X`,
   `X Is Already Dead`, `This KILLS Y`. IndyDevDan's top five all kill something.
7. **Name the viewer's identity** where it fits: *The Claude Code Feature Senior
   Engineers KEEP MISSING* (1.81x).
8. **Under 70 characters** so nothing truncates on mobile.

### Tyler's own credential — use it

8 years as a software engineer at IBM and Chase, now an AI engineer at Pfizer.
David Ondrej's top three videos are all borrowed authority (*Ex-NASA dev*,
*L8 Principal's setup*, *explained by a 10x developer* — 3.55x / 2.11x / 1.82x).
**Tyler does not have to borrow it.** It currently appears in zero titles, zero
thumbnails and zero hooks across the last thirty videos.

Never write copy implying Tyler is not a developer. He is one.

### Standing prohibitions

- **No money amounts in titles** (`CLAUDE.md`). Money is the strongest single
  pattern in the competitor data at 1.89x, so put it in the **thumbnail and the
  first line of the description** instead. Chase's 5.10x does exactly this.
- **No em dashes** in any content (`BRAIN/tyler-voice.md`).
- **Do not cover a launch late.** A term is won in the first days then closed —
  the Claude Cowork winners published ~10 weeks before we did and we got 4,588
  impressions. Cover news **inside 48 hours and short**, or skip the term and
  spend the slot on an established one.

---

## THUMBNAILS

### The one thing most likely to be missing

**A before/after split.** Six of the eighteen top competitor thumbnails are a
split, an arrow, or a transformation. **Zero of our last nine are.** The single
best video in the whole comparison set — Chase AI, 5.10x, 256,518 views — is a
plain before/after of an ugly webpage next to a fixed one, with no face.

If the video contains a before and an after, that is the thumbnail. Stop looking.

### Spec

| | |
|---|---|
| Words | **2 to 4.** Never a sentence, never a caption |
| Size | type fills **35-50% of frame width** |
| Contrast | high and saturated. **Light or dark are both fine** — Chase's 5.10x is light, IndyDevDan's top three are dark. Our 0.9% failure was light-on-light with thin grey type |
| Structure | a split, an arrow, or old ❌ / new ✅ |
| Face | **absent**, or **large and reacting**. Five of the six best competitor thumbnails have no face at all. Ours is a medium neutral smile in nine of nine, which averages to invisible |
| Objects | **one**. Not a logo grid, not two concepts |

### Keep the face when

The video sells on trust — a course, or anything asking for 30+ minutes. Use
Chase's `OPUS 5` composition: huge type across the left two thirds, face in the
right third. Not the faceless split.

### Always do the feed check

Render at **210px wide** and look at it. That is the size it actually occupies.
If a word is unreadable there, the design is wrong no matter how it looks at full
size. `youtube/thumbnails/assets/build-thumb-refs.py` emits this automatically.

### Never

- The course length (`55 MIN` is a reason not to click).
- A near-blank light field with thin type. That is the 0.9% on 19,334
  impressions, the worst ratio in the last 30.
- More than one product logo competing with the promise.

---

## DURATION — decide before filming, it changes the package

Measured across 89 competitor long-form videos:

| Band | Median outlier |
|---|---:|
| Under 10 min | **1.56x** |
| 10-35 min | ~1.00x |
| **35-60 min** | **0.72x** ← dead zone |
| 60+ min | **2.11x** |

**Ship under 20 minutes, or commit to a real course.** Never 40. Both our
47-minute Cowork course and Chase's 51-minute course landed in the dead zone.

---

## After publishing

Log the title, the thumbnail, the impressions and the CTR in the package's
`performance.md`. **Do not swap a title inside 7 days** — a payoff word buys the
first 72 hours, not the week, and day-1 multiples flatter badly. The Opus 5 video
was swapped at 48-72h and finished at 0.9% on 19,334 impressions; the locked
title was never actually tested and that impression pool is gone.

When swapping, change the **strategy** (outcome-led vs term-led vs accusation),
not the wording. A reworded variant tests nothing.
