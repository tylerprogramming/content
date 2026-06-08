# Filming Guide: Claude Code /btw

## Pre-Recording Setup

1. **Clean terminal** — Clear history, close unnecessary tabs, clean desktop
2. **Have a project open** — Something with enough files/context that /btw has material to answer from
3. **Prepare a task prompt** — Something that takes 30-60 seconds to run so you have time to demo /btw while it's working. Suggestions:
   - "Build a React component that displays a list of users with search and pagination"
   - "Refactor this file to use TypeScript interfaces and add error handling"
   - Something visible — you want the viewer to see Claude is actively working
4. **Test /btw before recording** — Make sure it's working in your current Claude Code version
5. **Font size** — Bump terminal font to at least 16pt so it's readable on YouTube

## Filming Steps

### Step 1: Hook (Face to Camera)
**What you do:** Look at camera, deliver the hook
**What you say:**
> "Every time you open a new Claude Code session just to ask a quick question, you're burning ten to twenty thousand tokens for nothing..."

**Tips:** Quick energy. Don't over-explain. Get through this in 20-25 seconds.

---

### Step 2: The Problem (Terminal + Face)
**What you do:** Show Claude Code open in terminal. Optionally show opening a second tab to illustrate the "old way."
**What you say:**
> "Here's the situation. You've got Claude Code working on something..."

**Tips:** This is relatable pain. Let the frustration land. Everyone who uses Claude Code has felt this.

---

### Step 3: What /btw Does (Screen Recording)
**What you do:** Type a task prompt into Claude Code. While it's working, type:
```
/btw what files have you read so far?
```
**What you say:**
> "/btw lets you ask a side question without interrupting the main task..."

**What happens:** An overlay appears with the answer. The main task continues running above it.

**What you show:** Point out that the main task is still running. Press Space to dismiss the overlay.

---

### Step 4: Live Demo (Screen Recording)
**What you do:** Run a real task. While it's processing:

**Demo 1 — Successful /btw:**
```
/btw what's the name of the utility function you created?
```
Show it answering. Press space to dismiss.

**Demo 2 — Showing the limitation:**
```
/btw actually, can you make that a CSV instead of JSON?
```
Show that it answers but explain it can't actually make changes — no tool access.

**Tips:** Do this LIVE. Don't fake it. The authenticity matters. If something unexpected happens, roll with it — that's content.

---

### Step 5: When to Use What (Face to Camera)
**What you do:** Explain the mental model
**What you say:**
> "/btw sees everything but can't touch anything. A subagent can touch everything but starts with nothing. They're opposites."

**Tips:** This is the key insight of the video. Say it clearly. Maybe repeat it.

---

### Step 6: Recap + CTA (Face to Camera)
**What you do:** Quick summary, clean sign-off
**What you say:**
> "So that's /btw. Side questions that cost almost nothing..."

**Tips:** 15-20 seconds max. Don't drag it.

---

## Timing Cheat Sheet

| Section | Target Duration | Running Total |
|---------|----------------|---------------|
| Hook | 0:25 | 0:25 |
| The Problem | 0:35 | 1:00 |
| What /btw Does | 0:45 | 1:45 |
| Live Demo | 1:00 | 2:45 |
| When to Use What | 0:45 | 3:30 |
| Recap + CTA | 0:30 | 4:00 |

**Target total: ~4 minutes**

## On-Camera Tips

- **Energy:** Match the reference video's pace — informative but not hype. You're teaching, not selling.
- **If /btw doesn't work during recording:** Don't panic. Show the error, explain it, move on. Bugs are relatable.
- **Terminal font size:** 16pt minimum. Viewers watch on phones.
- **Leave space for text overlays** in the recording — keep the terminal centered, not full-screen edge-to-edge.
- **Record the demo in one take if possible** — the continuous flow of /btw working while the task runs is the whole visual payoff.
