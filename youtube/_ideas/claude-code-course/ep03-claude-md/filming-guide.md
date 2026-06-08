# Episode 3 — Filming Guide
## Claude Code Tutorial #3 - CLAUDE.md Changes Everything

---

## Pre-Recording Setup

### Build the Demo Project
This episode needs a pre-built project for the before/after demo. Create it ahead of time.

```bash
# Create the demo project
mkdir -p ~/demo/ep03-taskmanager
cd ~/demo/ep03-taskmanager
```

- [ ] Create `index.html` — a simple task manager page with an input field, task list, add/delete buttons
- [ ] Create `styles.css` — clean styling using CSS custom properties for colors
- [ ] Create `app.js` — vanilla JS with DOM manipulation, add/complete/delete tasks
- [ ] Initialize git: `git init && git add -A && git commit -m "initial"`
- [ ] **IMPORTANT:** Make sure there is NO CLAUDE.md file yet
- [ ] Test the app in browser — make sure it works

### Test Both Demo Scenarios

**Test the "without" demo:**
```bash
cd ~/demo/ep03-taskmanager
claude
# Type: "Add a dark mode toggle to this app."
# Verify Claude does something wrong (uses React, Tailwind, creates new files, etc.)
# If Claude gets it right by accident, tweak the project or prompt until it guesses wrong
/exit
git checkout .  # Reset changes
```

**Test the "with" demo:**
- Create the CLAUDE.md file (from script section 4)
- Run the same prompt
- Verify Claude follows the rules
- Delete CLAUDE.md and reset: `rm CLAUDE.md && git checkout .`

[NOTE: You MUST test both scenarios before recording. The "without" demo needs to visibly fail. If vanilla JS is too simple for Claude to get wrong, make the project slightly more complex — add a second JS file, use a CSS naming convention, etc.]

### Terminal Prep
- [ ] Terminal font 16pt+, dark theme, high contrast
- [ ] Terminal at ~80% screen width
- [ ] Notifications OFF, all other apps closed
- [ ] Clean terminal history: `history -c`

### Files to Have Ready
- [ ] The complete CLAUDE.md content (from script section 4) saved in a notes app for reference
- [ ] Your real ~/.claude/CLAUDE.md as an example of a global one

---

## Recording Playbook

### Scene 1: Hook (0:00-0:35)
**Setup:** Claude Code open in the demo project (no CLAUDE.md)
**Action:**
1. Type: `Add a dark mode toggle to this app.`
2. Show the bad result (wrong framework, wrong files)
3. Quick cut — reset the project
4. Add CLAUDE.md (can be a quick cut — don't show the creation process yet)
5. Same prompt — show the good result
**Say:** "Same prompt. One file changed everything."
**Tip:** This should be FAST. Quick cuts. Save the explanation for later.

---

### Scene 2: What Is CLAUDE.md (0:35-2:00)
**Setup:** Facecam with terminal/file tree in background
**Say:** Instruction manual analogy. New developer with no onboarding vs full briefing.
**On screen:** Show a file tree with CLAUDE.md highlighted. Quick scroll through an example file.
**Tip:** Keep it conceptual. Don't show code details yet.

---

### Scene 3: Demo — Without CLAUDE.md (2:00-3:30)
**Setup:** Demo project, no CLAUDE.md, clean git state
**Exact commands:**
```bash
cd ~/demo/ep03-taskmanager
# Verify no CLAUDE.md
ls -la
# Start Claude Code
claude
```
**Type in Claude Code:**
```
Add a dark mode toggle to this app.
```
**After output:** Show what went wrong. Point at the wrong files, wrong framework.
**Say:** "It guessed wrong. Not Claude's fault — we didn't tell it."
**Reset:**
```bash
/exit
git checkout .
```

---

### Scene 4: Using /init (3:30-5:30)
**Exact commands:**
```bash
claude
```
**Type in Claude Code:**
```
/init
```
**On screen:** Claude analyzes the project and generates CLAUDE.md
**Say:** Narrate what Claude is doing. "It's looking at our files... figuring out the tech stack..."
**After generation:** Open and read through the generated CLAUDE.md
```bash
# After Claude creates it, review it
cat CLAUDE.md
```
**Say:** "Good starting point. But let's make it better."

---

### Scene 5: What to Put In (5:30-8:00) — KEY TEACHING SCENE
**Setup:** Edit CLAUDE.md (can use any editor visible on screen)
**Action:** Build the CLAUDE.md file section by section, talking through each part

Type each section live (or edit what /init generated):

**Section 1 — Project overview:**
```markdown
# Task Manager App

A simple browser-based task manager. Single-page app using
vanilla HTML, CSS, and JavaScript. No frameworks. No build tools.
```

**Section 2 — Tech stack:**
```markdown
## Tech Stack
- HTML5, CSS3, vanilla JavaScript (ES6+)
- No frameworks (no React, no Vue, no Tailwind)
- No build tools or bundlers
- Single stylesheet: styles.css
- Single script file: app.js
```

**Section 3 — File structure:**
```markdown
## File Structure
- index.html — main page, all markup here
- styles.css — all styles, using CSS custom properties for theming
- app.js — all logic, uses DOM manipulation (no jQuery)
```

**Section 4 — Rules:**
```markdown
## Rules
- Keep all code in these three files. Do not create new files.
- Use CSS custom properties (variables) for colors and spacing.
- Mobile-first responsive design.
- No external dependencies or CDN links.
- Comments on functions only, not on every line.
```

**Section 5 — Do NOTs:**
```markdown
## Do NOT
- Do not add React, Vue, or any JavaScript framework
- Do not add Tailwind or any CSS framework
- Do not create new files without asking first
- Do not add a package.json — this is not a Node project
```

**Tip:** Go slow enough for viewers to read each section. Explain WHY each rule matters.

---

### Scene 6: Demo — With CLAUDE.md (8:00-9:15) — PAYOFF SCENE
**Setup:** CLAUDE.md is now in the project. Start fresh conversation.
**Exact commands:**
```bash
/clear
```
**Type the EXACT same prompt:**
```
Add a dark mode toggle to this app.
```
**On screen:** Claude follows all the rules. No new files. Vanilla JS. CSS custom properties.
**After output:**
```bash
open index.html
```
**Show:** The dark mode toggle working in the browser.
**Say:** "Same prompt. Totally different result. One file."

---

### Scene 7: Global vs Project (9:15-10:15)
**Exact commands:**
```bash
# Show your real global CLAUDE.md
cat ~/.claude/CLAUDE.md
```
**Say:** Explain the difference. Global = personal preferences. Project = project rules.
**On screen:** Show the global file briefly. Don't go deep — just show it exists.
**Tip:** 60 seconds max. Quick and clear.

---

### Scene 8: Iteration Approach (10:15-11:15)
**Setup:** CLAUDE.md open in editor
**Action:** Show adding a rule after a "mistake"
**Say:** "Every mistake becomes a rule."
**On screen:** Type a new rule into CLAUDE.md based on a hypothetical mistake
**Example rules to add:**
```markdown
- Do not create .env files. Environment variables are handled by Vercel.
- Use snake_case for all file names and variable names.
```
**Tip:** This is the most important conceptual takeaway. Say it slowly. Repeat it.

---

### Scene 9: @imports Quick Mention (11:15-11:30)
**On screen:** Show @import syntax in a CLAUDE.md example
```markdown
@coding-standards.md
@api-conventions.md
```
**Say:** "For bigger projects. Don't worry about it yet."
**Tip:** 15 seconds. Just plant the seed.

---

### Scene 10: Outro (11:30-12:00)
**Say:** Recap. Tease episode 4.
**On screen:** End screen with playlist link.

---

## Timing Cheat Sheet

| Section | Start | Duration | Priority |
|---------|-------|----------|----------|
| Hook | 0:00 | 0:35 | HIGH |
| What Is CLAUDE.md | 0:35 | 1:25 | MEDIUM |
| **Demo — Without** | **2:00** | **1:30** | **HIGH** |
| Using /init | 3:30 | 2:00 | MEDIUM |
| **What to Put In** | **5:30** | **2:30** | **HIGHEST** |
| **Demo — With** | **8:00** | **1:15** | **HIGH** |
| Global vs Project | 9:15 | 1:00 | MEDIUM |
| Iteration Approach | 10:15 | 1:00 | HIGH |
| @imports | 11:15 | 0:15 | LOW |
| Outro | 11:30 | 0:30 | LOW |

---

## Common Mistakes to Avoid
- The "without" demo MUST visibly fail. Test beforehand. Adjust prompt/project if Claude guesses right.
- Don't spend too long on /init output — viewers want to see the customization
- Don't make the CLAUDE.md file too long on camera — 30 lines max feels approachable
- Don't skip the "Do NOT" section — it's the most impactful part for beginners

## If Things Go Wrong
- **Claude follows rules without CLAUDE.md:** Make the project more ambiguous. Add a package.json with React as a dependency but don't actually use React in the code. Claude will gravitate toward React.
- **/init produces a bad CLAUDE.md:** That's actually fine — it proves why manual customization matters
- **"With" demo still has issues:** Use a follow-up prompt to fix it. Then add the fix as a new rule — this actually demonstrates the iteration approach live.
- **Git reset doesn't clean everything:** Use `git checkout . && git clean -fd` to fully reset
