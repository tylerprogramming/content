# Filming Guide: Claude Code for Beginners

---

## Overview

Format: Solo tutorial, screen-heavy with face-to-camera intros and reaction cuts
Length target: 15-20 minutes edited
Setup: Screen recording + webcam (picture-in-picture or full cuts between the two)

---

## Screen Recordings Needed

### SR-01: Bad Plan Demo (Section: "What NOT to do")
Purpose: Show what beginner failure looks like — vague prompts, Claude going off-rails
Prompt to type exactly:
  > build me an app that stores AI prompts
Expected result: Claude asks clarifying questions or makes too many assumptions. Let it run partially, then stop it to show the chaos.
Notes: Do this in a fresh, empty directory. Leave the mistakes in — that's the point.

### SR-02: AskUserQuestion Demo (Section: "Planning with AskUserQuestion")
Purpose: Show the right way to start — Claude interviewing you about your project
Prompt to type exactly:
  > Before writing any code, use the AskUserQuestion tool to ask me everything you need to know to build a great AI Prompt Library app. Ask one question at a time.
Expected result: Claude fires structured questions one at a time. Answer them naturally on screen.
Notes: Record your actual answers being typed. This is the money shot of the tutorial — don't rush it. Show 3-4 questions minimum.

### SR-03: CLAUDE.md Setup (Section: "CLAUDE.md and Skills")
Purpose: Show creating and editing CLAUDE.md in the project root
Steps to record:
  1. Open terminal at project root
  2. Run: touch CLAUDE.md
  3. Open in editor and paste your project-specific instructions (role, stack, rules)
  4. Show Claude reading it on next prompt
Notes: Keep this section tight — 60-90 seconds of screen time max.

### SR-04: Feature-by-Feature Building (Section: "Building Feature by Feature")
Purpose: Show the feature-scoped approach — one thing at a time, never multi-tasking Claude
Prompts to use in sequence (record each separately, edit together):
  Prompt 1: > Build just the data model for storing prompts. Nothing else yet.
  Prompt 2: > Now add the ability to create a new prompt. No UI yet, just the logic.
  Prompt 3: > Now build a simple UI to list all prompts and add a new one.
Notes: Speed up Claude's output in editing. Show pauses where you review what it built before moving on.

### SR-05: Ralph Loop Demo (Section: "Ralph Loops")
Purpose: Show iterative loop: run -> review -> fix -> run again
Steps to record:
  1. Trigger a bug or imperfect output (run the app, show a broken state)
  2. Go back to Claude and say: > That didn't work as expected. [describe the issue]. Fix only this.
  3. Show the fix being applied
  4. Run the app again — show it working
Notes: Don't fake perfection. If something breaks for real, keep it in — that's authentic and educational.

### SR-06: Tips Montage (Section: "Tips and Tricks")
Purpose: Quick-hit tips shown directly on screen
Tips to demo in order:
  Tip 1: Compact context — show /compact command in Claude Code terminal
  Tip 2: Scoped prompts — show typing a tight, specific one-task prompt
  Tip 3: Ask Claude to explain — show: > Before you write any code, explain your plan in plain English
  Tip 4: Custom skills — briefly show a skill file in ~/.claude/skills/
Notes: Keep each tip to 15-20 seconds of screen time. Edit with quick cuts between them.

### SR-07: Finished App Demo (Section: "Outro")
Purpose: Show the complete, working AI Prompt Library app in the browser
Steps:
  1. Run the app
  2. Add a prompt live
  3. Search/filter prompts
  4. Show a clean, polished state of the UI
Notes: Record this last after the app is fully built. This is also used for the thumbnail and the hook teaser.

---

## Face-to-Camera Segments

### FTC-01: Hook (30-45 seconds)
Use Hook 1 or Hook 5 from hooks.md
Energy: High, fast, direct. No warmup.
Shot: Medium close-up. Slight forward lean. No lower-third needed.

### FTC-02: Section Intro — "Bad Plans" (15-20 seconds)
Set up the concept before going to screen: "Before I show you the right way, let me show you exactly how I was doing this wrong..."

### FTC-03: Section Intro — "AskUserQuestion" (20-30 seconds)
Explain WHY this tool matters before the demo: "This is the tool that changed how I plan every project..."

### FTC-04: Section Intro — "Ralph Loops" (15-20 seconds)
Define Ralph loop in plain language before showing it on screen.

### FTC-05: Outro (45-60 seconds)
- Recap what was built
- Tell them what to do next (subscribe, watch next video)
- Call out the resources in the description
- End with a specific CTA: "If this saved you time, the subscribe button is right there."

---

## B-Roll Suggestions

- Time-lapse of code being written (Claude typing in terminal) — great for transitions
- Split-screen: bad prompt result (left) vs. AskUserQuestion result (right)
- Close-up of terminal text scrolling (good for energy/pacing moments)
- Screen zoom-in on the AskUserQuestion tool output (emphasize the key moment)
- App UI slowly loading in browser (great for the "reveal" moment in hook and outro)

---

## Editing Notes

### Pacing
- Hook through "Bad Plans" section: Keep tight. Every cut should have a reason.
- AskUserQuestion section: Slow down here intentionally. Let each question breathe — viewers need to absorb it.
- Feature-by-feature building: Speed up Claude's output to 1.5x-2x. Cut between features — don't show full generation time unless something interesting is happening.
- Ralph Loops section: Real time on the bug and fix. This is where authenticity pays off.
- Tips section: Fast cuts, almost montage-style. 10-15 seconds per tip max.

### Where to Speed Up
- Any time Claude is generating boilerplate code (>10 seconds): speed to 2x-4x
- Terminal output scrolling with no action needed: cut or speed up aggressively
- File creation / installs (npm install, etc.): speed to 4x or cut with a jump-cut

### Where to Keep Real Time
- Tyler typing prompts (let viewers read along)
- AskUserQuestion firing and Tyler answering
- Bug appearing live and Tyler's reaction — keep authentic

### Transitions
- Screen to face-to-camera: hard cut preferred (fast paced tutorial energy)
- Between tips: smash cut with a subtle zoom punch
- Section breaks: simple lower-third title card with section name (no flashy animations)

### Text / Graphics
- Add callout text on-screen when key terms appear: "AskUserQuestion", "Ralph Loop", "CLAUDE.md"
- Highlight key prompts in a code block overlay when Tyler types them
- Progress bar or chapter marker at the bottom (optional but good for long-form)

---

## Thumbnail Concepts

### Concept 1: The Reaction Shot
- Tyler face — surprised/impressed expression
- Overlay text: "Claude Code BUILT THIS" (bold, high contrast)
- Background: Screenshot of the finished Prompt Library app
- Color palette: Black background, yellow or cyan text

### Concept 2: Before / After Split
- Left half: Messy, broken Claude Code terminal (red tint)
- Right half: Clean, working app in browser (green tint)
- Tyler in the center with a pointing gesture toward the right
- Text: "Do THIS instead" (large, white)

### Concept 3: The Prompt Close-Up
- Full-bleed screenshot of the AskUserQuestion tool firing in terminal
- Tyler's face in corner (small, reaction expression)
- Text overlay: "The tool beginners miss" (white text, dark shadow)
- Works well if Hook 5 (Secret Weapon) is used

---

## Pre-Production Checklist

- [ ] Fresh Claude Code install confirmed (show version in terminal)
- [ ] Empty project directory created for recording
- [ ] CLAUDE.md template written and ready to paste
- [ ] AskUserQuestion prompt scripted and tested
- [ ] App concept defined: AI Prompt Library (name, tags, search)
- [ ] Screen recording software set up (1080p minimum, 60fps preferred)
- [ ] Webcam framing checked — medium close-up, good light on face
- [ ] Microphone tested — no background noise
- [ ] Notifications disabled on screen (do not disturb mode on)
