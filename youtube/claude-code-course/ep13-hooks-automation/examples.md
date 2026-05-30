# Episode 13: Hooks & Automation — Examples

## Project Context

This is the finale. We're adding hooks to automate code formatting, logging, and file protection in LinkLaunch — then bringing everything together in one grand finale prompt.

---

## 1. Auto-Format Hook

Set up a hook that automatically formats code after Claude edits any file:

```
Set up a hook that runs prettier on any HTML, CSS, or JS file after Claude edits it
```

### What this does

- Triggers after every file edit (post-edit hook)
- Runs `npx prettier --write` on the edited file
- Only applies to `.html`, `.css`, and `.js` files
- Code is always clean and consistently formatted

---

## 2. Logging Hook

Set up a hook that creates an audit trail of every file Claude touches:

```
Set up a hook that logs every file Claude edits to .claude/edit-log.txt with timestamps
```

### What this does

- Triggers after every file edit (post-edit hook)
- Appends a line to `.claude/edit-log.txt` with the timestamp and file path
- Creates a full history of changes for review

### Example log output

```
[2026-03-07 14:23:01] Edited: index.html
[2026-03-07 14:23:05] Edited: style.css
[2026-03-07 14:23:12] Edited: script.js
```

---

## 3. Protection Hook

Set up a hook that prevents Claude from deleting any file:

```
Set up a hook that blocks Claude from deleting any file. Exit code 2.
```

### What this does

- Triggers before file deletion (pre-delete hook)
- Returns exit code 2, which blocks the action
- Claude cannot delete any file in the project
- Acts as a safety guardrail for destructive operations

### Why exit code 2?

| Exit Code | Behavior |
|-----------|----------|
| 0 | Action allowed — proceed normally |
| 1 | Hook failed — show error but allow Claude to continue |
| 2 | Action BLOCKED — Claude cannot perform this action |

---

## 4. The Grand Finale

This is the money moment. One prompt that triggers everything we've learned across the course:

```
I want to add a link click analytics dashboard to LinkLaunch. Use Plan Mode to plan it first. After you implement it, the auto-format hook will clean up the code. Then use the ux-reviewer agent to review the changes. Finally, commit everything and push to GitHub.
```

### What happens (the chain reaction)

1. **Plan Mode** (Episode 7) — Claude creates a detailed implementation plan before writing any code
2. **Implementation** — Claude builds the analytics dashboard following the LinkLaunch UI skill (Episode 10)
3. **Auto-Format Hook** fires — Prettier cleans up every edited file automatically
4. **Logging Hook** fires — Every edit is recorded in `.claude/edit-log.txt`
5. **Sub-Agent** (Episode 12) — The UX Reviewer agent audits the new dashboard for usability issues
6. **MCP** (Episode 11) — Claude commits the code and pushes to GitHub via the GitHub MCP server

### Features from every episode in action

| Episode | Feature Used |
|---------|-------------|
| Ep 3 | CLAUDE.md project instructions |
| Ep 7 | Plan Mode for architecture planning |
| Ep 8 | Session management (checkpoint created) |
| Ep 10 | LinkLaunch UI skill (design system rules) |
| Ep 11 | GitHub MCP (commit and push) |
| Ep 12 | UX Reviewer sub-agent |
| Ep 13 | Hooks (auto-format, logging, protection) |

> This is the power of Claude Code. Every feature compounds. Sessions track your work. Skills encode your standards. Hooks automate your workflow. Sub-agents review your output. MCP connects you to the world. And it all works together in a single prompt.

---

## Key Takeaways

| Concept | Details |
|---------|---------|
| Post-edit hooks | Run after Claude edits a file (formatting, logging) |
| Pre-delete hooks | Run before Claude deletes a file (protection, approval) |
| Exit code 2 | Blocks the action entirely |
| Hook chaining | Multiple hooks can fire on the same event |
| Grand finale | One prompt triggers Plan Mode, skills, hooks, sub-agents, and MCP |

> Hooks are the automation layer. They turn Claude from an assistant into a full development pipeline.
