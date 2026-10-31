# Thumbnail brief, video 063

Reference files: `reference-thumbnails/riley-brown-ZIBI6FiLxgQ.jpg` (106,416 views, "I'M HOOKED"), `reference-thumbnails/peter-yang-D-pz8L1orVI.jpg` (91,399 views, "Claude Duet"). Copied from the researcher's pull (`research/2026-10-27-claude-duet-thumbnails/`), not re-downloaded.

## Reference A: Riley Brown, "I'M HOOKED"

| | |
|---|---|
| Layout | Face dead center, hands on a keyboard at the bottom, Duet icon in a glass tile left, Claude asterisk in a glass tile right, dashed white arc over the top connecting them |
| Colors | Near-black background with warm orange rim light, orange icons, yellow text in a dark glass pill |
| Typography | Heavy condensed caps, yellow, 2 words, in a rounded dark pill across the lower third |
| Elements | Two app icons as 3D glass tiles, a keyboard, the arc |
| Face | Neutral, direct eye contact, lit from the front. Not smiling, not reacting |
| Composition | Symmetric. Person between two products. The arc says "these connect" |
| Why it clicks | Yellow on black reads at 210px. Both icons are orange so the whole frame is one color family. "I'M HOOKED" is a verdict without a claim |

## Reference B: Peter Yang, "Claude Duet"

| | |
|---|---|
| Layout | Face center, Claude asterisk tile left, Duet icon tile right, dashed arc over the top, wordmark across the bottom third |
| Colors | Bright, soft-focus home office in daylight, white tiles, orange icons, white text with a drop shadow |
| Typography | Heavy sans, title case, white, 2 words, fills about 75% of width |
| Elements | Two icons, the arc, blurred plants and windows |
| Face | Glasses, slight open-mouth mid-sentence, direct eye contact |
| Composition | Same icon-arc-icon frame as Riley's, light instead of dark |
| Why it clicks | The product name is the whole thumbnail. On launch week that is enough; the icon does the recognition |

What both share, and what the researcher's 6-thumbnail read confirms: the Duet icon (orange circle, black loop) is on 6 of 6; two icons plus a dashed arc appears twice; 5 of 6 have a face; only 1 of 6 (How I AI) shows real product UI; 0 of 6 show the thing Duet made. That is the open spot.

## Our rule check (packaging-rules.md)

- The video has a before and after: the artifact next to the source, with a count. Packaging rules: if the video has a before and after, that is the thumbnail. So the primary concept is a split.
- 2 to 4 words, type at 35 to 50% of frame width, one object.
- Face: absent, or large and reacting. Not the medium neutral smile.
- Money allowed in the thumbnail, not the title. There is no price to show here (included in Pro and Max), so skip it.
- One product logo max. The Duet icon, not Duet plus Claude plus YouTube.
- Feed check at 210px before choosing.

## Concept 1 (primary): the split with a count

Left half: the Channel Pulse dashboard, a real screenshot, slightly angled. Right half: YouTube Studio's Content list, real screenshot. Thin vertical seam. Across the top in heavy yellow caps: "7 OF 10 RIGHT" (use the real count from `receipts.md`; if it is 10 of 10, "10 OF 10" is stronger). Small Duet icon bottom left as the only logo. No face. Dark background behind both screenshots so the yellow type carries.

Why: it is the before/after shape the rules say is missing from the channel, it shows the output (0 of 6 do), and the number is the promise. The 210px risk is the screenshots turning to mush; keep them large and crop to the table rows.

## Concept 2: face plus the artifact

Left two thirds: the dashboard screenshot, big. Right third: Tyler's face, large, eyebrows up, looking at the dashboard, not the camera (reacting, not posing). Text across the top in yellow: "IT BUILT THIS". Duet icon small, bottom left. Chase "OPUS 5" composition.

Why: the video sells partly on trust (Tyler checking the work), and the face says "I looked at it." Use this if Concept 1 fails the 210px check.

## Concept 3: the card

One real screen: the approval card from step 7, cropped tight, the Approve button visible. Text, bottom right, yellow: "IT ASKED FIRST". No face, no second logo. Nobody has shown this screen.

Why: the most honest option and the most novel. Also the hardest to read small, and it only exists if PRE-BUILD 6 produced a card. Third choice.

## Prompts for generation (Step 6, ask Tyler first, about $0.09 per image at 2K)

No text in any prompt; the overlay is added after. Leave the top 25% empty. Concepts 1 and 3 are real screenshots and should be composited by hand, not generated; only Concept 2 and a backdrop plate benefit from generation.

1. Reference style (dark backdrop plate for Concept 1): "Dark studio desk from above, two glowing laptop screens side by side showing data tables, left screen warm orange tint, right screen cool white tint, thin vertical gap between them, cinematic rim light, shallow depth of field, 16:9, top quarter of the frame empty and dark."
2. With face (Concept 2, use `--reference-images ~/.hermes/profiles/packager/skills/yt-package/scripts/tylerai.png`): "Man in his thirties with short hair, eyebrows raised, looking to his left at a large glowing dashboard on a monitor that fills the left two thirds of the frame, dark room, orange accent light from the monitor on his face, 16:9, top quarter empty."
3. Fresh take: "A single small orange circle app icon glowing on a dark desk next to a printed spreadsheet with a red pen check mark on three rows, overhead shot, warm lamp light, 16:9, large empty area across the top."

Command:

```bash
python3 ~/.hermes/profiles/packager/skills/yt-package/scripts/generate_thumbnail.py "<prompt>" --count 1 --resolution 2K --slug claude-duet --aspect-ratio 16:9
```

Not run. Tyler decides.
