# Episode 8 — Filming Guide
## Claude Code Tutorial #8 - Sessions & Checkpoints

---

## Pre-Recording Setup

1. **Project:** Use the same web app from Episode 7 (with the dark mode toggle). This gives continuity. Make sure it's in a working state.
2. **Pre-create sessions:** Before recording, create 3-4 sessions over the course of a day or two so that `claude --resume` shows a real list with different timestamps. Name one of them with /rename so it shows up named in the list.
3. **Terminal:** Clean terminal, font size 16+, dark theme.
4. **Browser:** Have the web app open for the "break it and rewind" demo.
5. **Git:** Make sure the project has git initialized (from earlier episodes). Commit the current working state before filming so you have a clean baseline.

---

## Recording Playbook

### Segment 1: INTRO (0:00 - 1:30)

**What to show:** Terminal with a broken app (pre-stage this or do it live).
**What to say:** Deliver Hook A from hooks.md.
**On screen:** Error messages, broken UI, then a quick flash of /rewind fixing it.
**Tip:** You can record the "broken" state first, then the "fixed" state, and splice them in editing.

---

### Segment 2: SESSIONS BASICS (1:30 - 3:00)

**What to show:** Terminal with a normal Claude Code session.
**What to say:** Explain that sessions save automatically. No action needed.
**Action:** Just show a working session. Maybe scroll through some conversation to show there's history.
**Then:** Close the terminal window to set up the next segment.

---

### Segment 3: RESUMING SESSIONS (3:00 - 5:00)

**Exact commands:**

```bash
# Option 1: Most recent session
claude --continue
```
*Show the conversation coming back. Scroll up to prove it's the same session.*

```bash
# Close Claude Code (Ctrl+C or close terminal), then:

# Option 2: Pick from a list
claude --resume
```
*Show the list of sessions. Point out the timestamps and the one you renamed.*

```
# Inside a session, rename it:
/rename adding dark mode feature
```
*Show the rename happening. Then close and do --resume again to show the new name in the list.*

**What to say:** Walk through each command. Emphasize --continue for quick access, --resume for picking from history.

---

### Segment 4: CHECKPOINTS EXPLAINED (5:00 - 6:30)

**What to show:** Terminal with Claude Code making edits.
**What to say:** Explain that checkpoints are automatic snapshots before every edit.
**Action:** Ask Claude to make a few small changes so there are several checkpoints created:

```
Add a footer with a copyright notice to the page
```

Then:

```
Change the page title to "My Awesome App"
```

**What to say during edits:** "Every time Claude edits a file, a checkpoint is saved. You don't see it happening, but it's there."

---

### Segment 5: DEMO — BREAK IT AND REWIND (6:30 - 9:00)

**This is the most important segment. Rehearse it.**

**Step-by-step:**

1. Show the app working in the browser. Give it a beat so viewers see it's fine.
2. Back in Claude Code, type:
   ```
   Refactor the entire CSS to use a new naming convention and reorganize all the files
   ```
3. Let Claude make changes. Narrate: "It's making a lot of changes here..."
4. Switch to browser. Refresh. Show the broken app. Let the audience feel the pain for a moment.
5. Back in Claude Code, type:
   ```
   /rewind
   ```
6. Show the checkpoint list. Point to the entries. "See? Every edit."
7. Select the checkpoint from before the refactor.
8. When asked what to restore, choose **code and conversation**.
9. Switch to browser. Refresh. Show the app working again.
10. Celebrate: "Back to normal. Like it never happened."

**What happens on screen:** The dramatic before/after is the hero moment. Make sure the browser is prominent.

**Backup plan:** If the refactor doesn't visibly break the app, use a more destructive prompt like "Delete the CSS file and rewrite it from scratch with a completely different approach."

---

### Segment 6: WHEN TO USE /REWIND (9:00 - 10:00)

**What to show:** Bullet points (text overlay or just talk to camera).
**What to say:** Quick guidance on when to rewind vs. just asking Claude to fix it.
**Key line:** "Checkpoints make it safe to experiment."

---

### Segment 7: PUTTING IT TOGETHER (10:00 - 11:00)

**What to show:** Quick montage of the full workflow.
**Commands in sequence:**
```bash
# Day 2 — resume where you left off
claude --continue

# Work on something, then rewind if needed
/rewind

# When done, commit
```
**What to say:** Narrate the day-one / day-two workflow story from the script.

---

### Segment 8: RECAP (11:00 - 12:00)

**What to show:** Bullet points on screen.
**What to say:** Recap from script. Tease episode 9 — slash commands.
**End with:** "Subscribe and I'll see you there."

---

## Timing Cheat Sheet

| Segment | Start | Duration | Key Action |
|---------|-------|----------|------------|
| Intro | 0:00 | 1:30 | Hook, broken-then-fixed teaser |
| Sessions Basics | 1:30 | 1:30 | Concept explanation |
| Resuming Sessions | 3:00 | 2:00 | --continue, --resume, /rename |
| Checkpoints Explained | 5:00 | 1:30 | Concept + small edits |
| Demo: Break & Rewind | 6:30 | 2:30 | The money shot |
| When to Rewind | 9:00 | 1:00 | Guidance |
| Full Workflow | 10:00 | 1:00 | Putting it together |
| Recap | 11:00 | 1:00 | Summary, next ep tease |

**Total: ~12 minutes**

---

## Backup Plan

If /rewind doesn't show a clean checkpoint list (rare), make sure you've made at least 3-4 edits in the session before attempting the rewind. Each edit creates a checkpoint.

If `claude --resume` shows an empty list, you need to have had previous sessions. Create a few dummy sessions beforehand: open Claude Code, ask a question, close it. Repeat 3-4 times.
