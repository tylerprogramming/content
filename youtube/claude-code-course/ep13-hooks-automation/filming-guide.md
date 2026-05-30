# Filming Guide — Claude Code Tutorial #13: Hooks & Automation (Course Finale)

## Pre-Recording Checklist

- [ ] Prettier installed globally or in project: `npm install -g prettier`
- [ ] Have a demo project with JavaScript/TypeScript files ready
- [ ] Create a `migrations/` folder in the demo project (empty is fine)
- [ ] Remove any existing hooks from settings: check `~/.claude/settings.json`
- [ ] Clear any existing `.claude/command-log.txt`
- [ ] Terminal font size: 16pt+
- [ ] Screen recording: 1920x1080, 30fps
- [ ] Webcam positioned for face cam overlay
- [ ] Have the course recap diagram ready (prepare in Keynote/Figma or draw live)

---

## Recording Playbook

### Segment 1: INTRO (Target: 1:15)

**What to say:** Deliver Hook Option 1 word-for-word

**What to show:**
1. Terminal with Claude editing a file and Prettier auto-firing (pre-record this as B-roll if hooks aren't set up yet)
2. Face cam for hook delivery

---

### Segment 2: WHAT ARE HOOKS (Target: 1:45)

**What to say:** Follow script Section 1

**What to show:**
1. Diagram: Event > Hook > Shell Script (prepare as graphic)
2. Comparison table: Skills/Commands vs Hooks
3. Lifecycle events list

**No terminal commands — pure explanation with visuals.**

**Key moment:** Emphasize "zero AI tokens" — this is the hook (pun intended) for the audience. Say it clearly and let it land.

---

### Segment 3: SETTING UP FIRST HOOK (Target: 2:30)

**What to say:** Follow script Section 2

**Exact commands:**

```bash
# Open Claude Code
claude

# Use the /hooks command
/hooks
```

**Walk through the /hooks interface. Show:**
1. Selecting PostToolUse
2. Setting the matcher to Write|Edit
3. Entering the auto-format shell script

**Then show the alternative — asking Claude:**
```
Set up a hook that auto-formats JavaScript and TypeScript files with Prettier after every edit
```

**Let Claude create the hook. Show the configuration it produces.**

---

### Segment 4: AUTO-FORMAT DEMO (Target: 1:30)

**What to say:** Follow script Section 3

**Exact commands:**

```bash
# In Claude Code, ask Claude to create a messy JS file
> Create a new file called demo.js with a simple Express server. Don't worry about formatting.
```

**What to watch for:**
- Claude writes the file
- Hook fires (should see Prettier run in terminal output)
- Open the file to verify clean formatting

**If Prettier doesn't fire visibly:** Open the file before and after to show the difference. You can also add `echo "Formatting..."` to the hook script so it's visible in terminal.

---

### Segment 5: LOGGING HOOK (Target: 1:30)

**What to say:** Follow script Section 4

**Exact commands:**

```bash
# Ask Claude to set up the logging hook
> Set up a hook that logs every Bash command Claude runs to a file called .claude/command-log.txt with timestamps
```

**Then trigger it:**
```
> Check what version of Node I'm running, then list the files in this directory
```

**Then verify:**
```bash
cat .claude/command-log.txt
```

**Show the timestamped entries. React: "Every command. Timestamped. Automatic."**

---

### Segment 6: PROTECTION HOOK (Target: 1:30)

**This is the money demo. Make it land.**

**Exact commands:**

```bash
# Ask Claude to create the protection hook
> Create a PreToolUse hook that blocks any file writes or edits to the migrations/ folder. It should show a warning message and prevent the action.
```

**Then test it:**
```
> Create a new migration file at migrations/001_add_users.sql
```

**What to expect:** Claude attempts to create the file. Hook fires. Action is BLOCKED. Warning message appears.

**Key moment:** Let the "BLOCKED" message sit on screen for 3-4 seconds. Say: "That's protection you can rely on."

**If the hook doesn't block:** Check that exit code is 2. If needed, manually adjust the hook script and re-run the test. Don't let this demo fail — it's the episode's climax.

---

### Segment 7: SETTINGS.JSON (Target: 45 sec)

**What to say:** Follow script Section 6

**Exact commands:**

```bash
cat ~/.claude/settings.json
```

**Show the hooks section. Point out the structure briefly.**

**This segment should be quick — don't linger.**

---

### Segment 8: COMBINING EVERYTHING (Target: 45 sec)

**What to say:** Follow script Section 7

**What to show:** Build the full-stack diagram on screen. Use a pre-made graphic with each layer appearing as you mention it:
1. CLAUDE.md (context)
2. Commands (shortcuts)
3. Skills (expertise)
4. MCP Servers (external tools)
5. Sub-agents (delegation)
6. Hooks (automation & safety)

**This should feel like a satisfying recap. Each layer clicking into place.**

---

### Segment 9: COURSE WRAP-UP (Target: 30 sec)

**What to say:** Follow script Section 8

**What to show:**
- Face cam — genuine, slightly reflective tone
- End screen with subscribe, course playlist link, Episode 1 card

**Delivery note:** This is the farewell. Don't rush. Look into the camera. Thank them. Mean it.

---

## Timing Cheat Sheet

| Segment | Target Duration | Running Total |
|---------|----------------|---------------|
| Intro | 1:15 | 1:15 |
| What Are Hooks | 1:45 | 3:00 |
| Setting Up First Hook | 2:30 | 5:30 |
| Auto-Format Demo | 1:30 | 7:00 |
| Logging Hook | 1:30 | 8:30 |
| Protection Hook | 1:30 | 10:00 |
| Settings.json | 0:45 | 10:45 |
| Combining Everything | 0:45 | 11:30 |
| Course Wrap-Up | 0:30 | 12:00 |

**Total: ~12 minutes**

---

## Backup Plans

**If /hooks command doesn't work as expected:**
- Manually edit `~/.claude/settings.json` and add hooks there
- Narrate: "You can also set these up directly in your settings file"

**If auto-format hook doesn't trigger visibly:**
- Add an `echo` statement to the hook script: `echo "[HOOK] Auto-formatting $TOOL_INPUT_FILE_PATH"`
- Show the before/after of the file content

**If protection hook doesn't block:**
- Verify exit code is 2 in the script
- Test the hook script manually: `TOOL_INPUT_FILE_PATH="migrations/test.sql" bash hook-script.sh; echo $?`
- Should output exit code 2

---

## Post-Recording Notes

- This is the course finale — consider adding a brief montage of highlights from episodes 1-12 during the wrap-up section
- Create a "Full Course" playlist and link it in the end screen
- Pin a comment with: "What was your favorite episode? What should I cover next?"
- Consider creating a downloadable "Claude Code Cheat Sheet" PDF with all commands, features, and tips from the course — link in description
- Export all three hook scripts as a downloadable zip for the description
