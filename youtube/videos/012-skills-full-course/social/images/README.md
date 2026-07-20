# Hero Images - Claude Code Skills Masterclass drip

One 16:9 (1600x900) hero per day. Attaches to X + LinkedIn + YT Community that day. IG uses carousels.
All branded: dark header bar with the day's hook, @TylerReedAI handle bottom-right.

| File | Day | Hook | Source |
|------|-----|------|--------|
| hero_sun.png | Sun | A Claude Code skill is just one file. | real frame @ 01:52 (SEO SKILL.md open) |
| hero_mon.png | Mon | Skills vs MCP vs Plugins | built 3-box diagram card |
| hero_wed.png | Wed | You don't write skills. You ask. | real frame @ 07:45 (Claude writing standup SKILL.md) |
| hero_fri.png | Fri | Same skill. Now running in Claude Cowork. | real frame @ 23:10 (standup skill in Cowork) |

## Regenerate / edit
- Screenshot cards: `python3 build_card.py <frame.jpg> "<hook>" <out.png> [16x9|1x1|4x5]`
- Diagram card: `python3 build_diagram.py`
- To swap a frame, extract with: `ffmpeg -ss <HH:MM:SS> -i "<video>" -frames:v 1 -q:v 2 out.jpg`
- Source video: ~/Downloads/( claude skills masterclass - CAMERA ).mp4

## Notes
- Screenshot on-screen text is small at feed size (it signals "real software" rather than being read). For a readable SKILL.md, re-run build_card.py on a tight-cropped frame.
- build_card.py supports 1x1 and 4x5 if we later want IG single-image versions.
