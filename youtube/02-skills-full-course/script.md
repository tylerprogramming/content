# Script: Claude Code Skills - The Complete Course (Build One + Run It in Cowork)

**Target length:** 45-52 minutes
**Format:** Write-once-run-everywhere hook -> what a skill really is -> the ecosystem (skills vs MCP vs subagents vs plugins) -> full SKILL.md anatomy -> proof it is not a toy -> live build (/standup) -> the Cowork payoff -> best practices -> ONE CTA
**Energy:** Authoritative but warm. Teaching-paced in the anatomy sections, high energy on the build, the Cowork payoff, and the CTA.
**Voice rules:** Riff, do not read. Show actual commands and files. No em dashes. Answer on-camera questions on camera. ONE CTA.

---

## [0:00 - 0:25] Cold Open - Write Once, Run Everywhere

[SHOW: Three quick beats over ~8 seconds. Beat 1: terminal, type a custom slash command, real output lands. Beat 2: cut to the Claude Cowork desktop app, the SAME skill name appears and runs on a document. Beat 3: a single SKILL.md file open in the editor, glowing, sitting visually between the two. Lower-third text: "ONE FILE."]

> *(VO at 0:03)*
> This is one file. About 50 lines of plain English. I'm going to run it right here, in Claude Code, in the terminal. And then I'm going to run the exact same file over here, in Claude Cowork, on a document. Same file. Two completely different apps.

> *(at 0:14)*
> That file is called a skill. By the end of this video you'll understand them completely, you'll have built one from scratch with me, and you'll know how to make it run everywhere you use Claude. No SDK. No framework. Nothing to install. Let's get into it.

[NOTE: Energy HIGH. The "same file, two apps" visual is the entire hook. Let it land for 2 seconds before the VO drops. This is the screenshot moment of the whole video, plan the shot carefully.]

---

## [0:25 - 2:00] Why This Video Exists

[CAMERA: Face to camera, direct, confident]

> Quick framing so you know what you're getting and whether it's worth your next 45 minutes.

> There are a hundred skills videos on YouTube. Most of them have the same problem. They show you one flashy demo, it looks amazing, and then you go to build your own and you have no idea where to start. I call it the cooking-show problem. Looks incredible, you can't actually reproduce it.

> This is the opposite of that. This is the complete picture. I'm going to teach you what a skill actually is, the one thing everyone confuses it with, every part of the file that makes it work, and then we build one together, live, from an empty folder. And at the end I'll show you the thing almost nobody is showing yet: the same skill running in Claude Cowork, not just the terminal.

> My background, so you know I'm not guessing. I'm a full-time software engineer. I've built 43 of these skills. They run my entire content business on the side, between 4 and 5:30 PM on weekdays. Skills are the single highest-leverage thing in Claude Code, and most people are barely scratching the surface.

> Let's start with the question nobody actually answers clearly. What is a skill.

[NOTE: This is the trust-build. Medium energy, 7/10. Do not rush, but do not dwell. The "cooking-show problem" line is a keeper, deliver it with a little smile.]

---

## [2:00 - 5:30] Chapter 1 - What a Skill Actually Is

[SHOW: Face to camera, then cut to a finder/editor window showing ~/.claude/skills/ with a list of folders]

> Here's the definition, and it's simpler than people make it.

> A skill is a saved way of working with Claude. That's it. Instead of explaining what you want every single time, you write it down once, in a file, and Claude remembers it forever as a reusable procedure.

[SHOW: Open one skill folder, e.g. ~/.claude/skills/transcribe/, show SKILL.md]

> Mechanically, a skill is a folder with one required file in it, called SKILL.md. That file has two parts. A little bit of structured info at the top, called frontmatter, which is just a name and a description. And below that, plain English instructions telling Claude what to do.

> That is the whole thing. No code required. No SDK. No deployment. You drop the folder in the right place, and Claude can now do that task on command.

[SHOW: A simple visual or text overlay of the three "levels"]

> Now here's the part that makes skills genuinely clever, and it's worth understanding because it changes how you think about building them. It's called progressive disclosure. Three levels.

> Level one: when Claude starts up, it only reads the name and description of every skill you have. That's about a hundred tokens each. Tiny. So you can have a hundred skills installed and it costs almost nothing.

> Level two: when something you say matches a skill, Claude reads the full instructions. Only then.

> Level three: if that skill points to other files, or scripts, Claude only reads those when it actually needs them. And here's the kicker. If a skill runs a script, Claude runs it and only sees the output. The code itself never even enters the conversation.

> So you can bundle a skill with thousands of lines of reference material and scripts, and it costs you zero context until the moment it's used. That's the architecture. Lightweight until needed, then exactly as deep as it has to be.

[NOTE: This is foundational teaching, energy 6-7/10. Calm and clear. The progressive disclosure explanation is what separates this video from the shallow ones. Use a simple on-screen graphic for the 3 levels if possible, even a hand-drawn one.]

---

## [5:30 - 11:00] Chapter 2 - Skills vs MCP vs Subagents vs Plugins

[SHOW: Big on-screen text, five terms appearing one at a time: SKILL, MCP, SUBAGENT, PLUGIN, SLASH COMMAND]

> Okay. Before we go deeper, I have to clear up the single most confusing thing in this entire ecosystem, because if you don't get this, nothing else makes sense.

> People constantly mix up skills, MCP servers, subagents, and plugins. They are completely different things that work together. Let me give you the whole mental model in a few minutes, and you'll be ahead of ninety percent of people using this tool.

### Skills vs MCP (5:50 - 7:30)

[SHOW: Two columns. Left: "SKILL = know-how." Right: "MCP = access."]

> Start with the big one. Skills versus MCP.

> Here's the analogy that makes it click. Knowing how to write a professional email, the structure, the tone, when to follow up, that's a skill. It's know-how. It's procedure.

> Opening Gmail to actually send the email, that's a tool. That's MCP. It's access to something Claude can't do on its own.

> A skill teaches Claude HOW to do something the way you want it done. An MCP server gives Claude ACCESS to something it otherwise couldn't reach, like your database, your Gmail, a third-party API.

> And the best part, they compose. A skill can use MCP tools. You can write a skill that says "pull the last week of support tickets" using an MCP connection, "then summarize them this specific way" using the skill's instructions. Know-how plus access.

> One more practical difference. An MCP server can cost you fifty thousand tokens just to connect, because it loads every tool definition up front. A skill costs about a hundred tokens until you use it. That matters more than you'd think.

### Subagents and Plugins (7:30 - 9:30)

[SHOW: Add SUBAGENT and PLUGIN to the columns]

> Two more terms and then you've got the whole map.

> A subagent is a separate, isolated Claude session with its own context and its own tools. You use it when you want to hand off a big chunk of work without polluting your main conversation, or run several things in parallel. Think of it as a parallel worker you delegate to. A skill can actually spin one up.

> A plugin is just a package. It's how you bundle and share a collection of skills, commands, subagents, and MCP connections together, so someone else can install all of it at once. Skills are the contents. Plugins are the box you ship them in.

### The cheat sheet (9:30 - 11:00)

[SHOW: A clean summary table on screen]

> So here's your cheat sheet. Memorize this one and you're done.

> Procedural knowledge, how to do something? That's a skill.
> Connection to an external tool or data source? That's MCP.
> Heavy or parallel work you want isolated? That's a subagent.
> A bundle you want to share? That's a plugin.

> Skills are the know-how. MCP is the plumbing. Subagents are the parallel workers. Plugins are the packaging. And they all work together.

> Now that you've got the map, let's open up a real skill and look at every single part of it.

[NOTE: This chapter is the differentiator. Energy 7/10, a little faster, you are clarifying confusion the viewer has felt. The email analogy is the moment, slow down on it. The cheat sheet should be a clean graphic the viewer can pause and screenshot. That screenshot-ability is intentional, it drives shares.]

---

## [11:00 - 20:00] Chapter 3 - The Complete Anatomy of a Skill

[SHOW: Open a real, well-built SKILL.md in the editor. Use one of Tyler's own, like /yt-search or /content, something with rich frontmatter. Scroll to the top.]

> This is a real skill from my system. Let's go top to bottom and I'll explain every piece, because once you can read a skill, you can write one.

### The frontmatter (11:20 - 16:00)

[SHOW: Highlight the frontmatter block between the --- markers]

> Everything between these two sets of three dashes is the frontmatter. It's the configuration. Let me go field by field.

> **Name.** Lowercase, hyphens, that's it. Honestly the folder name is what becomes your slash command, so the name field is mostly a label. Keep it matching the folder and move on.

> **Description.** This is the most important line in the entire file, and I need you to really hear this. The description is how Claude decides when to use the skill automatically. When you type something, Claude reads all your skill descriptions and fuzzy-matches against them. So the description has to say two things: what the skill does, AND when to use it.

[SHOW: Show a good description vs a bad one, side by side]

> Bad description: "helps with PDFs." Too vague, it'll never fire reliably. Good description: "Extract text and tables from PDF files, fill forms, merge documents. Use when the user mentions PDFs, forms, or document extraction." See the difference? It lists the triggers. Write your descriptions in the third person, like you're describing the skill to someone else, and pack in the trigger words people would actually say.

> **Allowed-tools.** This is your pre-approval list. Whatever tools you put here, the skill can use without stopping to ask you for permission every time. So if your skill needs to run a date command and write a file, you list those. Important nuance: this does not restrict anything, it only pre-approves. It's about removing friction, not about security limits.

> **User-invocable.** True by default. If you set it to false, the skill won't show up in the slash menu, which you'd do for a skill that's pure background knowledge you want Claude to have but you'll never type yourself.

> **Disable-model-invocation.** The opposite control. Set this to true and Claude won't fire the skill automatically, only you can, by typing it. You'd use this for anything with a consequence. A deploy skill. A send-email skill. Something you never want triggered by accident.

> **Argument-hint and arguments.** This is how your skill takes input. Argument-hint is just the little reminder of what to pass. Arguments lets you name those inputs so you can use them inside the skill body. So you could type slash-fix-issue, then a number, and the skill knows that number is the issue to fix.

> **Model.** You can actually pin a skill to a specific model. If a skill needs heavy reasoning, pin it to Opus. If it's a quick formatting job, pin it to Haiku and it runs faster and cheaper. The skill overrides your session model just while it runs.

[NOTE: This is the meat of the education. Energy 6/10, teaching pace. Do NOT rush this. Highlight each field on screen as you say it. This is the section people will rewatch and timestamp. It's okay to be methodical here, the payoff sections come later.]

### The body (16:00 - 18:30)

[SHOW: Scroll below the frontmatter to the markdown instructions]

> Below the frontmatter is the body. This is just plain English, written as instructions to Claude. Numbered steps, the way you'd explain a process to a smart new hire who's never done this specific task before you.

> Two things make a body good. First, structure. Steps in order, clear sections. Second, and this is straight from Anthropic's own engineering team, the highest-value thing you can put in a skill is the gotchas. The stuff that's specific to your situation that Claude couldn't guess. "Always exclude test accounts." "Our fiscal year starts in February." "Never touch this file." That contextual knowledge is the whole reason the skill exists.

> There's a trap here. Don't write instructions for things Claude already does well by default. Anthropic put it perfectly: a skill that just restates what Claude would already do adds words without adding value. Only write down the stuff that's actually specific to you.

### Where skills live (18:30 - 20:00)

[SHOW: Two finder windows, ~/.claude/skills/ and a project's .claude/skills/]

> Last part of the anatomy: location, because where you put the folder decides where it works.

> Drop it in this folder in your home directory, tilde slash dot claude slash skills, and it works in every project, everywhere. That's a personal skill. Most of mine live here.

> Drop it inside a specific project, in dot claude slash skills, and it only works in that project, and it travels with the repo. So your whole team gets it when they clone. That's a project skill.

> And skills can come bundled inside a plugin, which is how you install someone else's. Those get a little namespace prefix so they never collide with yours.

> One genuinely great quality-of-life thing: you don't have to restart for edits anymore. Claude Code watches these folders. Add or change a skill and it picks it up live. The one exception is creating the very first skills folder mid-session, that one needs a restart.

[NOTE: Energy 6-7/10. The location explanation is practical, keep it concrete with real finder windows open. End this chapter by raising the energy, because the next chapter is proof and then we build.]

---

## [20:00 - 25:00] Chapter 4 - Proof This Is Not a Toy

[SHOW: Pull up the Anthropic blog post from June 3, 2026, "How we use skills," on screen. Scroll it live.]

> Before we build one, I want to kill the idea that this is a cute trick. Because that's the reaction a lot of people have. "Cool, a markdown file, neat."

> This is Anthropic's own engineering blog from June. The company that builds Claude. And they say they run hundreds of skills internally. Across their whole engineering org. Nine different categories, everything from API reference to CI/CD to incident runbooks.

[SHOW: Highlight the line about verification skills]

> And here's the line that reframed it for me. They said the skills that improved Claude's output the most weren't the impressive ones. They were the boring verification skills. The ones that check the work. That tells you something about where the real value is.

[SHOW: Cut to github.com/anthropics/skills, then scroll an awesome-claude-skills list]

> It's not just them. Anthropic open-sourced a pile of official skills, you can read them right here. And the community has built well over a thousand. There's a pack called superpowers that's basically a senior engineer's brain as a set of skills: test-driven development, systematic debugging, code review. There's a skill whose entire job is to build other skills.

> So this is not a toy. This is how serious teams are actually working now. Which means it's worth the next twenty minutes of building one with me. Let's do it.

[NOTE: Energy 7-8/10, building. This chapter is the credibility injection that earns the rest of the watch. Make sure the blog post and the GitHub repos are actually on screen, real receipts, not just talking. This is also a natural mid-roll ad point if monetizing.]

---

## [25:00 - 35:00] Chapter 5 - Live Build: /standup From Scratch

[SHOW: VS Code with an empty folder at ~/.claude/skills/standup/. Visibly empty.]

> Alright. Empty folder. We're building a skill called slash-standup. You type it, it asks what you worked on, and it generates a clean standup update: what you did, what you're doing next, and any blockers, and it saves it with today's date. Universally useful, devs and non-devs both do standups, and it's going to touch every concept we just learned.

> And quick note, this isn't a random example. A standup skill is literally one of the categories Anthropic uses internally. So we're building a real one.

### The frontmatter, live (26:00 - 28:30)

[SHOW: Create SKILL.md, type the frontmatter LIVE, narrating each line]

```yaml
---
name: standup
description: Generate a daily standup update with what I did, what I'm doing next, and blockers. Triggers on - standup, daily update, what did I do today, status update.
argument-hint: [optional notes]
allowed-tools: Read, Write, Bash(date:*), AskUserQuestion
user-invocable: true
---
```

> Name, standup, matches the folder. Description, and watch what I'm doing here, I'm listing the trigger phrases. Standup, daily update, what did I do today. Those are the words I'd actually say, so Claude will fire this when I say them.

> Argument-hint, optional notes, so I can pass a quick brain-dump if I want. Allowed-tools: I'm pre-approving Read, Write, the date command so it can get today's date, and AskUserQuestion so it can ask me what I did. User-invocable, true, so it shows up when I type slash.

### The body, live (28:30 - 31:30)

[SHOW: Below the frontmatter, type or paste the body]

```markdown
# Standup Generator

Generate a clean daily standup update and save it.

## What to Do

1. If the user didn't pass notes, ask them with AskUserQuestion: "What did you work on?" Offer quick options: "Shipped a feature", "Fixed bugs", "In meetings", plus Other.

2. Get today's date with `date +%Y-%m-%d`.

3. Build the standup in this format:
   - Title: Standup - <date>
   - **Yesterday / Done:** what they completed
   - **Today / Next:** what they're doing next
   - **Blockers:** anything in the way, or "None"

4. Save to `~/notes/standups/<date>-standup.md`.

5. Show the user the final standup and confirm the saved path.

## Rules

- Use today's real date from `date`, never hardcode it.
- Keep each section to 1-3 bullet points. Standups are short.
- If there are no blockers, write "None" - don't leave it empty.
- Never overwrite. If today's file exists, append -2, -3, and so on.
- No em dashes. Use plain hyphens.
```

> Plain English. Numbered steps. And notice the rules section at the bottom, because this is where I prevent the skill from doing something dumb later. Use the real date. Keep it short. Never overwrite my existing file. These rules are the difference between a skill that's reliable and one that surprises you.

### Restart and test (31:30 - 34:00)

[SHOW: Save the file. Because the skills folder already exists, it should hot-reload, but show typing the command.]

> Saved. Now I type the command.

```
/standup
```

[SHOW: Claude fires AskUserQuestion with the quick options. Pick "Shipped a feature" ON CAMERA.]

> And there it is. It hit the AskUserQuestion step and it's asking me what I worked on. I'll pick "Shipped a feature." This is the part I want you to actually see, the back and forth. I asked, it asked me back, I answer. That loop is the whole point.

[SHOW: Claude runs the rest, calls date, generates the file, confirms the path. Open the file.]

```markdown
# Standup - 2026-06-XX

**Done:** Shipped the new skill onboarding flow
**Next:** Wire up the Cowork demo
**Blockers:** None
```

> Today's date, pulled live. Three tight sections. Blockers says None, exactly like the rule said. That's a real, working skill, and we wrote it in about five minutes.

[SHOW: Run it once more with the same date to prove the no-overwrite rule appends -2]

> And the rule held. Second run got -2 instead of clobbering the first file. That's reliability you designed in.

### The aha (34:00 - 35:00)

[CAMERA: Face to camera, slow down]

> That's it. About fifty lines of plain English and a little bit of config at the top. No code. No SDK. No deployment. And now slash-standup is a permanent command in my Claude Code, forever.

> Every single one of my 43 skills works exactly like this one. Longer bodies, more tools, but the same structure. Once you've built one, the floodgates open. You stop asking "how do I automate this" and you start asking "what do I call the skill and what does the body say."

[NOTE: This is the core payoff of the build. Energy ramps from 7 during the build to 9 on the test (the money shot) and settles to 8 on the aha. The on-camera AskUserQuestion answer is mandatory, do not edit out the loop. If the test fails, fix off-camera and re-shoot from the restart only.]

---

## [35:00 - 42:00] Chapter 6 - The Payoff: The Same Skill in Claude Cowork

[SHOW: Quit the terminal view. Open the Claude Cowork desktop app.]

> Now here's the part I promised in the first ten seconds, and the part most people have not seen yet.

> Everything we just did was in Claude Code, in the terminal. That's the developer surface. But Anthropic shipped something this year called Claude Cowork. It went generally available in April, on Mac and Windows, on every paid plan. And Cowork is Claude for the rest of your work. It's a desktop app, not a terminal. It reads and writes your actual files, works with Excel and Word and PowerPoint, runs tasks for you. It's built for people who don't live in a terminal.

> Here's why that matters for today. Cowork uses the exact same skill system. The same SKILL.md format. So a skill I wrote for the terminal can run in this completely different app, for a completely different kind of work.

[SHOW: In Cowork, show the skill being available / invoked. NOTE TO TYLER: verify the exact invocation UI before filming, see filming guide. Demonstrate the standup skill, or an office-flavored skill, running on a real doc.]

> Watch. Same standup skill. I'm not in a terminal now, I'm in a desktop app that's looking at my actual work files. And it runs. Same instructions, same output format, totally different surface.

[SHOW: If demoing an office angle, show Cowork using a skill on an Excel or Word file]

> And this is where it gets powerful for teams. In Cowork, if you're an org owner, you can push approved skills out to your entire company. Everybody gets the same skill, the same quality output, without anyone rebuilding it. So one person writes the skill, the whole org runs it.

[CAMERA: Face to camera]

> So sit with that for a second. The file we wrote together, in an empty folder, five minutes ago, in plain English. That same file runs in Claude Code for developers, in Claude on the web, and in Claude Cowork for everybody else. Write it once. Run it everywhere. That is the whole reason skills are the most important thing to understand in this ecosystem right now.

[NOTE: THIS IS THE UNIQUE PAYOFF AND THE SCREENSHOT MOMENT. Energy 9/10. CRITICAL PRE-PRODUCTION: confirm exactly how skills surface and get invoked in the current Cowork build before filming, the precise UX was not fully documented as of research. Have a real custom skill loaded and visibly working in Cowork. If the standup skill is awkward in Cowork, use an office-document skill instead, but keep the "same SKILL.md" message. Do NOT fake this, Tyler's brand is verifiability.]

---

## [42:00 - 47:00] Chapter 7 - Making Skills Robust (Best Practices)

[SHOW: On-screen list builds as Tyler talks, one principle at a time]

> Okay, you can build one and you understand the whole picture. Let me give you the handful of principles that separate a skill that works once from a skill you trust for a year. These come straight from how Anthropic builds them and how I've built mine.

> **One. Keep the main file lean.** Your SKILL.md body should be short, ideally under a couple hundred lines. If you have a ton of reference detail, put it in separate files and let the skill pull them in only when needed. Remember progressive disclosure. Lean by default, deep on demand.

> **Two. The gotchas are the gold.** I said it earlier, it's worth repeating because it's the single best tip. The most valuable thing in your skill is the context Claude can't guess. Your weird edge cases. Your team's conventions. The thing that broke last time. Write those down.

> **Three. Ask when something's missing.** Don't let a skill error out because it's missing input. Use AskUserQuestion, like our standup skill did. A skill that asks a clarifying question feels ten times more solid than one that fails.

> **Four. Write to predictable paths.** Always save output to a consistent, documented location. This is what lets skills cooperate. My content skill knows where my YouTube skill puts files because they agree on the path. Predictable paths turn separate skills into a pipeline.

> **Five. Put hard rules at the bottom.** A rules section. Never overwrite. Always confirm before sending. Use real dates. These are guardrails, and they prevent the disasters.

> **Six, and this one's about safety.** Skills can run code and use your tools. So only install skills from sources you trust, and actually read a skill before you run it. If you grab one off the internet, open the file, see what it does. Treat it like you'd treat any script you're about to run on your machine.

[NOTE: Energy 7/10, practical and tight. This is the section that makes the video genuinely educational rather than just a demo. Each principle gets a clean on-screen label. Keep it moving, one principle every 40 seconds or so.]

---

## [47:00 - 50:00] CTA

[CAMERA: Direct to lens, energy up]

> So let's bring it home. You now understand what a skill is, how it's different from MCP and subagents and plugins, every part of the file, you watched us build slash-standup from nothing, and you saw it run in both Claude Code and Cowork. That's the complete picture. You're genuinely ahead of most people using this tool now.

> Here's what to do next. The fastest way to get good at this is to build a few and to read other people's. So I put together a free starter pack. It's got the slash-standup skill we just built, the actual SKILL.md, plus five more starter skills I'd recommend you build next, and links to the best community skill collections so you're not starting from a blank page.

> It's all free in my Skool community. Link is in the description, and I'm building a full Claude Code course in there, so if you join the waitlist you'll get first access and founding-member pricing when it opens.

> That's the one thing I'll ask. Grab the starter pack, build your first skill tonight, and come tell me what it does. I read every post.

> See you in the next one.

[SHOW: Quick callback montage mirroring the open: the one SKILL.md file -> running in the terminal -> running in Cowork -> the standup file appearing. Fast cuts, 1.5 seconds each, same energy as the cold open.]

---

## Production Notes

### Critical Pre-Production
- [ ] Delete `~/.claude/skills/standup/` if it exists - fresh build for authenticity
- [ ] Clear or move anything in `~/notes/standups/`
- [ ] **VERIFY the current Cowork skill-invocation UX** and have a real custom skill loaded and working in Cowork before filming Chapter 6. This is the riskiest segment, do a full dry run.
- [ ] Re-check SKILL.md frontmatter field names against the live docs the morning of recording (spec is evolving in 2026)
- [ ] Pull up the June 3, 2026 claude.com "How we use skills" blog post and github.com/anthropics/skills in browser tabs ready to show
- [ ] Have a rich, safe SKILL.md of your own ready to dissect in Chapter 3 (use /yt-search or /content, do NOT show any file with API keys)
- [ ] OBS scenes: Face Cam, Terminal (Claude Code), VS Code, Finder, Browser, Cowork desktop app

### Sensitive Content Check
- [ ] Never show `~/.claude/.env` or any API keys
- [ ] When dissecting a SKILL.md, pick a safe one
- [ ] When opening `~/notes/standups/` make sure no real/private notes are visible
- [ ] In Cowork, make sure no confidential documents are on screen

### Demo Continuity
- The standup skill should be the through-line: built in Chapter 5, then run again in Cowork in Chapter 6. Same skill, two surfaces. That continuity IS the payoff.

### Accuracy callouts (say these carefully)
- "Anthropic runs hundreds of skills internally" - from the June 3, 2026 blog, this is a real citation, show it.
- "Over a thousand community skills" and "dozens of tools adopted the standard" - directionally true but from community sources, say "over a thousand" and "dozens of tools," do not cite exact figures as hard fact.
- Cowork: "generally available in April 2026, Mac and Windows, all paid plans" - verified, safe to state.

### Energy Curve
| Segment | Energy | Notes |
|---|---|---|
| Cold open (one file, two apps) | 10/10 | The hook + screenshot moment |
| Why this video | 7/10 | Trust build |
| Ch1 What a skill is | 6/10 | Foundational, calm |
| Ch2 Ecosystem | 7/10 | Clarifying confusion, the email analogy lands |
| Ch3 Anatomy | 6/10 | Methodical teaching, the rewatch section |
| Ch4 Proof | 8/10 | Receipts, credibility |
| Ch5 Live build | 7 -> 9/10 | Build climbs, the test is the money shot |
| Ch6 Cowork payoff | 9/10 | The unique screenshot moment |
| Ch7 Best practices | 7/10 | Tight and practical |
| CTA | 10/10 | Get the click |

### Common Mistakes to Avoid
1. Don't read the script. Use it as a map and riff. Sounds 10x better.
2. Don't rush Chapter 3, the anatomy is the educational core people came for.
3. Don't fake the Cowork demo. If it's not ready, push the shoot, don't fake it.
4. Don't re-demo the content pipeline (yt-search/transcribe/yt) - that's 067's job. Reference, don't rebuild.
5. Answer the AskUserQuestion on camera. Show the human-AI loop.
6. No em dashes in the spoken script.
7. ONE CTA. Skool waitlist. Don't pile on.

### Chapters (paste into description)
- 0:00 One file, two apps (the demo)
- 0:25 Why this video exists
- 2:00 What a Claude Code skill actually is
- 5:30 Skills vs MCP vs subagents vs plugins
- 11:00 The complete anatomy of a SKILL.md
- 20:00 Proof: Anthropic runs hundreds of these
- 25:00 Live build: /standup from scratch
- 35:00 The payoff: the same skill in Claude Cowork
- 42:00 Making your skills robust (best practices)
- 47:00 Get the free starter pack
