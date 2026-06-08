# Episode 3: Examples & Exact Prompts

## The CLAUDE.md File (copy-paste the entire block below into CLAUDE.md)

```markdown
# LinkLaunch — Project Rules

## Tech Stack
- Vanilla HTML, CSS, and JavaScript only
- No frameworks (no React, Vue, Tailwind, etc.)
- No external CDNs or third-party libraries
- No inline styles — all styling goes in styles.css

## Code Style
- JavaScript: camelCase for variables and functions
- CSS: use custom properties (variables) for all colors and spacing
- Mobile-first responsive design (min-width media queries)
- All interactive elements must have hover states

## Design System
- Background: #0a0a0f
- Accent color: #6c63ff
- Text color: #ffffff
- Secondary text: #a0a0b0
- Card/surface background: #1a1a2e
- Border radius: 8px on all rounded elements
- Font: system font stack (no Google Fonts)

## File Structure
- index.html — main page
- styles.css — all styles
- script.js — all JavaScript

## Rules
- Dark theme by default
- Never remove existing features when adding new ones
- Always maintain responsive design when making changes
- Buttons should have smooth transitions (0.3s ease)
```

---

## Demo: WITHOUT CLAUDE.md

Delete or rename your CLAUDE.md first, then use this prompt:

```
Add a theme switcher to LinkLaunch.
```

What typically goes wrong without CLAUDE.md:
- Claude might use a CSS framework
- Colors won't match the existing theme
- Might use inline styles
- Could break the mobile layout
- Might add Google Fonts or external dependencies

---

## Demo: WITH CLAUDE.md

Make sure CLAUDE.md is saved in the project root, then use the same prompt:

```
Add a theme switcher to LinkLaunch.
```

What happens with CLAUDE.md in place:
- Uses vanilla CSS custom properties for the theme toggle
- Stays within the existing color palette
- Follows mobile-first approach
- No external dependencies added
- Hover states included automatically
- Existing features remain untouched

---

## How to Create the File

```bash
# From inside your linklaunch project folder:
touch CLAUDE.md
# Then paste the content above into it
```

Claude Code reads CLAUDE.md automatically every time you start a conversation. No import or command needed.
