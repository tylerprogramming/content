# Episode 9: Slash Commands — Examples

## Project Context

We're adding custom slash commands to LinkLaunch so we can run common workflows with a single command. Each command is a markdown file inside `.claude/commands/`.

---

## 1. Preview Command

### File: `.claude/commands/preview.md`

Create this file with the exact content below:

```markdown
Start a local HTTP server to preview the LinkLaunch site.

Steps:
1. Run `python3 -m http.server 8080` in the project root directory
2. Open the browser to http://localhost:8080
3. Tell me the server is running and how to stop it (Ctrl+C)

If port 8080 is already in use, try 8081 instead.
```

### How to use it

```
/project:preview
```

---

## 2. Audit Command

### File: `.claude/commands/audit.md`

Create this file with the exact content below:

```markdown
Run a full audit of the LinkLaunch project. Check every HTML, CSS, and JS file for the following issues:

## Accessibility
- Color contrast ratios (WCAG AA minimum — 4.5:1 for normal text, 3:1 for large text)
- Missing or empty `aria-label` attributes on interactive elements
- Missing `alt` text on images
- Keyboard navigation — all interactive elements must be focusable and operable

## Links
- Broken or placeholder links (href="#", href="", javascript:void(0))
- Links missing `rel="noopener noreferrer"` when using `target="_blank"`

## Mobile Responsiveness
- Missing viewport meta tag
- Fixed widths that would break on small screens
- Touch targets smaller than 44x44px
- Text that doesn't scale properly

## Performance
- Unoptimized images (missing width/height, no lazy loading)
- Render-blocking resources
- Unused CSS or JavaScript

## Meta Tags
- Missing or empty `<title>` tag
- Missing meta description
- Missing Open Graph tags (og:title, og:description, og:image)
- Missing favicon

Format the results as a report with sections for each category. Use checkmarks for passing items and X marks for issues found. Include specific line numbers and suggested fixes for every issue.
```

### How to use it

```
/project:audit
```

---

## 3. Add Link Command

### File: `.claude/commands/add-link.md`

Create this file with the exact content below:

```markdown
Add a new link button to the LinkLaunch page.

Ask me for the following information:
1. **Platform name** — the display text for the button (e.g., "YouTube", "GitHub", "Portfolio")
2. **URL** — the full link URL (e.g., "https://youtube.com/@tylerreed")
3. **Icon emoji** — an emoji to display next to the platform name (e.g., "🎬", "💻", "🌐")

Then:
1. Add a new link button to the HTML that matches the existing button style and structure
2. Make sure it uses the theme system (CSS custom properties, not hardcoded colors)
3. Place the new button in the links container with the other link buttons
4. Add a smooth hover animation consistent with the other buttons
5. Ensure the link opens in a new tab with `target="_blank"` and `rel="noopener noreferrer"`

Do NOT modify any existing buttons — only add the new one.
```

### How to use it

```
/project:add-link
```

When prompted, provide something like:

```
Platform name: GitHub
URL: https://github.com/tylerreed
Icon emoji: 💻
```

---

## Setting Up the Commands

Create the commands directory and all three files:

```
Create the .claude/commands/ directory and add these three slash command files:

1. .claude/commands/preview.md — starts a local server and opens the browser
2. .claude/commands/audit.md — runs a full accessibility, links, mobile, performance, and meta tag audit
3. .claude/commands/add-link.md — asks for platform name, URL, and emoji, then adds a new link button

I'll give you the content for each file.
```

---

## Key Takeaways

| Command | What It Does |
|---------|-------------|
| `/project:preview` | Starts local server and opens browser |
| `/project:audit` | Full project audit (a11y, links, mobile, perf, meta) |
| `/project:add-link` | Interactive prompt to add a new link button |

> Slash commands live in `.claude/commands/` and are available via `/project:<filename>`. They turn multi-step workflows into one-liners.
