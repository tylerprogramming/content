# Thumbnail brief, video 062

Reference files: `reference-thumbnails/paul-lipsky-9RYDaLnB6ec.jpg` (288k views), `reference-thumbnails/riley-brown-WXhOxfPECnM.jpg` (128k views). Copied from the researcher's pull, not re-downloaded.

## Reference A: Lipsky, "I Get It Now"

| | |
|---|---|
| Layout | Text top-left across 60% of width, laptop bottom-left, face right third, yellow arrow from text to laptop |
| Colors | Dark studio background, white bold text, yellow arrow, bright plush dots on a black laptop screen, dark red shirt |
| Typography | Heavy sans, title case, white with soft shadow, 3 words |
| Elements | MacBook showing the "dots" wordmark and 12 plush dot characters |
| Face | Big smile, pointing at the laptop, eyes to camera |
| Composition | Classic "person presents object." The arrow is the only motion |
| Why it clicks | The plush dots are OpenAI's own brand asset, so recognition is instant. "I Get It Now" promises a reframe without saying what it is |

## Reference B: Riley Brown, "I'M OBSESSED"

| | |
|---|---|
| Layout | Face fills the left 45%, phone in hand on the right, text across the top right |
| Colors | Warm brown background, yellow caps text, black phone, rainbow "dots" wordmark and waveform |
| Typography | Condensed caps, yellow, 2 words |
| Elements | Phone with wordmark and voice waveform, 4 plush dots peeking in from the edges |
| Face | Neutral, close, direct eye contact. Not smiling |
| Composition | Face and object share the frame equally. Dots are decoration |
| Why it clicks | Yellow on dark reads at 210px. Face is huge. Waveform says "voice" without a word |

What both share, from the researcher's 5-thumbnail read: 4 of 5 use the plush dots, 4 of 5 have a face, 0 of 5 show a real screen doing real work. That is the open spot.

## Our rule check (packaging-rules.md)

- The video has a before and after: it has a side by side. Packaging rules: "if the video contains a before and an after, that is the thumbnail." So the primary concept is a split.
- 2 to 4 words, type at 35 to 50% of frame width, one object.
- Face: absent, or large and reacting. Not a medium neutral smile.
- Money is allowed in the thumbnail, not the title. "$100" can go on the Dot side if Tyler wants it.
- Feed check at 210px before choosing.

## Concept 1 (primary): the split

Left half: one plush dot (OpenAI's asset, one only) over a Slack DM bubble, label "DOT". Right half: the Hermes bot avatar over a Slack DM bubble, label "MINE". Thin vertical seam. Text across the top, 3 words: "SAME JOB. BOTH." or "SAME 3 JOBS". No face. Dark background, the two bubbles are the only light.

Why: it is the before/after shape the rules say is missing from the channel, and it is the thing 0 of 35 videos show.

## Concept 2: face plus the split

Same split in the left two thirds. Tyler's face in the right third, large, eyebrows up (reacting, not smiling). Text: "DOT vs MINE" across the top of the split. Use this if the video sells on trust rather than curiosity; it is the Chase "OPUS 5" composition.

## Concept 3: the receipts table

One real screen: the two Slack messages stacked, timestamps visible (7:45 and 7:46), both delivering the same brief. Text: "WHO WON?" in yellow, bottom right. No face, no plush dot. The most honest option and the hardest to read at 210px, so only if the feed check passes.

## Prompts for generation (Step 6, ask Tyler first, ~$0.09 per image at 2K)

No text in any prompt; the overlay is added after. Leave the top 25% empty.

1. Reference style: "Dark studio desk, two chat bubbles side by side on a black screen, left bubble glowing teal, right bubble glowing orange, thin vertical divider between them, cinematic rim light, shallow depth of field, 16:9, empty space across the top for a title."
2. With face (use `--reference-images ~/.hermes/profiles/packager/skills/yt-package/scripts/tylerai.png`): "Man in his thirties with short hair, eyebrows raised, looking at the camera, right third of frame, dark studio background, on the left two thirds a split screen with two glowing chat windows, one teal, one orange, 16:9, top quarter empty."
3. Fresh take: "A single soft plush ball character sitting on a MacBook keyboard next to a small terminal window with green text, overhead desk shot, dark wood, warm lamp light, 16:9, large empty area top left."

Command:

```bash
python3 ~/.hermes/profiles/packager/skills/yt-package/scripts/generate_thumbnail.py "<prompt>" --count 1 --resolution 2K --slug openai-dots --aspect-ratio 16:9
```

Not run. Tyler decides.
