# Thumbnail brief — 047 How To Give AI Agents Access To ALL Your Apps

Rev 2, rebuilt from `youtube/analytics/2026-08-13-competitor-teardown.md`
(180 videos, 6 channels) rather than from the Sabrina read.

**Why rev 1 was rebuilt:** it was derived from Sabrina Ramonov's thumbnails. She
runs **5,970 median long-form views on 353,000 subscribers — 1.7% of subs,
against our 1.4%.** She is in the same hole we are, so her thumbnails are not
evidence. The channels actually performing are Chase AI (31% of subs per video)
and IndyDevDan (22.6%), and they are the two closest to us in size.

## This is the one to keep the face on

Five of the six best competitor thumbnails have **no face**. This video is the
exception, and deliberately: **a course sells on trust.** Someone committing 50
minutes wants to see who is teaching.

So use Chase's `OPUS 5` composition, not his faceless `SLOP → FIXED` one:

```
┌──────────────────────────────┬────────────┐
│                              │            │
│   ANY APP        ← huge      │    face    │
│                              │  (right    │
│   [ 8 app logos in a row ]   │   third)   │
│                              │            │
└──────────────────────────────┴────────────┘
```

## Spec

| | |
|---|---|
| Text | **`ANY APP`** — two words. Full height of the left two thirds |
| Type size | 35-50% of frame width. Test at 210px wide |
| Colour | one accent on a saturated ground. High contrast is the requirement, light or dark are both fine |
| Face | right third, **large and reacting**. Not medium and pleasantly smiling — that is what nine of our nine currently do |
| Objects | one row of recognisable app marks (Gmail, Slack, Calendar, Notion...). This is the single supporting object |

## The contrast rule, corrected from rev 1

Rev 1 said "bright background, **not dark**, dark thumbnails vanish against
YouTube's UI." Too strong, and the data contradicts it. Chase's 5.10x winner is
**light**. IndyDevDan's top three are **dark**. Both work, because both are high
contrast and saturated.

Our actual failure mode is neither: the Opus 5 thumbnail is thin grey type on
white — light on light — and it did **0.9% CTR on 19,334 impressions**.

## Two to make

1. **`ANY APP`** + logo row + face right third. Primary.
2. **`ANY APP`** with no face and the logo row doubled in size — the faceless
   variant, in case the trust argument above is wrong. Keep for the day-7 swap.

Reference renders: `thumbnails/reference/` (run `assets/build-thumb-refs.py`).

## What not to do

- Do not put the course length on it. `55 MIN` is a reason not to click.
- Do not add the Arcade mark. The title deliberately does not say Arcade, and
  the thumbnail should not undo that.
- No near-blank white treatment. That is the 0.9%.

## Benchmark

The four course videos that produced 554 subscribers ran 5.5 to 9.1% CTR.
**Under 5% on this one means the thumbnail, not the topic** — the topic is the
channel's proven best format.
