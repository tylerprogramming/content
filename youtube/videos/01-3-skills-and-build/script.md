# Script: 3 Claude Code Skills That Run My Week + How to Build Your Own (Live)

**Target length:** 28-32 minutes
**Format:** Triple receipt hook → Setup → 3 skill demos (pipeline order) → The aha transition → Live build → 3 patterns → ONE CTA
**Energy:** Practical, proof-heavy, demos fast / talking head medium / payoff high
**Reference pattern:** Tyler's AntiGravity script (receipt-first cold open, concrete prompts in code blocks, real demos, `[SHOW:]` and `[NOTE:]` cues for editor)

---

## [0:00 - 0:25] Triple Receipt Hook

[SHOW: Split-screen montage in three vertical bands. Left band: terminal running `/yt-search claude code`, then a folder filling up with PNG thumbnails. Middle band: `/transcribe https://...` running, then a transcript file appearing in `~/content/transcripts/`. Right band: `/yt ~/content/transcripts/transcript_xxx.txt` running, then a package folder filling with files. All three layered, appearing in parallel over 6 seconds.]

> *(VO at 0:03)*
> Research, transcripts, video packages. Three Claude Code skills, three outputs, total time about 8 minutes.

> *(at 0:10)*
> I'm going to show you all three working, then I'm going to build a brand new one from scratch live on camera. By the end you'll know what a Claude Code skill can do and how to build your own.

[NOTE: Energy HIGH. The three receipts ARE the proof. Don't talk over the visual — let it land for ~3 seconds before VO drops.]

---

## [0:25 - 1:45] Setup

[CAMERA: Face to camera, fast and clear]

> Quick framing so you know what you're getting.

> I'm a full-time software engineer. I have a wife and kids. Content gets made between 4 and 5:30 PM on weekdays and a few hours on weekends. That's the time budget.

> If you're not full-time on content, you have to be ruthless about leverage. Skills are how I get leverage out of Claude Code. I've built 43 of them. Most are experiments. About 7 I actually use every week.

> Today I'm going to show you three of those 7 — the three that kick off every Monday morning. They're a complete content pipeline: research, input, output. Then I'm going to show you how simple they really are by building a brand new one — `/meeting-notes` — from scratch in front of you.

> Let's start with the one that kicks everything off.

[NOTE: Don't dwell. Get to the demos. Keep this under 90 seconds.]

---

## [1:45 - 7:30] Skill 1 — `/yt-search`

### The setup (1:45 - 2:30)

[SHOW: Talking head, then cut to terminal]

> Every Monday at 4 PM I sit down to plan two long-form videos for the week. The first question I ask isn't "what should I make?" It's "what's actually working right now in my space?"

> If you don't answer that question first, you're guessing. And guessing is how channels die before they ever get traction.

### The prompt + the demo (2:30 - 5:30)

[SHOW: Terminal — type the command in real time]

```
/yt-search claude code
```

> That's the whole command. Keyword: "claude code." Under the hood the skill uses yt-dlp to pull recent videos, filters to the last 30 days, sorts by views, downloads the thumbnails into a folder, and saves a markdown report.

[SHOW: Terminal runs for ~60 seconds. Show the progress output. Speed-ramp if it takes longer.]

> About a minute. Let me open the report.

[SHOW: VS Code opening `~/content/research/<today>-claude-code.md` — scroll through the table of titles, views, durations.]

> 33 videos in the last 30 days. Sorted by views. I can see in 30 seconds what title formulas are working, who's making them, what durations are hitting.

[SHOW: Open the thumbnails folder in Finder. Scroll through them.]

> And the thumbnails are downloaded. I can see what's working visually too — Alberta Tech's "Well... that explains it" thumbnail with the face on the left, text on the right? That formula is doing 413,000 views right now.

### Why it matters (5:30 - 7:30)

> This is research that used to take me 2 hours a week of clicking around YouTube. Now it's 60 seconds.

> And this report is the input to every other skill in my pipeline. Garbage in, garbage out. Research is the moat.

> Skill 1 of 3. Done. On to the second.

[NOTE: Make sure the search you run on camera returns real, current data. If filming on a different day, re-run it that morning so the views are fresh.]

---

## [7:30 - 13:30] Skill 2 — `/transcribe`

### The setup (7:30 - 8:00)

[SHOW: Face to camera, then terminal]

> Once I know what's working, I need to study the actual content. Watching a 30-minute competitor video to take notes is a waste of time when I can just read it.

### The prompt + the demo (8:00 - 11:30)

[SHOW: Pull the top result URL from the yt-search report — Alberta Tech's "Why devs are OBSESSED" — and run the transcribe command.]

```
/transcribe https://youtube.com/watch?v=LACyqdAfnaw
```

> Paste any YouTube URL. The skill downloads the audio with yt-dlp, runs it through OpenAI Whisper, saves the transcript to my scripts folder.

[SHOW: Progress bars for download + whisper. Speed-ramp.]

> About 90 seconds for a 12-minute video.

[SHOW: Open `~/content/transcripts/transcript_LACyqdAfnaw.txt` in VS Code.]

> Full transcript with timestamps. Now I can read the whole video in 5 minutes.

[SHOW: Type into Claude Code chat:]

```
read ~/content/transcripts/transcript_LACyqdAfnaw.txt and tell me the hook, the 3 main beats, and the CTA in bullet form
```

[SHOW: Claude's response appearing — bullet breakdown.]

> 30 seconds of reading. I have the structural takeaways. I can riff on them, beat them, or steal them. That's how I plan a video.

### Why it matters (11:30 - 13:30)

> Most creators are watching their competitors. I'm reading them. I can process 5 competitor videos in the same time it takes someone to watch one.

> One small thing — there's a corrections file in the skill that auto-fixes common whisper mishears for my topic. "Cloud" gets corrected to "Claude." "Appify" to "Apify." Set it once, it runs forever.

> Skill 2 done. On to the heavy lifter.

---

## [13:30 - 21:30] Skill 3 — `/yt` (the heaviest)

### The setup (13:30 - 14:15)

[SHOW: Talking head]

> Skill 3 is the one that does the most work.

> Most people, when they decide to make a YouTube video, sit down with a blank doc and start typing. I never start with a blank doc. I run `/yt` with a transcript as input, and 5 minutes later I have a complete video package.

### The prompt + the demo (14:15 - 19:00)

[SHOW: Terminal]

```
/yt ~/content/transcripts/transcript_LACyqdAfnaw.txt
```

> Point the skill at the transcript I just pulled.

[SHOW: The skill responds — asks 1-2 clarifying questions. Tyler answers on camera.]

> See that? It just asked me what my angle is. My take. The unique slot I'm filling. Because if I skip this question, the script will sound like every other one.

[SHOW: Type the answer:]

```
Mine is the technical / creator angle. I'll show actual commands and skills, not just talk about Claude Code at a high level.
```

[SHOW: Skill runs — show the package folder filling up at `~/content/youtube/<new-slug>/`]

> Watch the folder fill. `analysis.md`. `titles.md` with 10 scored options. `hooks.md` with 4 hooks to test. `script.md` — word for word, scene by scene. `description.md`. `filming-guide.md` with timestamps, b-roll notes, and energy cues for the editor.

[SHOW: Open each file briefly. Show the title scorecard. Show the script's chapter structure.]

> This used to be my entire weekend. Sit down Saturday morning, finish Sunday night, exhausted. Now it's 5 minutes.

### Why it matters (19:00 - 21:30)

> Here's the thing I want you to internalize. The skill isn't writing the video *for* me. It's writing the *80% draft* I edit and personalize. I still bring the stories, the contrarian takes, the actual recording. But I never start from zero. Ever.

> That's the difference between people who publish 1 video a month and people who publish 8.

> Three skills, complete pipeline. Research, input, output. Monday morning, 90 minutes total, two long-form videos planned for the week.

[NOTE: When the skill asks a question on camera, ALWAYS answer it on camera. Viewer needs to see the human-AI interaction loop.]

---

## [21:30 - 22:30] THE AHA (Screenshot Moment)

[SHOW: Cut from the third skill's output folder back to face cam. Slow down for one beat.]

> Now pause for one second. Look at what you just watched.

> Three skills. Different jobs. Different outputs. Different time savings.

[SHOW: Open `~/.claude/skills/yt-search/SKILL.md` — show the top of the file]
[SHOW: Open `~/.claude/skills/transcribe/SKILL.md` — same]
[SHOW: Open `~/.claude/skills/yt/SKILL.md` — same]

> All three of those — same format. A markdown file. About 50 to 100 lines each. Frontmatter on top, plain English instructions below.

> No SDK. No framework. No plugin install.

[CAMERA: Direct to lens, energy up]

> Let me build a brand new one in front of you right now. From scratch. In about 7 minutes.

[NOTE: THIS IS THE SCREENSHOT MOMENT. Someone tweets "All Claude Code skills are just markdown files" with this frame. Plan the visual carefully — the three SKILL.md files visible at the same time IS the proof.]

---

## [22:30 - 29:30] Live Build — `/meeting-notes`

### Setup (22:30 - 23:00)

[SHOW: Empty folder in VS Code at `~/.claude/skills/meeting-notes/` — visibly empty]

> Here's an empty folder. The skill we're building today is `/meeting-notes` — type the command with a topic, Claude generates a meeting note template with an agenda, action items, decisions, and saves it to my notes folder.

> Universally useful. Touches every important concept: frontmatter, arguments, asking the user a question, writing a file. Watch.

### The frontmatter (23:00 - 24:30)

[SHOW: Create `SKILL.md`, type the frontmatter LIVE]

```yaml
---
name: meeting-notes
description: Generate a meeting note template with agenda, action items, and decisions. Triggers on - meeting notes, take notes, meeting template.
argument-hint: [topic]
allowed-tools: Read, Write, Bash(date:*), AskUserQuestion
user-invocable: true
---
```

> Five fields. Name matches the folder. Description tells Claude when to fire this skill. Argument-hint shows the user what to pass. Allowed-tools is what the skill can use — keep it minimal. User-invocable true makes it a slash command.

### The body (24:30 - 26:30)

[SHOW: Below the frontmatter, paste/type the body — can paste for speed]

```markdown
# Meeting Notes Skill

Generate a structured meeting notes template based on a topic the user provides.

## What to Do

1. If the user didn't pass a topic, ask them using AskUserQuestion. Ask "What's this meeting about?" with 3 quick-pick options: "1:1", "Team sync", "Customer call", plus Other.

2. Get today's date using `date +%Y-%m-%d`.

3. Create the markdown with:
   - Title (h1 of the topic)
   - Date
   - Attendees (blank)
   - Agenda (3 relevant bullets)
   - Decisions (empty section)
   - Action items (empty + one example row formatted "- [ ] Owner: Action - Due: date")
   - Notes (empty)

4. Save to `~/notes/meetings/<date>-<slug>.md`. Slug = topic lowercased, spaces to hyphens.

5. Confirm the saved path.

## Rules

- Use today's actual date from `date`, not a hardcoded one.
- Never overwrite. If today's slug exists, append `-2`, `-3`, etc.
- No em dashes — use regular hyphens.
```

> Plain English. No code. The body tells Claude what to do step by step. The rules section at the bottom prevents the skill from doing something dumb later.

### Restart + test (26:30 - 28:30)

[SHOW: Save the file. Restart Claude Code.]

> Save. Restart Claude Code so it picks up the new skill.

[SHOW: Claude Code restarts. Type the command.]

```
/meeting-notes
```

[SHOW: Claude responds with AskUserQuestion — shows "What's this meeting about?" with the 3 quick-pick options]

> It hit the AskUserQuestion step. I'll pick "Team sync."

[SHOW: Click "Team sync." Claude runs the rest — calls `date`, generates the file, confirms.]

```
Saved to ~/notes/meetings/2026-05-23-team-sync.md
```

[SHOW: Open the file in VS Code]

```markdown
# Team Sync

**Date:** 2026-05-23
**Attendees:**

## Agenda
- Review last week's progress against priorities
- Surface blockers or risks
- Align on this week's top 3 outcomes

## Decisions

## Action Items
- [ ] Owner: Action - Due: date

## Notes
```

> Title. Today's date. Attendees blank. Three relevant agenda bullets. Decisions empty. Action items with an example row. Notes blank. Exactly what I described in plain English.

[SHOW: Quick verification — run it again with the same topic, show it appends `-2`]

> And the rule worked — second run got `-2` appended instead of overwriting.

### The aha (28:30 - 29:30)

[CAMERA: Face to camera]

> That's it. About 50 lines of YAML and English. No code. No SDK install. Now I have a slash command in Claude Code that does a real, useful task forever.

> Every skill in my system works exactly like this. The three you saw at the start — same format. Longer body, more tools allowed, same structure.

> Once you understand this, the floodgates open. You stop thinking "how do I automate this" and start thinking "what's the skill called and what should the body say."

[NOTE: This is the AHA payoff. Let it land. 2-3 seconds of silence is okay here.]

---

## [29:30 - 31:00] 3 Reusable Patterns

[SHOW: On-screen text overlays for the 3 pattern names as Tyler explains each]

> Three patterns make every skill robust. You'll use these forever.

> **Pattern one** — when input is missing, don't error out. Ask. We did this with AskUserQuestion. The skill becomes more forgiving.

> **Pattern two** — write output to predictable paths. Meeting notes go to `~/notes/meetings/`. My video packages go to `~/content/youtube/<slug>/`. Consistent paths let skills cooperate. The `/content` skill knows where `/yt` puts files because they share a convention.

> **Pattern three** — put rules in a rules section at the bottom. "Never overwrite." "Always confirm." "No em dashes." Rules prevent disasters.

> Ask when missing. Predictable paths. Explicit rules. That's 80% of what makes a skill robust.

---

## [31:00 - 32:00] CTA

[CAMERA: Direct to lens, energy up]

> If you want all three skills you just saw — `/yt-search`, `/transcribe`, `/yt` — plus the `/meeting-notes` SKILL.md we just built, plus 5 more starter skill templates I'd recommend you build next, they're in my free Skool community.

> Link is in the description below. Join the waitlist for the full Claude Code skills course I'm building. That's it.

> See you in the next one.

[SHOW: Quick callback montage — triple receipt from the hook → SKILL.md being typed → `/meeting-notes` firing → meeting note file opening. Fast cuts, 1.5 seconds each. Mirror the energy of the open.]

---

## Production Notes

### Critical Pre-Production (Friday)

- [ ] **Delete `~/.claude/skills/meeting-notes/` if it exists** — must be a fresh build for authenticity
- [ ] Clear `~/notes/meetings/` of real notes (or move them)
- [ ] Run `/yt-search claude code` once Friday afternoon — keeps results fresh for Saturday's demo
- [ ] Smoke-test `/transcribe` on a short YouTube URL (under 5 min) — make sure OpenAI quota is good
- [ ] Smoke-test `/yt` on a recent transcript — make sure it asks the clarifying question
- [ ] OBS scenes ready: Face Cam, Terminal (Claude Code session), VS Code, Finder
- [ ] Have both the transcribe URL (Alberta Tech for continuity) and the meeting-notes body in a side doc you can paste from

### Demo Continuity (important)

The three skills should chain together on camera. Use the **same Alberta Tech URL** throughout:
1. `/yt-search` returns Alberta Tech as a top result
2. `/transcribe` runs on that URL
3. `/yt` reads that transcript

That continuity is what sells the "complete pipeline" narrative. If the URL doesn't appear in the live `/yt-search` results, restart the search with a slightly different keyword until it does.

### Sensitive Content Check

- [ ] Don't show `~/.claude/.env` at any point
- [ ] Don't show OpenAI/Apify/other API keys
- [ ] When opening other SKILL.md files for the AHA reveal, pick safe ones — `/yt-search`, `/transcribe`, `/yt` all OK to open
- [ ] When opening `~/notes/meetings/` ensure no real meeting notes are visible

### Energy Curve

| Segment | Energy | Notes |
|---|---|---|
| Hook | 10/10 | Triple receipt |
| Setup | 7/10 | Stakes |
| Skill 1 demo | 6/10 (demo) → 8/10 (payoff) | Let screen do work |
| Skill 2 demo | 6/10 (demo) → 8/10 (payoff) | Same |
| Skill 3 demo | 6/10 (demo) → 9/10 (payoff) | Heaviest lifter |
| THE AHA | 10/10 | Screenshot moment |
| Live build (write) | 7/10 | Building anticipation |
| Live build (test) | 9/10 | Money shot |
| Aha payoff | 8/10 | Let it breathe |
| 3 patterns | 7/10 | Practical, tight |
| CTA | 10/10 | Get the click |

### Common Mistakes to Avoid

1. **Don't re-record a demo if it works the first time.** Even if your wording wasn't perfect. The demo is the demo.
2. **Don't show every file in the `/yt` output folder.** Show the folder filling up, then maybe open 2 files. Otherwise the segment drags.
3. **Don't apologize on camera if a skill takes 30 seconds.** Edit out the pause.
4. **Don't mention other skills you have during the showcase.** Save the credential drop (43 skills) for the setup. The showcase is about these 3.
5. **Don't fake the AskUserQuestion answer.** When Claude asks you a question during the `/yt` demo OR the meeting-notes test, ANSWER ON CAMERA. The viewer needs to see the loop.
6. **No em dashes in spoken script.** Tyler's standing rule.

### Chapters (paste into YouTube description)

- 0:00 What 3 skills look like running
- 0:25 The setup (43 skills, why these 3)
- 1:45 Skill 1: /yt-search (60 seconds of research)
- 7:30 Skill 2: /transcribe (read competitors in 5 min)
- 13:30 Skill 3: /yt (full video package in 5 min)
- 21:30 Wait — they're all just markdown files
- 22:30 Live build: /meeting-notes from scratch
- 29:30 3 patterns that make any skill robust
- 31:00 Grab the SKILL.mds + 5 starter templates (free)
