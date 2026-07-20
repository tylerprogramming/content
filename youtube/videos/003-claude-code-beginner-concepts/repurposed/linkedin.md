# LinkedIn Posts — 10 Claude Code Concepts

Source: ~/content/youtube/videos/003-claude-code-beginner-concepts/script.md

Rules: no hashtags, no markdown bold, no promotional framing - teach, don't sell.

---

## Post 1 — Context Rot (Recommended)

Most people think Claude Code is getting worse mid-session.

It's not. You're hitting something called context rot.

Claude has a memory limit called the context window. Every message, every file it reads, every response - it all lives there. When it fills up, Claude starts forgetting what you told it earlier.

This is why your sessions feel sharp for 20 minutes and then slowly fall apart.

Three ways to handle it:

1. Watch the green bar at the bottom of your terminal. That's your context meter.

2. Type /compact when it starts getting full. Claude summarizes the conversation and clears the noise. You can even specify what to keep: "/compact keep the API structure decisions"

3. Start fresh sessions when you switch tasks. Don't try to do everything in one conversation.

I wasted weeks wondering why Claude felt inconsistent. Context rot was the answer almost every time.

If you're using Claude Code and your sessions degrade over time - this is your fix.

---

## Post 2 — CLAUDE.md

Every Claude Code session, Claude reads one file before it does anything else.

Most people don't know this file exists.

It's called CLAUDE.md. It sits at the root of your project (or home directory for global settings). Think of it as your permanent instruction manual for Claude.

Mine has:
- My communication preferences
- My workflow rules
- My writing style and voice
- Project-specific conventions

I wrote it once, over an hour, with Claude's help. Now every single session starts with Claude already knowing how I work - my preferences, my rules, my way of doing things.

Without it, Claude is guessing. Every session. From scratch.

The fastest way to create one: open Claude Code and type "Help me create a CLAUDE.md for my project. Ask me questions about my preferences and workflow."

Claude will interview you and build the file for you.

It takes an hour. It pays back that hour every single day.

---

## Post 3 — Skills vs Slash Commands

There's a difference between a Claude Code slash command and a Claude Code skill that most people never learn.

A slash command says "do this."

A skill says "here's exactly how to do this - step by step, with all my preferences and rules baked in, every time."

A skill is a markdown file. No code. Just detailed instructions for how Claude should run a specific workflow your way.

I have one skill that plans my YouTube videos. When I type /yt, Claude:
- Does web research on the topic
- Analyzes the transcript structure
- Asks me specific questions about my angle
- Generates a full script package with titles, hooks, and a filming guide

Without the skill, I'd be writing a 500-word prompt every time. With it, I type two characters.

I have 20 of these skills now. One for each workflow I kept repeating manually.

This is the point where Claude Code stops being a chatbot and starts being a system.

If you're using Claude for any repeated workflow and you haven't turned it into a skill yet - that's the next thing to do.
