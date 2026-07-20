# Episode 2 — Filming Guide
## Claude Code Tutorial #2 - Write Prompts That Actually Work

---

## Pre-Recording Setup

### Terminal Prep
- [ ] Clean terminal history: `history -c`
- [ ] Terminal font 16pt+, dark theme, high contrast
- [ ] Terminal at ~80% screen width
- [ ] Notifications OFF, all other apps closed

### Project Prep
- [ ] Create clean demo directory: `mkdir -p ~/demo/ep02 && cd ~/demo/ep02`
- [ ] Delete any old files: `rm -rf ~/demo/ep02/*`
- [ ] Confirm Claude Code is installed and working: `claude` then `/exit`
- [ ] **Test both prompts beforehand** — make sure the vague one looks generic and the specific one looks good. Adjust wording if needed.
- [ ] Have the detailed prompt saved in a notes app (for reference, but type it live on camera)

### Key Prompts to Prepare

**Vague prompt (Round 1):**
```
Build me a portfolio website.
```

**Specific prompt (Round 2):**
```
Build me a personal portfolio website. Single HTML file with embedded CSS.

About me: I'm Tyler, a content creator who makes videos about AI tools.

Design: Dark theme with a deep navy background (#0a192f). Clean, minimal.
Use Inter or system sans-serif font. Subtle hover animations on links.

Sections:
1. Hero — my name large, one-line tagline "I help people build with AI",
   and links to YouTube and Twitter
2. Projects — 3 cards in a grid: "Claude Code Course" (description: beginner
   series on AI coding), "AI Tool Reviews" (description: honest reviews of
   the latest AI tools), "Newsletter" (description: weekly AI tips)
3. Footer — simple, just "Made with Claude Code" and a copyright line

Make it responsive. Mobile-first.
```

**Follow-up prompts:**
```
Add a "Contact" section before the footer with an email link
and a short message that says "Let's build something together."
```
```
The project cards need more spacing between them. Add 2rem gap.
And make the card backgrounds slightly lighter than the page background.
```

---

## Recording Playbook

### Scene 1: Hook (0:00-0:30)
**Setup:** Claude Code open in terminal
**Action:** Type the vague prompt. Show result briefly. Then cut to the specific prompt result.
**Tip:** This needs to be punchy. Quick cuts. Show don't tell.

---

### Scene 2: Why Prompts Matter (0:30-2:00)
**Setup:** Facecam, terminal in background
**Say:** Contractor analogy — "build me a house" vs detailed blueprint
**On screen:** Terminal with Claude Code open (idle)
**Tip:** Use hand gestures. Keep energy conversational.

---

### Scene 3: Side-by-Side Demo (2:00-4:30) — CRITICAL SCENE

**Round 1 — Vague prompt:**
```bash
# Start in clean directory
cd ~/demo/ep02
mkdir vague && cd vague
claude
```
**Type in Claude Code:**
```
Build me a portfolio website.
```
**After output:**
```bash
open index.html   # or whatever file Claude creates
```
**React honestly.** "It's... fine. But it's generic."

**Reset:**
```bash
/exit
cd ~/demo/ep02
mkdir specific && cd specific
claude
```

**Round 2 — Specific prompt:**
Type the full specific prompt (from prep above).
**After output:**
```bash
open index.html
```
**React with energy.** "Look at this. Night and day."

**Side by side:** Open both browser windows, drag them next to each other. This is the thumbnail moment.

---

### Scene 4: The Prompt Formula (4:30-7:00)
**Setup:** Can use a simple overlay graphic for C+T+C+F
**Action:** Walk through each part, highlighting the relevant section of the specific prompt
**Exact highlights to show:**
1. CONTEXT: "About me: I'm Tyler, a content creator..."
2. TASK: "Build me a personal portfolio website"
3. CONSTRAINTS: "Dark theme with deep navy... responsive... mobile-first"
4. FORMAT: "Single HTML file with embedded CSS"

**Tip:** Point at the screen or use cursor to highlight each section.

---

### Scene 5: Common Mistakes (7:00-9:00)
**Setup:** Claude Code open (can be idle)
**Action:** Show each bad/good example. Don't actually run them — just show the text.
**On screen:** Type each example in Claude Code's input (but don't hit enter). Or use text overlays.
**Pace:** Quick fire. ~40 seconds each mistake.

---

### Scene 6: Follow-up Demo (9:00-10:30)
**Setup:** Use the specific portfolio site from Scene 3 (should still be in the conversation)
**Exact commands:**
```bash
# Should still be in Claude Code from the specific prompt
# If not, cd to the specific folder and run claude
```
**Type follow-up 1:**
```
Add a "Contact" section before the footer with an email link
and a short message that says "Let's build something together."
```
**Show result in browser (refresh).**

**Type follow-up 2:**
```
The project cards need more spacing between them. Add 2rem gap.
And make the card backgrounds slightly lighter than the page background.
```
**Show result in browser (refresh).**

**Say:** "First prompt gets me 80%. Two or three follow-ups to polish."

---

### Scene 7: Starting Fresh (10:30-11:30)
**Setup:** Still in Claude Code
**Action:**
```bash
/clear
```
**Say:** "Sometimes the conversation goes sideways. Just start fresh."
**Tip:** Keep this short. The concept is simple.

---

### Scene 8: Outro (11:30-12:00)
**Say:** Recap the formula. Tease episode 3.
**On screen:** End screen with episode 3 teaser.

---

## Timing Cheat Sheet

| Section | Start | Duration | Priority |
|---------|-------|----------|----------|
| Hook | 0:00 | 0:30 | HIGH |
| Why Prompts Matter | 0:30 | 1:30 | MEDIUM |
| **Side-by-Side Demo** | **2:00** | **2:30** | **HIGHEST** |
| **Prompt Formula** | **4:30** | **2:30** | **HIGH** |
| Common Mistakes | 7:00 | 2:00 | MEDIUM |
| Follow-up Demo | 9:00 | 1:30 | HIGH |
| Starting Fresh | 10:30 | 1:00 | LOW |
| Outro | 11:30 | 0:30 | LOW |

---

## Common Mistakes to Avoid
- Don't rush the side-by-side comparison — let viewers absorb the difference
- Don't show too much code — this is about the prompts, not the output
- Don't over-explain the formula — show it, demonstrate it, move on
- The vague prompt NEEDS to look mediocre. If Claude randomly does a great job, re-record with an even vaguer prompt.

## If Things Go Wrong
- **Vague prompt produces something good:** Use an even vaguer prompt like "Make me a site" or re-record
- **Specific prompt has issues:** Use a follow-up to fix it on camera — this actually helps the narrative
- **Claude is slow:** Narrate what's happening while it works. Don't sit in silence.
- **Browser cache shows old version:** Hard refresh with Cmd+Shift+R
