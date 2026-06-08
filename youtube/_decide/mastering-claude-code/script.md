# Video Script: How I Actually Use Claude Code (Full Workflow)

---

## [0:00 - 0:30] Hook

> Most people use Claude Code like a chatbot. They type a vague prompt, get mediocre code, and blame the model.

> But here's the thing — the model isn't the problem. Your workflow is.

> Today I'm going to show you my exact Claude Code setup — the CLAUDE.md file, the custom skills, the planning workflow — and then I'm going to build a full app live on camera using a Ralph loop. No editing tricks. You're going to watch it go from a plan to a working app.

[SHOW: Face to camera, quick energy]
[NOTE: Keep this tight — 30 seconds max. The "build it live" promise is what keeps people watching.]

---

## [0:30 - 2:00] The Core Problem

> Here's what most people do. They open Claude Code, type something like "build me an app that tracks my contacts," and then get frustrated when the output isn't what they wanted. The styling is off. Features are missing. It made weird decisions about the database.

> The issue is simple — garbage in, garbage out. The models in 2026 are insanely good. Opus 4.6 just came out. If you're getting bad code, it's because you gave bad instructions. And I don't mean your prompt needs to be longer. I mean your entire workflow needs structure.

> There are four things that separate people who get great results from people who don't. CLAUDE.md files, custom skills, proper planning with the Ask User Question tool, and Ralph loops for autonomous building. I'm going to show you all four. And by the end, we'll have a working app called Peeps — a local app that tracks people in your life, their birthdays, their info — built entirely by Claude Code from a plan.

> Let's get into it.

[SHOW: Face to camera. Maybe quick B-roll flash of the finished Peeps app to tease the payoff]
[NOTE: This sets up the 4-part structure AND the Peeps app as the throughline. People now know what they're getting.]

---

## [2:00 - 5:00] Part 1: CLAUDE.md — Your Project Brain

> The first thing you need is a CLAUDE.md file. This is a markdown file that Claude reads at the start of every single conversation. It's how you give Claude persistent context about your project — your tech stack, your folder structure, your rules.

> Without this, every time you start a new session, Claude is starting from zero. It doesn't know you use React. It doesn't know you're on Tailwind v3. It doesn't know your project conventions. You'd have to re-explain all of that every time. CLAUDE.md fixes that.

> Let me show you mine.

[SHOW: Open terminal, navigate to ~/yt-ralph-project, open CLAUDE.md]

> So here's a real CLAUDE.md I use. Notice — it starts with the tech stack. React 18, Vite, TypeScript, Tailwind CSS v3, shadcn/ui. This tells Claude exactly what tools we're working with.

> Then there's this critical section — see this? "Do NOT upgrade to Tailwind v4." This is the kind of thing that saves you hours. Without this, Claude might try to "help" by upgrading your dependencies. With this, it knows the boundary.

[SHOW: Scroll through the CLAUDE.md, pause on the Tailwind warning section]

> Then you've got the project structure — where components live, where utilities are. And down here — development workflows. The exact commands to install, run dev, build for production. Claude can read these and use them.

> Now there's three levels of CLAUDE.md. You can have a global one at ~/.claude/CLAUDE.md that applies to everything. Then a project-level one in your repo root. And even directory-level ones for monorepos.

> Here's my global one.

[SHOW: Open ~/.claude/CLAUDE.md, scroll through briefly]

> This has my personal preferences that apply to every project. My custom skills, my YouTube workflow stuff, general rules.

> The way I think about it — your CLAUDE.md should answer three questions. What is this project? Why does it exist? And how should Claude work on it? If you cover those three, you're ahead of 90% of people.

> And if you're starting fresh — you can run /init inside Claude Code and it'll generate one for you based on your project structure.

[SHOW: Open a project folder, run /init, show the generated CLAUDE.md]

> It scans your package.json, your folder layout, figures out the stack, and gives you a starter file. Then you refine it from there.

[NOTE: Spend real time on this section. Show the actual files. Let people read the key parts. This is foundational.]

---

## [5:00 - 7:30] Part 2: Custom Skills

> The second thing that levels up your Claude Code workflow is skills. Skills are custom capabilities you give to Claude. You define what the skill does in a markdown file, and Claude can invoke it whenever the task matches.

> Think of them like saved workflows. Instead of typing the same five-paragraph prompt every time you want to do something, you package it as a skill and just call it.

> I have seven custom skills set up. Let me show you.

[SHOW: Open terminal, show ~/.claude/skills/ directory listing]

> I've got /transcribe — that downloads YouTube audio and transcribes it with Whisper. /yt — that does full video planning with web research, title generation, script writing. /save-idea — saves video ideas to a tracker. /journal — daily journal entries. /resize — batch image resizing. /rmbg — background removal. /prd — generates product requirement documents.

> These are things I do all the time. Instead of re-explaining the process each time, I just call the skill.

> Let me show you one working. I'll transcribe a YouTube video right now.

[SHOW: Open Claude Code, type "/transcribe" and paste a short YouTube URL]

> I type /transcribe, paste the URL, and watch. It downloads the audio using yt-dlp, sends it to OpenAI Whisper, and saves a timestamped transcript.

[SHOW: Skill running — downloading, transcribing, saving]

> And there it is. Full transcript with timestamps, saved to my scripts folder. That whole process — download, transcribe, save — happened in about 30 seconds because I packaged it as a skill.

[SHOW: Open the transcript file, scroll through briefly]

> Now let me show you what a skill actually looks like under the hood.

[SHOW: Open one of the skill markdown files]

> It's just a markdown file. Plain English instructions. "Download the audio using yt-dlp. Send it to Whisper. Save the transcript to this folder." Claude reads this and follows the steps. You don't need to be a developer to write these.

> The rule of thumb — if you find yourself typing the same prompt more than twice, make it a skill. It'll save you so much time.

[NOTE: The live demo of /transcribe is the money shot here. Make sure it works before recording. Have a SHORT video URL ready — under 2 minutes.]

---

## [7:30 - 12:00] Part 3: The Ask User Question Tool

> Okay, this is the part I'm most excited about. I actually just learned about this tool recently and it completely changed how I approach planning.

> So Claude Code has this built-in tool called Ask User Question. Most people don't even know it exists. What it does is — instead of Claude just generating a plan for you and making a bunch of assumptions, it stops and interviews you first. It asks you detailed questions about what you actually want.

> Let me show you why this is a big deal. First, I'll show you the normal way people plan.

[SHOW: Open Claude Code in a fresh session, enter plan mode with Shift+Tab]

> I'm going to plan the app we're building today — Peeps. It's a local app for keeping track of people — birthdays, contact info, notes. Let me just ask Claude the basic way.

[SHOW: Type the prompt]

```
I want to build a local fullstack app called Peeps that tracks people's birthdays, contact info, and notes. It stores each person as a markdown file and displays them in a clean UI with cards. I'm using React, Vite, TypeScript, shadcn/ui, and Tailwind CSS v3.
```

> Let's see what it comes up with.

[SHOW: Let Claude generate a basic plan. Wait for it.]

> Okay, so it gave us a plan. It's... fine. It's got some features, a rough structure. But look at all the things it decided for us. How are the cards laid out? What fields does each person have? Is there search? Is there filtering? What happens when you click a card? It just assumed all of that.

> Now watch what happens when I invoke the Ask User Question tool.

[SHOW: Type the follow-up prompt]

```
Read the plan you just created. Now interview me in detail using the ask user question tool about technical implementation, UI/UX decisions, data structure, and trade-offs. Don't start building until you've asked me at least 3 rounds of questions.
```

> And now look.

[SHOW: Claude starts presenting multiple-choice questions]

> See this? Round one. It's asking me — how should the cards be laid out? What fields are required versus optional? Do I want a detail view or inline expansion? How should birthdays be displayed?

> These are decisions I wouldn't have thought to specify up front. Let me answer these.

[SHOW: Answer round 1 questions thoughtfully, talking through your choices]

> I want a responsive grid — one column on mobile, three on desktop. Name and birthday are required, everything else is optional. I want a detail panel when you click a card. And yeah, show me upcoming birthdays.

[SHOW: Submit answers, wait for round 2]

> Round two. Now it's getting more specific. How should search work? Do I want tag-based filtering? What about the add/edit forms — dialog or separate page? How should delete work — immediate or with confirmation?

> See how each round gets more granular? The first round was big-picture. Now it's asking about specific interactions.

[SHOW: Answer round 2]

> And round three — now it's asking about data format, the markdown frontmatter structure, how to handle the API, error states.

[SHOW: Answer round 3]

> By the time we're done, look at this plan compared to the first one.

[SHOW: Scroll through the detailed plan. Maybe split-screen or side-by-side comparison if possible in editing]

> Night and day. The first plan was a rough sketch. This plan is a blueprint. It knows exactly what fields each person has, how the UI works, what happens on every interaction. This is what Claude needs to build something you actually want.

> And here's the thing that makes this so practical — you save money. Because you're not going back and forth after the fact saying "no, I wanted it this way." You're not burning tokens on revisions. You planned it right the first time.

> Now, I took this plan and turned it into a proper PRD — a product requirements document — that breaks everything into tasks. Let me show you that.

[SHOW: Open the prd.md file for Peeps]

> Six tasks. Backend API server, seed data, the card grid UI, add and edit forms, detail view with delete, and search and filter. Each task has specific requirements, and each one has a test to verify it works.

> This is what we're going to feed to the Ralph loop.

[NOTE: This is the longest section but also the most important. Take your time. Show the contrast between basic plan and interview plan. Let people see the questions. Your genuine reactions to discovering this tool are what make it authentic.]

---

## [12:00 - 12:30] Transition to Ralph Loop

> So now we have a real plan. A PRD with six detailed tasks. A CLAUDE.md that tells Claude our tech stack and rules. This is the setup. Now let's let Claude build it.

[SHOW: Face to camera, building excitement]

> I'm going to run a Ralph loop — which means Claude is going to work through every single task in this PRD autonomously. It builds a feature, tests it, moves to the next one. And it doesn't stop until it's done. Let's see what happens.

---

## [12:30 - 13:00] What is a Ralph Loop?

> Quick explainer for anyone who hasn't heard of this. A Ralph loop — named after Ralph Wiggum from The Simpsons, by the way — is basically a script that tells Claude Code to keep working until a plan is complete.

> It reads your PRD, picks up the first task, builds it, writes a test. If the test passes, it checks off that task and moves to the next. If the test fails, it goes back and fixes it. It loops until everything is done.

> The key thing to understand is — the Ralph loop is only as good as your plan. If your plan is vague, Ralph builds vague features. If your plan is detailed — like what we just created with the Ask User Question tool — Ralph knows exactly what to build.

[SHOW: Face to camera or simple diagram/graphic]

---

## [13:00 - 18:00] Part 4: Ralph Loop Live Demo — Building Peeps

> Alright, let's do this. I'm in the project directory. I've got my prd.md with six tasks. I've got my CLAUDE.md with the tech stack. Let's run the loop.

[SHOW: Terminal, show the project directory is clean/fresh]

> Let me quickly show you the PRD one more time so you know what we're building.

[SHOW: Open prd.md, quickly scroll through tasks — don't read every line, just hit the highlights]

> Six tasks. API server that reads and writes markdown files. Seed data so we have something to display. Card grid UI. Add and edit forms. Detail view with delete. Search and filter. Each one has a test.

> Here we go.

[SHOW: Run the Ralph loop command]

```
./ralph.sh --agent claude --plan prd.md
```

> And it's running. You can see it picked up Task 1 — setting up the Express backend. It's creating the server file, adding the endpoints, setting up the markdown file parsing.

[SHOW: Terminal output showing the loop working on Task 1]

> While it's working, let me explain what's happening. It's building an Express server on port 3001. This server reads and writes markdown files from a /data/peeps/ directory. Each person is a single .md file with frontmatter for structured data — name, birthday, phone, email, tags — and then a freeform notes section below.

> The cool thing about storing data as markdown files is Claude Code can read and edit these directly. So even after the app is built, you can ask Claude to add a person and it just creates a new markdown file.

[SHOW: Loop continuing, maybe switching to show files being created]

> Oh look — it finished Task 1 and the test passed. Now it's moving to Task 2, the seed data. It's creating five example people as markdown files.

[SHOW: Open the /data/peeps/ directory, show .md files appearing]

> Let me open one of these.

[SHOW: Open a seed data .md file, show the frontmatter and notes]

> See? Frontmatter with name, birthday, phone, email, tags. And below that, freeform notes. Clean and simple.

[SHOW: Loop continuing through tasks. Time-lapse / speed up Tasks 3-5 in editing]

> I'm going to speed this up — but you can see it's working through the UI tasks now. Building the card grid, the add form, the detail view. Each time it finishes a task, it tests it, and moves on.

[NOTE: Talk over the time-lapse. Don't go silent.]

> This is the part that blows my mind every time. I wrote a plan, hit enter, and walked away. Claude is building an entire app — frontend, backend, data layer, UI components — all from the PRD we created.

> And because we used the Ask User Question tool to plan, it knows exactly how the cards should be laid out, what fields to include, how the forms should work. No guessing.

[SHOW: Loop finishing up the final tasks]

> And... it's done. Six tasks complete. Let me run it.

[SHOW: Start the Express backend and Vite dev server]

```
# Terminal 1
node server.js

# Terminal 2
npm run dev
```

> Let me open the browser.

[SHOW: Open http://localhost:5173 — the Peeps app should load with seed data cards]

> There it is. Peeps. Five people showing as cards. I can see their names, birthdays, tags. Look — this one says "Birthday in 3 days" because that's how we planned it.

> Let me click on one.

[SHOW: Click a card, show the detail view]

> Full detail view. All the info, the notes rendered from markdown. Edit button, delete button.

> Let me add someone new.

[SHOW: Click "+ Add Person," fill out the form, submit]

> And there they are in the grid. Let me check — yep, new markdown file in the data folder.

[SHOW: Show the new .md file on disk]

> Let me try search.

[SHOW: Type in the search bar, show filtering in real-time]

> That entire app — backend, frontend, data layer, search, CRUD — was built autonomously from a plan. I didn't write a single line of code.

[NOTE: THIS IS THE PAYOFF. The whole video builds to this moment. Linger on the working app. Click around. Show it off. This is what the reference video was missing — a finished product.]

---

## [18:00 - 20:00] Wrap-up, Tips, & CTA

> So let's recap. Four things that will completely change how you use Claude Code.

[SHOW: Face to camera]

> Number one — set up your CLAUDE.md. Give Claude persistent context about your project, your stack, your rules. Think of it as onboarding docs for an AI teammate. Run /init to get started, then refine it.

> Number two — build custom skills for tasks you repeat. If you do something more than twice, package it as a skill. It's just a markdown file with instructions. Takes five minutes to set up, saves you hours.

> Number three — use the Ask User Question tool when planning. This is the biggest unlock. Don't let Claude make assumptions about your app. Make it interview you first. Your plan should be so detailed that there's nothing left to guess.

> Number four — Ralph loops. Once your plan is solid, let Claude build autonomously. Feature by feature, test by test. You just saw it build a full app in minutes.

> A couple bonus tips before I go. Watch your context window. Claude has a 200k token limit, but once you pass 50% in a single session, quality starts to drop. Start a new session when you notice things slipping.

> And don't get overwhelmed by the ecosystem. MCPs, plugins, hooks, agent teams — there's a lot. But these four things are the foundation. Get these right first. Everything else is a bonus.

> If you want to see me go deeper on any of these — skills, Ralph loops, CLAUDE.md setup — let me know in the comments. I read all of them.

> If you found this helpful, hit subscribe. I'll see you in the next one.

[SHOW: Face to camera, clean ending]
[NOTE: Don't rush this. Let the recap land. Smile at the end.]
