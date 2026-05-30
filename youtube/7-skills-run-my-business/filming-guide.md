# Filming Guide: 7 Claude Code Skills

**Target runtime:** 30-35 min
**Estimated filming time:** 90-120 min (including b-roll captures)
**Setup:** Desk camera + terminal screen recording. Lapel mic.

---

## Pre-Production Checklist

- [ ] Clean terminal — clear scrollback, set tab to "tyler@home" or similar
- [ ] Confirm all 7 skills work end-to-end without errors (do a dry run today)
- [ ] Create a "demo" folder under `~/content/youtube/_filming-demos/2026-05-17/` for any test outputs that will appear on screen
- [ ] Have a transcript from a fresh `/yt-search` run cached so `/transcribe` can complete in <30 sec on camera
- [ ] Clear `~/.claude/projects/` cache if any sensitive context might appear in `/transcribe` output
- [ ] Camera: 1080p min, 4K preferred. Static shot, face dead-center, eyes at the top third
- [ ] Screen recording: OBS or QuickTime. 1080p. Cursor highlight enabled
- [ ] Lighting: face-light at 45°, no overhead, no window backlight

---

## Shot List (in script order)

### Segment 0 — Cold Open (0:00-0:20)
- **Terminal capture:** type `/` slowly, let autocomplete show full list of 43 skills. Scroll through it.
- **VO:** record voiceover separately, layer over the terminal cap in edit
- **Montage prep:** capture 5-sec clips of each of the 7 skills firing (just the command + first 2 sec of output) — these become the 1-sec montage cuts

### Segment 1 — Setup (0:20-1:30)
- Face to camera, eye-line down the lens
- High energy, fast cuts every 6-10 sec
- No notes visible — riff from outline only

### Segment 2 — Skill 1 `/yt-search` (1:30-6:00)
- Face to camera for setup
- Switch to terminal recording for demo — type the command live, no editing tricks
- Show the report markdown opening in Finder or VS Code
- Cut back to face for the "why it matters" segment

### Segment 3 — Skill 2 `/transcribe` (6:00-10:30)
- Same pattern: face → terminal → face
- Use a fresh YouTube URL pulled from the `/yt-search` report (continuity matters — viewer should see the same content flowing through the pipeline)

### Segment 4 — Skill 3 `/yt` (10:30-15:30)
- This is the heaviest lifting skill — give it the most camera time
- When the skill asks the clarifying question, answer it on camera so viewer sees the interaction
- Show the resulting folder filling up with all the files — speed-ramp this in edit if it takes more than 2 min in real time

### Segment 5 — Skill 4 `/seo` (15:30-18:30)
- Show the before/after title comparison clearly on screen
- This is the shortest segment — keep it tight

### Segment 6 — Skill 5 `/shorts` (18:30-22:30)
- Show the resulting 5 folders in Finder
- Open one of the script.md files briefly to show the format
- Don't read every script — just show the structure

### Segment 7 — Skill 6 `/content` (22:30-26:30)
- Show the `/social/` folder filling up
- Quick scrub through each platform's file — 3-5 seconds each
- Highlight the platform-native differences (hashtag counts, no markdown for LinkedIn, etc.)

### Segment 8 — Skill 7 `/skool` (26:30-30:00)
- Show the actual Skool dashboard open in a browser, with the post appearing after the skill runs
- B-roll of the SQLite database in TablePlus or DB Browser for the member sync

### Segment 9 — Workflow Tie-Together (30:00-33:00)
- Use a whiteboard, animated diagram, or just a clean markdown file on screen
- Walk through the Monday morning routine
- If possible, do a Remotion animation here (see ai-video skill) — chained boxes lighting up as each skill fires

### Segment 10 — How to Build Your Own + CTA (33:00-35:00)
- Open a SKILL.md file in VS Code
- Walk through the 4 frontmatter fields and the body
- End on direct-to-camera CTA with high energy

---

## Energy Cues

| Segment | Energy | Notes |
|---|---|---|
| Cold open | 10/10 | Hook lives or dies here |
| Setup | 7/10 | Setting the stakes, building trust |
| Each skill setup | 7/10 | Lead with the problem |
| Each skill demo | 5/10 | Let the screen do the work |
| Each skill payoff | 8/10 | Sell the value |
| Workflow segment | 9/10 | The "aha" moment |
| CTA | 10/10 | Get the click |

---

## Common Mistakes to Avoid

1. **Don't read the script.** Use it as a map, riff the lines. Sounds 10x better.
2. **Don't apologize on camera if a skill takes a second.** Cut the pause in edit.
3. **Don't mention every skill in the cold open.** Save the payoff for each segment.
4. **Don't show your CLAUDE.md or any sensitive `.env` content.** Verify before recording.
5. **Don't blur through the demos.** The demos ARE the video. Let them breathe.

---

## Post-Production Notes

- Chapters timestamps already in script.md — copy to YouTube description
- Run `/chapters` on final cut to validate timestamps
- Thumbnail brief: dark BG, "43 → 7" giant text top-left, Tyler face right side, orange Claude asterisk anchor bottom-right
- Send to editor with: "Tight cuts, jump cuts allowed, no music under VO during demos, music allowed under face-to-camera segments only"

---

## Pre-Filming Final Check (the morning of)

- [ ] Battery charged (camera + mic)
- [ ] 64GB+ SD card formatted
- [ ] OBS scenes set up: Face Cam, Terminal, Browser
- [ ] All 7 skills smoke-tested in the last 24 hours
- [ ] Coffee + water on the desk
- [ ] Phone in another room
