# Filming Guide: 3 Skills + Live Build

**Runtime target:** 28-32 min
**Session 1 (Friday 4-5 PM):** Prep + thumbnail
**Session 2 (Saturday 1-3 PM):** Smoke tests + cold open + first skill demo
**Session 3 (Saturday 7-11 PM):** Full record
**Stack:** OBS, face cam, lapel mic, VS Code, Claude Code terminal

---

## Friday Prep Block (4:00-5:00 PM)

- [ ] Read this script aloud once. Mark beats. Time it. (20 min)
- [ ] Open `/thumbnail` skill. Generate 4 Nano Banana Pro variants on the brief in `titles.md`. Pick 1. Save to `~/content/youtube/067-3-skills-and-build/thumbnail-final.png`. **Hard cap: 30 min.**
- [ ] Verify the meeting-notes folder is deleted: `rm -rf ~/.claude/skills/meeting-notes/`
- [ ] Verify `~/notes/meetings/` is empty or moved aside
- [ ] Run `/yt-search claude code` once Friday afternoon. Read the report. Confirm Alberta Tech appears as a top result.
- [ ] Smoke-test `/transcribe` on a short YouTube URL (under 5 min). Confirm OpenAI API works (quota not exhausted).
- [ ] Smoke-test `/yt` on any recent transcript. Confirm it asks a clarifying question.
- [ ] Confirm OBS scenes set up: Face Cam, Terminal, VS Code, Finder, Browser

---

## Saturday 1-3 PM (Prep + First Take)

### 1:00-1:30 Pre-record check
- [ ] Lighting check (face well-lit, no window backlight)
- [ ] Audio check (record 30 sec, play back, listen for room echo / mic clipping)
- [ ] Camera framing (face dead-center, eyes at upper third of frame)
- [ ] Terminal cleared (no scrollback visible from prior sessions)
- [ ] Phone in another room

### 1:30-2:00 Cold open + setup
Record segments 0:00-0:25 (Triple Receipt Hook) and 0:25-1:45 (Setup).
- The triple-receipt montage can be captured as separate clips and edited in post — OR done as 3 visible windows in one take. Whichever you prefer.
- If the cold open feels stiff, do up to 3 takes. If it still feels off, do the setup first and come back to the cold open at the end.

### 2:00-3:00 Skill 1: /yt-search demo
Record segment 1:45-7:30 (Skill 1).
- Pre-frame the terminal before running the command
- Type the command in real time — don't paste
- Capture the full ~60 second run (speed-ramp in edit later)
- Open the report file in VS Code, scroll through naturally
- Open thumbnails folder in Finder, scroll through
- Land the "60 seconds replaced 2 hours" payoff line directly to camera

**End of session checkpoint:** Cold open + setup + Skill 1 in the can. ~7 min of finished video. Take a break before evening session.

---

## Saturday 7-11 PM (Full Record)

### 7:00-7:30 Setup refresh
- Re-check lighting + audio (4 hours later, sun position different)
- Same outfit as afternoon session (continuity)
- Quick warm-up: re-read Skill 2 + Skill 3 sections aloud
- Coffee + water on the desk

### 7:30-8:30 Skill 2: /transcribe demo (segment 7:30-13:30)
- Use the Alberta Tech URL specifically (continuity with Skill 1 result)
- Capture the download + whisper progress
- Open the transcript file briefly
- Ask Claude for hook/beats/CTA breakdown — this is interactive, answer on camera
- Land the "read 5 competitors in time to watch one" payoff

### 8:30-10:00 Skill 3: /yt demo (segment 13:30-21:30)
- Point /yt at the transcript file from Skill 2 (continuity again)
- ANSWER the clarifying question on camera (the script provides a good answer)
- Show the package folder filling up — this is one of the strongest visuals
- Open titles.md, hooks.md, script.md briefly (don't read everything)
- Land the "5 minutes replaced a weekend" payoff

### 10:00-10:15 Break
- Switch demo state: delete the meeting-notes folder (if it got recreated by accident)
- Open empty `~/.claude/skills/meeting-notes/` folder in VS Code
- Clear notes meetings folder again if anything's there

### 10:15-10:45 THE AHA + Live Build (segments 21:30-29:30)
- AHA reveal: open the 3 source SKILL.md files (`/yt-search`, `/transcribe`, `/yt`) — show they're just markdown
- **THIS IS THE SCREENSHOT MOMENT.** If the reveal doesn't feel landed on the first take, reshoot just this 60 seconds.
- Move into the live build of `/meeting-notes`
- Type the frontmatter LIVE on camera
- Body can be pasted (5 sec) while you narrate — viewer doesn't need to watch all 30 lines being typed
- Restart Claude Code on camera
- Run `/meeting-notes`, click "Team sync", show the file appearing
- Run again with same topic to demo the `-2` append rule
- Land the "50 lines of YAML and English" payoff

### 10:45-11:00 3 patterns + CTA (segments 29:30-32:00)
- Face to camera
- Hit the 3 pattern names with on-screen text overlays (capture clean takes — these can be re-shot easily)
- ONE CTA: Skool waitlist for the SKILL.mds + 5 starter templates
- Direct-to-lens delivery
- Capture the callback montage shots needed for the edit

### 11:00 STOP
- Hard cap. Hit it whether or not you're "done."
- The CTA can be re-recorded Sunday morning if needed in 10 minutes.
- Don't chase perfection past 11 PM. Sleep.

---

## Sunday 7 AM - noon (Edit + Publish)

### 7-9 AM Edit pass
- Self-edit OR send to editor
- If self-editing, use this cuts list:
  - Cut all "umm" "uhh" and silent pauses longer than 1 second
  - Speed-ramp any terminal output longer than 15 seconds
  - Cut to face cam during long demos every ~20 seconds for variety
  - Add on-screen text overlay for the 3 pattern names
  - Add the title cards at chapter boundaries
- **Hard cap: 2 hours**

### 9-11 AM Automation pass
- Run `/transcribe` on the final cut
- Run `/seo 3-skills-and-build` for title/desc/tag optimization
- Run `/shorts` (this video's research feeds the shorts for the week)
- Run `/content 3-skills-and-build` for X / LinkedIn / Instagram / YT Community / Skool posts

### 11 AM - noon Upload + schedule
- Upload to YouTube
- Paste chapters from script.md into description
- Add thumbnail
- Pin a comment with the Skool waitlist link
- Schedule cross-platform posts via Blotato

### Noon onward
- Close the laptop
- Live your life
- Check analytics Monday morning, not before

---

## Energy Cues

| Segment | Energy | Notes |
|---|---|---|
| Hook | 10/10 | Triple receipt |
| Setup | 7/10 | Stakes |
| Skill 1 setup | 7/10 | Lead with problem |
| Skill 1 demo | 5/10 | Let screen do work |
| Skill 1 payoff | 8/10 | "60 seconds replaced 2 hours" |
| Skill 2 setup | 7/10 | Lead with problem |
| Skill 2 demo | 5/10 | Let screen do work |
| Skill 2 payoff | 8/10 | "Read 5 in time to watch 1" |
| Skill 3 setup | 7/10 | Heaviest lifter framing |
| Skill 3 demo | 5/10 | Let screen do work, show folder filling |
| Skill 3 payoff | 9/10 | "Weekend → 5 minutes" |
| THE AHA | 10/10 | Screenshot moment, slow down |
| Live build write | 7/10 | Building anticipation |
| Live build test | 9/10 | Money shot |
| Aha payoff | 8/10 | "50 lines of YAML" |
| 3 patterns | 7/10 | Practical, tight |
| CTA | 10/10 | Get the click |

---

## Avoid These Mistakes

1. **Don't re-record working demos.** Every demo that runs end-to-end is a win.
2. **Don't show every file in the /yt output.** Show the folder filling, open 2 files max.
3. **Don't apologize on camera if a skill takes 30 sec.** Edit out the pause.
4. **Don't mention other skills during the showcase.** Save the 43 credential for setup. Showcase is about these 3.
5. **Don't fake the AskUserQuestion answer.** Answer on camera every time.
6. **Don't use em dashes.** Tyler's standing rule.
7. **Don't chase perfection past 11 PM.** Hard cap.
8. **Don't open `~/.claude/.env` ever.** Period.

---

## After-Filming Checklist

- [ ] Watch the full recording for sensitive content before uploading
- [ ] Render at 720p for review, 4K for final
- [ ] Chapters from script.md → YouTube description
- [ ] Run `/chapters` on final cut to validate timestamps
- [ ] Thumbnail uploaded
- [ ] Skool waitlist link in pinned comment
- [ ] Shorts scripted from this content (4-5 from the recording's best moments)
- [ ] Social posts scheduled via Blotato
- [ ] Update status.md
- [ ] Mark `7-skills-run-my-business` and `build-first-skill-15-min` in video-ideas.md as "merged into 3-skills-and-build for restart, may revisit standalone later"

---

## Companion Video Cross-Linking

This video sets up the next one (the 50-min full course covering all 7 skills). When this one ships:

- End screen → "Want all 7 skills + the full breakdown? Coming next video."
- Pinned comment → Skool waitlist (primary CTA)
- Description → link to old AntiGravity beginner video as related (showcases same skill-build pattern)
