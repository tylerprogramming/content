# Shorts — Week of 2026-03-23

**Topic:** Claude Code — beginner concepts + skills
**Source research:** ~/content/research/2026-03-22-claude-code-beginner.md + 2026-03-22-claude-code-skills.md
**Links in descriptions → main videos:**
- Concepts video: "10 Claude Code Concepts I Wish I Knew From the Start"
- Skills video: "I Built a Claude Code Skill from Scratch (Watch Me Do It)"

---

## Short #1: The Context Rot Mistake

**Format:** Talking head (optional: 2-sec flash of a long messy chat thread)
**Target length:** 60–75 seconds (~110 words)

---

### Hook (first 3 seconds)
"Your Claude sessions are slowly getting dumber — and you're causing it."

### Script
Your Claude sessions are slowly getting dumber — and you're causing it.

Here's what's happening. Every message you send, every file Claude reads, every response it gives — that all goes into something called the context window. It's like short-term memory. And it has a limit.

Once you hit that limit, Claude starts dropping earlier context to make room. It forgets what you told it an hour ago. Output gets worse. You think Claude is broken. It's not — your session just got too long.

The fix is simple: start a fresh session every one to two hours. Or when you switch tasks.

One of the 10 concepts I cover in the full video — link below.

### On-Screen Text
- "context window = Claude's short-term memory" (at hook)
- "start fresh every 1–2 hours" (at fix)
- "10 Claude Code concepts → link below" (closing)

### Filming Checklist
- [ ] Talking head — clean background, good lighting
- [ ] Optional: have a long Claude chat open to flash on screen for 2 seconds at "context window" line
- [ ] Teleprompter loaded — moderate pace, pause after "you're causing it"
- [ ] Estimated takes: 2–3 (~5 min)

---

## Short #2: The One File

**Format:** Talking head + screen flash (CLAUDE.md open in VS Code for ~3 seconds)
**Target length:** 60–75 seconds (~110 words)

---

### Hook (first 3 seconds)
"There's one file that changes how Claude behaves in every single session. Most people have never heard of it."

### Script
There's one file that changes how Claude behaves in every single session. Most people have never heard of it.

It's called CLAUDE.md. You put it in your project folder — or in your home directory for global settings — and Claude reads it automatically at the start of every session.

[SHOW: CLAUDE.md open in VS Code — scroll slowly for 3 seconds]

You can put anything in here. How you want Claude to respond. What tools it's allowed to use. Your workflow preferences. Rules it should always follow.

No more typing the same instructions every time. You write it once, it works forever.

Full breakdown — what to actually put in this file — in the video linked below.

### On-Screen Text
- "CLAUDE.md" (on screen when you say the name)
- "reads it automatically every session" (mid-script)
- "write it once → works forever" (closing)

### Filming Checklist
- [ ] Talking head + screen switch
- [ ] Have CLAUDE.md open in VS Code — your real one, content visible
- [ ] Scroll slowly during the show moment — don't rush it
- [ ] Teleprompter for talking head portion
- [ ] Estimated takes: 2–3 (~5 min)

---

## Short #3: Slash Commands in Action

**Format:** Screen recording with voiceover + brief talking head at start/end
**Target length:** 75–90 seconds (~125 words)

---

### Hook (first 3 seconds)
"I type 12 characters and get a full YouTube competitor research report. Let me show you."

### Script
I type 12 characters and get a full YouTube competitor research report. Let me show you.

[SHOW: Terminal — type `/yt-search claude code`, hit enter]

This is a Claude Code skill. A skill is a markdown file that teaches Claude how to do a specific task your way. I wrote this one once. Now I just call it with a slash command.

[SHOW: Output streaming in — the research report appearing]

Watch what it produces. Competitor videos ranked by views. Content gaps. Title patterns. Everything I need to plan a video — in under 30 seconds.

I have 20 of these. One for every workflow I used to do manually.

How to build your own from scratch — link in the description.

### On-Screen Text
- "/yt-search claude code" (on screen at terminal)
- "a skill = a reusable workflow" (mid-script)
- "build your own → link below" (closing)

### Filming Checklist
- [ ] Screen recording ready (terminal + Claude Code)
- [ ] Have `/yt-search claude code` ready to type live — do a test run first
- [ ] Brief talking head at hook (3 sec) and closing CTA (5 sec)
- [ ] Make sure output is visible and readable at 1080p
- [ ] Estimated takes: 2–3 for screen portion, 1–2 for talking head (~10 min total)

---

## Short #4: 3 Types of Memory

**Format:** Talking head (optional: simple 3-row static graphic)
**Target length:** 60–75 seconds (~110 words)

---

### Hook (first 3 seconds)
"Claude Code has three types of memory. Most people are only using one."

### Script
Claude Code has three types of memory. Most people are only using one.

The first is your context window — that's the conversation you're having right now. Temporary. Gone when the session ends.

The second is CLAUDE.md — a file Claude reads at the start of every session. Permanent instructions. Always on.

The third is the memory skill — Claude can actually write notes about you and your preferences across sessions. Like a real assistant building a profile over time.

Most people rely entirely on the context window and wonder why Claude forgets everything. Use all three.

Full breakdown in the video linked below.

### On-Screen Text
- "3 types of Claude memory" (hook)
- "context / CLAUDE.md / memory skill" (mid-script — show all three at once)
- "use all three → link below" (closing)

### Filming Checklist
- [ ] Talking head — option to flash a simple text graphic (3 rows: Context Window / CLAUDE.md / Memory Skill)
- [ ] If using graphic: prepare it in advance — just plain text on dark background
- [ ] Teleprompter loaded — slow down on the three items, let them land
- [ ] Estimated takes: 2–3 (~5 min)

---

## Short #5: Stop Retyping Instructions

**Format:** Talking head + screen flash (type one line into CLAUDE.md, open new session)
**Target length:** 75–90 seconds (~125 words)

---

### Hook (first 3 seconds)
"Stop typing the same instructions into every Claude chat. There's a better way."

### Script
Stop typing the same instructions into every Claude chat. There's a better way.

Go to your home directory. Create a file called CLAUDE.md. Type one rule in it — anything. "Always respond concisely." "Never use em dashes." "Ask before running any command."

[SHOW: Type a rule into CLAUDE.md — e.g., "Always respond in bullet points when listing steps"]

Now open a fresh Claude Code session.

[SHOW: New session — Claude immediately following the rule without being told]

Claude reads that file automatically. Every session. You never have to say it again.

That's the most underused feature for beginners. One file, permanent behavior.

Everything that goes in mine — in the video linked below.

### On-Screen Text
- "CLAUDE.md — permanent instructions" (hook)
- "Claude reads this automatically" (at screen show moment)
- "one file → permanent behavior" (closing)

### Filming Checklist
- [ ] Talking head + screen switch
- [ ] Prep: have CLAUDE.md ready to edit live, add a simple rule during filming
- [ ] Open a new Claude session immediately after — shows the effect live
- [ ] Keep screen text large enough to read on mobile
- [ ] Estimated takes: 2–3 screen takes, 1–2 talking head (~8 min)
