# Filming Guide: I Built an AI Video Editor With Claude Code

**Date:** 2026-06-19
**Estimated filming time:** One focused session. Talking-head plus two live screen-recorded demos.
**Golden rule:** The two demos are REAL and must be captured live. Run the actual commands on the actual clip on camera. No faked outputs - that is the whole brand. If a command fails on camera, that is fine, re-run it, but never stage a fake result.

---

## The Single Most Important Prep Step

**Build the tool and test BOTH commands before you film anything.** The entire video collapses if `hyperframes silence` or `hyperframes caption` breaks on camera. Do a full dry run start to finish the day before. You should have run both commands on the exact clip you will use, seen the 3:00 to 1:50 result, and rendered all three caption styles, before the camera turns on.

Checklist:
- [ ] `tylerprogramming/hyperframes-studio` repo cloned and working locally.
- [ ] `hyperframes silence` runs clean and produces the cut clip.
- [ ] `hyperframes caption --style bold` renders correctly.
- [ ] `hyperframes caption --style tiktok` renders correctly.
- [ ] `hyperframes caption --style clean` renders correctly.
- [ ] ffmpeg, Whisper, and Hyperframes all installed and confirmed working.
- [ ] You have run the FULL workflow (raw clip to silence to caption) end to end at least once.

---

## Pre-Recording Setup

### The raw demo clip (this is the hero asset)
- A REAL talking-head clip with obvious pauses, around 3:00 long, that cuts down to about 1:50.
- The pauses need to be audible - this is what sells Demo 1. Do not over-perform the pauses, but a natural raw take with real dead air is perfect.
- Confirm before filming: this exact clip produces the 3:00 to 1:50, 71-second cut. The numbers in the script are tied to this clip. If you swap the clip, update the numbers in the script.
- Keep the content of the clip safe to show on screen (nothing sensitive said in it).

### Terminal and environment
- Terminal font large enough to read on a phone screen. Increase font size before filming.
- Clean working directory - only the demo clip and the repo visible. No clutter, no unrelated files.
- Prompt should not show anything sensitive (no full home path with anything private, no secrets in the prompt).
- Have the commands ready to type but type them live so it reads as real.

### Recording setup
- Screen recording at clean resolution, cursor visible, terminal windowed so the command and output both fit.
- Teleprompter loaded with the word-for-word cold open and the CTA.
- Talking-head and screen-capture audio levels checked once up front.
- The before/after result clip pre-rendered and ready to drop into the cold open in the edit.

---

## On-Screen Safety (READ THIS)

- **Never show repo secrets, tokens, API keys, or .env files on camera.** Close any file or terminal that could surface them. If you open the code to show the silencedetect logic, open only the specific file, and scan it first for anything sensitive.
- **Blur anything sensitive** in post if it slips into frame - paths with private info, other repo names, browser tabs, notifications.
- Turn off desktop and app notifications before recording (Slack, Mail, Messages, etc.).
- If you show the repo at all, it is fine to show it is named `hyperframes-studio` and that it is a fork - but do not show private settings, collaborators, or anything that should stay private.
- The demo clip audio plays on camera - make sure nothing private is said in it.

---

## Honest-Framing Reminders (say these, do not skip them)

These lines protect the brand. They are in the script for a reason. Do not cut them to save time.

1. "I did not build this from scratch." Say it early, mean it.
2. Name all three open-source tools by name - Hyperframes, ffmpeg, Whisper - and say what each one does.
3. Credit Hyperframes as HeyGen's open-source, Apache-2.0 framework.
4. Be explicit about what YOU added: the silence-cutting layer and the one-command caption flow. That is the honest scope.
5. In the limitations section, actually say it does NOT replace creative editing. Do not soften that into nothing.
6. The result clip in the cold open is real - it is this exact workflow on a real clip. Never imply a result you did not actually produce.

---

## Per-Section Capture Notes

### Cold open (0:00-0:30)
- Film the talking-head delivery word for word from the teleprompter. High energy.
- The before/after clip is dropped in during the edit at the very top, before the talking-head line. Pre-render it.
- Do not explain the build here. Just the reveal. Resist over-explaining.

### The problem (0:30-2:00)
- Talking head only. Conversational, relatable. You are describing a pain the viewer feels.
- Energy can be a little lower here, but keep it moving - this section trims first if you run long.

### What I did - the build (2:00-4:00)
- Talking head plus a simple graphic of the three tools (Hyperframes, ffmpeg, Whisper). The editor can build the graphic.
- You can show the terminal and the repo briefly here, safely (see on-screen safety).
- Hit the honest-framing lines clearly. This is the trust-setting section.

### DEMO 1 - silence cut (4:00-7:30) [LIVE]
- REAL screen recording. Play 5 seconds of the raw clip so the pauses are audible. Type and run `hyperframes silence` live.
- Show the ~2 second runtime. Do not speed it up - if it is fast, that is the point, let it be fast.
- Play 5 seconds of the cut result. Call out the numbers: 3:00 to 1:50, 71 seconds, 39 percent.
- For the Whisper-vs-silencedetect lesson: you can show the code or use an explainer graphic. Keep this part clear and slow enough to follow, then pull energy back up before Demo 2. This is the deepest beat - do not rush the insight, it is the most valuable 90 seconds in the video.

### DEMO 2 - captions (7:30-10:30) [LIVE]
- REAL screen recording. Run `hyperframes caption --style bold` live, play the result.
- Then show all three styles. You can pre-render the three style outputs and cut between them in the edit, but the COMMAND being run must be real. Show each command (bold, tiktok, clean) on screen.
- Call back the lesson: Whisper for words, ffmpeg for silence. Right tool for each job.

### The full workflow (10:30-12:00)
- Recap sequence. Can be a slightly sped-up montage of the two commands back to back, or a clean re-statement.
- Call back to the cold open: "that clip at the start was this exact workflow." Show the before/after side by side once more.

### Honest limitations (12:00-13:30)
- Talking head. Sincere, direct. This section builds the most trust - do not throw it away.
- Hit all four limits: not creative editing, built on open-source, render speed, rough CLI tool.

### CTA (13:30-14:30)
- Talking head plus the three-tools graphic one more time.
- Default is option (c): teach the recipe, soft Skool CTA. If Tyler changed the CTA decision, re-film this section to match (see the CTA note in script.md and the decision in analysis.md).
- Subscribe ask at the end, framed around "building tools with Claude Code is what I do here."

---

## Timing Cheat Sheet

| Section | Target | Format |
|---------|--------|--------|
| Cold open | 0:30 | Result clip + talking head (word for word) |
| The problem | 1:30 | Talking head |
| The build | 2:00 | Talking head + tools graphic |
| Demo 1 silence | 3:30 | **LIVE screen recording** |
| Demo 2 captions | 3:00 | **LIVE screen recording** |
| Full workflow | 1:30 | Recap montage |
| Honest limits | 1:30 | Talking head |
| CTA | 1:00 | Talking head + graphic |
| **Total** | **~14:30** | Trim problem + limits first to hit 12:00 |

**If you must cut for time:** trim the problem section and the limitations section. Never trim the two live demos or the Whisper-vs-silencedetect insight - those are the spine of the video.
