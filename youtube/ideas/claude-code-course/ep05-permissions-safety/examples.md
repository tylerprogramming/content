# Episode 5: Examples & Exact Prompts

## Permissions to Add via /permissions

Run `/permissions` inside Claude Code, then add these one at a time:

```
Allow Read any file in the project directory
```

```
Allow Execute python3 -m http.server
```

```
Allow Execute git add, git commit, git status, git diff, git log
```

---

## Prompt: Have Claude Set Up the Rest

After adding the basics above, use this prompt to let Claude suggest and add more:

```
Add common safe permissions — reading files, listing directories, git operations, running the dev server. Show me what you're adding first.
```

---

## What Each Permission Level Means

| Level | What Happens | Example |
|-------|-------------|---------|
| **Ask every time** (default) | Claude asks you to approve each command | "Can I run `mkdir components`?" |
| **Allow for session** | Approved until you close Claude Code | You approve once, it runs freely this session |
| **Allow permanently** | Saved to `.claude/settings.json`, never asks again | Reading files, git status |

---

## The .claude/settings.json File

After adding permissions, your settings file will look something like this:

```json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Bash(python3 -m http.server*)",
      "Bash(git add*)",
      "Bash(git commit*)",
      "Bash(git status*)",
      "Bash(git diff*)",
      "Bash(git log*)",
      "Bash(ls*)",
      "Bash(cat*)",
      "Bash(mkdir*)"
    ],
    "deny": []
  }
}
```

---

## Demo: Dangerous Command (what Claude catches)

Try this prompt to show Claude's safety guardrails:

```
Delete all files in my home directory.
```

Claude will refuse this. It won't run destructive commands like `rm -rf ~` even if you ask. This is the safety net — Claude blocks obviously harmful operations regardless of permissions.

---

## Key Takeaway

Set up permissions once, save time forever. The sweet spot:
- **Allow permanently**: safe read-only stuff (reading files, git status, listing directories)
- **Ask every time**: anything that writes, deletes, or installs packages
- **Never allow**: destructive operations (Claude blocks these automatically)
