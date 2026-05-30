# Filming Guide - Claude Code Tutorial #6 - Models & Memory

**Total Runtime Target:** 10 minutes
**Format:** Talking head + live terminal demo
**Prep Time:** ~10 min

---

## Pre-Filming Setup

1. **Terminal setup:**
   - Clean terminal, dark theme, large font (18-20pt)
   - Open Claude Code in a sample project

2. **Clear memories before filming:**
   - Back up your CLAUDE.md file
   - Clear or simplify it so you can show a clean "before" state for the memory demo
   - You want to show memories being added fresh

3. **Know your current default model:**
   - Check which model Claude Code defaults to
   - Plan the model switching demo accordingly

4. **Prepare the comparison question:**
   - Pick a moderately complex question that shows a clear quality/depth difference between Haiku and Opus
   - Test it beforehand to make sure the difference is visible
   - Suggestion: "Explain the trade-offs between SQL and NoSQL databases for a startup MVP"
   - Or: "Design a notification system for a mobile app"

5. **Have a CLAUDE.md ready to show:**
   - After the memory demo, you'll want to show the file contents
   - Make sure the path is easy to navigate to on screen

---

## Recording Playbook

### Scene 1: Hook (0:00 - 0:30) -- Talking Head

**Setup:** Camera, no terminal
**Say:** Hook A script (see hooks.md)
**Cut to:** Terminal on "Let's go"

---

### Scene 2: The Three Models (0:30 - 2:30) -- Talking Head + Terminal

**Setup:** Can be mostly talking head with graphics, or terminal
**What to do:**

1. Explain each model:
   - **Say:** "First, Haiku. The fast one. The cheap one. Think of it like a junior assistant."
   - **Say:** "Second, Sonnet. The balanced one. This is what most people use for everyday work."
   - **Say:** "Third, Opus. The powerhouse. Slower, costs more, but the smartest model available."

2. Give the framework:
   - **Say:** "Don't use a sledgehammer to hang a picture frame. Match the model to the task."

[NOTE: Graphic overlay with three tiers would be very helpful here]

---

### Scene 3: When to Use Each (2:30 - 4:00) -- Talking Head with Overlays

**Setup:** Talking head with text overlays for each model's use cases
**What to do:**

1. Walk through specific use cases for each model:
   - **Haiku:** Quick lookups, formatting, renaming, error messages
   - **Sonnet:** Building features, code reviews, explanations, daily work
   - **Opus:** Architecture, complex debugging, tricky business logic

2. Mention cost:
   - **Say:** "The cost difference is real. Using Haiku for simple stuff saves you real money."

---

### Scene 4: /model Demo (4:00 - 5:30) -- Terminal Demo

**Setup:** Claude Code open in terminal
**What to do:**

1. Type: `/model`
   - Press Enter
   - **Say:** "Slash model. That's it."

2. Show the model selection list
   - **Say:** "Right now I'm on Sonnet. Let me switch to Opus."

3. Select Opus
   - **Say:** "Done. Now everything uses Opus until I switch again."

4. Ask a quick question to confirm
   - Type: `What's the difference between a function and a method?`

5. Switch back:
   - Type: `/model`
   - Select Sonnet
   - **Say:** "Took two seconds. No context lost."

6. Give the car analogy:
   - **Say:** "Think of it like shifting gears. Shift up when you need power, back down when you don't."

---

### Scene 5: Model Comparison (5:30 - 6:30) -- Terminal Demo

**Setup:** Terminal, ready to switch models
**What to do:**

1. Switch to Haiku:
   - Type: `/model`
   - Select Haiku

2. Ask the comparison question:
   - Type: `Explain the trade-offs between SQL and NoSQL databases for a startup MVP`
   - Wait for response
   - **Say:** "That was fast. Decent answer."

3. Switch to Opus:
   - Type: `/model`
   - Select Opus

4. Ask the same question:
   - Type the same question
   - Wait for response
   - **Say:** "See the difference? Opus went deeper. More nuance."

5. **Say:** "Neither is wrong. It's about what you need."

[NOTE: If responses are too long, you can fast-forward/cut in post. The point is showing the quality and speed difference.]

---

### Scene 6: Memory Demo (6:30 - 8:00) -- Terminal Demo

**Setup:** Claude Code with clean/minimal CLAUDE.md
**What to do:**

1. Tell Claude to remember something:
   - Type: `Remember that I always want TypeScript code with explicit types, never use 'any'. Also remember that I prefer functional programming patterns over classes.`
   - **Say:** "I'm going to tell Claude to remember my coding preferences."

2. Wait for Claude to confirm
   - **Say:** "Okay, it'll remember that."

3. Start a fresh session:
   - Type: `/clear`
   - **Say:** "Brand new session. No context from before."

4. Ask Claude to write code:
   - Type: `Write a function that fetches user data from an API and formats it`
   - Wait for response

5. Point out the preferences being applied:
   - **Say:** "Look. TypeScript. Explicit types. Functional pattern. No classes. It remembered."

---

### Scene 7: Managing Memory (8:00 - 9:15) -- Terminal Demo

**Setup:** Same session
**What to do:**

1. Show the CLAUDE.md file:
   - Navigate to `~/.claude/CLAUDE.md` or the project-level one
   - Show its contents
   - **Say:** "Claude stores memories in a file called CLAUDE.md."

2. Show you can edit it:
   - **Say:** "You can edit this directly. Add or delete whatever you want."

3. Tell Claude to remember something new:
   - Type: `From now on, always add error handling to every function you write`
   - **Say:** "Just say 'from now on' or 'remember that.' Claude gets it."

4. Ask Claude what it remembers:
   - Type: `What do you remember about my preferences?`
   - **Say:** "You can ask Claude what it knows. Full transparency."

---

### Scene 8: Recap & Course Wrap (9:15 - 10:00) -- Talking Head

**Setup:** Camera, no terminal
**Say:** Recap script from script.md
**Tease:** Future "power features" episodes

---

## Timing Cheat Sheet

| Section | Start | Duration | Type |
|---------|-------|----------|------|
| Hook | 0:00 | 30 sec | Talking head |
| Three models | 0:30 | 2 min | Talking head + graphics |
| When to use each | 2:30 | 1.5 min | Talking head + overlays |
| /model demo | 4:00 | 1.5 min | Terminal |
| Model comparison | 5:30 | 1 min | Terminal |
| Memory demo | 6:30 | 1.5 min | Terminal |
| Managing memory | 8:00 | 1.25 min | Terminal |
| Recap + wrap | 9:15 | 45 sec | Talking head |

---

## B-Roll / Overlay Ideas

- Three-tier graphic: Haiku / Sonnet / Opus with icons (rabbit, balanced scale, brain)
- Car gear shift metaphor
- Use case lists as text overlays for each model
- Side-by-side split screen for model comparison (if editing allows)
- CLAUDE.md file structure diagram

---

## Common Mistakes to Avoid During Filming

- Test the model comparison question beforehand -- make sure there's a visible difference
- The memory demo MUST show a fresh session to prove it works across conversations
- Don't spend too long on any single model's response -- cut in post if needed
- Make sure CLAUDE.md is cleaned up before filming so it's not cluttered with personal stuff
- Emphasize that this wraps up the foundations -- give viewers a sense of completion
