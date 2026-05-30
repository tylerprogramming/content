# Episode 7: Examples & Exact Prompts

## Plan Mode Prompt (copy-paste this)

```
I want to add a full theme system to LinkLaunch. Users should be able to pick from 5 preset themes (dark, light, ocean, sunset, forest) using a floating theme picker in the corner. Each theme changes colors, button styles, and background. Store the selected theme in localStorage. Plan how you'd implement this before building.
```

---

## How to Toggle Plan Mode

Press **Shift+Tab** to toggle between:
- **Plan Mode** — Claude outlines its approach, asks clarifying questions, does NOT write code
- **Act Mode** — Claude writes and edits code (the default)

---

## Workflow for This Demo

1. **Start in Plan Mode** — press Shift+Tab until you see the Plan indicator
2. **Paste the prompt** above and hit Enter
3. **Review the plan** — Claude will outline:
   - What CSS custom properties to define for each theme
   - How the theme picker UI will work
   - How localStorage persistence works
   - What files will be modified
4. **Give feedback on the plan** — e.g., "Move the theme picker to the bottom-right instead of top-right"
5. **Switch to Act Mode** — press Shift+Tab again
6. **Tell Claude to execute** with:

```
Looks good. Build it.
```

---

## What Claude's Plan Should Cover

Expect the plan to include something like:

- **5 theme definitions** using CSS custom properties:
  - Dark: #0a0a0f background, #6c63ff accent
  - Light: #f5f5f7 background, #6c63ff accent
  - Ocean: #0b1628 background, #00b4d8 accent
  - Sunset: #1a0a0a background, #ff6b35 accent
  - Forest: #0a1a0a background, #2d6a4f accent
- **Theme picker**: floating button group, bottom-right corner, small color circles
- **JavaScript**: click handler that swaps a `data-theme` attribute on `<body>`, saves to localStorage, loads on page init
- **Files touched**: styles.css (theme variables + picker styles), script.js (theme logic), index.html (picker markup)

---

## When to Use Plan Mode

| Situation | Use Plan Mode? |
|-----------|---------------|
| Adding a small button | No — just let Claude build it |
| Renaming variables | No — straightforward task |
| Building a multi-part feature | Yes — plan the architecture first |
| Refactoring existing code | Yes — make sure nothing breaks |
| You're unsure what you want | Yes — let Claude propose options |
| Complex CSS/animation system | Yes — get the approach right before coding |

---

## Key Takeaway

Plan Mode saves you from building the wrong thing. For any feature that touches multiple files or has design decisions, plan first, then build. It takes 30 extra seconds and saves you from starting over.
