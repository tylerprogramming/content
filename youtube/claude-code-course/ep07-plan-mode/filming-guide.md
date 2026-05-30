# Episode 7 — Filming Guide
## Claude Code Tutorial #7 - Plan Before You Build

---

## Pre-Recording Setup

1. **Project:** Have a simple web app ready (HTML/CSS/JS) — something like a to-do app or landing page. Nothing fancy. It just needs a header, some content, and a styles file.
2. **Terminal:** Clean terminal, font size 16+, dark theme for readability.
3. **Claude Code:** Open in the project directory. Fresh session.
4. **Browser:** Have the web app open in a browser tab for showing the final dark mode result.
5. **Close** all other apps, notifications off.

---

## Recording Playbook

### Segment 1: INTRO (0:00 - 1:30)

**What to show:** Terminal with Claude Code open.
**What to say:** Deliver Hook A from hooks.md.
**On screen:** Quick flash of messy code changes, then the clean plan output.
**Action:** No commands yet. Just talking to camera / voiceover with terminal visible.

---

### Segment 2: WHAT IS PLAN MODE? (1:30 - 3:00)

**What to show:** Terminal with Claude Code.
**What to say:** Explain the concept — Claude reads but doesn't write.
**On screen:** Just the terminal. No commands yet.
**Key line:** "It's the difference between a contractor who just starts swinging a hammer and one who shows you blueprints first."

---

### Segment 3: HOW TO TOGGLE (3:00 - 4:30)

**Exact commands:**
```
# In Claude Code input area:
Press Shift+Tab     → shows "plan" mode indicator
Press Shift+Tab     → back to normal
Press Shift+Tab     → plan mode again
Press Shift+Tab     → normal again
```

**What to say:** "You toggle Plan Mode with Shift+Tab. That's it."
**On screen:** Zoom into the mode indicator so viewers can clearly see it changing.
**Key point:** Mention the third mode (plan auto-accept) but tell them to skip it for now.

---

### Segment 4: DEMO — PLANNING A FEATURE (4:30 - 7:00)

**Step-by-step:**

1. Make sure Plan Mode is ON (Shift+Tab)
2. Type this prompt:
   ```
   I want to add a dark mode toggle to this app. A button in the top
   right corner that switches between light and dark themes. The
   user's preference should be saved.
   ```
3. Press Enter. Let Claude read files and generate a plan.
4. **Wait for the plan.** Show it clearly on screen.
5. Type a revision:
   ```
   Looks good but skip the transition effect. Just make it an instant switch.
   ```
6. Let Claude update the plan.
7. Toggle Plan Mode OFF (Shift+Tab)
8. Type:
   ```
   Go ahead and implement the plan.
   ```
9. Let Claude build. Show files being created/edited.
10. Switch to browser and show the dark mode toggle working.

**What to say during waits:** Narrate what Claude is doing. "See? It's reading the HTML file. Now the CSS. It's mapping out the structure."

**What happens on screen:** Claude reads files, proposes a 4-step plan, you revise it, then it implements.

---

### Segment 5: THE WORKFLOW (7:00 - 8:30)

**What to show:** Can do this as a talking-head with text overlay, or in the terminal.
**On screen:** The four steps appearing:
1. EXPLORE
2. PLAN
3. IMPLEMENT
4. COMMIT

**What to say:** Walk through each step with a one-sentence explanation.
**Optional:** Quick montage of each step in the terminal (can be sped up in editing).

---

### Segment 6: WHEN TO USE IT (8:30 - 9:30)

**What to show:** Two-column graphic or text overlay.
**What to say:**
- "Use Plan Mode when the task touches multiple files, or you're not sure how the codebase works."
- "Skip it when it's a simple one-liner."
**Key line:** "Fix a button color? Skip Plan Mode. Add a payment system? Plan Mode. Every time."

---

### Segment 7: EXTENDED THINKING (9:30 - 11:00)

**What to show:** Terminal with Claude Code processing a slightly complex request.
**Exact command:**
```
# In normal mode, type something that requires thinking:
Refactor the CSS to use CSS custom properties and create a theme system
that supports light, dark, and high-contrast modes.
```

**What to say:** "See that pause? Claude is thinking. Extended thinking is on by default."
**On screen:** Show Claude's thinking indicator, then the response.
**Key point:** "You don't need to manage this. It just works."

---

### Segment 8: RECAP (11:00 - 12:00)

**What to show:** Bullet points (can be text overlay or terminal).
**What to say:** Recap the four key points from the script.
**End with:** Tease episode 8 — sessions and checkpoints. "It's like an undo button for your entire project."

---

## Timing Cheat Sheet

| Segment | Start | Duration | Key Action |
|---------|-------|----------|------------|
| Intro | 0:00 | 1:30 | Hook, course context |
| What is Plan Mode | 1:30 | 1:30 | Concept explanation |
| How to Toggle | 3:00 | 1:30 | Shift+Tab demo |
| Demo: Planning | 4:30 | 2:30 | Full Plan Mode workflow |
| The Workflow | 7:00 | 1:30 | 4-step framework |
| When to Use It | 8:30 | 1:00 | Use vs. skip guidance |
| Extended Thinking | 9:30 | 1:30 | Thinking demo |
| Recap | 11:00 | 1:00 | Summary, next ep tease |

**Total: ~12 minutes**

---

## Backup Plan

If Plan Mode doesn't produce a clean-looking plan on the first try, have a second project ready. Or re-run the prompt — the plans are usually slightly different each time. Pick the cleanest one.

If extended thinking doesn't show a visible pause, use a more complex prompt to trigger a longer think time.
