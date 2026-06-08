# Tweets — 10 Claude Code Concepts

Source: ~/content/youtube/claude-code-beginner-concepts/script.md
Rules: no hashtags, under 280 chars, standalone insights only

---

## Tweet 1 — Context Rot (Hot Take)
Your Claude Code isn't getting worse. You're hitting context rot.

Claude has a memory limit. When it fills up, Claude forgets what you said an hour ago.

Type /compact to clear it. Start fresh sessions when you switch tasks.

That's it.

---

## Tweet 2 — CLAUDE.md (Practical Tip)
Claude Code reads one file before every session.

It's called CLAUDE.md. Your preferences, rules, and workflow - written once, applied every time.

Without it, Claude guesses how you like to work. Every. Single. Session.

Create one today.

---

## Tweet 3 — Hot Take: Skills vs Chatbots
Claude Code users who only use it as a chatbot are leaving 80% of the value on the table.

The upgrade: build skills.

A skill is a markdown file that encodes your workflow. Type one slash command. Claude runs your whole process.

---

## Tweet 4 — Practical: Permissions
Claude Code will ask permission before every action by default.

It's safe - but it kills your flow.

Fix: pre-approve the safe stuff in settings.json (reading files, running tests, git ops).

Claude still asks for anything risky. You just stop getting interrupted every 30 seconds.

---

## Tweet 5 — Hot Take: Sub-agents
Running one Claude instance is the slow way.

Sub-agents let you spin up specialist Claude instances - each with a clean context window.

Main Claude plans. Sub-agent researches. Another writes code. All simultaneously.

Parallel Claude is how you actually scale.

---

## Tweet 6 — Memory (Insight)
The difference between Claude that feels like a tool and Claude that feels like a collaborator:

Memory.

Claude Code can remember your preferences, project conventions, and working style across every session.

Every session. Already knowing you. Not guessing.

---

## Tweet 7 — Thread Option: Context Rot Fix

Tweet 1/3:
Your Claude Code sessions degrade over time. Here's why and how to fix it in 2 minutes.

Tweet 2/3:
Claude has a context window - a memory limit. Every message, file read, and response fills it up. When it's full, Claude starts forgetting earlier parts of your session. This is context rot.

Fix: watch the green bar at the bottom of your terminal. When it gets full, type /compact. Claude summarizes and clears the noise. You can specify what to keep: "/compact keep the API structure decisions"

Tweet 3/3:
Or just start fresh sessions when you switch tasks. Don't try to do everything in one conversation.

Context rot explains 80% of "Claude is getting dumber" complaints. Now you know how to stop it.
