# Thumbnail brief, video 058

Written 2026-09-15 against `BRAIN/youtube/packaging-rules.md`.

## Reference: Bart Slodyczka, "I Tested OpenAI's New Cloud Agents... What You Need To Know" (16,207 views, top English creator video on the API)
`reference-thumbnails/bart-slodyczka-JFWq93b4_Oo.jpg`

| | |
|---|---|
| Layout | Title text across the full top edge. A fake app window fills the left two thirds below it. Face in the right third, cropped at the chest. |
| Text | "Codex Cloud Agents" (three words, white, heavy sans, about 85% of frame width). Inside the window: "CLOUD AGENTS" under a pixel cloud, "AGENT 01 / 02 / 03" labels, a fake status bar "SYSTEM: ACTIVE | LOG: OK". |
| Colors | Near-black navy background. Cyan glow on the window border and the title. Three blue-to-violet cloud icons with a terminal prompt in each. White pixel cloud in the center. One small red-to-green gauge as the only warm accent. |
| Typography | Heavy geometric sans for the title, monospace for the labels. |
| Face | Yes, large, right third, warm smile, pointing at the window with one finger. Trust-and-tutorial expression, not reacting. |
| Objects | One (the window), but the window contains a triangle of three agents, a cloud, five small icons and dotted lines. Busy inside one frame. |
| Composition | Diagram left, face right. The classic explainer layout. |
| Why it clicks | "Cloud Agents" is a two-word promise, the glowing diagram says "system", the face says "a person will walk you through it". Cyan on black reads cleanly at feed size. |

## Against `packaging-rules.md`

- Words: his three-word title works. We stay at two to four.
- The split is the gap. Six of eighteen top competitor thumbnails are a split, arrow or transformation, zero of our last nine, and none of the fourteen Agents API thumbnails are. **This video has an honest split**: OpenAI's cloud on one side, a Mac on the other, with an arrow between them. That is the story of the video, not an invention.
- Face: absent or large and reacting. At 12 minutes this does not sell on trust, so the faceless split is allowed. Test it against a face version.
- Money belongs in the thumbnail, not the title. The container rate is public and it is the withheld payoff. "$1.92 vs $0" is a candidate overlay.
- One object. The Mac and the cloud are one relationship, not two logos. Do not put an OpenAI logo and a Hermes logo side by side; that is the "two logos competing" failure.
- Feed check at 210px before committing.

## Concept A, the split (RECOMMENDED)

Left half: a glowing cloud with a terminal prompt in it, dimmed, with a small red X or a cost tag. Right half: a MacBook on a dark desk, screen lit with a terminal, one line of green text. A hard vertical seam or a thick arrow from the cloud to the Mac. No face.

Overlay (added in the editor): **YOUR MAC** in the right half, large. Optional small tag on the left: **$1.92**.

Prompt (no text baked in):
`A dark split composition, on the left a large glowing translucent cloud icon with a faint terminal prompt symbol inside it, dimmed and slightly desaturated, on the right a MacBook laptop on a dark desk with its screen glowing with a single line of green terminal text, a thick bright cyan arrow pointing from the cloud to the laptop, hard vertical seam between the halves, near-black navy background, high contrast, cinematic lighting, generous clean space in the upper right for a text overlay`

## Concept B, reference style with Tyler

Bart's layout, ours. A window on the left two thirds showing one terminal line, `codex exec-server`, connected. Tyler in the right third, large, reacting (eyebrows up, not the neutral smile). Cyan glow.

Overlay: **ON MY MAC** or **NO SANDBOX**.

Prompt:
`A software developer on the right third of the frame, surprised and pleased expression, eyebrows raised, looking at a dark app window that fills the left two thirds, the window showing a single glowing line of terminal text and a small green connected indicator, cyan rim light on the window border, near-black navy studio background, high contrast, cinematic, leave the upper left clean for a text overlay`

Face reference: `~/.hermes/profiles/packager/skills/yt-package/scripts/tylerai.png` via `--reference-images`.

## Concept C, the cost card

No face. A single MacBook center frame, screen lit. Above it, two price tags floating: one crossed out, one reading zero. Lots of negative space top left.

Overlay: **$1.92 → $0** as the only text, or **FREE ON YOUR MAC**.

Prompt:
`A single MacBook laptop centered on a dark desk, screen glowing with a terminal, two small floating price-tag shapes above it, one dimmed and crossed with a red line, one bright green, dramatic dark background, one focal object, high contrast, cinematic product-shot lighting, generous empty space in the upper left for text`

## Overlay text options (two to four words)

- YOUR MAC
- NO SANDBOX
- ON MY MAC
- $1.92 → $0 (money is allowed here, not in the title)
- THEIR LOOP, MY DISK (four words, test at 210px)

## Never

- The runtime on the image.
- An OpenAI logo next to a Hermes logo.
- A three-agent triangle diagram. That is Bart's, and it is busy.
- Light-on-light with thin type.

## Cost to generate

About $0.09 per image at 2K via `generate_thumbnail.py`. Three concepts, one image each, is about $0.27. Ask Tyler before running.
