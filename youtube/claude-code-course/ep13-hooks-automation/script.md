# Claude Code Tutorial #13 - Hooks: Automate Everything (Course Finale)

## Full Script

---

### INTRO (0:00 - 1:15) ~1.25 min

Every time Claude edits a file, my code automatically gets formatted. Every command it runs gets logged. And if it ever tries to touch my database migrations folder? Blocked. Instantly.

[SHOW: Terminal — Claude editing a file, then the formatter firing automatically]

No AI tokens. No extra prompts. Just shell scripts that fire automatically at exactly the right moment.

These are hooks. They're the last major feature we're covering in this course. And honestly? They might be the most practical.

[NOTE: Title card — "Claude Code Tutorial #13 - Hooks & Automation"]

Let me show you how they work.

---

### SECTION 1: WHAT ARE HOOKS? (1:15 - 3:00) ~1.75 min

Hooks are shell scripts that run at specific moments in Claude Code's lifecycle.

[SHOW: Simple diagram on screen]
```
Event Happens  --->  Hook Fires  --->  Shell Script Runs
(Claude edits     (automatic,        (format, log,
 a file)           no AI needed)      block, etc.)
```

Here's the key thing — and I want you to really get this. Hooks are NOT AI. They don't use tokens. They don't call Claude. They're just regular shell scripts that execute deterministically.

That means they run every single time. No hallucinations. No variations. No cost. Just reliable automation.

[SHOW: Comparison on screen]
```
SKILLS / COMMANDS          HOOKS
- Use AI tokens            - Zero AI tokens
- Can vary each time       - Same result every time
- Intelligent, flexible    - Deterministic, reliable
- Good for creative tasks  - Good for automation
```

Think of hooks as the guardrails and automations that run alongside your AI work.

Here are the lifecycle events you can hook into.

[SHOW: List building on screen]

**PreToolUse** — fires before Claude runs a tool (like before it writes a file or runs a command)
**PostToolUse** — fires after a tool completes
**Notification** — fires when Claude sends a notification
**Stop** — fires when Claude finishes its response

[NOTE: Keep this list on screen for at least 5 seconds]

The two you'll use most are PreToolUse and PostToolUse. PreToolUse is your gatekeeper — block things before they happen. PostToolUse is your automation layer — do things after Claude acts.

---

### SECTION 2: SETTING UP YOUR FIRST HOOK (3:00 - 5:30) ~2.5 min

Let's set one up. The easiest way is to use the `/hooks` command inside Claude Code.

[SHOW: Terminal — Claude Code]

```
/hooks
```

[SHOW: The hooks configuration interface appearing]

This shows you all the lifecycle events you can hook into. Let's set up an auto-format hook. Every time Claude edits a JavaScript file, we'll run Prettier on it automatically.

[SHOW: Navigating the hooks interface]

Select "PostToolUse" — we want this to fire after Claude writes a file.

For the matcher, we'll match on the "Write" and "Edit" tools.

For the hook script:

```bash
#!/bin/bash
# Auto-format JavaScript files after Claude edits them
if [[ "$TOOL_INPUT_FILE_PATH" == *.js ]] || [[ "$TOOL_INPUT_FILE_PATH" == *.ts ]]; then
  npx prettier --write "$TOOL_INPUT_FILE_PATH" 2>/dev/null
fi
```

[SHOW: Entering the script in the hooks interface]

Let me break this down.

The script checks if the file Claude just edited is a JavaScript or TypeScript file. If it is, it runs Prettier on it. The `2>/dev/null` just hides any error output so it stays clean.

[NOTE: Pause on each line as you explain it]

But here's the thing — you don't have to write hooks yourself. You can just ask Claude.

[SHOW: Claude Code prompt]

> Set up a hook that auto-formats JavaScript and TypeScript files with Prettier after every edit

[SHOW: Claude creating the hook configuration]

Claude knows the hooks system. It writes the shell script, configures the lifecycle event, sets the matcher — all of it. You just tell it what you want.

That's my pro tip for this whole episode. If you're not sure how to write a hook, just ask Claude to do it.

---

### SECTION 3: DEMO — AUTO-FORMAT HOOK (5:30 - 7:00) ~1.5 min

Let's see it in action.

[SHOW: Claude Code prompt]

> Create a new file called demo.js with a simple Express server. Don't worry about formatting.

[SHOW: Claude creating the file — intentionally with messy formatting (or just standard formatting)]

Now watch the terminal. The hook should fire right after Claude saves the file.

[SHOW: Prettier running automatically, visible in terminal output]

There it is. Prettier just ran. The file is perfectly formatted. Claude didn't have to think about formatting. No AI tokens spent. Just a shell script doing its job.

[SHOW: Opening the file to show clean formatting]

Every time. Automatically. For every JavaScript file Claude touches.

---

### SECTION 4: LOGGING HOOK (7:00 - 8:30) ~1.5 min

Let me show you another practical hook — a command logger.

This one logs every command Claude runs. Super useful for debugging, auditing, or just understanding what Claude is doing under the hood.

[SHOW: Setting up the hook]

> Set up a hook that logs every Bash command Claude runs to a file called .claude/command-log.txt with timestamps

[SHOW: Claude creating the hook]

The hook will look something like this:

```bash
#!/bin/bash
# Log all commands with timestamps
echo "[$(date '+%Y-%m-%d %H:%M:%S')] $TOOL_INPUT_COMMAND" >> .claude/command-log.txt
```

[SHOW: The hook configuration]

Now let me have Claude do some work.

[SHOW: Claude Code prompt]

> Check what version of Node I'm running, then list the files in this directory

[SHOW: Claude running commands, hook logging them]

Now let's check the log.

```bash
cat .claude/command-log.txt
```

[SHOW: Log file with timestamped commands]

Every command. Timestamped. Logged automatically. You could use this for compliance. For debugging. For understanding what Claude does when you give it a complex task.

---

### SECTION 5: PROTECTION HOOK (8:30 - 10:00) ~1.5 min

Now my favorite — a protection hook. This one blocks Claude from modifying certain files or folders.

Let's say you have a database migrations folder. You never want Claude touching those files. Migrations need to be carefully managed.

[SHOW: Claude Code prompt]

> Create a PreToolUse hook that blocks any file writes or edits to the migrations/ folder. It should show a warning message and prevent the action.

[SHOW: Claude creating the hook]

The hook will look something like this:

```bash
#!/bin/bash
# Block writes to migrations folder
if [[ "$TOOL_INPUT_FILE_PATH" == */migrations/* ]]; then
  echo "BLOCKED: Cannot modify files in migrations/ folder"
  echo "Migrations must be managed manually."
  exit 2
fi
```

[SHOW: The hook configuration — emphasize that exit code 2 blocks the action]

The secret sauce is `exit 2`. In Claude Code hooks, an exit code of 2 means "block this action." Exit 0 means "let it through." This is how PreToolUse hooks act as gatekeepers.

Let's test it.

[SHOW: Claude Code prompt]

> Create a new migration file at migrations/001_add_users.sql

[SHOW: Claude attempting to create the file, hook firing, action blocked with warning message]

Blocked. Claude tried to write the file. The hook caught it. The action was prevented. Claude sees the warning message and understands it can't write there.

[NOTE: Let this moment land. This is a powerful demo — show the blocked message clearly.]

That's protection you can rely on. Not AI judgment — deterministic code. It will block the action every single time, no exceptions.

---

### SECTION 6: HOOKS IN SETTINGS.JSON (10:00 - 10:45) ~45 sec

Quick note on where hooks live. You have two options.

The `/hooks` command stores them interactively. But you can also edit them directly in your settings file.

[SHOW: Opening settings.json]

```bash
cat ~/.claude/settings.json
```

[SHOW: The hooks section of settings.json]

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "~/.claude/hooks/auto-format.sh"
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "~/.claude/hooks/protect-migrations.sh"
      }
    ]
  }
}
```

You can put your hook scripts in a `~/.claude/hooks/` folder and reference them from settings. This is great for sharing hooks across projects or backing them up in version control.

---

### SECTION 7: COMBINING EVERYTHING (10:45 - 11:30) ~45 sec

Here's what's amazing. Everything we've covered in this course works together.

[SHOW: Diagram building on screen]

You have **CLAUDE.md** giving Claude context about your project.

You have **commands** for quick templates and workflows.

You have **skills** giving Claude deep domain expertise with auto-invocation.

You have **MCP servers** connecting Claude to your external tools.

You have **sub-agents** so Claude can delegate to specialists.

And now you have **hooks** providing reliable automation and guardrails around all of it.

[SHOW: Full diagram with all features connected]

```
CLAUDE.md (context)
    |
Commands (shortcuts) + Skills (expertise)
    |
MCP Servers (external tools)
    |
Sub-agents (delegation)
    |
Hooks (automation & safety)
```

This is the full stack. You're not just using Claude Code. You've configured an entire AI-powered operating system that works exactly the way you want it to.

---

### SECTION 8: COURSE WRAP-UP (11:30 - 12:00) ~30 sec

That's it. Thirteen episodes. You went from "what is Claude Code?" to building skills, connecting tools, delegating to sub-agents, and automating with hooks.

[SHOW: Face cam — genuine, slightly reflective]

Here's my honest advice for what to do next. Pick one thing from this course. One thing that excited you. And go build it. Don't try to do everything at once. Start with one skill. Or one MCP server. Or one hook. Use it for a week. Then add more.

The whole point of Claude Code is that it adapts to you. So start shaping it.

If this course helped you, subscribe. Leave a comment telling me what you built — I read every single one. And if you want to see more advanced Claude Code content, let me know.

Thanks for watching the whole course. I'll see you in the next one.

[SHOW: End screen with subscribe button, playlist link to full course]

[NOTE: End screen — 20 seconds. Include a card linking back to Episode 1 for new viewers.]
