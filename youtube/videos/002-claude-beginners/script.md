# Claude Code for Beginners — Full Script

---

## [0:00 - 0:45] Hook

[SCREEN: Terminal with Claude Code open, quick cuts of code being generated, tests passing, the finished Prompt Library app running in a browser]

> Everyone's talking about Claude Code but most people are using it wrong. They type a vague prompt, get messy output, and blame the model. "Claude sucks, it doesn't understand what I want." No. You suck at telling it what you want. There's a difference.

[SCREEN: Quick flash of the finished Prompt Library app — clean UI, prompts organized with tags, search bar working]

> In this video I'm giving you the exact crash course — from zero to building a real app — so you never waste tokens again. By the end of this, you'll know how to plan properly, build feature by feature, test everything, and eventually let Claude build entire apps for you autonomously. Let's get into it.

[NOTE: Hard cut, no transition animation. Keep energy high from frame one.]

---

## [0:45 - 2:30] The #1 Mistake: Bad Plans

[SCREEN: Tyler talking to camera]

> So here's the number one mistake I see beginners make with Claude Code. They open the terminal and they type something like: "Build me a web app for saving prompts." And then Claude goes off, generates a bunch of files, and the person looks at it and goes, "This is sort of what I wanted but it's not exactly what I wanted."

> Garbage in, garbage out. The models are incredible now. Like genuinely incredible. If your output sucks, it's because your input sucks. That's just the reality.

[SCREEN: Side-by-side comparison — vague prompt on left, detailed plan on right]

> Here's the thing people get wrong. They describe products, not features. They say "build me a prompt library" and expect Claude to read their mind about what that means. Does it have tags? Does it have folders? Is it local or cloud? What does the search do? Claude doesn't know any of that unless you tell it.

> I like to use the car analogy. If you walk up to someone and say "build me a car" — they don't know if you need a steering wheel, a radio, leather seats, four-wheel drive. They're just going to guess. And the guess is going to be wrong.

[SCREEN: Tyler talking to camera]

> So how do you actually create a great plan? Let me show you.

[NOTE: Quick transition — cut to screen recording]

---

## [2:30 - 7:00] Planning with AskUserQuestion Tool

[SCREEN: Terminal, opening Claude Code fresh]

> Alright, I'm in my terminal. I've got Claude Code open. First thing I'm going to do — and this is important — I'm going to hit Shift+Tab to go into plan mode. Plan mode tells Claude "don't write any code yet, just think."

[SCREEN: Show Shift+Tab toggle, mode indicator changes]

> Now I'm going to give it my initial prompt.

[SCREEN: Tyler types the prompt into Claude Code]

> I'm telling it: "I want to build an AI Prompt Library app — a local web app where I can save, organize, tag, and search my best AI prompts. Please help me create a plan, write it to prd.md."

[SCREEN: Claude generates a plan, writing to prd.md]

> Okay, so Claude just generated a plan. Let's look at it.

[SCREEN: Open prd.md, scroll through it]

> It's... fine. It's got the basic structure — some features listed, a rough tech stack suggestion. But look at this. It's surface-level. It says "tag system" but doesn't specify how tags work. It says "search functionality" but doesn't say whether that's full-text search, fuzzy matching, or just filtering by title. This is the kind of plan that leads to a mediocre app and three hours of back-and-forth fixing things.

> This is where most people stop. They take this plan and say "cool, build it." Don't do that.

[SCREEN: Tyler pastes a new prompt into Claude Code]

> Instead, I'm going to paste this prompt. Watch what happens. I'm telling Claude: "Read this plan file. Interview me in detail using the ask user question tool about technical implementation, UI/UX concerns, and trade-offs. Ask me one question at a time."

[SCREEN: Claude starts asking questions via ask user question]

> And now Claude is going to interrogate me. Watch.

[SCREEN: Show the first question from Claude — something like "What tech stack do you prefer for the frontend?"]

> It's asking me what tech stack I want. I'm going to say React with Vite because it's fast and I know it.

[SCREEN: Tyler answers, Claude asks next question]

> Now it's asking about storage. Do I want a database or local file storage? I'm going local with SQLite because I don't need a server for this. It's a personal tool.

[SCREEN: Tyler answers, Claude asks about categories vs tags]

> Categories or tags? Both. I want free-form tags and also a few fixed categories like "coding," "writing," "research."

[SCREEN: Show 3-4 more rapid-fire questions and answers — search behavior, UI layout preferences, import/export, etc.]

> See what's happening? It's asking me about search behavior — do I want fuzzy matching? Yes. Should search hit the prompt body or just titles? Both. What about the layout — cards or list view? Cards, with a preview of the first few lines.

[NOTE: Speed up the middle Q&A section slightly in editing, keep the first and last questions at normal speed so viewers understand the pattern]

> Now I know what you're thinking. "Tyler, this is annoying. It's asking me so many questions." Yes. It's supposed to be annoying. The more questions it asks, the better your plan gets. Every question Claude asks is a decision you would have had to make later anyway — except later, Claude would have guessed wrong and you'd be rewriting code.

[SCREEN: Claude finishes questions, updates the PRD]

> Alright, it's done asking questions and now it's updating the PRD with everything we discussed. Let's look at the before and after.

[SCREEN: Split screen — original basic PRD on left, enriched PRD on right, scrolling through both]

> Look at this. The original plan was maybe thirty lines. The new one is detailed, specific, with exact feature specs, data models, UI descriptions, edge cases. Night and day difference. This is a plan you can actually build from.

> Quick tip here — if Claude asks you a technical question and you don't know the answer, that's totally fine. Copy the question, open ChatGPT or Claude chat in a browser, and ask it there. Get your answer, come back, paste it in. There's no rule that says you have to know everything off the top of your head.

[SCREEN: Tyler talking to camera briefly]

> Alright, we've got a killer plan. Now let's actually build this thing.

---

## [7:00 - 10:00] Build Feature-by-Feature

[SCREEN: Tyler talking to camera]

> Okay, this is where I need to be real with you for a second. I know a lot of you have seen the viral videos of people using autonomous loops — Ralph, agentic workflows, whatever you want to call it — where Claude just builds an entire app by itself. And you want to skip straight to that.

> Don't. If you haven't built something manually with Claude Code, you have no business using Ralph yet. You need to get your reps in first. You need to understand what Claude is doing, how it structures code, how to catch mistakes. Once you have that foundation, then you graduate to autonomous mode. But not yet.

> So here's how we build. Feature by feature. One at a time.

[SCREEN: Back to terminal, Claude Code open with the PRD visible]

> I'm telling Claude: "Let's build feature one — prompt storage with full CRUD operations. Create, read, update, delete. Follow the PRD."

[SCREEN: Claude starts generating files — backend routes, database schema, basic UI components]

> Watch it work. It's setting up the SQLite database, creating the schema, building out the API routes, wiring up the frontend components. And because our plan is detailed, it knows exactly what fields a prompt needs — title, body, category, tags, created date, last used date.

[SCREEN: App running in browser, showing basic CRUD working]

> Alright, feature one is running. I can create a prompt, edit it, delete it. Basic stuff but it works. Now here's the critical step most people skip.

[SCREEN: Tyler types in Claude Code]

> I'm telling Claude: "Write tests for the prompt CRUD functionality."

[SCREEN: Claude writes tests, runs them, they pass]

> Tests pass. This matters. Every feature gets a test before we move on. If you skip this, you're building on a shaky foundation and everything breaks later.

> Now feature two. I'm telling Claude: "Build the tagging and category system per the PRD."

[SCREEN: Claude builds tagging — show it working quickly, then tests passing]

> Tags are working. I can add multiple tags to a prompt, filter by them, remove them. Tests pass. Moving on.

> Feature three — search.

[SCREEN: Claude builds search, quick demo of fuzzy search working, tests pass]

> Full-text search with fuzzy matching. I type "react" and it finds prompts that mention React anywhere in the title or body. Tests pass.

[SCREEN: Show the app running with all three features working together]

> Look at this. We've got a real, working app. Prompts with tags, categories, search — all tested, all functional. And we built it methodically, one feature at a time.

> One more thing. Commit early, commit often. After every feature that works, commit your code. Before you prompt Claude to fix anything, before you try adding the next feature — commit what works. If Claude breaks something in the next step, you can always roll back. I've seen people lose hours of progress because they didn't commit and Claude overwrote something that was working. Don't be that person.

[NOTE: Show a quick terminal flash of `git add . && git commit -m "feat: add search functionality"` to reinforce the point]

---

## [10:00 - 11:30] CLAUDE.md and Skills

[SCREEN: Tyler talking to camera]

> Alright, quick detour. Once you're comfortable with the basics, there are two things that level you up significantly. I'm not going deep on either of these — I have dedicated videos on both, links in the description — but you should know they exist.

> First: CLAUDE dot md. This is a markdown file that sits in your project root and Claude reads it at the start of every session. Think of it like onboarding a new engineer. You put your tech stack, your project structure, coding conventions, anything Claude needs to know about your project.

[SCREEN: Show a quick example CLAUDE.md file]

> Something like this. "This project uses React with Vite, SQLite for storage, tests are in the tests directory, use TypeScript, follow this naming convention." Now every time Claude starts a session, it already knows the rules. No more explaining the same stuff over and over.

> Second: Skills. These are custom slash commands that automate repetitive workflows. I use them constantly. I've got a skill that plans entire videos for me, one that transcribes YouTube videos, one that does TikTok research. They're like saved macros for Claude Code.

> Again, not going deep here. The point is — these tools exist. Learn the basics first, then layer these on top when you're ready. Links are in the description.

---

## [11:30 - 15:00] Ralph Loops — Autonomous Building

[SCREEN: Tyler talking to camera, slightly more intense energy]

> Okay. Now that you understand manual building, THIS is where it gets crazy. This is the thing that makes Claude Code different from every other AI coding tool. Autonomous loops. I call mine Ralph.

> Here's the concept. You give Claude a detailed PRD — like the one we just built. The PRD has a task list. Claude reads task one, builds it, writes a test for it, logs its progress to a file, then moves on to task two. It repeats this cycle until every task is done. No human in the loop. You can literally walk away, get coffee, come back, and your app is built.

[SCREEN: Show the PRD with a numbered task list]

> But here's the catch, and I cannot stress this enough — it is only as good as your plan. If your plan sucks, you're just donating money to Anthropic. The tokens are burning, Claude is building, but it's building the wrong thing. That's why we spent all that time on planning earlier. This is where it pays off.

[SCREEN: Terminal, setting up the Ralph loop]

> Let me show you. I'm going to run a Ralph loop on our Prompt Library app. In practice, you'd do this from scratch with the PRD, but I want you to see how it works.

[SCREEN: Claude picks up the first task from the PRD, starts building]

> Watch. It's reading the task list. It picks up the first task, starts building. You can see it creating files, writing code, running tests.

[SCREEN: Time-lapse of Claude working through multiple tasks — show progress.txt being updated]

> And it's logging everything to progress dot txt. Every task it completes gets checked off. Every test result gets recorded. So when you come back, you can see exactly what happened.

[SCREEN: Claude moves through tasks autonomously — show 2-3 task transitions]

> Look at it go. Task one done, moving to task two. Building the component, writing the test, test passes, logging progress. Task three. Same thing. It's just cranking through the list.

> Now, does it work perfectly every time? No. Sometimes it gets stuck. Sometimes a test fails and it needs to debug. But here's the thing — because our plan is detailed and each task is specific, it recovers most of the time on its own. When it can't, it tells you in the progress log and you can jump in to help.

[SCREEN: Show the finished app running, built entirely by the Ralph loop]

> And there it is. A fully functional Prompt Library app, built autonomously. Working CRUD, tags, categories, search, all tested. I was sitting here watching for the video, but normally? I'd be doing something else entirely.

[SCREEN: Tyler talking to camera]

> This is why the planning phase matters so much. Five minutes of extra planning saves you an hour of debugging later. And when you're running autonomous loops, the plan is literally the only thing between you and a working app or a mess of broken code.

---

## [15:00 - 17:00] Context Management and Tips

[SCREEN: Tyler talking to camera, slightly more relaxed pace]

> Before we wrap up, let me give you some tips that took me way too long to figure out.

> Tip number one: watch your context usage. Claude Code has a context window, and as your conversation gets longer, it starts forgetting stuff from earlier. Once you hit about forty to fifty percent context usage, start a new session. You can use the compact command or just start fresh. A new Claude session with a good CLAUDE dot md file is better than a bloated session where Claude is losing track of your project.

[SCREEN: Show context usage indicator in Claude Code]

> Tip number two: don't obsess over MCPs, plugins, and custom tools when you're starting out. I see beginners spending three hours configuring MCP servers before they've even built anything. Your plan matters ten times more than your tool setup. Get good at planning and prompting first. Add the fancy stuff later.

> Tip number three: use plan mode. Shift plus Tab. Before you write any code, explore the problem, make a plan, then code, then commit. Explore, plan, code, commit. That's the rhythm. If you jump straight to coding, you're going to waste time and tokens going in circles.

[SCREEN: Quick visual showing the cycle: Explore -> Plan -> Code -> Commit]

> Tip number four, and this one is more of a mindset shift: treat Claude like a senior engineer, not a magic genie. You don't say "make it work." You say "implement the search component using this specific approach, handle these edge cases, and write tests that cover these scenarios." Clear, firm, specific. The more you communicate like you're talking to a real engineer, the better your results.

> And honestly, that applies to every AI tool, not just Claude Code. Specificity wins. Always.

---

## [17:00 - 18:00] Outro and CTA

[SCREEN: Tyler talking to camera]

> Alright, let's recap the workflow. Step one: build a great plan. Use the AskUserQuestion technique to force Claude to interview you until the plan is bulletproof. Step two: build feature by feature. One feature at a time, test each one, commit before moving on. Step three: once you're comfortable building manually, graduate to autonomous Ralph loops and let Claude build entire apps for you.

> That's it. That's the system. It's not complicated but it works ridiculously well when you actually follow it.

> If this video helped you, drop a like and subscribe. I make videos on Claude Code, AI tools, and practical workflows like this every week. If you want the deep dive on CLAUDE dot md, skills, or Ralph loops, those videos are linked in the description.

> And if you build something cool with Claude Code after watching this, leave a comment. I actually read all of them and I want to see what you're making.

> I'll see you in the next one.

[SCREEN: End screen with subscribe button, related video cards]

[NOTE: Total spoken word count is approximately 2,700 words. At 150 wpm this lands around 18 minutes. Pacing should feel fast but not rushed — let the screen recordings breathe where needed.]
