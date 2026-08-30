# 028 re-test, 2026-08-19

All six rounds re-run through Kie.ai with the exact prompts from `../test-prompts.md`.
Reference photo: `~/social-studio/images/likeness/tyler.png`. 17/17 generations succeeded.
Raw timings in `results.json`.

**These are fresh generations, not frames from the video.** Where they disagree with what was
said on camera, that is the interesting part, not an error.

## Speed (Round 5 data)

| Model | n | Median |
|---|---|---|
| Nano Banana Pro | 8 | 91.6s |
| GPT Image 2 | 8 | 92.6s |
| Seedream 4.5 | 1 | 206.2s |

Flagships are now a dead heat. The budget model was **more than twice as slow**, which inverts
the usual assumption that cheap means fast. Fastest single run was Nano on the quote graphic
(34.5s); slowest was Seedream on the thumbnail (206.2s).

## Round 1 - thumbnail with likeness

Both held the likeness and both rendered `NOT DETHRONED` cleanly. Nano stayed on brief: the two
images being pointed at are AI/robot subjects. **GPT drifted** and put a fantasy castle in one
frame, which is not "two glowing AI-generated images." GPT was faster (53.4s vs 87.5s).

Edge: Nano, on brief-following. Not on text.

## Round 3 - exact short text

**Tie.** Both rendered "Consistency beats intensity." exactly, on cream, with a minimal line icon
and real negative space. No legibility gap at this length.

## Round 6a - dense infographic (the gotcha)

**GPT wins, clearly, and the reason is not rendering.**

Nano produced a fully legible three-column layout. Every word readable, clean type. But the
content is **false**: it described Nano Banana Pro as "Fast, Local Processing (Edge-optimized)",
"Open Source Foundation" and "Free (Community / Self-Hosted)". It is a paid cloud model from
Google. It appears to have inferred all of that from the word "Nano".

GPT got the vendors right (Google / OpenAI / Midjourney, Inc.), used real logos, gave plausible
pricing, and added its own "pricing may change" disclaimer. Its one slip is a stale
"Prices as of May 2024" line.

## What changed since the video

The video's verdict was: GPT wins on complex text and fact-checked infographics, Nano wins for
creators. **That still holds.** What has moved is the boundary:

- "GPT wins on text" is now only true for **dense, factual** text.
- **Short display text is a tie.** Thumbnails and quote graphics are no longer a reason to pick GPT.
- The real differentiator on an infographic is not legibility, it is **factual grounding**. A model
  can render text perfectly and fill it with confident nonsense.

That last point is the post. Nobody covers it, and it is the failure mode that actually costs you,
because a beautiful wrong infographic ships and a blurry one does not.

## Do not reuse the R6a output as fact

`r6a-nano.png` contains false claims about real products. It is evidence of a failure mode, not a
reference. Never post it without saying so.
