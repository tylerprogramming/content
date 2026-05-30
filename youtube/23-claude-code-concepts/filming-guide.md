# Filming Guide: 23 Claude Code Concepts

## Pre-Recording Setup

### Environment Prep
- [ ] Clean terminal — clear history, set a clean prompt
- [ ] Make terminal font size large enough for screen recording (18-20pt)
- [ ] Close all unnecessary apps/notifications
- [ ] Have a sample project folder ready (something simple like a landing page project)
- [ ] Have Claude Code installed and working
- [ ] Have a CLAUDE.md file already created in the sample project
- [ ] Have at least one custom skill ready to demo (recommend /thumbnail or /fitness)
- [ ] Have an MCP server configured (GitHub is easiest)
- [ ] Have a screenshot of a webpage with a visible bug saved to desktop
- [ ] Open your code editor alongside the terminal
- [ ] Have a custom agent file ready in .claude/agents/ (e.g., code-reviewer.md)
- [ ] Have Claude Max subscription for Remote Control demo
- [ ] Have Claude app installed on your phone

### Files to Have Ready
- A sample project with a few files (e.g., a simple Next.js or HTML project)
- A CLAUDE.md file with 5-6 rules
- A custom skill in .claude/skills/
- A custom agent in .claude/agents/
- A hook configured in settings.json

---

## Timing Cheat Sheet

| Concept | Target Duration | Running Total |
|---------|----------------|---------------|
| Hook | 0:30 | 0:30 |
| 1. What is Claude Code | 0:45 | 1:15 |
| 2. The Terminal | 0:45 | 2:00 |
| 3. Prompting | 1:00 | 3:00 |
| 4. Permissions | 1:00 | 4:00 |
| 5. Tool Use | 1:00 | 5:00 |
| 6. Context Window | 1:15 | 6:15 |
| 7. CLAUDE.md | 1:00 | 7:15 |
| 8. Memory | 0:45 | 8:00 |
| 9. Models | 0:45 | 8:45 |
| 10. /init | 0:45 | 9:30 |
| 11. Plan Mode | 0:45 | 10:15 |
| 12. Compact & /clear | 0:45 | 11:00 |
| 13. Session History | 0:45 | 11:45 |
| 14. Checkpoints & /rewind | 0:45 | 12:30 |
| 15. @ File References | 0:45 | 13:15 |
| 16. Screenshots | 0:45 | 14:00 |
| 17. Slash Commands | 0:45 | 14:45 |
| 18. Skills | 1:15 | 16:00 |
| 19. MCP Servers | 1:00 | 17:00 |
| 20. Sub-agents | 1:00 | 18:00 |
| 21. Hooks | 1:00 | 19:00 |
| 22. Custom Agents | 0:45 | 19:45 |
| 23. Remote Control | 1:00 | 20:45 |
| Recap + CTA | 0:45 | 21:30 |

**Target total: ~21 minutes** (editing will tighten to ~17-18 min)

---

## Filming Steps

### Step 1: Record the Hook (0:00 - 0:30)
**What you do:** Talking head, high energy
**What you say:**
> "I watched every Claude Code tutorial on YouTube and they all have the same problem — they explain concepts but never actually show you. So in the next 15 minutes, I'm going to walk you through 21 Claude Code concepts, and for every single one, I'll open my terminal and demo it live. No slides. No theory. Just Claude Code running on screen. Let's go."

**On-camera tip:** Start with a pause, then hit it with energy. Cut to terminal montage in editing.

---

### Step 2: Concept 1 — What is Claude Code (0:30 - 1:15)
**What you do:**
1. Have ChatGPT open in a browser — ask it "build me a landing page" — it gives text response
2. Switch to terminal with Claude Code open
3. Type: `build me a simple landing page with a hero section`
4. Show Claude actually creating files

**What you say:**
> "Chatbots talk. Claude Code takes action."

**What happens:** Claude will create an HTML file. Let it run for a few seconds, then cut.

---

### Step 3: Concept 2 — The Terminal (1:15 - 2:00)
**What you do:**
1. Open a fresh terminal window
2. Type `claude` — show it launching
3. Type `Control+C` twice — show it closing
4. Reopen with `claude`
5. Type `/clear` — show it clearing

**What you say:**
> "Three commands. That's all you need."

---

### Step 4: Concept 3 — Prompting (2:00 - 3:00)
**What you do:**
1. Have Claude Code open
2. Type a vague prompt: `make a website`
3. Let it generate something basic
4. Then paste the specific prompt (have it copied beforehand):
```
build me a one-page landing page for a consulting business with a green color scheme, a contact form, and three service cards
```
5. Show the better result

**What you say:**
> "Better prompts, better results. That's the whole game."

**Tip:** Pre-write the specific prompt so you can paste it quickly.

---

### Step 5: Concept 4 — Permissions (3:00 - 4:00)
**What you do:**
1. Show an approval prompt appearing (Claude asking to run a command)
2. Click approve a couple times
3. Then type `/permissions`
4. Add a safe action to the allow list

**What you say:**
> "Pre-approve the safe stuff, gate-keep the risky stuff."

---

### Step 6: Concept 5 — Tool Use (4:00 - 5:00)
**What you do:**
1. Give Claude a task like: `read my package.json and add a start script`
2. Point out where Claude says "Read file" in the output
3. Point out where it says "Edit file"
4. Point out where it says "Bash" when it runs a command

**What you say:**
> "You don't tell Claude which tool to use. You describe the goal, Claude picks the tools."

---

### Step 7: Concept 6 — Context Window (5:00 - 6:15)
**What you do:**
1. Point to the context bar at the bottom of the terminal
2. Chat for a bit — show the bar growing
3. Explain that when it fills up, Claude forgets things

**What you say:**
> "This is the single most important concept. If you learn nothing else from this video, learn this."

**Tip:** Give this concept extra breathing room. It's the foundation for everything.

---

### Step 8: Concept 7 — CLAUDE.md (6:15 - 7:15)
**What you do:**
1. Open your CLAUDE.md file in the editor — show some rules
2. Start a Claude Code session — show it reading the file at startup
3. Give a task that relates to one of the rules — show Claude following it

**What you say:**
> "If you're not using a CLAUDE.md file, you're making Claude guess."

---

### Step 9: Concept 8 — Memory (7:15 - 8:00)
**What you do:**
1. Tell Claude: `remember that I always prefer using bun instead of npm`
2. Show it saving the memory
3. Start a new session, ask Claude to install a package
4. Show it using bun

**What you say:**
> "Claude learns your preferences over time."

---

### Step 10: Concept 9 — Models (8:00 - 8:45)
**What you do:**
1. Type `/model`
2. Show the model selector with Haiku, Sonnet, Opus
3. Switch between them

**What you say:**
> "Sonnet for most things. Opus when it matters. Haiku for quick stuff."

---

### Step 11: Concept 10 — /init (8:45 - 9:30)
**What you do:**
1. Create a new empty-ish project folder (or use an existing one without CLAUDE.md)
2. Open Claude Code in it
3. Type `/init`
4. Show it scanning the project and generating a CLAUDE.md
5. Open the generated file

**What you say:**
> "This is the fastest way to start any project. Don't write your CLAUDE.md from scratch."

---

### Step 12: Concept 11 — Plan Mode (9:30 - 10:15)
**What you do:**
1. Hit `Ctrl+G` — show the Plan Mode indicator appear
2. Ask Claude to plan a feature: `plan adding a dark mode toggle to this app`
3. Show it reading files and proposing steps without editing
4. Hit `Ctrl+G` again to exit Plan Mode

**What you say:**
> "Think first, build second."

---

### Step 13: Concept 12 — Compact & /clear (10:15 - 11:00)
**What you do:**
1. Show a conversation that's been going a while (context bar partially full)
2. Type `/compact focus on the database schema`
3. Show the context bar shrinking
4. Then show `/clear` for a full reset

**What you say:**
> "Compact keeps the good stuff, clears the noise. Clear starts fresh."

---

### Step 14: Concept 13 — Session History (11:00 - 11:45)
**What you do:**
1. Close Claude Code (Ctrl+C twice)
2. Type `claude --resume`
3. Show the session list
4. Pick a session and resume it
5. Then show `claude --continue` for quick resume

**What you say:**
> "You never lose progress."

---

### Step 15: Concept 14 — Checkpoints & /rewind (11:45 - 12:30)
**What you do:**
1. Make a few changes with Claude
2. Let one go wrong (or pretend it did)
3. Type `/rewind`
4. Show the checkpoint list
5. Select one and restore

**What you say:**
> "It's like an undo button for your entire project."

---

### Step 16: Concept 15 — @ File References (12:30 - 13:15)
**What you do:**
1. Type a prompt with `@` and a file path: `look at @src/config.ts and add a new setting`
2. Show Claude reading the file immediately
3. Show it using the file content in its response

**What you say:**
> "Instead of describing where things are, just point Claude right at them."

---

### Step 17: Concept 16 — Screenshots (13:15 - 14:00)
**What you do:**
1. Have a screenshot of a webpage with a visible bug saved
2. Paste/drag it into Claude Code
3. Show Claude identifying the issue from the image
4. Show it fixing the code

**What you say:**
> "Show Claude the problem instead of describing it."

---

### Step 18: Concept 17 — Slash Commands (14:00 - 14:45)
**What you do:**
1. Type `/help` — show the full list of commands
2. Highlight the ones you've already used: /clear, /compact, /model, /init, /rewind
3. Briefly mention custom commands in .claude/commands/

**What you say:**
> "You've already been using these all video. Slash commands are shortcuts for everything."

---

### Step 19: Concept 18 — Skills (14:45 - 16:00)
**What you do:**
1. Open `.claude/skills/` and show your skill files
2. Open one skill's SKILL.md (recommend /thumbnail or /fitness for visual impact)
3. Show the instructions inside
4. Trigger the skill and show Claude following the specialized instructions
5. Show the output

**What you say:**
> "Skills are expert playbooks. You write the instructions once, Claude follows them perfectly every time."

**Tip:** This is the money demo. Pick a skill that produces something visible and impressive. /thumbnail generating an actual image is great here.

---

### Step 20: Concept 19 — MCP Servers (16:00 - 17:00)
**What you do:**
1. Show that you have GitHub MCP configured
2. Ask Claude something like: `show me my open pull requests` or `create a new GitHub issue titled "test issue"`
3. Show Claude pulling real data from GitHub

**What you say:**
> "MCP connects Claude Code to your tools. GitHub, Notion, databases — all from one terminal."

---

### Step 21: Concept 20 — Sub-agents (17:00 - 18:00)
**What you do:**
1. Give Claude a complex enough task that it spawns a sub-agent naturally
2. Or ask: `use a sub-agent to review this codebase for any security issues`
3. Show the sub-agent spinning up in the output
4. Show the result coming back

**What you say:**
> "Your main context stays clean. The sub-agents do the heavy lifting in their own space."

**How to fill dead air:** Talk about how sub-agents have their own context window while waiting for the result.

---

### Step 22: Concept 21 — Hooks (18:00 - 19:00)
**What you do:**
1. Show a hook in your settings or type `/hooks`
2. Show a simple hook — like auto-formatting after file edits
3. Have Claude edit a file and show the hook firing automatically
4. Point out: "No AI tokens used. It's just a script."

**What you say:**
> "Hooks are guardrails that run in the background without costing you anything."

---

### Step 23: Concept 22 — Custom Agents (19:00 - 19:45)

**What you do:**
1. Open `.claude/agents/` and show a custom agent file (e.g., `code-reviewer.md`)
2. Show the YAML frontmatter — model, tools, instructions
3. Trigger it: `use the code-reviewer agent to review this file`
4. Show it working in its own context and returning results

**What you say:**
> "You can build your own specialists. Define the model, the tools, the job — and run them on demand."

**Tip:** Keep this brief since sub-agents already introduced the concept. This is just "now you can build your own."

---

### Step 24: Concept 23 — Remote Control (19:45 - 20:45)

**What you do:**
1. Type `/rc` in the terminal
2. Show the QR code appearing
3. Pick up your phone, scan the QR code with the Claude app
4. Show the session loading on the phone
5. Approve a change or send a message from the phone
6. Show the terminal reflecting the activity

**What you say:**
> "Type slash rc, scan the QR code, and now your phone is a window into your terminal. Approve changes from the couch. This is the difference between babysitting the terminal and letting Claude actually be an agent."

**Tip:** This is a strong closer — visual and impressive. Pre-set up a session with an approval prompt ready so the demo is snappy.

---

### Step 25: Recap & CTA (20:45 - 21:30)
**What you do:** Talking head, energy up
**What you say:**
> "That's all 23 concepts. If you're just getting started, focus on the first ten. Get comfortable with CLAUDE.md, Plan Mode, and managing your context window. Those three alone will transform how you use Claude Code. Bookmark this video and come back when you need a refresher. If this was helpful, smash that like button and subscribe — I put out Claude Code content every week. See you in the next one."

---

## On-Camera Tips

- **If Claude errors during a demo:** Don't panic. Say "this happens sometimes" and show how you recover. It's actually more authentic.
- **If Claude takes too long:** Talk over it. Explain what it's doing while you wait. "You can see it reading the files..."
- **Energy:** Keep it conversational but moving. Each concept is under a minute — don't linger.
- **Transitions:** You can say the concept number as a transition: "Concept 7 — CLAUDE.md." Keep it simple.
- **Editing note:** You'll cut dead time in editing. Don't stress about pauses during recording.
- **Screen recording:** Make sure the terminal text is readable. Test at YouTube's 1080p playback size before recording the whole thing.
