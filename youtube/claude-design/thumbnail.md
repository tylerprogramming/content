# Thumbnail Brief — Claude Design Video

## Reference thumbnail analysis

### Chase AI — "Claude Design is INSANE" (190K views)
- **Layout:** Left two-thirds = text + product screenshot. Right third = Chase's face, cropped close, looking at camera.
- **Color:** Warm terracotta/rust background. Grainy texture. White text headline. Orange palette icon on Claude Design logo card.
- **Typography:** Massive white sans-serif headline ("DESIGN KING") at top, all-caps, heavy weight, slight drop shadow for legibility against the terracotta.
- **Visual elements:** Crisp cream rectangle showing the "Claude Design / by Anthropic Labs / Research Preview" UI detail. Small hand-drawn yellow crown doodle sitting on top-left of the card.
- **Face:** Chase smiling, medium crop, right-aligned, looks friendly and confident.
- **Composition:** Clean, minimal. One focal point (the product card), one supporting element (Chase's face), one headline. Lots of breathing room.
- **Why clickable:** Warm earthy palette stands out in a feed of dark tech thumbnails. The crown doodle adds personality. "DESIGN KING" is short, superlative, high-confidence. Pairs novelty ("just launched") with authority ("king").

### Nate Herk — "Claude Design Just Became Unstoppable" (121K views)
- **Layout:** Centered composition. Claude logo/icon dominates the middle with a crown on top. Broken competitor logos (Canva heart, Gamma G) fall apart on either side. Explosion debris at the bottom.
- **Color:** Dark slate/black bg with golden glow radiating from the Claude logo. White headline. Heart icon keeps its pink/purple, Gamma keeps its blue.
- **Typography:** Large white sans-serif "It's over." with a period. Low word count, high impact. Slight shadow.
- **Visual elements:** Glowing crown, halo light behind Claude logo, cracked glass effect on competitor logos, rubble/debris at base, orange/gold lighting.
- **Face:** No face in frame.
- **Composition:** Busy, cinematic, three-element rule (left competitor, Claude center, right competitor). Very YouTube-tech aesthetic.
- **Why clickable:** Dramatic "AI wars" framing. "It's over" is a provocative claim that forces scroll-stop. Visual hierarchy resolves instantly: Claude wins, competitors lose.

## Patterns that work for this topic
- **Crown motif** — both videos used it. Signals "best in category / new king."
- **Short high-contrast headline** — 2-4 words max. ALL CAPS or bold lowercase with period.
- **Product screenshot or logo** — the Claude Design branding element is recognizable and legitimizes the video.
- **Face OR drama** — Chase goes face-forward friendly. Nate goes faceless cinematic. Both work.
- **Warm or dramatic color palette** — the warm terracotta (Chase) and golden-glow-on-dark (Nate) both stand out against the typical cool-blue tech thumbnail sea.

## Differentiation for Tyler's thumbnail
Neither reference communicates **the workflow / handoff**. Tyler's angle is the complete Claude Design → Claude Code flow. The thumbnail should hint at two things coming together (not just Claude Design in isolation).

## 3 Thumbnail Concepts

### Concept 1 — "Reference-mirror" (closest to Chase's style)
Warm orange/terracotta background, grainy. Centered/left: the Claude Design product card (same "Claude Design / by Anthropic Labs / Research Preview" style). Right third: Tyler's face (use tylerai.png), confident half-smile, medium crop, looking at camera. Small visual element: a bold arrow or handoff icon between the product card and a Claude Code terminal mini-icon to communicate "design → code."

**Prompt direction:** Professional man in his late 30s, medium crop right-aligned, confident friendly expression looking at camera, warm terracotta studio background with subtle grain, soft studio lighting, clean composition, two-thirds negative space on the left for text overlay, photorealistic YouTube thumbnail style.

### Concept 2 — "Handoff / bridge" (differentiator)
Dark dramatic background. Centered composition: Claude Design palette icon on the left side fades/streams into a Claude Code terminal on the right. Golden bridge of light connects them. Tyler's face bottom-right, looking up at the transition, expression of focused impressed awe.

**Prompt direction:** Professional man in his late 30s bottom-right of frame looking up with focused expression at a glowing energy stream connecting two floating UI cards, left card shows a design interface, right card shows a dark code terminal, dramatic cinematic lighting, dark background with gold/orange accent lighting, sparks and particles along the connection, photorealistic YouTube thumbnail style.

### Concept 3 — "Split-screen before/after"
Vertical split thumbnail. LEFT half: blank Claude Design canvas with a single UI prompt typed in, warm earthy palette. RIGHT half: the finished live landing page rendered in a browser window with a real URL bar visible. Tyler's face overlaps the vertical seam in the center, medium crop, looking at camera with raised eyebrows (impressed).

**Prompt direction:** Professional man in his late 30s centered in frame medium crop, slight smile and raised eyebrows expression, behind him a clean vertical split of a design prompt interface on the left and a completed polished landing page on the right, soft studio lighting, photorealistic YouTube thumbnail style, warm color grading.

## Text overlay (added in editor after)
Top 3 candidates to overlay on whichever thumbnail we pick:
1. **"DESIGN → SHIP"** (2 words, clear workflow story)
2. **"I SHIPPED THIS IN 23 MIN"** (time-specific, curiosity)
3. **"BUILT & DEPLOYED"** (two verbs, completion)

## Notes for /thumbnail generation
- Use `--reference-images ~/assets/identity/tylerai.png` for all 3
- Resolution: 2K, aspect 16:9
- Model: Nano Banana Pro (best likeness preservation)
- Do NOT include the headline text in the prompt — editor adds it after
