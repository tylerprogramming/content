# Repurposed Shorts — 10 Claude Code Concepts

Source: ~/content/youtube/videos/003-claude-code-beginner-concepts/script.md

---

## Short #1: "Why Claude Gets Dumb Mid-Session"

**Source section:** Concept 2 — Context Window & Context Rot (2:30–3:45)
**Format:** Talking head
**Target length:** 50-60 seconds

### Hook (first 3 seconds)
"Your Claude Code sessions start sharp and slowly fall apart. Here's exactly why."

### Script
Your Claude Code sessions start sharp and slowly fall apart. Here's exactly why.

Claude has a memory limit called the context window. Every message, every file it reads, every response — it all lives in that window.

When it fills up, Claude starts forgetting what you told it an hour ago. This is called context rot. It's the #1 reason Claude feels like it's getting dumber mid-session.

Here's the fix. See that green bar at the bottom of your terminal? That's your context meter. Watch it.

When it starts getting full, type /compact. Claude summarizes the conversation and clears the noise. You can even tell it what to keep: /compact keep the API structure decisions.

Or just start a fresh session when you switch tasks. Don't try to do everything in one conversation.

Context rot is why your sessions feel great for 20 minutes and then go sideways. Now you know how to stop it.

### Text Overlays
- "context rot" — bold, red, kinetic slam at hook
- "/compact" — terminal typing effect, monospace green
- "fresh session = fresh Claude" — clean close, white on dark

### CueCard
Your sessions start sharp and slowly fall apart. Here's why.

Claude has a MEMORY LIMIT. Called the context window.

Every message, every file, every response - lives in that window.

When it fills up? Claude starts FORGETTING.

This is called CONTEXT ROT.

Fix:
- Watch the green bar at the bottom of your terminal
- Type /compact - summarizes, clears the noise
- Or: start a fresh session when you switch tasks

Don't try to do everything in one conversation.

Context rot = why sessions go sideways after 20 min. Now you know how to stop it.

### Remotion Prompt
```
Lines:
1. "context rot." — red bold text, slams in at 0s, slight shake effect
2. "/compact" — monospace terminal font, green on black, types in letter by letter at ~25s
3. "fresh session = fresh Claude" — clean white text, fade in at ~48s
Style: dark bg, high contrast, terminal aesthetic
```

---

## Short #2: "The One File Every Claude Code User Needs"

**Source section:** Concept 1 — CLAUDE.md (1:00–2:30)
**Format:** Talking head + screen demo
**Target length:** 55-65 seconds

### Hook (first 3 seconds)
"There's one file that changes how Claude Code works. Most people don't know it exists."

### Script
There's one file that changes how Claude Code works. Most people don't know it exists.

It's called CLAUDE.md.

Every time you open Claude Code, before it does anything else, it reads this file. Think of it as your instruction manual for Claude.

I've got my preferences, my workflow rules, my writing style — all in here. I wrote it once. Now every session starts with Claude already knowing how I work.

Without it? Claude is guessing. Every. Single. Time.

Day one task if you're just starting: create a CLAUDE.md. You don't even have to write it yourself.

Open Claude Code and type: "Help me create a CLAUDE.md for my project. Ask me questions about my preferences and workflow."

Claude will interview you and build the file for you.

One file. Every session. It compounds.

### Text Overlays
- "CLAUDE.md" — bold, types in like a filename at 0s
- "I wrote it once." — italic, slow fade
- "every session. it compounds." — strong close, pulse effect

### CueCard
There's ONE file that changes everything. Most people don't know it exists.

It's called CLAUDE.md.

Every time you open Claude Code - FIRST thing it does is read this file.

Your instruction manual for Claude.

Mine has:
- My preferences
- My workflow rules
- My writing style

I wrote it ONCE. Now every session starts with Claude already knowing how I work.

Without it? Claude is GUESSING. Every. Single. Time.

Day one task: create a CLAUDE.md.

Type this in Claude Code:
"Help me create a CLAUDE.md for my project. Ask me questions about my preferences and workflow."

Claude interviews you. Builds it for you.

One file. Every session. It COMPOUNDS.

### Remotion Prompt
```
Lines:
1. "CLAUDE.md" — large monospace filename, types in character by character at 0s, cursor blink
2. "I wrote it once." — italic white text, slow fade in at ~28s
3. "it compounds." — bold, warm yellow/gold color, pulse animation at ~55s
Style: clean dark terminal bg, minimal - let the filename breathe
```

---

## Short #3: "I Stopped Writing Long Prompts. I Do This Instead."

**Source section:** Concept 5 — Skills (6:15–7:45)
**Format:** Talking head + screen recording
**Target length:** 60-70 seconds

### Hook (first 3 seconds)
"I used to write a 500-word prompt every time I wanted Claude to plan a video. Now I type two characters."

### Script
I used to write a 500-word prompt every time I wanted Claude to plan a video. Now I type two characters.

This is a Claude Code skill. It's a markdown file that teaches Claude how to do a specific task your way, every time.

A slash command says "do this." A skill says "here's exactly how to do this — step by step, with all my preferences and rules baked in."

This one skill plans my YouTube videos. It tells Claude to do web research, analyze transcript structure, ask me specific questions, then generate a full script package.

I type /yt. That's it.

I have 20 of these. One for each workflow I kept doing manually — research, social posts, thumbnails, email campaigns.

Claude Code stops being a chatbot when you build skills. It becomes a system.

What's one task you do manually every week that could be a skill?

### Text Overlays
- "500-word prompt → 2 characters" — before/after contrast, hook
- "/yt" — terminal typing effect, big, centered
- "a system, not a chatbot" — bold close

### CueCard
I used to write a 500-WORD PROMPT every time I wanted to plan a video.

Now I type TWO characters.

This is a Claude Code SKILL.

A markdown file. Teaches Claude how to do a specific task YOUR way, every time.

Slash command = "do this"
Skill = "here's EXACTLY how to do this - step by step, all my preferences baked in"

My /yt skill:
- Does web research
- Analyzes transcript structure
- Asks me specific questions
- Generates a full script package

I just type /yt. That's it.

I have 20 of these.

Claude Code stops being a chatbot when you build skills.

It becomes a SYSTEM.

What's one task you do manually every week?

### Remotion Prompt
```
Lines:
1. "500-word prompt" strikethrough → "2 characters" — red strikethrough animates, then "2 characters" slams in green at 0s
2. "/yt" — massive terminal font, types in slowly centered on screen at ~30s
3. "a system, not a chatbot." — bold white, clean fade at ~58s
Style: high contrast, before/after color coding (red/green), terminal aesthetic
```

---

## Short #4: "I Run 3 Claude Instances at the Same Time"

**Source section:** Concept 8 — Sub-agents (9:45–10:45)
**Format:** Talking head
**Target length:** 45-55 seconds

### Hook (first 3 seconds)
"Most people run one Claude. I run three simultaneously. Here's how."

### Script
Most people run one Claude. I run three simultaneously. Here's how.

Sub-agents are separate Claude instances that your main Claude can spin up to handle specific tasks.

Each one gets its own context window. Clean slate. No context rot from the main session.

So instead of one Claude doing everything and slowly degrading — you have specialists.

Main Claude planning the strategy. One sub-agent doing research. Another writing the code.

And here's the wild part: Claude decides to spin them up on its own when the task warrants it. You don't always have to ask.

When to use them intentionally: any task that's self-contained. "Go analyze this dataset and come back with findings." That's a sub-agent task.

Parallel Claude. It's how you actually scale.

### Text Overlays
- "3 Claude instances. simultaneously." — bold, splits into 3 on screen at hook
- "specialists, not generalists" — clean mid
- "parallel Claude." — strong close

### CueCard
Most people run ONE Claude. I run THREE simultaneously.

Sub-agents = separate Claude instances your main Claude spins up.

Each one gets its own context window. Clean slate. No context rot.

Instead of ONE Claude doing everything and degrading:

- Main Claude: planning the strategy
- Sub-agent 1: research
- Sub-agent 2: writing the code

Wild part: Claude spins them up ON ITS OWN when the task warrants it.

When to use them intentionally: any self-contained task.
"Go analyze this dataset and come back with findings."

That's a sub-agent task.

Parallel Claude. That's how you scale.

### Remotion Prompt
```
Lines:
1. "3 Claude instances." — bold, then splits visually into 3 columns at 0s, each column pulses
2. "specialists, not generalists" — clean white italic, centered, fade at ~25s
3. "parallel Claude." — large bold, green accent, slam in at ~45s
Style: dark bg, visual split-screen effect on hook, minimal text overlays
```
