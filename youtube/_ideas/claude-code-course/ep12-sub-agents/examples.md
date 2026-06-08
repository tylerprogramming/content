# Episode 12: Sub-Agents — Examples

## Project Context

We're using sub-agents to delegate specialized review tasks for LinkLaunch. Sub-agents are scoped Claude instances with specific roles, models, and tool access.

---

## 1. Auto-Spawned Sub-Agents

Claude can automatically spawn sub-agents when the task is large enough. Try this prompt:

```
Review the entire LinkLaunch codebase: check JavaScript for bugs, CSS for accessibility, and HTML for SEO issues. Give me a full report.
```

### What happens

Claude recognizes this is a multi-domain review and may spawn sub-agents to handle each area (JS bugs, CSS accessibility, HTML SEO) in parallel. Watch the output — you'll see sub-agent activity in the logs.

---

## 2. Custom Agent: UX Reviewer

### File: `.claude/agents/ux-reviewer.md`

Create this file with the exact content below:

```markdown
---
name: UX Reviewer
description: Reviews LinkLaunch for user experience issues and design best practices
model: sonnet
allowed_tools:
  - Read
  - Grep
  - Glob
---

You are a UX reviewer specializing in link-in-bio pages and personal landing pages. Your job is to review the LinkLaunch codebase and identify user experience issues.

You have READ-ONLY access. You can read files, search for patterns, and find files — but you cannot edit anything. Your output is a review report.

## Review Checklist

### Visual Hierarchy
- Is the most important content (profile, main CTA) visually prominent?
- Is there clear visual grouping of related elements?
- Does the typography establish a clear heading/body hierarchy?
- Is whitespace used effectively to reduce cognitive load?

### Touch Targets
- All clickable elements must be at least 44px x 44px (Apple HIG / WCAG)
- Check button padding, link areas, and icon tap zones
- Ensure adequate spacing between adjacent touch targets (at least 8px gap)

### Loading Performance
- Are images optimized (width/height attributes, lazy loading)?
- Is CSS loaded efficiently (no unused rules, no render-blocking imports)?
- Is JavaScript deferred or loaded at the end of the body?
- Are there any large assets that would slow down mobile loading?

### Color Contrast
- Check all text/background combinations against WCAG AA standards
- Normal text: 4.5:1 minimum contrast ratio
- Large text (18px+ bold or 24px+ regular): 3:1 minimum
- Interactive element borders and focus indicators: 3:1 minimum

### Mobile Layout
- Does the layout work on screens as narrow as 320px?
- Do elements stack properly on mobile?
- Is horizontal scrolling prevented?
- Is text readable without zooming (minimum 16px body text)?

### Theme Consistency
- Are all colors using CSS custom properties (not hardcoded)?
- Do hover/focus states use theme-consistent colors?
- Is the dark theme applied uniformly with no light-theme leaks?
- Are transitions and animations consistent across components?

## Output Format

Structure your review as:

1. **Summary** — overall UX quality score (Good / Needs Work / Critical Issues)
2. **Issues Found** — grouped by category, with severity (Low / Medium / High)
3. **Recommendations** — prioritized list of improvements
4. **Positive Findings** — things done well (important for morale)

Include specific file names, line numbers, and code snippets for every issue.
```

---

## 3. Run the UX Reviewer

After creating the agent file, use this prompt to invoke it:

```
Use the ux-reviewer agent to review LinkLaunch
```

### What happens

- Claude spawns a sub-agent using the Sonnet model
- The sub-agent has read-only access (Read, Grep, Glob only)
- It reviews the entire codebase against the UX checklist
- It returns a structured report without modifying any files

---

## Setting Up the Agent

Create the agent file:

```
Create the .claude/agents/ directory and add a ux-reviewer.md file. I'll give you the content.
```

---

## Key Takeaways

| Concept | Details |
|---------|---------|
| Auto sub-agents | Claude spawns them automatically for large, multi-domain tasks |
| Custom agents | Defined in `.claude/agents/<name>.md` with YAML frontmatter |
| `model` | Which Claude model the sub-agent uses (e.g., `sonnet`, `haiku`) |
| `allowed_tools` | Restricts what tools the sub-agent can access |
| Read-only agents | Use `Read`, `Grep`, `Glob` only — great for reviewers and auditors |

> Sub-agents let you build a team of specialists. The main agent orchestrates, and each sub-agent focuses on what it does best.
