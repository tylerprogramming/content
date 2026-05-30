# Master Demo Guide: One Project, One Mega-Video

The entire course builds ONE project from scratch in a single mega-video (~45-60 min). By the end, viewers have seen LinkLaunch grow from nothing into a fully-configured project with CLAUDE.md, permissions, custom commands, skills, MCP, sub-agents, and hooks — all stacked on top of each other.

**Format:** Single mega-video with chapters (can also be split into 13 playlist episodes)
**Target total:** 45-60 minutes (each section ~3-5 min, demos included)

---

## The Project: "LinkLaunch" — A Link-in-Bio Page Builder

A personal link-in-bio page (like Linktree/Bento). Why this project:
- Every creator and founder needs one — instantly relatable
- Simple enough to build in section 1 (just HTML/CSS)
- Complex enough to grow (themes, analytics, social icons, animations)
- Visually impressive on camera at every stage
- Natural reasons to add every concept (permissions, MCP, skills, hooks)
- Viewers can actually USE what they build

---

## Section-by-Section Build Path

### Section 1: What is Claude Code & Setup (~4 min)
**What you build:** Install Claude Code. Build LinkLaunch v1.

**Exact prompt:**
```
Build me a personal link-in-bio page called LinkLaunch. Use HTML, CSS,
and vanilla JavaScript. Dark theme with a centered layout. Include my
name at the top, a profile picture placeholder (use a circle with my
initials "TR"), and 5 link buttons that go to YouTube, Twitter, GitHub,
Instagram, and my website. Make the buttons have a hover animation.
Modern, clean design.
```

**What happens:** Claude creates index.html, style.css, app.js. Open in browser — instant visual payoff.

**Files after section 1:**
```
linklaunch/
  index.html
  style.css
  app.js
```

---

### Section 2: Prompting (~4 min)
**What you build:** Show vague vs specific prompting on LinkLaunch.

**Vague prompt (show briefly):**
```
add some social media stuff to my page
```

**Specific prompt (the good one):**
```
Add a social stats bar below my profile that shows follower counts for
each platform. Use icons (emoji is fine) with the platform name and a
number. Style it as a horizontal row with subtle separators. Also add
a "Latest Video" section that shows an embedded YouTube thumbnail with
a title and view count. Use placeholder data for now.
```

**Follow-up iteration:**
```
The social stats look too cramped on mobile. Make them wrap into a 2x2
grid on screens under 600px. Also make the YouTube thumbnail rounded
corners with a play button overlay.
```

**Key line:** "Same project, two completely different results. Specificity is the whole game."

---

### Section 3: CLAUDE.md (~4 min)
**What you build:** Add CLAUDE.md to LinkLaunch. Show it enforcing rules.

**First, WITHOUT CLAUDE.md:**
```
Add a theme switcher to LinkLaunch
```
(Claude might use React, Tailwind, or make weird choices)

**Then create CLAUDE.md with /init, edit to include these rules:**

→ See `ep03-claude-md/examples.md` for the exact CLAUDE.md content

**Then, WITH CLAUDE.md, same request:**
```
Add a theme switcher to LinkLaunch
```
(Claude follows every rule perfectly)

**Key line:** "Same prompt, completely different result. That's the power of CLAUDE.md."

---

### Section 4: Context Window (~3 min)
**What you build:** Add features to LinkLaunch until context fills up.

**Feature chain (rapid fire):**
```
Add a visitor counter that shows how many times the page has been loaded.
Use localStorage to persist the count.
```
Then:
```
Add an animation where the link buttons slide in from the left one by one
when the page loads. Use CSS keyframes, stagger each button by 100ms.
```
Then:
```
Add a contact form at the bottom with name, email, and message fields.
Style it to match the existing dark theme. Store submissions in localStorage.
```

**Show context bar growing.** Then `/compact focus on LinkLaunch's file structure and the CLAUDE.md rules`. Show it shrink. Briefly show `/clear`.

**Key line:** "Context window is Claude's short-term memory. When it fills up, things go sideways. /compact and /clear are your tools."

**Keep this SHORT — 3 min max.** Don't belabor it.

---

### Section 5: Permissions (~3 min)
**What you build:** Configure permissions for LinkLaunch.

**Show the approval prompt once,** then immediately go to `/permissions`:
```
Allow reading all files
Allow python3 -m http.server (dev server)
Allow git add, git commit, git status, git diff, git log
```

Then ask Claude to set up the rest:
```
Add common safe permissions — reading files, listing directories, git
operations, running the dev server. Show me what you're adding first.
```

**Key line:** "Pre-approve the safe stuff, keep your eyes on the risky stuff. Claude works twice as fast."

---

### Section 6: Models & Memory (~3 min)
**What you build:** Switch models for LinkLaunch tasks. Set memory.

**Haiku (simple task):**
```
Change the "GitHub" button text to "My Code"
```
(Fast, cheap, done)

**Opus (complex task):**
```
Redesign the link buttons to be interactive cards — when you hover, they
flip to show a preview/description of where the link goes. Use pure CSS
3D transforms.
```
(Opus reasons through the 3D CSS carefully)

**Memory:**
```
Remember that I always want to preview changes by opening index.html in
the browser after you edit it
```

Then `/clear`, new request, show Claude remembering.

---

### Section 7: Plan Mode (~3 min)
**What you build:** Plan and implement a major LinkLaunch feature (theme system).

**Toggle Plan Mode (Shift+Tab), then:**
```
I want to add a full theme system to LinkLaunch. Users should be able to
pick from 5 preset themes (dark, light, ocean, sunset, forest) using a
floating theme picker in the corner. Each theme changes colors, button
styles, and background. Store the selected theme in localStorage. Plan
how you'd implement this before building.
```

Watch Claude READ files, propose plan, NOT edit anything. Review the plan. Toggle back to normal mode. "Implement the plan."

**Key line:** "Think first, build second. Ctrl+G is your best friend for big features."

---

### Section 8: Sessions & Checkpoints (~3 min)
**What you build:** Demo session management and break-then-rewind LinkLaunch.

1. `/rename LinkLaunch - Theme System`
2. Close Claude (Ctrl+C), reopen with `claude --resume`, show session list
3. Quick `claude --continue` demo
4. Now the BREAK IT moment:
```
Convert all the CSS to use Sass with nested selectors and variables.
Rename style.css to style.scss.
```
5. This breaks the project (browser can't read .scss)
6. `/rewind` — pick the checkpoint before the Sass conversion
7. LinkLaunch works again.

**Key line:** "Claude has a built-in time machine. Use /rewind and you'll never be afraid to try things."

---

### Section 9: Slash Commands (~4 min)
**What you build:** Three custom commands for LinkLaunch.

Quick `/help` tour (30 seconds, just show the list).

**Command 1 — /preview:**
```
Create a slash command at .claude/commands/preview.md that starts a local
HTTP server for LinkLaunch and opens it in the browser
```

**Command 2 — /audit:**
```
Create a slash command at .claude/commands/audit.md that checks all
LinkLaunch files for accessibility issues, broken links, mobile
responsiveness problems, and performance suggestions
```

**Command 3 — /add-link:**
```
Create a slash command at .claude/commands/add-link.md that asks me for
a platform name, URL, and icon emoji, then adds a new link button to
LinkLaunch matching the existing style
```

Test each one. `/add-link` is the showstopper — show it adding a TikTok link live.

---

### Section 10: Skills (~5 min)
**What you build:** A UI component skill for LinkLaunch + show your real skills.

**Build the skill:**
```
Create a skill at .claude/skills/linklaunch-ui/SKILL.md that teaches
Claude how to build UI components for LinkLaunch. Include rules about
our design system: dark theme with CSS custom properties, 8px border
radius, smooth transitions on all interactive elements, mobile-first,
accessible with aria labels and keyboard navigation, always match the
current selected theme's color palette.
```

**Test it (without mentioning the skill):**
```
Build me a "bio section" component where I can write a short bio
with a character counter and an edit button
```

Watch Claude auto-detect the skill and follow all the rules.

**Then the wow moment:** Show your real skills briefly — `/thumbnail` generating an actual thumbnail is the money shot.

---

### Section 11: MCP Servers (~4 min)
**What you build:** Connect LinkLaunch to GitHub.

```
Initialize a git repo for LinkLaunch and make the first commit with
all current files
```

Set up GitHub MCP (show the command). Then:
```
Create a new GitHub repository called "linklaunch" and push my code to it
```
```
Create a GitHub issue titled "Add analytics tracking" with a description
about tracking link clicks and page views
```
```
Show me all open issues on the LinkLaunch repo
```

Open GitHub in browser — verify the repo, the code, and the issue are all real.

---

### Section 12: Sub-agents (~4 min)
**What you build:** Custom code reviewer for LinkLaunch.

**Auto-spawn demo:**
```
Review the entire LinkLaunch codebase: check JavaScript for bugs,
CSS for accessibility, and HTML for SEO issues. Give me a full report.
```
(Watch Claude spawn sub-agents — point them out)

**Custom agent:**
```
Create a custom agent at .claude/agents/ux-reviewer.md that reviews
LinkLaunch for user experience issues. It should check: visual hierarchy,
touch target sizes, loading performance, color contrast, and mobile
layout. Use Sonnet model. Only give it Read, Grep, and Glob tools.
```

Run it: `Use the ux-reviewer agent to review LinkLaunch`

---

### Section 13: Hooks & Grand Finale (~5 min)
**What you build:** Three hooks + the grand finale combining EVERYTHING.

**Hook 1 — Auto-format:**
```
Set up a hook that runs Prettier on any HTML, CSS, or JS file after
Claude edits it
```

**Hook 2 — Logging:**
```
Set up a hook that logs every file Claude edits to .claude/edit-log.txt
with timestamps
```

**Hook 3 — Protection:**
```
Set up a hook that blocks Claude from deleting any file. Exit code 2.
```

**THE GRAND FINALE (the money moment):**
```
I want to add a link click analytics dashboard to LinkLaunch. Use Plan
Mode to plan it first. After you implement it, the auto-format hook will
clean up the code. Then use the ux-reviewer agent to review the changes.
Finally, commit everything and push to GitHub.
```

Watch it all fire in sequence:
1. Plan Mode activates → reads files, proposes plan
2. You approve → Claude implements
3. Hooks auto-format every file edit (visible in output)
4. Sub-agent reviews the changes
5. MCP pushes to GitHub

**Key line:** "That's 13 concepts working together in one workflow. CLAUDE.md, permissions, Plan Mode, skills, hooks, sub-agents, and MCP — all from one terminal."

---

## Final Project Structure

```
linklaunch/
  index.html                  (sec 1-12: built up over time)
  style.css
  app.js
  CLAUDE.md                   (sec 3: project rules)
  .claude/
    settings.json             (sec 5: permissions)
    commands/                 (sec 9: custom commands)
      preview.md
      audit.md
      add-link.md
    skills/                   (sec 10: custom skill)
      linklaunch-ui/
        SKILL.md
    agents/                   (sec 12: custom agent)
      ux-reviewer.md
    edit-log.txt              (sec 13: hook output)
  README.md                   (sec 11: generated via MCP)
```

---

## Mega-Video Timing

| Section | Topic | Target | Running Total |
|---------|-------|--------|---------------|
| Intro/Hook | What we're building | 1:00 | 1:00 |
| 1 | Setup & First Build | 4:00 | 5:00 |
| 2 | Prompting | 4:00 | 9:00 |
| 3 | CLAUDE.md | 4:00 | 13:00 |
| 4 | Context Window | 3:00 | 16:00 |
| 5 | Permissions | 3:00 | 19:00 |
| 6 | Models & Memory | 3:00 | 22:00 |
| 7 | Plan Mode | 3:00 | 25:00 |
| 8 | Sessions & Checkpoints | 3:00 | 28:00 |
| 9 | Slash Commands | 4:00 | 32:00 |
| 10 | Skills | 5:00 | 37:00 |
| 11 | MCP Servers | 4:00 | 41:00 |
| 12 | Sub-agents | 4:00 | 45:00 |
| 13 | Hooks & Grand Finale | 5:00 | 50:00 |
| Outro/CTA | Recap + subscribe | 1:00 | 51:00 |

**Target: ~50 minutes** (edits may tighten to 40-45 min)

---

## Compounding Summary

| Section | What Gets Added | Builds On |
|---------|----------------|-----------|
| 1 | LinkLaunch v1 (profile + 5 link buttons) | Fresh start |
| 2 | Social stats, YouTube embed, mobile fix | Sec 1's page |
| 3 | CLAUDE.md with project rules, theme switcher | Sec 2's project |
| 4 | Visitor counter, animations, contact form | Sec 3's rules |
| 5 | Permissions in settings.json | Sec 4's workflow |
| 6 | 3D flip cards (Opus), model switching, memory | Sec 5's speed |
| 7 | Full 5-theme system via Plan Mode | Sec 3's rules + 6's cards |
| 8 | Session resume, Sass break + /rewind | Sec 7's theme system |
| 9 | /preview, /audit, /add-link commands | Sec 1-8's workflow |
| 10 | UI component skill, bio section | Sec 3's rules + 9's commands |
| 11 | GitHub repo, README, issues via MCP | Entire project |
| 12 | UX reviewer sub-agent | Sec 11's repo + 10's standards |
| 13 | Auto-format + logging + protection hooks + GRAND FINALE | ALL 12 sections |

---

## Filming Tips

1. **Save project state between sections.** `cp -r linklaunch/ linklaunch-backup-sec03/` after each section. If you need to re-record section 7, start from the section 6 backup.

2. **Film in order.** The compounding only works sequentially.

3. **Reference previous sections.** "Remember when we set up CLAUDE.md? Watch what happens now..." Rewards viewers who stick through the whole video.

4. **Show the .claude/ folder growing.** Quick file tree shot at the start of sections 9, 10, 12, and 13. Viewers see it growing from 3 files to a full ecosystem.

5. **The section 13 finale should feel like a victory lap.** Everything fires in sequence. This is the payoff for 50 minutes of watching.

6. **Put LinkLaunch on GitHub.** Link it in the video description. Viewers can clone and follow along.

7. **Chapters in the YouTube description** let viewers jump to any concept. This makes it work as both a watch-through AND a reference.
