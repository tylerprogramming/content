# Script — I Built a Claude Code Skill from Scratch (Watch Me Do It)

**Target length:** 13–16 minutes
**Format:** Talking head + live terminal build (real files, real demo)
**Audience:** Founders/entrepreneurs who've heard of skills but haven't built one

---

## [0:00 – 0:30] Hook

[SHOW: Talking head, direct to camera]

I have 20 Claude Code skills. And I built every single one of them the same way.

In this video, I'm going to build one from scratch — live, right now — so you can see exactly how it's done.

No theory. No slides. We're opening a terminal, writing a SKILL.md file, and testing it before this video is over.

Let's go.

[NOTE: Under 30 seconds. High energy. Cut fast to screen.]

---

## [0:30 – 1:30] What We're Building + Why It Matters

[SHOW: Talking head briefly, then switch to skills folder]

Before we build — real quick on why this matters.

A Claude Code skill is a markdown file that teaches Claude how to do a specific task your way. Every time you invoke it, Claude reads your instructions first and follows them exactly.

[SHOW: ~/.claude/skills/ folder — all skills visible]

This is my skills library. Twenty skills. Each one encodes a workflow I used to do manually.

This one plans my YouTube videos. This one generates thumbnails. This one searches YouTube for trending topics and gives me a full report.

The video you're watching right now was planned using one of these skills.

[SHOW: Highlight one skill file briefly]

Every skill is just a markdown file with a specific structure. That's it.

Today we're going to build a new one — live. We're building a hook writer skill.

[NOTE: "Hook writer" = give it a video topic, it generates 5 YouTube hook options. Simple enough to build in the video, immediately useful for founders doing content.]

---

## [1:30 – 3:00] The SKILL.md Structure

[SHOW: Open a blank file in editor labeled SKILL.md]

Every skill starts with a SKILL.md file. And it has two parts.

**Part 1: Front matter.**

[SHOW: Type the front matter live]

```yaml
---
name: hook-writer
description: Generate 5 YouTube hook options for a video topic. Triggers on: write hooks, hook options, youtube hooks, hook ideas for my video.
argument-hint: [video topic or title]
allowed-tools: Read, Write
user-invocable: true
---
```

This front matter is critical. The `description` field is how Claude knows when to trigger this skill. When you say "write me some hooks for my Claude Code video" — Claude matches that to this description and loads the skill.

`allowed-tools` limits what Claude can do inside this skill. Hook writing only needs Read and Write — no web search, no bash commands.

`user-invocable: true` means you can trigger it manually with `/hook-writer`.

[SHOW: Pause on the front matter — let viewers read it]

That front matter? Took me weeks to understand why it mattered. Now I never skip it.

---

## [3:00 – 5:30] Writing the Instructions

[SHOW: Continue typing below the front matter]

Part 2 is the instructions — the actual workflow Claude follows.

Think of this like writing an SOP for a new employee. Step by step. What to do, in what order, what the output should look like.

[SHOW: Type the instructions live]

```markdown
Generate 5 YouTube hook options for the video topic at $ARGUMENTS.

## Step 1: Understand the Topic

Parse $ARGUMENTS for:
- The video topic or working title
- Target audience (if mentioned)
- Any specific angle (if mentioned)

If no topic is provided, ask: "What's the topic or working title for this video?"

## Step 2: Generate 5 Hooks

Write 5 distinct hook options. Each hook should be:
- Word-for-word, 2-4 sentences, ready to read on camera
- Under 30 seconds when spoken (~60-80 words max)
- Starting with the first sentence — no "in this video" openers

Use a different technique for each hook:
1. Curiosity gap — create an information gap the viewer needs to close
2. Bold claim — make a strong, specific, possibly contrarian statement
3. Story open — start mid-story with a specific moment
4. Pattern interrupt — say something unexpected or counterintuitive
5. Pain/problem — name the exact frustration the viewer has right now

## Step 3: Present Options

Show all 5 hooks clearly labeled with their technique.
After each hook, one sentence explaining why it works.

Ask: "Which direction feels right? Want me to write more in that style or adjust any of these?"

## Rules

- Never start a hook with "In this video" or "Today I'm going to"
- Every hook must be usable word-for-word — no placeholders like [your topic]
- Keep hooks under 80 words — if it's longer, it's an intro, not a hook
- Match the speaking style: direct, conversational, no corporate language
- Always label the technique used
```

[SHOW: Pause on finished instructions — scroll through slowly]

That's the whole skill. Let me save it.

[NOTE: Actually save the file to ~/.claude/skills/hook-writer/SKILL.md during filming]

---

## [5:30 – 7:00] Testing It Live

[SHOW: Switch to Claude Code terminal]

Now the fun part. Let's test it.

[SHOW: Type in terminal]

```
/hook-writer Claude Code beginner concepts for founders
```

[SHOW: Claude loading the skill and generating hooks]

Watch what happens. Claude reads our SKILL.md first — the whole thing — and then follows the instructions.

[NOTE: Wait for Claude to generate. Fill dead air:]
> "Notice it's using the techniques we specified — curiosity gap, bold claim, story open. It's not just generating random options."

[SHOW: The 5 hooks appear with labels]

Five hooks. Each one a different technique. Each one labeled. Ready to use.

This would have taken me 20 minutes to write manually. Now it takes 3 seconds and a slash command.

---

## [7:00 – 8:30] Iterating — Making It Better

[SHOW: Screen with output, then back to SKILL.md]

Now here's what nobody talks about: the first version is never the final version.

Let me show you how I iterate.

Say the hooks Claude generated are a bit too formal — they don't sound like me. I'd go back to the rules section and add:

[SHOW: Add to rules section]

```
- Write in first person, casual and direct — like Tyler talking to a friend, not a marketer writing copy
- Short sentences. Punchy. Never use em dashes.
```

[SHOW: Save and re-run]

Run it again. Now the output changes.

[SHOW: Second output — visibly more casual/direct]

That's skill engineering. You use it, you see what's off, you fix one thing at a time.

Ben AI who has 161K views on his skills video says he iterated on his infographic skill five times before he was happy with it.

My YouTube planning skill? Probably 15 iterations over 6 months.

Skills are never finished. But they get better every time.

---

## [8:30 – 10:00] Adding a Reference File

[SHOW: Create a references folder inside the skill]

Here's the upgrade. If I want the hooks to match my specific style — not just generic YouTube advice — I can add a reference file.

[SHOW: Create ~/. claude/skills/hook-writer/examples.md]

```markdown
# Good Hook Examples

## What Tyler's hooks sound like:

**Curiosity gap:**
"I've been using Claude Code every single day for months. And if I'm being honest — the first few weeks I was doing it completely wrong."

**Bold claim:**
"Most Claude Code tutorials start with installation. This one doesn't."

**Story open:**
"Six months ago I had zero Claude Code skills. Today my whole YouTube channel runs on autopilot."

## What to AVOID:
- "In this video I'm going to show you..."
- "Today we're talking about..."
- "Have you ever wondered why..."
- Corporate language, em dashes, passive voice
```

[SHOW: Add reference to SKILL.md instructions]

Now I add one line to the instructions:

```markdown
Read ~/. claude/skills/hook-writer/examples.md before writing any hooks. Match the tone and style of the good examples. Avoid anything in the "what to avoid" section.
```

[SHOW: Run again with the reference file]

Now Claude has a style guide. Output is immediately more on-brand.

That's the difference between a skill that's okay and a skill that sounds like you.

---

## [10:00 – 11:30] The Folder Structure (Full Picture)

[SHOW: File tree of the finished hook-writer skill folder]

Let me show you what we've built:

```
~/.claude/skills/hook-writer/
├── SKILL.md          ← the core instructions
└── examples.md       ← style reference file
```

That's a complete skill. Two files.

[SHOW: Compare to a more complex skill like /yt]

More complex skills — like my YouTube video planner — have more files: Python scripts for web search, multiple reference docs, a filming guide template. But the structure is the same.

SKILL.md is always the brain. Reference files and scripts are the supporting knowledge.

[SHOW: Quick tour of the skills folder — highlight a few]

This one has a Python script that downloads YouTube audio and transcribes it.
This one has a web search script.
This one just has the SKILL.md — two paragraphs — and it works perfectly.

Complexity scales with the task. Start simple.

---

## [11:30 – 12:30] Sharing Your Skills

[SHOW: Talking head briefly]

One more thing. Skills are shareable.

[SHOW: GitHub repo or zip file concept]

You can share a skill as a zip file — someone else unzips it into their `~/.claude/skills/` folder and they're running your workflow immediately.

Or put it on GitHub. The Anthropic skills repo has 87,000 stars. People are building and sharing skills every week.

[SHOW: awesome-claude-code GitHub page briefly]

My skills are on GitHub too. Link in the description — you can download them and use them as starting points for your own.

But the most powerful skills? They're the ones you build for your specific workflow. Nobody else has my YouTube planning skill with my CLAUDE.md and my filming guide format. That's the moat.

---

## [12:30 – 13:30] CTA

[SHOW: Talking head]

We just built a real Claude Code skill. From zero.

Front matter, instructions, reference file, tested, iterated.

That's the whole process.

If you want to see what a more complex skill looks like — I have a full breakdown of my YouTube planning skill in the next video. It's the one that actually runs this channel.

Subscribe if you want more. I post Claude Code tutorials every week.

[SHOW: Subscribe animation + end screen linking to Video 1]

[NOTE: The end card should link to the "10 Concepts" video — natural funnel between the two.]
