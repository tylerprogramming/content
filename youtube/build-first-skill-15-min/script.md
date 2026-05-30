# Script: Claude Code Skills in 15 Minutes - Build Your First One (Live)

**Target length:** 15-18 minutes
**Format:** Empty-folder hook → 60-sec format tour → Live build → Live test → 3 patterns → CTA
**Energy:** Fast, practical, hands-on. NO theory wandering.
**Reference pattern:** Tyler's AntiGravity script — empty folder cold open, concrete prompts in code blocks, real demos, `[SHOW:]` and `[NOTE:]` cues.

---

## [0:00 - 0:25] Hook (Empty Folder)

[SHOW: VS Code with a new folder open at `~/.claude/skills/meeting-notes/`. The folder is empty. No files visible in the left panel.]

> This is an empty folder. No files. No code. Nothing.

[SHOW: Quick flash-forward — type `/meeting-notes` in Claude Code, the skill fires, a file appears at `~/notes/meetings/2026-05-17-team-sync.md`, the file opens showing a beautifully formatted meeting note template with agenda, action items, decisions sections.]

> In the next 15 minutes I'm going to turn it into a real Claude Code skill - a slash command that generates structured meeting notes any time I type it. No SDK. No framework. No plugin system. Just one markdown file.

> Let's build it.

[NOTE: Energy HIGH. The flash-forward IS the proof. Make sure the finished output looks polished before recording.]

---

## [0:25 - 1:30] What We're Building + Why

[CAMERA: Face to camera, fast and clear]

> Quick setup.

> The skill we're building today is a meeting notes skill. I type `/meeting-notes` followed by a topic. Claude generates a meeting note template with agenda, action items, and decisions sections, then saves it to a notes folder I can pull up later.

> Three reasons we're building this one specifically:
>
> One - everyone has meetings. You can use this immediately.
>
> Two - it's small enough to finish in 15 minutes without speed-ramping the video.
>
> Three - it touches every important concept: frontmatter, arguments, asking the user a question, writing a file, slash command invocation. By the end you'll know how to build basically anything.

> I'm building this in front of you using Claude Code itself. So you'll see Claude write a Claude Code skill. Inception. Let's go.

---

## [1:30 - 4:00] The SKILL.md Format (60-Second Crash Course)

[SHOW: VS Code — create a new file at `~/.claude/skills/meeting-notes/SKILL.md` and start typing]

> Every skill lives at `~/.claude/skills/<skill-name>/SKILL.md`. The folder name becomes your slash command. So this folder is `meeting-notes`, our command will be `/meeting-notes`.

> The file has two parts. Frontmatter on top - YAML between two `---` lines. Body below - plain English instructions.

[SHOW: Type the frontmatter LIVE on camera]

```yaml
---
name: meeting-notes
description: Generate a meeting note template with agenda, action items, and decisions. Triggers on - meeting notes, take notes, meeting template.
argument-hint: [topic]
allowed-tools: Read, Write, Bash(date:*), AskUserQuestion
user-invocable: true
---
```

[NOTE: Pause briefly on each field for the explanation - don't speed through]

> Five fields:
>
> `name` matches the folder. Required.
>
> `description` tells Claude when to fire this skill. The more specific your triggers, the better the routing.
>
> `argument-hint` shows the user what to pass after the command. Optional.
>
> `allowed-tools` is what the skill is allowed to do. Keep it minimal - principle of least privilege. We need to read files, write files, get today's date with `date`, and ask the user a question.
>
> `user-invocable: true` makes the skill appear as a slash command.

> That's the frontmatter. Now the body.

---

## [4:00 - 8:30] Live Build - The Body

### Writing the instructions (4:00 - 6:30)

[SHOW: Below the frontmatter, type the body content - viewer sees this build in real time]

```markdown
# Meeting Notes Skill

Generate a structured meeting notes template based on a topic the user provides.

## What to Do

1. If the user didn't pass a topic in their request, ask them using AskUserQuestion. Ask "What's this meeting about?" and include 3 quick-pick options - "1:1", "Team sync", "Customer call" - plus an Other option for free text.

2. Once you have a topic, get today's date using `date +%Y-%m-%d`.

3. Create the markdown content with this structure:
   - Title: the topic (h1)
   - Date: today's date
   - Attendees: leave blank for the user to fill in
   - Agenda: 3 bullet points relevant to the topic
   - Decisions: empty section ready to fill in
   - Action items: empty section with one example row formatted as `- [ ] Owner: Action - Due: date`
   - Notes: empty section

4. Save the file to `~/notes/meetings/<date>-<slug>.md`. Slug is the topic lowercased with spaces replaced by hyphens. Create the meetings folder if it doesn't exist.

5. Confirm to the user with the file path.

## Rules

- Use today's actual date from `date`, not a hardcoded one.
- Slug must be filesystem-safe: lowercase, spaces to hyphens, strip special characters.
- Never overwrite an existing file. If one exists for today's date and slug, append `-2`, `-3`, etc.
- Don't add em dashes - use regular hyphens with spaces.
```

[NOTE: This is the meat of the skill. Don't rush. Explain each numbered step as you type it. Mention WHY each rule exists - the "never overwrite" rule prevents losing yesterday's notes.]

### Why this works (6:30 - 7:30)

[CAMERA: Face to camera briefly]

> Look at what just happened. I wrote instructions in English. No JSON config. No JavaScript. No Python. Plain English steps.

> When the user types `/meeting-notes` or says "take notes for me," Claude reads this file, follows the steps, and uses the tools I listed in `allowed-tools` to do the work.

### Save the file (7:30 - 8:30)

[SHOW: Save the file - `Cmd+S`. Then close VS Code or move to Claude Code.]

> Save it. That's the whole skill. 35 lines of frontmatter and English.

---

## [8:30 - 12:00] Restart + Test (The Money Shot)

### Restart Claude Code (8:30 - 9:00)

[SHOW: Terminal - quit Claude Code, restart it]

> Claude Code only picks up new skills on restart. So quit and reopen.

[SHOW: Claude Code restarts. Tab loads.]

### Test it (9:00 - 11:30)

[SHOW: Type the command]

```
/meeting-notes
```

[SHOW: Claude responds - asks "What's this meeting about?" with the 3 quick-pick options visible: "1:1", "Team sync", "Customer call", "Other"]

> It hit the AskUserQuestion step. I'll pick "Team sync."

[SHOW: Click "Team sync"]

[SHOW: Claude runs the rest of the skill - calls `date`, generates the markdown content, writes the file, confirms]

```
Saved to ~/notes/meetings/2026-05-17-team-sync.md
```

[SHOW: Open the file in VS Code or use `cat` in the terminal to display it]

```markdown
# Team Sync

**Date:** 2026-05-17
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

> Title. Today's date. Attendees blank. Three agenda bullets relevant to a team sync. Decisions empty. Action items with one example row. Notes blank. Exactly what I described.

> Saved to `~/notes/meetings/2026-05-17-team-sync.md`. Total time from typing the command to having the file - about 6 seconds.

### Verify the rules (11:30 - 12:00)

[SHOW: Run it again with the same topic. Skill detects existing file, appends `-2`.]

```
/meeting-notes team sync
```

[SHOW: Confirmation]

```
Saved to ~/notes/meetings/2026-05-17-team-sync-2.md
```

> See that? Second one got `-2` appended. The rule worked. The first file is preserved.

[NOTE: This is the MONEY SHOT. The live test must work first try. If it doesn't, troubleshoot off-camera and re-shoot from "let me restart Claude Code." Do not re-shoot from the beginning - keep the authenticity of the build segment.]

---

## [12:00 - 14:00] What Just Happened (The "Aha")

[CAMERA: Face to camera]

> Pause. Notice what we just did.

> I wrote one file. About 50 lines of YAML and English. No code. No deployment. No SDK install. And now I have a slash command in Claude Code that does a real, useful task forever.

> Every skill in my system works exactly like this. The `/yt` skill that plans a full YouTube video? Same format, longer body. The `/email` skill that runs my drip campaigns? Same format, with Python scripts referenced in the body. The `/skool` skill that posts to my community? Same format, with a Skool API client referenced.

> When you understand this, the floodgates open. You stop thinking "how do I automate this" and start thinking "what's the skill called and what should the body say."

> That's the unlock.

---

## [14:00 - 16:00] The 3 Patterns That Make Every Skill Robust

[SHOW: On-screen text overlay with 3 numbered pattern names as Tyler explains each]

### Pattern 1: AskUserQuestion When Input Is Missing (14:00 - 14:30)

> Pattern one - when input is missing, don't error out. Ask.

> We did this in the meeting notes skill. If no topic was passed, AskUserQuestion fires with quick-pick options. The skill becomes more forgiving and friendlier to use.

### Pattern 2: Write Output to Predictable Paths (14:30 - 15:15)

> Pattern two - write output to predictable, consistent paths.

> Meeting notes go to `~/notes/meetings/<date>-<slug>.md`. Other skills follow the same shape:
>
> `/yt` writes to `~/content/youtube/<slug>/`
> `/shorts` writes to `~/content/youtube/shorts/<NNN> - <title>/`
> `/content` writes to `~/content/youtube/<slug>/social/`
>
> Consistent paths make your skills cooperate. The `/content` skill can find the package because it knows where `/yt` puts it.

### Pattern 3: Tell Claude the Rules (15:15 - 16:00)

> Pattern three - put rules in a "Rules" section at the bottom of your skill.

> "Never overwrite an existing file." "Always confirm before sending." "Use today's date, not a hardcoded one." "No em dashes."

> These prevent disasters. Without them, the skill will eventually do something dumb that costs you data or trust.

> Those three patterns - ask when missing, predictable paths, explicit rules - that's 80% of what makes a skill robust.

---

## [16:00 - 17:30] Get Better Fast + CTA

### The shortcut (16:00 - 16:45)

[SHOW: Open `~/.claude/skills/` in Finder. Scroll through the list briefly.]

> Fastest way to get good at writing skills is to read other people's skills. There are 40+ of mine sitting in `~/.claude/skills/`. Open any one. Read the SKILL.md. Notice the patterns.

[SHOW: Open one of the simpler skills - `~/.claude/skills/save-idea/SKILL.md` or `~/.claude/skills/eod/SKILL.md`]

> Most of them are 50 to 200 lines. None of them are scary. The first one you build takes longer than 15 minutes. The fifth one takes you 5.

### CTA (16:45 - 17:30)

[CAMERA: Direct to lens, energy up]

> Three things if you got value.

> One - the full SKILL.md from this video, plus 5 more starter skill templates I'd recommend you build next, are in my free Skool community. Link below.

> Two - if you want to see what 7 production skills look like wired together into a real content business, watch my video "32 Posts a Week, 7 Claude Code Skills. Here's How." That's the companion to this one.

> Three - subscribe. New Claude Code workflows Mondays and Thursdays.

> See you in the next one.

[SHOW: Quick callback montage - empty folder from the hook → SKILL.md being typed → restart Claude Code → `/meeting-notes` firing → file appearing → file opening with the formatted template. Fast cuts, 1.5 sec each. Mirror the energy of the open.]

---

## Production Notes

### Critical Pre-Production

- [ ] **Delete `~/.claude/skills/meeting-notes/` if it exists** - this MUST be a fresh build
- [ ] Smoke-test the Claude Code restart-picks-up-new-skill flow with a throwaway skill 24h before
- [ ] Clear `~/notes/meetings/` of any real meeting notes, or move them
- [ ] Create `~/notes/` parent folder if it doesn't exist
- [ ] OBS scenes ready: Face Cam, VS Code, Terminal (Claude Code session)
- [ ] Have the script's body content in a side doc you can glance at - don't type purely from memory in case of brain fade

### Shot List

- **Hook:** empty folder in VS Code → flash-forward of finished file (capture the finished file FIRST as b-roll, then film the empty-folder cold open)
- **Format tour:** type frontmatter LIVE in real time, don't paste
- **Body build:** can paste the body if typing it all would take too long, but narrate each step as it appears
- **Restart + test:** continuous unbroken recording - if it fails, only re-shoot the restart-and-after portion
- **3 patterns:** on-screen text overlays for the pattern names, Tyler face cam for the explanation
- **CTA + callback montage:** assemble in edit

### Sensitive Content Check

- [ ] When opening `~/.claude/skills/` in Finder, no skill names that reveal unannounced launches
- [ ] When opening other skills' SKILL.md files as references, don't accidentally show ones with API keys in plaintext
- [ ] `~/notes/meetings/` should be empty or anonymized before filming

### Energy Curve

| Segment | Energy | Notes |
|---|---|---|
| Hook | 10/10 | Demystify hard and fast |
| Setup | 7/10 | Set stakes |
| Format tour | 6/10 | Teaching mode, calm |
| Body build | 7/10 | Building momentum |
| Restart + test | 9/10 | THE PAYOFF |
| Aha moment | 8/10 | Let it breathe |
| 3 patterns | 7/10 | Practical, tight |
| Shortcut tip | 7/10 | Empowering |
| CTA | 10/10 | Get the click |

### Avoid These Mistakes

1. **Don't over-explain the format.** Viewers want to BUILD, not study YAML.
2. **Don't skip the live test.** This is the proof. Without it the video loses 50% of its value.
3. **Don't apologize on camera if something takes a second.** Cut the pause in edit.
4. **Don't deep-dive other skills.** Name-drop, don't tour.
5. **Don't use em dashes in the script.** Tyler's standing rule.

### Chapters (paste into description)

- 0:00 Empty folder, 15 minutes
- 0:25 What we're building
- 1:30 The SKILL.md format (60-second tour)
- 4:00 Live build: the body
- 8:30 Restart and test (the payoff)
- 12:00 Why this works (the aha)
- 14:00 The 3 patterns that make every skill robust
- 16:00 Get better fast (steal from existing skills)
- 16:45 Grab the code (free)
