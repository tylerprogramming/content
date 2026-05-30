# Episode 6: Examples & Exact Prompts

## Haiku Task (simple, fast, cheap)

Switch to Haiku first:

```
/model claude-haiku-4
```

Then run this prompt:

```
Change the "GitHub" button text to "My Code".
```

Why Haiku is perfect here:
- It's a one-line text change
- No design decisions needed
- No complex logic
- Runs in seconds, costs almost nothing

---

## Opus Task (complex, creative, thorough)

Switch to Opus:

```
/model claude-opus-4
```

Then run this prompt:

```
Redesign the link buttons to be interactive cards — when you hover, they flip to show a preview/description of where the link goes. Use pure CSS 3D transforms. Each card should:
- Front side: the current button design with the link name
- Back side: a short description of that platform (e.g., "Watch my AI tutorials and tool reviews" for YouTube)
- Flip animation using rotateY with perspective
- Smooth 0.6s transition
- Keep the dark theme and accent colors from CLAUDE.md
```

Why Opus is needed here:
- Complex CSS 3D transforms require precise math
- Creative design decisions (card layout, descriptions)
- Multiple interacting CSS properties (perspective, backface-visibility, transform-style)
- Needs to maintain existing styles while rebuilding the component

---

## Memory Prompt (add to project memory)

```
Remember that I always want to preview changes by opening index.html in the browser after you edit it.
```

What this does:
- Claude saves this preference to `.claude/settings.json` under memory
- From now on, after every edit, Claude will automatically open the file in your browser
- Persists across sessions — you never have to say it again

---

## When to Use Each Model

| Task | Model | Why |
|------|-------|-----|
| Rename a variable | Haiku | Simple find-and-replace |
| Fix a typo | Haiku | One-line change |
| Add a comment | Haiku | No logic needed |
| Build a new feature | Sonnet | Good balance of speed and quality |
| Refactor architecture | Opus | Needs deep understanding |
| Complex CSS/animations | Opus | Creative + technical precision |
| Debug a tricky bug | Opus | Needs to reason through the code |

---

## How to Check Current Model

```
/model
```

This shows which model you're currently using without changing it.
