# Episode 8: Sessions & Checkpoints — Examples

## Project Context

We're continuing to build LinkLaunch, our link-in-bio page builder. This episode covers session management, resuming conversations, and using checkpoints to undo mistakes.

---

## 1. Rename the Session

Give the current session a descriptive name so it's easy to find later.

```
/rename LinkLaunch - Theme System
```

---

## 2. Resume and Continue Commands

### Resume a specific session (interactive picker)

```bash
claude --resume
```

This opens an interactive list of past sessions. Select the one you want to return to.

### Continue the most recent session

```bash
claude --continue
```

This immediately picks up where your last session left off — no picker needed.

---

## 3. The "Break It" Prompt

This is where we intentionally break the project to demonstrate the power of `/rewind`.

Copy-paste this prompt into Claude Code:

```
Convert all the CSS to use Sass with nested selectors and variables. Rename style.css to style.scss.
```

### What happens

Claude will:
- Rename `style.css` to `style.scss`
- Rewrite the CSS using Sass syntax (nesting, `$variables`)
- The page will break because the browser can't read `.scss` files directly

### Why it breaks

- The HTML `<link>` tag still references `style.css` (or Claude updates it to `style.scss`)
- Either way, browsers don't understand Sass — you need a build step
- The page loads with zero styling

---

## 4. Rewind to Restore

After confirming the project is broken, use `/rewind` to undo everything:

```
/rewind
```

Select the checkpoint from before the Sass conversion. Claude restores all files to their previous state.

### Verify the restore

```
Open style.css and confirm it's back to normal CSS. Then preview the page to make sure everything looks right.
```

---

## Key Takeaways

| Feature | What It Does |
|---------|-------------|
| `/rename` | Names the current session for easy identification |
| `claude --resume` | Opens a picker to resume any past session |
| `claude --continue` | Continues the most recent session instantly |
| `/rewind` | Rolls back to a previous checkpoint, undoing changes |

> Checkpoints are created automatically every time Claude edits files. You always have a safety net.
