# Episode 1: Examples & Exact Prompts

## Install Command

```bash
npm install -g @anthropic-ai/claude-code
```

## First Prompt (copy-paste this)

```
Build me a personal link-in-bio page called LinkLaunch. Use HTML, CSS, and vanilla JavaScript. Dark theme with a centered layout. Include my name "Tyler Reed" at the top, a profile picture placeholder (use a circle with my initials "TR"), and 5 link buttons that go to YouTube, Twitter, GitHub, Instagram, and my website. Make the buttons have a hover animation. Modern, clean design.
```

## Three Terminal Commands to Know

| Command | What It Does |
|---------|-------------|
| `claude` | Start Claude Code in the current directory |
| `Ctrl+C` twice | Stop Claude Code |
| `/clear` | Clear the conversation and start fresh |

## Project Setup (run before the first prompt)

```bash
mkdir linklaunch
cd linklaunch
claude
```

## Expected Output

After the first prompt, Claude should create:
- `index.html` — the main page
- `styles.css` — all styling
- `script.js` — any interactivity (hover effects, etc.)
