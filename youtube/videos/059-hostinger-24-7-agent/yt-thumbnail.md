# Thumbnail brief, video 059

Written 2026-09-21. References in `reference-thumbnails/`.

## Reference 1: Metics Media, "Hostinger Hermes Agent Tutorial - Full VPS Setup Guide" (21,303 views)
`reference-thumbnails/metics-vps.webp`

- **Layout:** "FULL GUIDE" in huge white block caps across the full top edge. Creator centered, face large, glasses, red beard, open palms out to both sides. Left palm holds the Hermes logo (the black-and-white anime girl tile). Right palm holds the purple Hostinger H tile. A thin white curved arrow goes from the Hermes tile over his head to the Hostinger tile.
- **Color:** dark navy left, purple gradient right (Hostinger brand), white type, blurred dashboard screenshot behind.
- **Face:** present, large, calm half-smile, direct eye contact.
- **Objects:** two product logos plus a face. That is three things competing.
- **Why it clicks:** the arrow says "move this into that", which is the whole promise in one glyph. The face is doing trust work for a 31-minute video.
- **Why it did 21K against 375K:** the general one (below) has one product and the word people search. This one has two logos and "FULL GUIDE" with no product name at all in the type.

## Reference 2: Metics Media, "Hermes Agent - Full Tutorial & Setup Guide (For Beginners)" (375,037 views)
`reference-thumbnails/metics-general.webp`

- **Layout:** left two thirds: Hermes logo tile, "HERMES AGENT" in white block caps on two lines, "TUTORIAL" in dark navy on a bright blue banner, "FULL GUIDE" small underneath. Right third: the creator's face, large, half-smile.
- **Color:** deep navy field, white type, one bright blue banner. High contrast.
- **Why it clicks:** it is the query, printed. One product, one banner, one face. This is the Chase "OPUS 5" composition the packaging rules recommend: huge type left two thirds, face right third.

## Against `packaging-rules.md`

| Rule | Call for 059 |
|---|---|
| Before/after split if the video has one | It does. Before: laptop closed, agent dead. After: phone lit with overnight runs. That is the thumbnail. |
| 2 to 4 words, 35 to 50% of frame width | Yes |
| One object | The phone. Not the phone plus the Hostinger logo plus the Hermes logo. |
| Face absent, or large and reacting | This is an 18 to 20 minute build, not a 30-minute course, so the face is optional. Concept A goes faceless. Concept B keeps a large reacting face for the A/B. |
| Money in the thumbnail, not the title | Yes: the monthly price goes on the image. Verify the number on the Hostinger page the day you export (09-21 pull shows KVM 1 at $6.49/mo promotional, renews $11.99; the Managed Hermes plan shows $5.99/mo, renews $11.99). Use the plan you actually bought. |
| Feed check at 210px | Run `youtube/thumbnails/assets/build-thumb-refs.py` before committing |
| Never the runtime on the image | "20 MIN" stays in the title only |
| Not more than one product logo | Drop the Hostinger H from the image. The title carries "Hostinger". |

## Concept A: the overnight split, no face (RECOMMENDED)

Left half, dim: a closed laptop on a dark desk, small, a faint "zz" or nothing at all. Right half, lit: a phone held up, screen bright, a stack of timestamped chat rows visible. Hard vertical seam. Price sticker in the lower right corner added in the editor. Overlay text top left.

Prompt (no text baked in):
`A dark split composition, left half a closed laptop on a dark wooden desk in dim blue light, right half a hand holding up a smartphone with a brightly lit screen showing a stacked list of glowing chat message rows with timestamps, hard vertical seam between the halves, dramatic dark background, high contrast, cinematic lighting, generous clean space in the upper left for text overlay`

Overlay: `RAN ALL NIGHT` or `WHILE YOU SLEPT`. Price badge: `$6/MO` (verify).

## Concept B: face reacting, Chase composition

Tyler in the right third, looking at a phone he is holding up, eyebrows up, genuine reaction. Left two thirds: dark field with the phone screen enlarged, chat rows glowing. One accent color on the overlay word.

Prompt:
`A software developer on the right third of the frame holding up a smartphone and reacting with raised eyebrows and a surprised smile, the phone screen brightly lit showing a list of glowing chat rows, dark studio background with subtle purple rim light, high contrast, cinematic, leave the left two thirds visually clean for text overlay`

Face reference: `~/.hermes/profiles/packager/skills/yt-package/scripts/tylerai.png` via `--reference-images`.

Overlay: `LAPTOP CLOSED` with an arrow to the phone. Price badge lower left.

## Concept C: the terminal proof, fresh take

No face, no phone. One terminal window center frame showing a cron run log: a column of timestamps, each with a green check. Nothing else. Overlay top: `6 RUNS. 0 LAPTOPS.` (that is five words, so trim to `0 LAPTOPS` if it reads long at 210px).

Prompt:
`A single glowing dark terminal window centered on a dark desk, the screen showing a neat vertical column of log lines each with a small green check mark, soft monitor glow, dramatic dark background, one focal object, high contrast, cinematic product-shot lighting, generous empty space at the top for text`

## Overlay text options (2 to 4 words)

- RAN ALL NIGHT
- WHILE YOU SLEPT
- LAPTOP CLOSED
- 0 LAPTOPS

`WHILE YOU SLEPT` pairs with the recommended title without repeating it. `LAPTOP CLOSED` pairs with Concept B where the image explains it.

## Cost

About $0.09 per image at 2K. Three concepts, one image each, about $0.27. Ask before generating.
