# Filming Guide - Claude Code Tutorial #5 - Permissions & Safety

**Total Runtime Target:** 10 minutes
**Format:** Talking head + live terminal demo
**Prep Time:** ~10 min

---

## Pre-Filming Setup

1. **Terminal setup:**
   - Clean terminal, dark theme, large font (18-20pt)
   - Open Claude Code in a sample project (Node.js project works well -- has npm test, dev server, etc.)

2. **Reset permissions before filming:**
   - Delete or clear any existing `.claude/settings.json` so you start from default
   - This ensures every action triggers a permission prompt in the demo

3. **Have a sample project ready with:**
   - A few source files Claude can read
   - A working test suite (`npm test` or similar)
   - A `package.json` or similar config file
   - Git initialized

4. **Pre-plan the multi-step task for Section 6:**
   - Something like "Read my source files, find any bugs, fix them, and run the tests"
   - This should trigger multiple permission types (read, write, execute)

---

## Recording Playbook

### Scene 1: Hook (0:00 - 0:30) -- Talking Head

**Setup:** Camera, no terminal
**Say:** Hook A script (see hooks.md)
**Cut to:** Terminal on "Let's go"

---

### Scene 2: Why Claude Asks Permission (0:30 - 2:00) -- Terminal Demo

**Setup:** Fresh Claude Code session, no pre-approved permissions
**What to do:**

1. Show the terminal
   - **Say:** "Claude Code isn't just a chatbot. It can actually do things on your computer..."

2. Type: `Create a new file called test.txt with the text "hello world"`
   - Wait for the permission prompt to appear
   - **Say:** "See that? Claude wants to create a file. It's asking me if that's okay."

3. Approve the action
   - Show the file was created (can `ls` or just reference it)
   - **Say:** "And that's the key difference from ChatGPT. ChatGPT just talks. Claude Code acts."

4. Quick cut to talking head for the "great safety feature" part

---

### Scene 3: Approval Flow (2:00 - 3:00) -- Terminal Demo

**Setup:** Same session
**What to do:**

1. Trigger another permission prompt:
   - Type: `Read the package.json file and tell me what dependencies I have`
   - **Say:** "When Claude wants to do something, you get a few options."

2. Point out the options on screen:
   - Approve once
   - Approve for session
   - Deny
   - **Say:** "But none of these are permanent. For permanent settings, we need the permissions system."

---

### Scene 4: /permissions Setup (3:00 - 5:30) -- Terminal Demo

**Setup:** Same session
**What to do:**

1. Type: `/permissions`
   - Press Enter
   - **Say:** "Here's where it gets good."

2. Walk through the interface
   - **Say:** "You've got two lists. Allow list and deny list."

3. Add permissions one by one, saying each out loud:
   - Allow: Read files
     - **Say:** "Reading files. Totally safe. Allow it."
   - Allow: `npm test`
     - **Say:** "Running tests. Safe. Allow it."
   - Allow: `npm run dev` (or equivalent)
     - **Say:** "Dev server. Also safe."
   - Allow: git commands (`git status`, `git diff`, `git add`, `git commit`)
     - **Say:** "Git commands. Local operations. Safe."

4. Explain what NOT to allow:
   - **Say:** "Installing packages. Deleting files. API calls. Keep those gated."
   - **Say:** "If Claude is just looking at stuff, probably safe. If it's changing stuff or reaching out to the internet, approve it."

---

### Scene 5: settings.json (5:30 - 7:00) -- Terminal Demo

**Setup:** Same session or file editor
**What to do:**

1. Show the settings.json file location:
   - Type: `cat .claude/settings.json` or open in an editor
   - **Say:** "Behind the scenes, these get saved to settings.json."

2. Walk through the file structure:
   - Point out the allow list entries
   - Point out the deny list entries
   - **Say:** "You can edit this directly or use slash permissions. Same result."

3. Mention project-level vs global settings briefly

---

### Scene 6: Claude Sets Up Permissions (7:00 - 8:30) -- Terminal Demo

**Setup:** Clear settings.json to start fresh (or use a different project)
**What to do:**

1. Type: `Set up permissions for this project. Allow reading files, running tests with npm test, and git commands. Deny any file deletions and package installs.`
   - **Say:** "Here's a pro tip. You can ask Claude to set up permissions for you."

2. Let Claude work through it
   - Approve when Claude wants to modify settings.json
   - **Say:** "See? It knows the format. It just sets it up."

3. Verify with `/permissions`
   - **Say:** "All configured."

---

### Scene 7: Speed Demo (8:30 - 9:15) -- Terminal Demo

**Setup:** Permissions fully configured
**What to do:**

1. Optional: show a quick "before" clip with constant interruptions (can be a replay or re-enactment)

2. Type a multi-step task:
   - `Read through my source files, check for any issues, and run the tests`
   - **Say:** "Watch. It just goes."

3. Let Claude work -- it should read files, analyze code, run tests, all without stopping
   - **Say:** "No interruptions. Night and day."

---

### Scene 8: Recap & Next Episode (9:15 - 10:00) -- Talking Head

**Setup:** Camera, no terminal
**Say:** Recap script from script.md
**Tease:** Episode 6 (Models & Memory)

---

## Timing Cheat Sheet

| Section | Start | Duration | Type |
|---------|-------|----------|------|
| Hook | 0:00 | 30 sec | Talking head |
| Why Claude asks | 0:30 | 1.5 min | Terminal |
| Approval flow | 2:00 | 1 min | Terminal |
| /permissions setup | 3:00 | 2.5 min | Terminal |
| settings.json | 5:30 | 1.5 min | Terminal/editor |
| Claude sets up perms | 7:00 | 1.5 min | Terminal |
| Speed demo | 8:30 | 45 sec | Terminal |
| Recap + next ep | 9:15 | 45 sec | Talking head |

---

## B-Roll / Overlay Ideas

- Bouncer at a door (metaphor for permission gating)
- Speed comparison: stopwatch showing time with vs without permissions
- Simple checklist graphic: "Allow" vs "Deny" categories
- settings.json structure diagram

---

## Common Mistakes to Avoid During Filming

- Make sure to reset permissions before filming so the "before" state is authentic
- Don't skip showing the deny list -- safety is important for beginner trust
- Keep the settings.json walkthrough brief; don't get lost in file details
- The speed demo at the end is the payoff -- make sure it's smooth and impressive
