# Filming Guide: How I Take a YouTube Video From Idea to Scheduled in Claude Code

The do-this / click-that playbook. Follow it top to bottom and you can film the whole thing without re-reading the script. This is the SIMPLE end-to-end workflow, one video idea to scheduled, all inside Claude Code. Nine skills, in order.

---

## Pre-recording setup

**Before you hit record, prep these so nothing stalls on camera:**

1. **Clean terminal** - fresh Claude Code session, `/clear` run, large readable font (18pt+). Dark theme, status line on so the model + context window show (proof it's the real tool).
2. **Pick your demo topic ahead of time** - decide the `/yt-search` topic (for example "claude code") so you're not thinking on camera.
3. **Pre-run the slow skills once** - `/yt-package`, `/yt-thumbnail`, and `/yt-shorts` take minutes. Run them BEFORE recording so the output folders and images already exist. Film the command going in live, then cut to the finished result. Never make the viewer wait.
4. **Have a real package open** - a finished `youtube/videos/NNN-slug/` folder so you can open `titles.md`, `script.md`, and `filming-guide.md` and show real depth.
5. **One SKILL.md open** - a simple, clean example skill open in your editor for the "what is a skill" section. Do not pick a complicated one.
6. **Follow-along doc ready** - open `_resources/youtube-workflow-starter.md`. Set its sharing to "Anyone with the link - Viewer" BEFORE filming so the link you say out loud actually works.
7. **GitHub repo tab** - the skills repo open in a browser tab to flash in Module 1 and Module 9.
8. **A finished mp4 on hand** - for the `/yt-chapters` demo you need a real edited video file so the timestamps come out real.
9. **yt-upload already authed** - do the one-time Google setup before you record so `/yt-upload` doesn't send you into a 10-minute detour on camera. Mention the setup honestly, but don't perform it live.
10. **Hide anything private** - API keys, unpublished titles you don't want leaked, anything you're not ready to show.

---

## Step 1 - Cold open + promise (0:00 - 0:45)

**What you do:** Talk to camera for the hook (see `hooks.md`), then cut straight to a fast montage of the terminal cycling through commands and a scheduled upload in Studio.

> "This entire video, the idea, the research, the script, the thumbnail, and it sitting scheduled on my channel, I made all of it inside one tool just by talking to it. Nine skills, in order, idea to scheduled, all inside Claude Code. Let me show you the exact workflow."

**Then one breath of framing, still fast:**
> "The whole system is in a free doc you can follow along with, and the skills are on my GitHub, both linked and pinned below. This is a repeatable system, not a magic button. It still takes your taste and your voice. But the busywork is gone."

**What happens next:** Cut to the terminal. Do NOT sit on your face for 45 seconds. Open on the result, get into the tool.

---

## Step 2 - What a skill is (0:45 - 2:00)

**What you do:** Switch to your editor. Open ONE simple SKILL.md. Point at the top line, then the body. Then run one skill so they see the payoff before any theory.

**What to show:** The name, the description line (when to use it), and the plain-English steps below.

> "A skill is a workflow you taught Claude Code once, and you trigger it with one command. It's just a markdown file. A name, a description of when to use it, and the steps in plain English. Build it once, run it forever. If you can describe your process in plain English, you can build one."

**How to fill dead air:** N/A, this is talking, not waiting. Keep it slow and clear. This is the section that keeps non-coders watching, so land "it's just text" plainly.

**Do NOT:** open the frontmatter / allowed-tools rabbit hole. One SKILL.md, one sentence, move on.

---

## Step 3 - Research, start from what works (2:00 - 4:00)

**What you do:** Run the research skill live (it's fast enough), then run deep research on the top results.

**Commands:**
```
/yt-search claude code
```
```
/yt-deep-research
```
> "I don't guess what to make. This researches what's actually working on YouTube for your topic and ranks it by views, split into long-form and shorts. Then deep research transcribes the top videos and breaks down the hooks and the structure."

**Fill dead air while it runs:** "This is the difference between hoping a video works and starting from a format that already works."

**What happens next:** It prints a ranked table and downloads thumbnails. Show the report file. React to one real insight you wouldn't have spotted, out loud. That reaction is the retention beat.

---

## Step 4 - Learn from the winners (4:00 - 5:00)

**What you do:** Transcribe one proven reference video so you can model it.

**Command:**
```
/transcribe <competitor URL>
```
> "This pulls the full transcript from a proven reference video, so I can model the structure and the hooks without sitting through ten videos. This is how I plan. I learn from what's already ranking, then I make it mine."

**What happens next:** The transcript file appears. Open it briefly so they see it's the real text.

---

## Step 5 - Plan the whole video (5:00 - 7:00)

**What you do:** Feed the transcript to the core planning skill, then optimize for search. Film the command going in, CUT to the pre-run result.

**Commands:**
```
/yt-package ~/content/scripts/transcript_<id>.txt
```
```
/yt-seo
```
> "This is the core planning skill. Feed it the reference and it writes the full package, titles, hooks, the script, the description, the filming guide. Then SEO optimizes the title, description, and tags against what's ranking."

**What happens next:** [PRE-RUN THIS] Cut straight to the finished package folder. Open `titles.md`, `script.md`, and `filming-guide.md` so viewers see real depth.

**Meta beat (say it out loud):** "The script for this exact video came out of this skill."

**Honest beat:** "I still rewrite anything that doesn't sound like me. This gives me the draft, not the final."

---

## Step 6 - Thumbnails (7:00 - 8:00)

**What you do:** Generate thumbnail variants using your own likeness. Film the command, CUT to the pre-run images.

**Command:**
```
/yt-thumbnail
```
> "This generates thumbnail options with the Claude image models, using my own face. I make a few variants so I can test them against each other. This is the one asset that decides if anyone clicks, done from the terminal."

**What happens next:** Show the grid of generated thumbnails side by side.

---

## Step 7 - One video into a week of shorts (8:00 - 9:15)

**What you do:** Turn the long-form into a set of Shorts scripts. Film the command, CUT to the result.

**Command:**
```
/yt-shorts
```
> "This turns one long-form video into a week of YouTube Shorts scripts. One filming session feeds the whole week."

**What happens next:** Open two or three of the generated Shorts scripts.

**Keep it YouTube:** stay on Shorts here, don't wander into every other platform. That's a different video.

---

## Step 8 - Post-production (9:15 - 10:15)

**What you do:** After the edit is done, run chapters on the finished mp4. Use a REAL edited file so the timestamps are real.

**Command:**
```
/yt-chapters <path to finished mp4>
```
> "After the edit, this extracts the audio, transcribes it, and writes accurate chapter timestamps straight into the description. The tedious finishing work, automated."

**What happens next:** Show the timestamps written into the description file. Point out that they're real, from the actual audio.

---

## Step 9 - Upload + schedule (10:15 - 11:30)

**What you do:** Upload and schedule the finished video from the terminal.

**Command:**
```
/yt-upload
```
> "This uploads and schedules the finished video right from the terminal. Real tags, custom thumbnail, publish time. Idea to scheduled, without ever leaving Claude Code."

**Honest one-time-setup beat:** "This one needs a quick 10-minute Google setup the first time. The walkthrough is in the same free doc."

**What happens next:** Flip to YouTube Studio and show the video sitting there scheduled. That landing is the payoff of the whole video. Linger on it.

---

## Step 10 - Recap + build your first skill (11:30 - 12:30)

**What you do:** Back to camera. Recap the nine skills in one breath, then the ask.

> "That's the whole workflow. Research, learn from the winners, plan the package, thumbnail, shorts, chapters, upload, all inside Claude Code. Everything you just saw is in a free doc, and the skills are on my GitHub, both linked below and pinned. Grab them, and get on the newsletter at free.tylerai.dev/youtube."

**Leave them with the build nudge:**
> "Pick the most repetitive part of your week and teach Claude Code to do it once. That's your first skill. Tell me in the comments which one you'd build."

[SHOW: the follow-along doc, then the funnel page / end card.]

---

## Timing cheat sheet

| Section | Target | Running total |
|---------|--------|---------------|
| Cold open + promise | 0:45 | 0:45 |
| What a skill is | 1:15 | 2:00 |
| Research (yt-search + deep-research) | 2:00 | 4:00 |
| Learn from winners (transcribe) | 1:00 | 5:00 |
| Plan the video (yt-package + seo) | 2:00 | 7:00 |
| Thumbnails | 1:00 | 8:00 |
| Shorts | 1:15 | 9:15 |
| Post-production (chapters) | 1:00 | 10:15 |
| Upload + schedule | 1:15 | 11:30 |
| Recap + build a skill | 1:00 | 12:30 |

---

## On-camera tips

- **Errors are content.** If a skill hiccups on camera, narrate it: "see, this is real, let me fix it." Don't panic-cut. It reinforces that it's not staged.
- **Pre-run the slow stuff.** `/yt-package`, `/yt-thumbnail`, and `/yt-shorts` take minutes. Film the command going in, cut to the result. Never make the viewer wait.
- **The payoff moment is the scheduled video in Studio.** That one screen closes the "idea to scheduled" loop. Linger on it.
- **Land "it's just text, you don't need to code" plainly** in the "what a skill is" section. That accessibility is what unlocks the audience. It's a message to the viewer, never a claim about me.
- **Signpost every module** so viewers can skip to the skill they want. Each one is a chapter.
- **Say the free doc out loud** at least once early and once at the end. One primary CTA only, the funnel.
- **Energy:** grounded and confident, not hyped. The edge of this video is that it's true, so let the proof carry it.
- **Visual variety:** rotate between talking-head, terminal, editor, browser (Studio), and the file tree. Don't sit on the terminal for five minutes straight.
