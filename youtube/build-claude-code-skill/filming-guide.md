# Filming Guide — I Built a Claude Code Skill from Scratch (Watch Me Do It)

## Pre-Recording Setup

- [ ] Create empty `~/.claude/skills/hook-writer/` folder (so it's ready to write into)
- [ ] Open VS Code or editor with that folder ready
- [ ] Open Claude Code terminal — fresh session
- [ ] Close all other apps, disable notifications
- [ ] Have `~/.claude/skills/` folder visible in editor sidebar (viewers will see your full skills library)
- [ ] Teleprompter loaded with script
- [ ] Screen layout: editor left half, terminal right half (or switch as needed)

### Files to Have Ready (Copy-Paste During Filming)

**SKILL.md front matter:**
```yaml
---
name: hook-writer
description: Generate 5 YouTube hook options for a video topic. Use when asked to write hooks, generate hook ideas, hook options, or youtube hooks for my video.
argument-hint: [video topic or title]
allowed-tools: Read, Write
user-invocable: true
---
```

**SKILL.md instructions (full):**
```markdown
Generate 5 YouTube hook options for the video topic at $ARGUMENTS.

## Step 1: Understand the Topic

Parse $ARGUMENTS for:
- The video topic or working title
- Target audience (if mentioned)
- Any specific angle (if mentioned)

If no topic is provided, ask: "What's the topic or working title for this video?"

## Step 2: Generate 5 Hooks

Write 5 distinct hook options. Each should be:
- Word-for-word, 2-4 sentences, ready to read on camera
- Under 80 words
- Starting strong — no "In this video" openers

Use a different technique for each:
1. **Curiosity gap** — create an information gap the viewer needs to close
2. **Bold claim** — make a strong, specific, possibly contrarian statement
3. **Story open** — start mid-story with a specific moment
4. **Pattern interrupt** — say something unexpected or counterintuitive
5. **Pain/problem** — name the exact frustration the viewer has right now

## Step 3: Present Options

Show all 5 hooks clearly labeled with their technique.
After each hook, one sentence explaining why it works.

Ask: "Which direction feels right? Want more in that style?"

## Rules

- Never start with "In this video" or "Today I'm going to"
- Every hook must be usable word-for-word — no placeholders
- Keep under 80 words — longer = intro, not a hook
- Direct, conversational tone — no corporate language, no em dashes
- Always label the technique
```

**examples.md (reference file):**
```markdown
# Hook Examples — Tyler's Style

## Good hooks:

**Curiosity gap:**
"I've been using Claude Code every single day for months. And if I'm being honest — the first few weeks I was doing it completely wrong."

**Bold claim:**
"Most Claude Code tutorials start with installation. This one doesn't."

**Story open:**
"Six months ago I had zero Claude Code skills. Today my whole YouTube channel runs on autopilot."

## What to AVOID:
- "In this video I'm going to show you..."
- "Today we're talking about..."
- Corporate language, em dashes, passive voice
- Hooks over 80 words
```

---

## Timing Cheat Sheet

| Section | Target | Running |
|---------|--------|---------|
| Hook | 0:30 | 0:30 |
| What we're building | 1:00 | 1:30 |
| SKILL.md structure | 1:30 | 3:00 |
| Writing instructions | 2:30 | 5:30 |
| Live test | 1:30 | 7:00 |
| Iterating | 1:30 | 8:30 |
| Reference file | 1:30 | 10:00 |
| Folder structure | 1:30 | 11:30 |
| Sharing | 1:00 | 12:30 |
| CTA | 1:00 | 13:30 |

**Target: 13–14 minutes total.**

---

## Step-by-Step Filming

### Step 1 — Hook (0:00–0:30)
**On camera, talking head.**

> "I have 20 Claude Code skills. And I built every single one of them the same way. In this video, I'm going to build one from scratch — live, right now..."

Cut to screen immediately after "Let's go."

---

### Step 2 — Show Skills Library (0:30–1:30)

**Switch to editor — skills folder visible in sidebar.**

> "This is my skills library. Twenty skills. Each one encodes a workflow I used to do manually."

Slowly scroll through the folder list. Let viewers see the names: yt, yt-search, transcribe, shorts, seo, chapters, etc.

Open one skill briefly (yt/SKILL.md) — scroll through it fast to show complexity.

> "Today we're building a new one — a hook writer. Give it a video topic, get 5 hook options back. Let's start."

---

### Step 3 — Create the Skill Folder + SKILL.md (1:30–3:00)

**In terminal:**
```bash
mkdir -p ~/.claude/skills/hook-writer
code ~/.claude/skills/hook-writer/SKILL.md
```

**Now in editor — type (or paste) the front matter:**

```yaml
---
name: hook-writer
description: Generate 5 YouTube hook options for a video topic...
argument-hint: [video topic or title]
allowed-tools: Read, Write
user-invocable: true
---
```

**What you say while typing:**
> "Every skill starts with front matter. The `description` field is the most important part — this is literally how Claude decides when to use this skill. Get this wrong and your skill never triggers."

Pause on the description field. Read it out loud.

> "`allowed-tools: Read, Write` — I'm limiting Claude to only reading and writing files. It doesn't need web search or bash to write hooks. Keep skills scoped."

---

### Step 4 — Write the Instructions (3:00–5:30)

**Continue typing below the front matter divider:**

Type (or paste) the instructions. Narrate as you go:

> "Below the front matter is the actual workflow. Think of this as an SOP — step by step, exactly what Claude should do."

Pause on **Step 2** (the 5 techniques):
> "I'm telling it which 5 techniques to use. This is the difference between a generic hook generator and one that produces 5 distinctly different hooks."

Pause on **Rules** section:
> "The rules section is where you handle everything that can go wrong. Every rule in here came from a bad output I got in testing."

**Save the file.** Show it saving.

---

### Step 5 — Test It Live (5:30–7:00)

**Switch to Claude Code terminal.**

```
/hook-writer Claude Code beginner concepts for founders
```

**While Claude loads the skill:**
> "Notice it's reading the SKILL.md first — that front matter triggered the match. Now it's following the instructions step by step."

**When output appears:**
Show all 5 hooks. Read the technique labels.

> "Five hooks. Five different techniques. Labeled. Word-for-word ready."

Point out 1-2 specifically that are strong.

> "This would have taken me 20 minutes. Now: three seconds and a slash command."

---

### Step 6 — Iterate (7:00–8:30)

**Back to SKILL.md in editor.**

> "First version is never the final version. Let's say these hooks sound a little too formal — not quite my voice."

Add to Rules section:
```
- Write like Tyler talking to a friend — direct, casual, punchy
- Short sentences. Never use em dashes or corporate language.
```

Save. Switch back to terminal. Run again:
```
/hook-writer Claude Code beginner concepts for founders
```

**Show the difference in the second output.** Point it out explicitly.

> "One rule change. That's it. The output shifts immediately. This is the loop: use it, spot what's off, fix one thing, run again."

---

### Step 7 — Add Reference File (8:30–10:00)

**In terminal:**
```bash
code ~/.claude/skills/hook-writer/examples.md
```

**Type/paste the examples file.** Narrate:
> "Now I'm giving Claude a style guide. Real examples of hooks that sound like me. And a list of what to avoid."

**Add one line to SKILL.md instructions:**
```
Read ~/.claude/skills/hook-writer/examples.md before writing. Match the tone. Avoid anything in the "what to avoid" section.
```

**Run the skill a third time.** Show output.
> "Now it has a reference point. Outputs are immediately more on-brand."

---

### Step 8 — Show Full Folder Structure (10:00–11:30)

**Show the file tree:**
```
~/.claude/skills/hook-writer/
├── SKILL.md
└── examples.md
```

> "Two files. That's a complete skill."

**Compare to a complex skill (yt or transcribe):**
```
~/.claude/skills/yt/
├── SKILL.md
└── (no additional files needed — uses tools)

~/.claude/skills/transcribe/
├── SKILL.md
└── transcribe_video.py
```

> "Complexity scales with the task. The transcribe skill has a Python script for downloading YouTube audio. The hook writer just needs two markdown files."

---

### Step 9 — Sharing (11:30–12:30)

**Briefly show GitHub concept — no long demo.**

> "Skills are shareable. My 20 skills are on GitHub — link in the description. Download them, use them as starting points, customize them for your workflow."

Show awesome-claude-code GitHub page briefly.

> "87,000 stars on the community skills repo. People are building and sharing these every week."

> "But the most powerful skills? The ones you build for your specific workflow. Nobody else has my YouTube planning skill with my CLAUDE.md and my filming guides. That's the real advantage."

---

### Step 10 — CTA (12:30–13:30)

**Back on camera.**

> "We just built a real Claude Code skill. From zero."
> "If you want to go deeper — I've got a full video on the 10 Claude Code concepts every beginner needs to know. That's the foundation for everything we just did."
> "Subscribe, I post Claude Code tutorials every week."

---

## On-Camera Tips

- **Type live, don't paste** for the most important sections (description, rules) — viewers want to see you thinking through it
- **Paste** for the boilerplate instructions block — no need to type 200 words live
- **When Claude is processing:** talk through what's happening. "It matched the description field. Now it's loading the SKILL.md. Now following Step 1..."
- **If the skill doesn't trigger right:** debug it on camera. "The description didn't match — let me adjust the trigger phrase." That's great content.
- **Energy:** confident builder, not teacher. You're showing how you work, not presenting a lesson.
- **Speed:** keep the terminal section moving. No long silences. Talk through every action.
