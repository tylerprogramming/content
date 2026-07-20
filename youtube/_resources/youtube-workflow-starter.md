# The YouTube Workflow Starter (Video 1)

This is the exact system I use to take one YouTube video from idea to scheduled, all inside Claude Code. YouTube only. Follow along, copy what's useful.

Free pack + newsletter: https://free.tylerai.dev/youtube/

> On-screen note: show this doc on screen as you run each step in the video, so viewers can see the command and the output side by side.

## Skills used in this video
Custom Claude Code skills. A skill is a workflow you taught Claude Code once, triggered with one command. Build it once, run it forever.

| Skill | What it does |
|---|---|
| `/yt-search` | Researches what's actually working on YouTube for a topic, ranks by views |
| `/yt-deep-research` | Searches YouTube, transcribes the top videos, deep analysis of hooks + structure |
| `/transcribe` | Pulls the transcript from a reference video so you learn from proven stuff |
| `/yt-package` | Writes the full package: titles, hooks, script, description, filming guide |
| `/yt-seo` | Optimizes the title, description, and tags against what's ranking |
| `/yt-thumbnail` | Generates the thumbnail with the Claude image models (Nano Banana) |
| `/yt-shorts` | Turns the video into YouTube Shorts scripts |
| `/yt-chapters` | Builds accurate chapters from the final edited video |
| `/yt-upload` | Uploads + schedules the finished video to YouTube (see setup doc below) |

## The flow (what you'll see on screen, in order)
1. `/yt-search <topic>` - research what's working. Show the ranked results.
2. `/transcribe <best reference video>` - pull the proven structure.
3. `/yt-package <transcript>` - generate titles, hooks, the script, the description, the filming guide. Open the real files on screen.
4. `/yt-seo <slug>` - optimize the title + description.
5. `/yt-thumbnail` - generate 3 thumbnail options for Test & Compare.
6. Film + edit (the human part - the tool doesn't do this for you).
7. `/yt-chapters <final.mp4>` - real timestamps from the final cut.
8. `/yt-shorts` - cut Shorts scripts from the video.
9. `/yt-upload` - schedule it. (One-time setup: see below.)

## One-time setup you need
Uploading through Claude Code needs a `token.json` (a 10-minute one-time Google setup). Full walkthrough here: **`yt-upload-setup.md`** in this same folder.

## Build your first skill (the template)
A skill is a folder with a `SKILL.md` file describing the steps in plain English. Copy this, fill it in, and you have your first one:

```markdown
---
name: my-first-skill
description: What this does and when to trigger it
---

# What this skill does
[One sentence.]

# Steps
1. [First thing]
2. [Second thing]
3. [Where to save the output]

# Rules
- [Anything it should always/never do]
```

If you can describe your process in plain English, you can build a skill. Start with the most repetitive part of your week.
