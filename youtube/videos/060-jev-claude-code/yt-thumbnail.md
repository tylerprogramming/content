# Thumbnail, video 060

Reference thumbnails saved in `reference-thumbnails/` (Isenberg, Theo, Witteveen; from the 09-23 yt-search pull).

## Reference: Greg Isenberg (619,961 views)

| Element | What it is |
|---|---|
| Layout | Left two thirds: "Jev" wordmark top-left plus a black rounded app tile with the white TypeSafe cube logo on a black pedestal, a gold 3D crown tilted on the tile's corner. Right third: face |
| Text | One word, "Jev," white bold sans, about 30% of frame width |
| Colors | Magenta to black radial background, hot pink neon glow under the tile, gold crown as the only warm accent, white shirt |
| Face | Large, right third, glasses, open-mouth smile, hand on chin (the "thinking" pose), looking at camera |
| Objects | One (the tile). The crown is a modifier on it, not a second object |
| Why it clicks | The word Jev is the whole search term at 30% width. The crown says "winner" without a word. One object, one face, high saturation on dark |

Theo and Witteveen do the same thing: pink flat with the wordmark and eyes up; orange flat, no face, "Jev / SYSTEM 1 IS HERE / CLASSIFICATION." All three put "Jev" at about 30% width. That is the lane, and it is crowded.

## What the packaging rules say

- If the video contains a before and an after, that is the thumbnail. Stop looking. This video is a before and an after.
- 2 to 4 words, type at 35 to 50% width, one object, face absent or large and reacting.
- Zero of our last nine thumbnails are a split. This one should be.

## Concepts for ours

### Concept 1: the two `real` lines (RECOMMENDED)

Split frame. Left half dark terminal, one line of output: `real  [N]s`. Right half the same terminal, `real  [N]ms`. A thin vertical seam. The word "JEV" in the right half only, white, about 40% of that half's width. No face. That is Chase AI's 5.10x composition (ugly page / fixed page) applied to a terminal.

Words: 3 ("JEV" plus the two numbers). Numbers are the [VERIFY] ones; render after the run, never before.

### Concept 2: split with Tyler reacting

Same split, but the seam is Tyler's face, large, right third, eyebrows up, looking at the right pane. Type "SAME DECISION" across the left two thirds at 40% width, "JEV" small under it. Use if the video ends up asking for trust more than the split alone gives.

### Concept 3: the 1.19

Dark field. Three lines of huge white type, stacked: `0.72`, `+ 0.47`, `= 1.19`, the last one in red. "JEV" small top-left. No face. This is the honesty beat as a thumbnail. Risky: it does not say what the video is about, and the packaging rules say the promise beats the puzzle. Keep as a swap candidate after day 7 if concept 1 underperforms (strategy change, not a reword).

## Feed check

Render every candidate at 210 px wide before choosing. If a number is unreadable at 210, drop to two words.

## Prompts (Step 6 of the skill; ask Tyler before spending, about $0.09 per image at 2K)

1. Reference style: "Split-screen YouTube thumbnail, two dark terminal windows side by side divided by a thin vertical line, left terminal shows a long slow process bar in dull grey, right terminal shows a single short bright green line, magenta and black gradient behind both, high contrast, no text, empty space in the upper right for an overlay."
2. With Tyler's face: "Split-screen YouTube thumbnail, dark terminal on the left with a dull grey progress line, dark terminal on the right with a single bright green line, a man with short hair in the right third looking at the right terminal with raised eyebrows, hot pink rim light, high contrast, no text, room at the top for a title overlay." Use `--reference-images ~/.hermes/profiles/packager/skills/yt-package/scripts/tylerai.png`.
3. Fresh take: "Minimal dark YouTube thumbnail, one giant glowing white toggle switch in the center flipped to the right, left side of the switch dim and slow with a small hourglass icon, right side bright with a small lightning icon, magenta glow, no text, no face, empty space top and bottom."
