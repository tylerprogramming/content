# Repurposed Shorts — Build a Claude Code Skill from Scratch

---

## Short 1: What a Claude Code Skill Actually Is

**Source section:** [0:30 – 1:30] What We're Building + Why It Matters
**Format:** Talking head with quick cuts to screen
**Estimated length:** 60-70 sec

---

**Hook (first 3 seconds):**
A Claude Code skill is just a markdown file. That's literally it.

---

**Script:**

A Claude Code skill is just a markdown file. That's it.

But here's what that file does - it teaches Claude how to do a specific task, your way, every single time.

I have 20 of them. One plans my YouTube videos. One generates thumbnails. One searches YouTube for trending topics and gives me a full research report.

Every single one is just a markdown file in a folder called skills.

The video you're watching right now was planned by one of those skills.

So if you've been thinking Claude Code skills are some complicated developer thing - they're not. They're instructions. Written in plain English. Stored in a folder.

If you can write a checklist, you can build a skill.

---

**Text Overlays:**
- "just a markdown file"
- "20 skills = 20 automated workflows"
- "if you can write a checklist, you can build this"

---

**CueCard:**

A Claude Code skill is just a markdown file. That's it.

But here's what that file does -
it teaches Claude how to do a specific task,
your way,
every single time.

I have 20 of them.
One plans my YouTube videos.
One generates thumbnails.
One searches YouTube for trending topics and gives me a full research report.

Every single one is just a markdown file
in a folder called skills.

The video you're watching right now was PLANNED by one of those skills.

So if you've been thinking Claude Code skills are some complicated developer thing -
they're not.
They're instructions.
Written in plain English.
Stored in a folder.

If you can write a checklist,
you can build a skill.

---

**Remotion Prompt:**

Style: Bold white sans-serif on dark background (near-black #111). High contrast.
Animation sequence:
1. 0:00-0:03 - "just a markdown file" types in one character at a time, terminal-style, then holds
2. 0:10-0:13 - Three bullet lines animate in fast stagger (0.1s apart): "YouTube plans", "Thumbnails", "Trending research"
3. 0:28-0:32 - "if you can write a checklist" fades in slow, then "you can build this" punches in bold and scales up slightly (1.0 to 1.05)
Font: JetBrains Mono or Inter Bold. No drop shadow. Clean.

---

---

## Short 2: The Description Field Controls Everything

**Source section:** [1:30 – 3:00] The SKILL.md Structure
**Format:** Mixed - talking head into screen recording of typing the front matter
**Estimated length:** 65-75 sec

---

**Hook (first 3 seconds):**
Most people build Claude Code skills that never trigger. Here's the one field they always get wrong.

---

**Script:**

Most people build Claude Code skills that never trigger. Here's the one field they always get wrong.

Every skill starts with a front matter block. And inside that block there's a field called description.

That description is how Claude decides when to activate your skill.

When you type "write me hooks for my video" - Claude scans every skill description in your library. If your description says "Generate YouTube hooks. Triggers on: write hooks, hook ideas, youtube hooks" - it matches, and your skill loads.

Get that description wrong? Claude ignores your skill entirely. You type the command, nothing happens, and you think skills don't work.

They work. You just didn't write the triggers.

Fix that one field and your skills start firing every single time.

---

**Text Overlays:**
- "the description field = the trigger"
- "Claude scans every skill"
- "fix this one field"

---

**CueCard:**

Most people build Claude Code skills that never trigger.
Here's the one field they always get wrong.

Every skill starts with a front matter block.
And inside that block there's a field called description.

That description is how Claude decides when to ACTIVATE your skill.

When you type "write me hooks for my video" -
Claude scans every skill description in your library.
If your description says
"Generate YouTube hooks. Triggers on: write hooks, hook ideas" -
it matches.
Your skill loads.

Get that description wrong?
Claude ignores your skill entirely.
You type the command, nothing happens,
and you think skills don't work.

They DO work.
You just didn't write the triggers.

Fix that one field
and your skills start firing every single time.

---

**Remotion Prompt:**

Style: Terminal-look. Dark green text on near-black background, monospace font (JetBrains Mono).
Animation sequence:
1. 0:00-0:03 - "skills that never trigger" types in fast, glitch effect on "never" (brief red flash then back to green)
2. 0:18-0:22 - A minimal YAML block appears character by character: description field line highlighted in yellow
3. 0:42-0:46 - "fix this one field" appears large, centered, white text on screen - brief scale punch (1.0 to 1.08 and back)
No background music cues needed. Keep it stark and technical.

---

---

## Short 3: Build a Hook Writer Skill in Under 5 Minutes

**Source section:** [3:00 – 5:30] Writing the Instructions + [5:30 – 7:00] Testing It Live
**Format:** Screen recording with occasional talking head cuts
**Estimated length:** 70-75 sec

---

**Hook (first 3 seconds):**
Watch me build a working Claude Code skill right now - from a blank file to a live slash command.

---

**Script:**

Watch me build a working Claude Code skill right now - from a blank file to a live slash command.

Step one - create a folder in your skills directory. Call it hook-writer.

Step two - create SKILL.md inside it. Add the front matter: name, description, allowed tools, and user-invocable set to true.

Step three - write the instructions. This is just an SOP. What should Claude do first? Then what? What should the output look like?

For a hook writer: parse the topic, generate 5 hooks using 5 different techniques, label each one, explain why it works, then ask which direction to go.

Save it.

Step four - go to your terminal and type /hook-writer Claude Code beginner tutorial.

Claude reads your SKILL.md, follows your instructions, and returns 5 hooks in under 10 seconds.

That's a real skill. Two files. Under five minutes. And you never write hooks manually again.

---

**Text Overlays:**
- "step 1: create the folder"
- "step 3: write the SOP"
- "never write hooks manually again"

---

**CueCard:**

Watch me build a working Claude Code skill right now -
from a blank file to a live slash command.

Step one -
create a folder in your skills directory. Call it hook-writer.

Step two -
create SKILL.md inside it.
Add the front matter: name, description, allowed tools, user-invocable true.

Step three -
write the instructions.
This is just an SOP.
What should Claude do first? Then what? What does the output look like?

For a hook writer:
parse the topic,
generate 5 hooks using 5 different techniques,
label each one,
explain why it works,
ask which direction to go.

Save it.

Step four -
go to your terminal and type /hook-writer Claude Code beginner tutorial.

Claude reads your SKILL.md,
follows your instructions,
returns 5 hooks in under 10 seconds.

That's a real skill.
Two files. Under five minutes.
And you never write hooks manually again.

---

**Remotion Prompt:**

Style: Split-screen energy. Left side: numbered step labels in bold white. Right side: minimal file tree visualization that builds as steps progress.
Animation sequence:
1. 0:00-0:03 - "from blank file to live slash command" sweeps in left to right, fast, white on dark
2. 0:08-0:35 - Step number cards (1, 2, 3, 4) pop in at each step mention - large number, short label below, then fades
3. 0:55-0:60 - "never write hooks manually again" - text grows from center, strong scale-in, holds 3 seconds
Font: Inter ExtraBold for step numbers, Inter Regular for labels.

---

---

## Short 4: Why Your First Skill Version Will Be Wrong (And That's Fine)

**Source section:** [7:00 – 8:30] Iterating - Making It Better + [8:30 – 10:00] Adding a Reference File
**Format:** Talking head with quick screen cuts
**Estimated length:** 60-70 sec

---

**Hook (first 3 seconds):**
The first version of every Claude Code skill I've built was wrong. Here's why that's the whole point.

---

**Script:**

The first version of every Claude Code skill I've built was wrong. Here's why that's the whole point.

You build a hook writer skill. You test it. The hooks come back too formal - they sound like a marketing email, not like you.

So you open SKILL.md and add two lines to the rules section: "Write in first person, casual and direct." "Short sentences. Punchy."

Run it again. Better.

Then you create an examples file. Drop in 5 hooks that actually sound like you. Add 5 examples of what to avoid. Tell the skill to read that file before generating anything.

Run it again. Now it sounds exactly like you.

That's skill engineering. You use it, you see what's off, you fix one thing at a time.

My YouTube planning skill took 15 iterations over 6 months. Now it's the best thing in my workflow.

Skills are never finished. But they get better every single time you use them.

---

**Text Overlays:**
- "first version = always wrong"
- "fix one thing at a time"
- "15 iterations over 6 months"

---

**CueCard:**

The first version of every Claude Code skill I've built was wrong.
Here's why that's the whole point.

You build a hook writer skill.
You test it.
The hooks come back too formal -
they sound like a marketing email,
not like you.

So you open SKILL.md
and add two lines to the rules section:
"Write in first person, casual and direct."
"Short sentences. Punchy."

Run it again. Better.

Then you create an examples file.
Drop in 5 hooks that actually sound like you.
5 examples of what to avoid.
Tell the skill to read that file before generating anything.

Run it again.
Now it sounds EXACTLY like you.

That's skill engineering.
Use it.
See what's off.
Fix one thing at a time.

My YouTube planning skill took 15 iterations over 6 months.
Now it's the best thing in my workflow.

Skills are never finished.
But they get better every single time you use them.

---

**Remotion Prompt:**

Style: Warm, slightly lighter background (#1a1a2e or similar dark navy). White text. Emphasis words in amber/gold (#FFB347).
Animation sequence:
1. 0:00-0:03 - "first version = always wrong" types in with a subtle shake/wobble effect on "wrong"
2. 0:20-0:24 - Two rule lines animate in as if being typed into a code editor, cursor blinking between them
3. 0:52-0:58 - "15 iterations" counter animates (number counts up 1 to 15 quickly), then "the best thing in my workflow" fades in beneath
Font: JetBrains Mono. Amber accents on key words only.

---
