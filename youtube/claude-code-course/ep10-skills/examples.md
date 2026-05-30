# Episode 10: Skills — Examples

## Project Context

We're creating a skill that teaches Claude our LinkLaunch design system. Once the skill is installed, Claude will automatically follow our design rules without being told — no more repeating style instructions in every prompt.

---

## 1. The Skill File

### File: `.claude/skills/linklaunch-ui/SKILL.md`

Create this file with the exact content below:

```markdown
---
name: LinkLaunch UI
description: Design system and component guidelines for the LinkLaunch link-in-bio page builder
---

# LinkLaunch UI Design System

You are building components for LinkLaunch, a link-in-bio page builder. Follow these rules for every component you create or modify.

## Color System

Use CSS custom properties for all colors. Never hardcode color values.

```css
--bg-primary: #0a0a0f;
--bg-secondary: #141420;
--bg-card: #1a1a2e;
--accent: #6c63ff;
--accent-hover: #5a52d9;
--text-primary: #ffffff;
--text-secondary: #a0a0b0;
--border: #2a2a3e;
```

Always reference these as `var(--accent)`, `var(--bg-primary)`, etc. This ensures compatibility with the theme system.

## Component Rules

- **Border radius**: Use `8px` for all containers, cards, and buttons
- **Spacing**: Use multiples of 4px (4, 8, 12, 16, 24, 32, 48)
- **Font stack**: `'Inter', -apple-system, BlinkMacSystemFont, sans-serif`
- **Max content width**: `680px`, centered with `margin: 0 auto`

## Accessibility Requirements

Every component MUST include:
- `aria-label` on all interactive elements (buttons, links, inputs)
- Keyboard navigation support — all interactive elements must be focusable
- Visible focus states using `outline: 2px solid var(--accent)` with `outline-offset: 2px`
- Color contrast ratio of at least 4.5:1 for normal text, 3:1 for large text

## Animations & Transitions

All interactive elements must have smooth transitions:

```css
transition: all 0.2s ease;
```

Hover states should include a subtle transform:

```css
transform: translateY(-2px);
```

Never use animations that could cause motion sickness. Respect `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    transition: none !important;
    animation: none !important;
  }
}
```

## Responsive Design

- Mobile-first: write base styles for mobile, then add `min-width` media queries
- Breakpoints: `480px` (small), `768px` (medium), `1024px` (large)
- Touch targets must be at least `44px x 44px`
- Use `rem` units for font sizes, `px` for borders and spacing

## Constraints

- No external dependencies (no Bootstrap, Tailwind, jQuery, etc.)
- No inline styles — all styles go in the CSS file
- All components must work with the existing theme system using CSS custom properties
- Vanilla HTML, CSS, and JavaScript only
```

---

## 2. Setting Up the Skill

Create the skill directory and file:

```
Create the directory .claude/skills/linklaunch-ui/ and add a SKILL.md file inside it. I'll give you the content.
```

---

## 3. Test the Skill

Use this prompt to test that Claude follows the design system automatically. Do NOT mention the skill, the design system, or any style rules — Claude should pick them up on its own.

```
Build me a bio section component where I can write a short bio with a character counter and an edit button
```

### What to look for

Claude should automatically:
- Use the dark theme colors (`#0a0a0f` background, `#6c63ff` accent)
- Use CSS custom properties (`var(--accent)`, `var(--bg-card)`, etc.)
- Add `aria-label` attributes to the edit button and textarea
- Include keyboard focus states
- Add `transition: all 0.2s ease` on interactive elements
- Use `8px` border radius
- Make it mobile-first and responsive
- Include `prefers-reduced-motion` media query
- Use no external dependencies

If Claude does all of this without being asked, the skill is working.

---

## Key Takeaways

| Concept | Details |
|---------|---------|
| Skill location | `.claude/skills/<skill-name>/SKILL.md` |
| Format | Markdown with YAML frontmatter (`name`, `description`) |
| Activation | Automatic — Claude reads skills when they exist in the project |
| Purpose | Encode project-specific knowledge so you never repeat instructions |

> Skills are like permanent context. Write the rules once, and Claude follows them in every conversation.
