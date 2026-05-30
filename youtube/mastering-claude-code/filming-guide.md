# Filming Guide: How I Actually Use Claude Code (Full Workflow)

---

## Pre-Recording Setup

### Environment Cleanup
- [ ] Close all unnecessary apps and browser tabs
- [ ] Clean your desktop (hide personal files)
- [ ] Set terminal font size large enough for screen recording (16-18pt minimum)
- [ ] Use a clean terminal theme with good contrast (dark background, bright text)
- [ ] Turn off system notifications (Focus mode on Mac)
- [ ] Make sure Claude Code is updated to latest version: `claude update`

### Project Setup
- [ ] Copy the CLAUDE.md from `~/yt-ralph-project/CLAUDE.md` into the Peeps project directory
- [ ] Copy the `prd.md` from `~/content/youtube/mastering-claude-code/prd.md` into the Peeps project directory
- [ ] Make sure the project has the shadcn/ui scaffold already set up (React + Vite + TypeScript + Tailwind v3 + shadcn)
- [ ] Verify `npm install` works and `npm run dev` runs without errors on the base scaffold
- [ ] Make sure your Ralph loop script is ready and tested
- [ ] Do a DRY RUN of the full Ralph loop before recording to catch any issues
- [ ] Delete the `/data/peeps/` folder between runs so it starts clean on camera

### Files to Have Ready
- [ ] `~/.claude/CLAUDE.md` — your global config (clean it up if needed)
- [ ] `~/yt-ralph-project/CLAUDE.md` — the project-level config to show on screen
- [ ] `~/.claude/skills/` — all 7 skills ready to show
- [ ] `~/content/youtube/mastering-claude-code/prd.md` — the Peeps PRD (copied into project dir)
- [ ] A short YouTube video URL (under 2 min) for the /transcribe demo

### Prompts to Have Ready (Copy-Paste)

**Basic Peeps planning prompt:**
```
I want to build a local fullstack app called Peeps that tracks people's birthdays, contact info, and notes. It stores each person as a markdown file and displays them in a clean UI with cards. I'm using React, Vite, TypeScript, shadcn/ui, and Tailwind CSS v3.
```

**Ask User Question follow-up prompt:**
```
Read the plan you just created. Now interview me in detail using the ask user question tool about technical implementation, UI/UX decisions, data structure, and trade-offs. Don't start building until you've asked me at least 3 rounds of questions.
```

---

## Filming Steps

### Step 1: Hook (Face to Camera)
**Target: 30 seconds**

**What you do:** Look at camera, deliver the hook with high energy.

> "Most people use Claude Code like a chatbot. They type a vague prompt, get mediocre code, and blame the model. But the model isn't the problem — your workflow is. Today I'm showing you my exact setup — and then building a full app live on camera using a Ralph loop. No editing tricks."

**Tips:**
- Highest energy of the whole video. This decides if people stay.
- Memorize this or use a teleprompter — no looking down.
- Cut stumbles in editing.

---

### Step 2: The Core Problem (Face to Camera)
**Target: 1.5 minutes**

**What you do:** Explain garbage in/garbage out, introduce the 4-part structure, tease Peeps.

> "Here's what most people do. Open Claude Code, type 'build me a contacts app,' get frustrated. The models are insanely good in 2026. If you're getting bad output, it's your workflow."

> "Four things fix this — and by the end, we'll have a working app called Peeps built entirely by Claude Code."

**Tips:**
- Hold up four fingers when you say "four things"
- If you can, flash a quick shot of the finished Peeps app here as a tease (record this after the Ralph demo is done)

---

### Step 3: CLAUDE.md Demo (Screen Recording)
**Target: 3 minutes**

**What you do:**
1. Open terminal
2. Navigate to the project: `cd ~/yt-ralph-project`
3. Open the CLAUDE.md in your editor or cat it in terminal
4. Walk through the three sections: WHAT (stack), WHY (rules like the Tailwind v3 warning), HOW (dev commands)
5. Show your global `~/.claude/CLAUDE.md` briefly
6. Run `/init` in a fresh folder to show auto-generation

**Exact actions:**
```bash
# Show the project CLAUDE.md
cat ~/yt-ralph-project/CLAUDE.md

# Show global CLAUDE.md
cat ~/.claude/CLAUDE.md

# Demo /init (open Claude Code in a fresh folder)
cd /tmp/demo-project && claude
# Then type: /init
```

**What you say:**
> "This is a real CLAUDE.md. Tech stack at the top — React 18, Vite, TypeScript, Tailwind v3, shadcn. See this warning? 'Do NOT upgrade to Tailwind v4.' This saves hours. Without it, Claude might upgrade your deps and break everything."

> "Three questions your CLAUDE.md should answer: What is this project? Why does it exist? How should Claude work on it?"

> "If you're starting from scratch, run /init and Claude generates one for you."

**How to fill dead air while /init runs:**
> "It's scanning the folder — package.json, directory layout, config files — figuring out what kind of project this is."

**Tips:**
- Zoom in on the Tailwind v3 warning — it's a concrete, relatable example
- Don't read the entire file — highlight 3-4 key sections

---

### Step 4: Skills Demo (Screen Recording)
**Target: 2.5 minutes**

**What you do:**
1. Show the skills directory listing
2. Name each skill quickly (don't deep-dive)
3. Open one skill's markdown file to show the format
4. Run `/transcribe` live with a short YouTube URL
5. Show the transcript output

**Exact actions:**
```bash
# Show skills folder
ls ~/.claude/skills/

# Open a skill file (pick the simplest one to show)
cat ~/.claude/skills/transcribe/transcribe.md   # or wherever the skill file lives

# Run the skill in Claude Code
# Type: /transcribe https://www.youtube.com/watch?v=SHORT_VIDEO_ID
```

**What you say:**
> "Seven custom skills. Transcription, video planning, journaling, image resize, background removal, PRD generation, and idea saving."

> "Let me show you one working. /transcribe — paste a YouTube URL — it downloads the audio, sends it to Whisper, saves a timestamped transcript."

> [While running] "Skills are just markdown files with instructions. Plain English. 'Download the audio, transcribe it, save to this folder.' Claude reads it and follows the steps."

> [After output] "30 seconds. Full transcript with timestamps. That's the power of packaging your workflow as a skill."

**What you say while showing the skill file:**
> "Look — it's just markdown. Not code. Just instructions. You tell Claude what tools to use and what steps to follow. Anyone can write these."

**Tips:**
- Pick a YouTube video under 2 minutes so the transcription is fast
- Have the URL in your clipboard before recording
- The "it's just a markdown file" moment is key — show it briefly

---

### Step 5: Ask User Question Tool (Screen Recording)
**Target: 4.5 minutes**

This is the most important demo. Take your time.

**What you do:**
1. Open Claude Code in a fresh session
2. Enter plan mode (Shift+Tab)
3. Paste the basic Peeps prompt
4. Let Claude generate a plan — pause to show it and point out assumptions
5. Paste the Ask User Question follow-up prompt
6. Answer 3 rounds of questions on camera
7. Show the final detailed plan
8. Briefly show the PRD you created from this plan

**Exact actions:**
```
# In Claude Code:
# 1. Shift+Tab to enter plan mode
# 2. Paste the basic Peeps prompt (see Prompts section above)
# 3. Wait for plan output
# 4. Paste the Ask User Question prompt (see Prompts section above)
# 5. Answer questions as they come
```

**What you say for each round:**

*Round 1 (big picture):*
> "See? It's asking about card layout, required fields, detail views, birthday display. These are things I wouldn't have specified. Let me answer..."

*Round 2 (interactions):*
> "Now it's more specific — search behavior, tag filtering, form style, delete confirmation. Each round gets more granular."

*Round 3 (technical):*
> "And now the technical stuff — data format, API design, error handling. By round three, it knows exactly what to build."

*After all rounds:*
> "Look at this plan compared to the first one. Night and day. Every decision is explicit. Nothing left to guess."

**Then show the PRD:**
> "I took this plan and broke it into six tasks in a PRD. Backend API, seed data, card grid, add/edit forms, detail view, search and filter. Each task has requirements and a test."

**How to fill dead air while Claude thinks:**
> "This is the part most people skip. They let Claude make every decision. But every assumption is a potential 'that's not what I wanted' moment later. Front-loading this saves you time, money, and frustration."

**Tips:**
- Genuinely think about your answers — your real reactions are more interesting than rehearsed ones
- If you don't know an answer, say it: "Honestly, I'm not sure. Let me think..."
- Don't skip rounds — the progression from general to specific is the whole point
- After 3 rounds, you can cut to the final plan to save time

---

### Step 6: Ralph Loop Transition (Face to Camera)
**Target: 1 minute**

**What you do:** Build excitement before the live demo.

> "So now we have a real plan. Six detailed tasks. A CLAUDE.md with our tech stack. Let's let Claude build it."

> "Quick explainer — a Ralph loop is a script that tells Claude to keep working until the plan is done. Build a feature, test it, move on. Fail a test, go back and fix it. Loop until everything's complete. Named after Ralph Wiggum, by the way."

> "The key — the Ralph loop is only as good as your plan. That's why we spent all that time planning. Let's see what happens."

---

### Step 7: Ralph Loop Live Demo (Screen Recording)
**Target: 5 minutes**

This is the payoff. Take time to show the result.

**What you do:**
1. Show the project directory is clean (just CLAUDE.md, prd.md, and the base scaffold)
2. Briefly scroll through prd.md one more time
3. Run the Ralph loop
4. Show Task 1 being picked up and built
5. Show files being created and the /data/peeps/ folder populating
6. Open a seed .md file to show the format
7. Time-lapse/speed up the middle tasks
8. Show it finishing
9. Start the backend + frontend
10. Open the browser and click around the app
11. Add a new person
12. Show the markdown file it created
13. Demo search/filter

**Exact commands:**
```bash
# Show clean project
ls

# Show the PRD
cat prd.md

# Run Ralph loop
./ralph.sh --agent claude --plan prd.md

# After completion — start the servers
# Terminal 1:
node server.js

# Terminal 2:
npm run dev

# Open browser to http://localhost:5173
```

**What you say during the loop:**

*Task 1 running:*
> "It picked up Task 1 — building the Express backend. It's creating the server, the API routes, the markdown parser."

*While Task 1 runs:*
> "What's happening here — it's building an Express server on port 3001 that reads and writes markdown files. Each person is a .md file with frontmatter — name, birthday, phone, email, tags — and freeform notes below. The cool part? Even after the app is built, Claude can create new people by just writing a markdown file."

*Task 2:*
> "Task 1 passed! Now it's creating seed data — five example people as markdown files."

*Show a seed file:*
> "Look at this. Frontmatter up top with structured data. Notes below. Clean and simple."

*Time-lapse (Tasks 3-6):*
> "I'm going to speed this up — but watch the tasks getting checked off. Card grid, add form, detail view, search. Each one built, tested, moved on."

> "This is what planning gets you. I hit enter and walked away. Claude is building frontend, backend, data layer, everything — from the PRD."

*After completion:*
> "Done. Six tasks. Let me run it."

*Showing the app:*
> "There it is. Peeps. Five people as cards. Names, birthdays, tags. This one says 'Birthday in 3 days.' Let me click it..."

> "Full detail view. Notes rendered from markdown. Edit, delete."

> "Let me add someone — [fill form] — and there they are. New card. New markdown file on disk."

> "Search — [type a name] — filters in real-time."

> "That entire app — built autonomously from a plan. I didn't write a single line of code."

**Tips:**
- The app reveal is the MOST IMPORTANT moment. Linger on it. Click around. Show it working.
- If something breaks, it's actually great content: "See? It failed the test. Watch — it goes back and fixes it."
- Have the terminal split so you can show the server running and the browser at the same time
- Consider a picture-in-picture layout (terminal + browser)

---

### Step 8: Wrap-up (Face to Camera)
**Target: 2 minutes**

**What you do:** Recap the four things, give bonus tips, CTA.

> "Four things. CLAUDE.md for persistent context. Skills for repetitive tasks. Ask User Question for better planning. Ralph loops for autonomous building."

> "Bonus tips. Watch your context window — past 50%, start a new session. And don't get overwhelmed by the ecosystem — MCPs, plugins, hooks, agent teams. These four things are the foundation. Everything else is a bonus."

> "Let me know in the comments what you're building with Claude Code. If you want me to go deeper on skills or Ralph loops, I'll make that video."

> "Hit subscribe. I'll see you in the next one."

**Tips:**
- Count on your fingers as you recap each point
- Don't rush — let each point land
- Smile at the end

---

## Timing Cheat Sheet

| Section | Target Duration | Running Total |
|---------|----------------|---------------|
| Hook | 0:30 | 0:30 |
| Core Problem | 1:30 | 2:00 |
| CLAUDE.md Demo | 3:00 | 5:00 |
| Skills Demo | 2:30 | 7:30 |
| Ask User Question Tool | 4:30 | 12:00 |
| Ralph Transition | 1:00 | 13:00 |
| Ralph Loop Live Demo | 5:00 | 18:00 |
| Wrap-up + CTA | 2:00 | 20:00 |
| **Total** | **~20 min** | |

---

## On-Camera Tips

### Energy & Pacing
- First 30 seconds = highest energy. This decides if people stay.
- Screen recording sections: talk while you type. Dead air kills retention.
- Speed up anything that takes more than 10 seconds of waiting (AI processing, npm install)
- Cut between face cam and screen — don't stay on screen recording for more than 3 minutes straight without a face cam break
- The Ask User Question section is long (4.5 min) — keep energy up by reacting genuinely to the questions

### Handling Errors Live
- If Claude gives an error: "See? This happens. Let me fix it." (Shows authenticity)
- If the Ralph loop fails a test: "This is actually perfect — watch what it does. It goes back and fixes it." (Turn bugs into a feature of the demo)
- If the final app has a styling issue: "Not bad for zero lines of code. We can fix this in 30 seconds." (Shows the iterative process)
- If something completely breaks: cut it out in editing and re-record that section

### Visual Moments to Capture (For Thumbnail / B-Roll)
- The Peeps app loaded in browser with cards displayed — this is your thumbnail candidate
- Your skills folder with 7 skills listed — shows you're a power user
- The moment Claude starts asking multiple-choice questions (Ask User Question) — "wow" moment
- Side-by-side of basic plan vs. detailed plan after interview
- The Ralph loop progress log with tasks being checked off
- The terminal + browser split showing the app running
- Opening a .md file that represents a person — the "oh that's how it stores data" moment
- Adding a new person and seeing the card appear in real-time

### Editing Notes
- Consider a quick flash of the finished Peeps app in the first 10 seconds (record after the demo, insert in post)
- Time-lapse the Ralph loop middle section (Tasks 3-5) with your voiceover
- Use a lower-third or text overlay when showing each of the 4 parts ("Part 1: CLAUDE.md", etc.)
- The Ask User Question section benefits from zooming in on the questions so viewers can read them
