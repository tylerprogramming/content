# Your First AI Agent (Video 2)

The easy way to build a real AI agent. No framework, no code, about ten minutes. Copy the file at the bottom, change the topic, run it. That's the whole thing.

Free pack + newsletter: https://free.tylerai.dev/youtube/

> On-screen note: show this doc as you build the agent live. The viewer should be able to copy the SKILL.md below and follow along in real time.

## What an agent actually is (plain English)
An agent is three things: a goal, a tool it can use, and the freedom to pick its own steps to reach the goal. That's it. Everything else is jargon. We're going to build one that researches a topic for you.

## What we're building
A Research Agent. You give it a topic. It searches the web, reads real sources, and writes you a one-page brief with the links. Useful for everyone, and it's unmistakably an agent - it decides what to search and what to read.

## Skills / tools used
| Piece | What it is |
|---|---|
| Claude Code | The runtime. Free to start, runs on your machine. |
| Web search | The one tool the agent uses to go read the internet. |
| `research-agent` (you build it) | A single `SKILL.md` file, in plain English. This IS the agent. |

## The flow (what you'll see on screen)
1. Make a folder called `research-agent`.
2. Create one file inside it: `SKILL.md`.
3. Paste the file below.
4. Trigger it in Claude Code and give it a topic.
5. Watch it search, read, and write the brief.

## The agent (copy this whole file)
Save as `research-agent/SKILL.md`:

```markdown
---
name: research-agent
description: Research a topic and write a one-page brief with real sources. Trigger on "research", "look into", "write me a brief on".
---

# What this agent does
Given a topic, it searches the web, reads the most relevant sources, and writes a clear one-page brief a normal person can act on.

# Steps
1. Take the topic the user gives you.
2. Search the web for it. Do a few different searches to cover the angles.
3. Open and actually read the most useful sources. Skip the junk.
4. Write a one-page brief with these sections:
   - The short answer (2-3 sentences)
   - Key points (5 bullets)
   - What to do next (3 bullets)
   - Sources (the links you actually used)
5. Save it as a markdown file named after the topic.

# Rules
- Only use things you actually read. No making up facts.
- If sources disagree, say so, don't pick one silently.
- Keep it to one page. Tight beats long.
- Plain language. Write like you're explaining it to a friend.
```

## Try it
Trigger the agent and say: "Research the best free tools for starting a newsletter in 2026." Watch it work, then open the brief it wrote.

## The honest part
It won't be perfect every time. It gets you most of the way there and you nudge it - fix a section, tell it to dig deeper on one point. That back-and-forth is the whole point. You're working with it.

## Start here
You just built one agent. Now change the steps to fit something YOU do every week - sorting a folder, drafting replies, summarizing a doc. Same file, different steps. That's how you build the next one.
