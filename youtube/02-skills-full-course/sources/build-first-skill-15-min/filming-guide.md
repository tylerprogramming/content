# Filming Guide: Build Your First Claude Code Skill in 15 Min

**Runtime target:** 15-18 min
**Filming session:** 45-75 min
**Stack:** OBS, face cam, lapel mic, VS Code, Claude Code terminal

---

## Pre-Production

- [ ] **Delete `~/.claude/skills/meeting-notes/` if it exists** — this needs to be a fresh build for authenticity
- [ ] Verify Claude Code restart picks up new skills cleanly (do a smoke test with a throwaway skill)
- [ ] Clear `~/notes/meetings/` of any real meeting notes, or move them temporarily
- [ ] Create the `~/notes/` parent folder if it doesn't exist
- [ ] OBS scenes: Face Cam, VS Code (with the skills folder open), Terminal (Claude Code session)
- [ ] Have the script's body content in a separate doc you can glance at — don't type from memory

---

## Shot List

### Segment 0 — Cold Open (0:00-0:20)
- VS Code opens, single file `SKILL.md` visible
- Quick face shot

### Segment 1 — Setup (0:20-2:00)
- Pure face cam, fast pacing
- Don't over-explain — get to the build

### Segment 2 — SKILL.md Format (2:00-4:30)
- VS Code typing — show frontmatter being built in real time
- Pause briefly on each field for the explanation
- Don't speed-ramp this — viewers need to see each field

### Segment 3 — Body Build (4:30-7:30)
- Type the markdown body live OR paste a pre-written version while explaining
- Recommendation: paste it. Faster, and your VO carries the teaching
- Highlight each numbered step as you explain it

### Segment 4 — Restart + Test (7:30-10:00)
- THIS IS THE MONEY SHOT — the live test must work first try
- If it doesn't work, troubleshoot off-camera and re-shoot from "let me restart"
- Capture the AskUserQuestion interaction in full
- Open the generated file in VS Code or Cursor to show the output

### Segment 5 — Aha Moment (10:00-12:30)
- Face cam only
- Slow down here. Let the realization land

### Segment 6 — 3 Patterns (12:30-14:30)
- Use on-screen text overlays for the 3 pattern names
- Quick references to other skills for each pattern (don't open them — just name-drop)

### Segment 7 — Steal From Existing (14:30-16:00)
- Open `~/.claude/skills/` in Finder
- Scroll through the list quickly
- Open ONE skill's SKILL.md briefly to show it's "just a markdown file" — picking one that's small (like /save-idea or /eod) keeps the lesson clean

### Segment 8 — CTA (16:00-17:30)
- Face cam, energy up
- Mention companion video by exact title

---

## Energy Cues

| Segment | Energy | Notes |
|---|---|---|
| Cold open | 9/10 | Demystify hard and fast |
| Setup | 7/10 | Set the stakes |
| SKILL.md format | 6/10 | Teaching mode, calm |
| Body build | 7/10 | Building momentum |
| Live test | 9/10 | The payoff |
| Aha moment | 8/10 | Let it breathe |
| 3 patterns | 7/10 | Practical, tight |
| Steal tip | 7/10 | Empowering |
| CTA | 10/10 | Get the click |

---

## Avoid These Mistakes

1. **Over-explaining the format** — viewers want to BUILD, not study YAML
2. **Typing every line on camera** — type the frontmatter live (it's short), paste the body
3. **Skipping the live test** — this is the proof. If you skip it, the video loses 50% of its value
4. **Apologizing if a step takes a second** — cut the pause in edit
5. **Promoting too many other skills** — name-drop your /yt and /email, don't deep-dive

---

## After Filming

- Verify the video proves the lesson — someone watching should be able to follow along and build the same skill
- Render at 720p for review, then 4K for final
- Chapters from script.md → YouTube description
- Thumbnail brief: "15 MIN" giant text, Tyler face, SKILL.md file icon, orange Claude asterisk
- Run `/content build-first-skill-15-min` to generate cross-platform posts
- Update `status.md`
- Mark video-ideas.md "Building Custom AntiGravity Skills From Scratch" related entry as done (this video covers the Claude Code version of that)

---

## Companion Video Cross-Linking

**End screen / pinned comment / first card:** Link to "I Have 43 Claude Code Skills. These Are the 7 I Actually Use." (the discover side of the funnel)

**Description cross-link:** Both directions — the 7-skills video should also point here for "want to build your own?" CTA.
