# Episode 9 — Filming Guide
## Claude Code Tutorial #9 - Build Your Own Commands

---

## Pre-Recording Setup

1. **Project:** Use the same web app from episodes 7-8 for continuity. Make sure it has:
   - A package.json with a test script (even a simple one)
   - A few files so the /report command has something to analyze
   - Some TODO comments scattered in the code
   - A few git commits for the report to reference
2. **Terminal:** Clean terminal, font size 16+, dark theme.
3. **Claude Code:** Fresh session in the project directory.
4. **Important:** Do NOT pre-create the .claude/commands/ folder. You want to create it live during recording.
5. **Dry run:** Run through the /deploy and /report command creation once off-camera to make sure it works. Then delete the commands folder and start fresh for filming.

---

## Recording Playbook

### Segment 1: INTRO (0:00 - 1:30)

**What to show:** Quick montage of slash commands running (can be pre-recorded B-roll).
**What to say:** Deliver Hook A from hooks.md.
**On screen:** Terminal with /deploy, /test, /report flashing by.
**Tip:** You can record the command demos first and use clips in the intro montage.

---

### Segment 2: BUILT-IN COMMANDS (1:30 - 4:00)

**Exact commands to run:**

```
/help
```
*Pause and show the list. Point out each command as you discuss it.*

```
/clear
```
*Show the conversation reset.*

```
/compact
```
*Show the compression happening. Say "This saves Claude's memory."*

```
/model
```
*Show the model options. Don't switch — just show the list and move on.*

Briefly mention /init, /rewind, /permissions without dwelling. Just name them and say "we covered these."

**Pacing:** Move through these briskly. 15-20 seconds per command max. The audience wants to get to custom commands.

---

### Segment 3: WHAT ARE CUSTOM COMMANDS? (4:00 - 5:00)

**What to show:** Can be talking-head or terminal.
**What to say:** The recipe analogy — "Write the steps once, run them anytime."
**On screen:** Examples list (deploy, test, report).
**Keep it short.** This is the concept bridge to the demo.

---

### Segment 4: THE .claude/commands FOLDER (5:00 - 6:00)

**What to show:** Terminal or a file tree graphic.
**On screen:** The folder structure diagram from the script.
**Key point:** "Filename becomes the command name. deploy.md becomes /deploy."
**Don't create anything yet.** Just explain the structure.

---

### Segment 5: DEMO — CREATE /deploy (6:00 - 8:30)

**This is the core demo. Step-by-step:**

1. In Claude Code, type:
   ```
   Create the .claude/commands/ folder for me
   ```
   *Let Claude create it.*

2. Then type:
   ```
   Create a custom slash command at .claude/commands/deploy.md that does the following:
   1. Run the test suite
   2. If tests pass, build the project
   3. Show me a summary of what would be deployed
   4. Ask me to confirm before deploying
   ```
   *Let Claude create the file.*

3. Show the file contents:
   ```
   Read .claude/commands/deploy.md and show me what you wrote
   ```
   *Or open it in your editor if that's easier to show on screen.*

4. Run the command:
   ```
   /deploy
   ```
   *Let it run. Narrate what's happening at each step.*

5. When it asks for confirmation, say "yes" or "go ahead."

**What to say during waits:** "It's running the tests first... tests passed... now it's building... and here's the summary."

**If tests fail:** That's actually fine for the demo. Show Claude catching the failure and stopping. Then fix the test and run /deploy again.

---

### Segment 6: DEMO — CREATE /report (8:30 - 9:30)

**Quick second demo to reinforce the pattern:**

1. Type:
   ```
   Create a custom command at .claude/commands/report.md that analyzes the current project and generates a brief report: how many files, what languages are used, any TODO comments in the code, and a summary of recent git commits.
   ```
   *Let Claude create it.*

2. Run it:
   ```
   /report
   ```
   *Show the output. Don't dwell — 30 seconds max.*

**What to say:** "See the pattern? Write instructions, save to the folder, run with a slash."

---

### Segment 7: MORE IDEAS (9:30 - 10:30)

**What to show:** List on screen (text overlay or talking-head).
**What to say:** Read through the list from the script — test, review, document, standup, optimize.
**Don't demo these.** Just list them. The audience gets the pattern.

---

### Segment 8: TIPS (10:30 - 11:00)

**What to show:** Side-by-side comparison (vague vs. specific command instructions).
**What to say:** "Be specific. Break it into steps. Handle errors."
**Keep it fast.** 30 seconds.

---

### Segment 9: RECAP (11:00 - 12:00)

**What to show:** Bullet points on screen.
**What to say:** Recap from script.
**End with:** Course progress summary and subscribe CTA.

---

## Timing Cheat Sheet

| Segment | Start | Duration | Key Action |
|---------|-------|----------|------------|
| Intro | 0:00 | 1:30 | Hook, montage |
| Built-in Commands | 1:30 | 2:30 | /help walkthrough |
| What Are Custom Commands | 4:00 | 1:00 | Concept explanation |
| .claude/commands Folder | 5:00 | 1:00 | Structure explanation |
| Demo: /deploy | 6:00 | 2:30 | Create and run /deploy |
| Demo: /report | 8:30 | 1:00 | Create and run /report |
| More Ideas | 9:30 | 1:00 | Quick list |
| Tips | 10:30 | 0:30 | Writing good commands |
| Recap | 11:00 | 1:00 | Summary, course progress |

**Total: ~12 minutes**

---

## Backup Plan

If /deploy doesn't work as a real deployment (project may not have a deploy setup), that's fine. The command can just go through the steps and report what it would do. The point is showing the workflow, not the actual deployment.

If Claude doesn't automatically pick up the new command after creating the file, you may need to start a new session or type the / and see if it auto-completes. In worst case, you can reference the command by telling Claude to follow the instructions in the file.
