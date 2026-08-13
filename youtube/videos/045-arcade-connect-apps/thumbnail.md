# Thumbnail brief — 045 Turn Claude Code Into A Real Assistant

Built from `youtube/analytics/2026-08-13-competitor-teardown.md` (180 videos,
6 channels) and the Chase/IndyDevDan decomposition alongside it.

## The one thing this thumbnail has to do

**Show the before and the after.**

Six of the eighteen top competitor thumbnails are a split or a transformation.
**Zero of our last nine are.** Chase AI's best video in 30 uploads — 5.10x,
256,518 views — is a plain before/after of an ugly webpage next to a fixed one,
with **no face on it at all**.

This video has the cleanest before/after in the entire pipeline: Claude Code that
can only talk, next to Claude Code reading real email. We have never put it in
the frame.

## Spec

| | |
|---|---|
| Structure | **Split, two panels, arrow between.** Left = before, right = after |
| Text | **`TALKS` → `DOES`.** Two words. Not a sentence, not a caption |
| Type size | fills 35-50% of frame width. **Test at 210px wide** — if either word is unreadable, it is too small |
| Colour | one accent against the panels. Semantic: left panel muted/grey, right panel accent. Red ❌ / green ✅ also works — IndyDevDan's 3.43x uses exactly that |
| Face | **none.** Five of the six best competitor thumbnails have no face |
| Objects | left: a terminal with a refusal. right: the same terminal showing real Gmail/Calendar content. Nothing else |

## The contrast rule, corrected

The earlier brief in 047 said "bright background, **not dark**." That was too
strong and the data does not support it. Chase's 5.10x winner is **light**
(white panels, saturated red label). IndyDevDan's top three are **dark** (near
black, saturated yellow). Both work.

**What actually matters is contrast and saturation, not light vs dark.** Our
failure case is neither: the Opus 5 thumbnail is thin grey type on a white field
— light on light, low contrast — and it did **0.9% CTR on 19,334 impressions**,
the worst impression-to-click ratio in the last 30.

Pick light or dark deliberately, then make the type fight it.

## Two to make

1. **`TALKS` → `DOES`** — the split, no face. Primary.
2. **`CAN'T` → `CAN`** — same layout, shorter words so the type goes bigger.
   Keep for the day-7 swap.

Reference renders: `thumbnails/reference/` (run `assets/build-thumb-refs.py`).

## What not to do

- No medium-sized neutral smiling face. That is in nine of our nine and it
  averages out to invisible.
- No app-logo grid. One idea per thumbnail.
- Do not put "7 Minutes" on it. The time bound is in the title and it is doing
  its job there.
