# Script: Claude Code Skills - The Complete Course (Build 3 + Run One in Cowork)

**Target length:** 45-52 minutes
**Format:** Write-once-run-everywhere hook -> what a skill is -> skills vs MCP vs plugins -> tight anatomy -> proof -> build THREE skills (two methods) -> real plugins -> the Cowork payoff -> best practices -> ONE CTA
**Energy:** Authoritative but warm. Teaching-paced in anatomy, high energy on the builds, the plugins, the Cowork payoff, and the CTA.
**Voice rules:** Riff, do not read. Show actual commands and files. No em dashes. Answer on-camera questions on camera. ONE CTA.

---

## [0:00 - 0:25] Cold Open - Write Once, Run Everywhere

[SHOW: Three quick beats over ~8 seconds. Beat 1: terminal, type a custom slash command, real output lands. Beat 2: cut to the Claude Cowork desktop app, the SAME skill name runs on a document. Beat 3: a single SKILL.md file open in the editor, glowing, sitting visually between the two. Lower-third: "ONE FILE."]

> *(VO at 0:03)*
> This is one file. About 50 lines of plain English. I'm going to run it right here, in Claude Code, in the terminal. Then I'm going to run the exact same file over here, in Claude Cowork, on a document. Same file. Two completely different apps.

> *(at 0:14)*
> That file is called a skill. By the end of this video you'll understand them completely, you'll have watched me build three from scratch, and you'll know how to make one run everywhere you use Claude. No SDK. No framework. Nothing to install. Let's get into it.

[NOTE: Energy HIGH. The "same file, two apps" visual is the entire hook. Let it land 2 seconds before the VO. This is the thumbnail/screenshot moment of the whole video.]

---

## [0:25 - 1:20] Why This Video Exists

[CAMERA: Face to camera, direct, warm]

> Let me be honest with you. AI is moving so fast that even I struggle to keep up, and this is literally my job. So if you feel like everyone else gets this stuff and you're the only one who doesn't, you're not. It's overwhelming for everybody. Here's my promise: I'm going to make skills genuinely simple, step by step, even if you've never written a line of code in your life.

> Most skills videos show you one flashy demo you can't actually reproduce. This is the opposite. We'll cover what a skill really is, the one thing everyone confuses it with, then I build three of them live, and I show you the same skill running in Claude Cowork. I'm a full-time software engineer, I've built dozens of these that run my whole content business on the side, so I've already made the mistakes for you.

> Let's start with the question nobody answers clearly. What is a skill.

[NOTE: Tightened to ~45-55 sec (was ~2 min). Keeps the empathy hook (relatable open from the proven Eliot Prince "Clearly Explained" approach), the promise, the contrast, a one-line credential, and the plan - just compressed. Warm, a touch vulnerable on "even I struggle," then confident. Don't pad it back out.]

---

## [2:00 - 5:00] Chapter 1 - What a Skill Actually Is

[SHOW: Face to camera, then a finder/editor window showing ~/.claude/skills/ with a list of folders]

> Here's the definition, simpler than people make it.

> A skill is a saved way of working with Claude. Instead of explaining what you want every single time, you write it down once, in a file, and Claude reuses it forever as a procedure.

[SHOW: Open one skill folder, e.g. ~/.claude/skills/transcribe/, show SKILL.md]

> Mechanically, a skill is a folder with one required file: SKILL.md. That file has two parts. A little structured info at the top, the frontmatter, basically a name and a description. And below it, plain English instructions telling Claude what to do. Drop the folder in the right place and Claude can do that task on command.

[SHOW: Simple on-screen "3 levels" graphic]

> Now the part that makes skills genuinely clever: progressive disclosure. Three levels.

> Level one: at startup, Claude only reads the name and description of each skill. Roughly a hundred tokens each. So you can have a hundred skills installed and it costs almost nothing.

> Level two: when something you say matches a skill, Claude reads the full instructions. Only then.

> Level three: if that skill points to other files or scripts, Claude only opens those when it needs them. And here's the kicker, and remember this for later: if a skill bundles a script, Claude runs the script and only sees the output. The code itself never enters the conversation.

> So you can bundle a skill with thousands of lines of reference material and scripts and it costs zero context until the moment it's used. Lightweight until needed, then exactly as deep as it has to be.

[NOTE: Foundational, 6-7/10. The progressive disclosure bit separates this from shallow videos. The "bundles a script, sees only the output" line sets up the skill-vs-tool beat in Ch2, plant it clearly.]

---

## [5:00 - 9:30] Chapter 2 - Skills vs MCP vs Plugins

[SHOW: On-screen text, three terms appearing one at a time: SKILL, MCP, PLUGIN]

> Before we go deeper, I have to clear up the most confusing thing in this whole ecosystem, because if you don't get this, nothing else makes sense. People constantly mix up skills, MCP, and plugins. Two minutes and you'll be ahead of most people using this tool.

### Skills vs MCP (5:20 - 7:00)

[SHOW: Two columns. Left: "SKILL = know-how." Right: "MCP = access."]

> The big one. Skills versus MCP. Here's the analogy that makes it click. Knowing how to write a professional email, the structure, the tone, when to follow up, that's a skill. It's know-how.

> Opening Gmail to actually send the email, that's a tool. That's MCP. It's access to something Claude can't do on its own.

> A skill teaches Claude HOW to do something your way. An MCP server gives Claude ACCESS to something it can't otherwise reach, your database, Gmail, a third-party API.

> And they compose. A skill can use MCP tools. You write a skill that says "pull the last week of support tickets" using an MCP connection, "then summarize them this exact way" using the skill's instructions. Know-how plus access.

### The "but a skill has code" question (7:00 - 7:45)

[SHOW: A SKILL.md folder with a .py file next to it highlighted]

> Now, sharp viewers are already thinking: wait, a skill can include code, isn't that a tool too? Great question, and the answer is the whole distinction.

> Yes, a skill folder can bundle a script. This skill of mine ships a Python file right here. But that script isn't a tool. When a step says "run this," Claude runs it through the Bash tool, the same way you'd run any script on your machine. It's a bundled helper that automates a step. A tool, especially an MCP tool, is something Claude calls by name that reaches outside itself. So: a skill packages the know-how, maybe with a helper script. MCP grants the access. The script doesn't give Claude new reach, it just does local work.

### Skills vs Plugins (7:45 - 9:30)

[SHOW: Add PLUGIN. Visual: a box with several skills inside it]

> Last one, and this sets up something we're going to do live later. A plugin is just a package. It's the box. It bundles a collection of skills, commands, and connections together so someone else can install all of it in one command. Skills are the contents. Plugins are the box you ship them in. When skills come from a plugin, they get a little namespace prefix so they never collide with yours.

[SHOW: Clean summary card]

> So your cheat sheet. Procedural know-how, how to do something? Skill. Access to an external tool or data source? MCP. A bundle you install and share? Plugin. Skills are the know-how, MCP is the plumbing, plugins are the packaging. They all work together.

[NOTE: This is the differentiator chapter. 7/10. The email analogy is the moment, slow on it. The "skill has code" beat is the smartest 45 seconds in the video, it preempts the viewer's own objection. The cheat-sheet card must be clean and pause-screenshot-able. Subagents intentionally cut, out of scope for this one.]

---

## [9:30 - 15:30] Chapter 3 - The Anatomy: The Description Is King

[SHOW: Open a real, well-built SKILL.md of Tyler's, e.g. /yt-search or /content. Scroll to the top.]

> This is a real skill from my system. I'm not going to read you every field like a manual, because you'll see most of them when we build. I'm going to give you the one part that actually decides whether a skill works.

### The description (9:50 - 12:00)

[SHOW: Highlight the description line in the frontmatter]

> Everything between the two sets of three dashes is the frontmatter, the config. And the single most important line in the entire file is the description. Hear me on this. The description is how Claude decides when to fire the skill automatically. You type something, Claude reads all your skill descriptions and fuzzy-matches against them. So it has to say two things: what the skill does, AND when to use it.

[SHOW: Good vs bad description side by side]

> Bad: "helps with PDFs." Too vague, it'll never fire. Good: "Extract text and tables from PDFs, fill forms, merge documents. Use when the user mentions PDFs, forms, or document extraction." It lists the triggers, the actual words you'd say. Write it in third person, pack in the trigger words. Get the description right and the skill just works. Get it wrong and it never even shows up.

### The rest of the frontmatter, fast (12:00 - 13:30)

[SHOW: Quickly highlight each field as named]

> The rest, quickly, because you'll see them in the build. Name, matches the folder. Allowed-tools, a pre-approval list so the skill doesn't stop to ask permission every time, it removes friction, it does not add security. Disable-model-invocation, set it true for anything with a consequence, a deploy or a send-email skill, so it only fires when you type it. Argument-hint, how the skill takes input. Model, you can even pin a skill to Opus for heavy reasoning or Haiku for speed. That's it. The description is the one you obsess over.

### The body and where skills live (13:30 - 15:30)

[SHOW: Scroll to the body; then two finder windows]

> Below the frontmatter is the body, plain English instructions, like you're briefing a smart new hire. Two things make a body good. Structure, steps in order. And gotchas, the context Claude can't guess, "always exclude test accounts," "never touch this file." That contextual knowledge is the whole reason the skill exists. Don't restate what Claude already does well, only write the stuff specific to you.

> And location decides reach. Tilde slash dot claude slash skills, it works everywhere, that's a personal skill. Inside a project, dot claude slash skills, it only works there and travels with the repo for your team. And Claude Code hot-reloads these folders, no restart needed for edits.

[NOTE: This used to be two chapters, now it's one tight one. 6-7/10. The description is the rewatch moment, slow on it. Everything else is fast because the three builds will reinforce it.]

---

## [15:30 - 19:30] Chapter 4 - Proof This Is Not a Toy

[SHOW: Pull up the Anthropic blog post from June 3, 2026, "How we use skills." Scroll it live.]

> Before we build, let me kill the idea that this is a cute trick, because that's the reaction a lot of people have. "Cool, a markdown file, neat."

> This is Anthropic's own engineering blog from June. The company that builds Claude. They run hundreds of skills internally, across their whole engineering org, everything from API reference to CI/CD to incident runbooks.

[SHOW: Highlight the verification-skills line]

> And the line that reframed it for me: the skills that improved Claude's output the most weren't the flashy ones. They were the boring verification skills, the ones that check the work. That tells you where the real value is.

[SHOW: Cut to github.com/anthropics/skills, then an awesome-claude-skills list]

> And it's not just them. Anthropic open-sourced a pile of official skills, you can read them right here. The community has built well over a thousand. There's a pack called superpowers that's basically a senior engineer's brain as skills. There's even a skill whose whole job is to build other skills, and we're going to use one like that in a minute.

> So this is not a toy. It's how serious teams work now. Let's build.

[NOTE: 7-8/10, building. Real receipts on screen, not just talk. Say "over a thousand" and "dozens of tools," do not cite exact figures as hard fact. Natural mid-roll point.]

---

## [19:30 - 33:00] Chapter 5 - Build Three Skills, Live

> Here's how this section works. I'm going to build three skills in front of you, using the two ways you'll actually make them. The first one I build by just talking to Claude. The second one I build with a skill whose only job is to build skills. And the third one bundles an actual script, so you see the code thing we talked about, live.

### Build 1: /standup - just talk to Claude (20:00 - 24:30)

[SHOW: Claude Code open. Empty ~/.claude/skills/ context. Tyler types a request in plain English.]

> Skill one. I'm not going to hand-write anything. I'm just going to ask. Watch.

[SHOW: Type the request live]

> "Build me a skill called standup. When I run it, it asks what I worked on, then generates a clean standup, what I did, what's next, and blockers, and saves it with today's date."

[SHOW: Claude creates the folder and writes SKILL.md. Open the generated file.]

> And there it is. Claude wrote the whole SKILL.md, frontmatter and body, from that one sentence. Look at the description, it already pulled out the trigger phrases. This is the part people miss, you don't have to write these by hand. You describe what you want, Claude writes the skill.

[SHOW: Run it. Claude fires AskUserQuestion. Pick an option ON CAMERA. The file generates, open it.]

> Now I run it. /standup. It's asking me what I worked on, I'll pick "shipped a feature." See that loop, I asked, it asked back, I answered. There's the file, today's date pulled live, three tight sections. We made a real, working skill by talking to it.

[NOTE: 7 -> 9/10 on the test. The AskUserQuestion answer on camera is mandatory. If it fails, fix off-camera, re-shoot from the run.]

### Build 2: /hook - using a skill-creator skill (24:30 - 28:30)

[SHOW: Show the installed skill-creator skill. NOTE TO TYLER: confirm the exact skill-creator you're using before filming, see production notes. It is an installed skill, NOT a built-in command, say it that way.]

> Skill two, second method. There's a skill whose entire job is to build other skills, you install it like any other. I'll use it to build something I actually want: a hook writer. Give it a video topic, get five scroll-stopping hooks.

[SHOW: Invoke the skill-creator, give it the spec, it scaffolds /hook]

> I tell the skill-creator what I want, and it interviews me, what should it do, when should it fire, then it writes a clean SKILL.md with a strong description and a structured body. Same result as build one, different path. Some people like talking, some like the guided builder.

[SHOW: Run /hook on a real topic, show the 5 hooks]

> Run it. /hook, topic, "claude code skills." Five hooks, instantly. Zero code in this one, by the way, it's pure instructions. That's a no-code skill.

[NOTE: 7-8/10. Keep it tight, the novelty is the second method. Pre-test the skill-creator so it doesn't stall.]

### Build 3: /wordcount - a skill that bundles a script (28:30 - 32:00)

[SHOW: Build a small skill that ships a Python helper, e.g. counts words and reading time in a transcript file.]

> Skill three, and this one closes the loop on the code question from earlier. This skill bundles an actual script. It takes a transcript file and tells me the word count and the reading time. The SKILL.md is still just instructions, but it points at a Python file sitting in the same folder.

[SHOW: Show the folder: SKILL.md + wordcount.py. Open both briefly.]

> See the structure, the instructions, and the helper script right next to it. When I run the skill, Claude runs that script with the Bash tool and only sees the output, exactly the progressive-disclosure thing from the start. The script does local work. It is not a tool Claude calls by name, it's a bundled helper.

[SHOW: Run it on a real file, show the output]

> Run it on a transcript. Word count, reading time, done. Three skills. One I talked into existence, one a builder made for me, one that ships its own code. Same format every time, SKILL.md.

[NOTE: 7-8/10. This is the payoff of the "skill has code" beat, it makes the abstract concrete. Keep the script trivial and LOCAL so it can't break. The aha line: "same format every time."]

### The aha (32:00 - 33:00)

[CAMERA: Face to camera, slow down]

> Three skills, fifteen minutes, no SDK, no deployment. Every one of my skills works exactly like these, longer bodies, more tools, same structure. Once you've built one, the floodgates open. You stop asking "how do I automate this" and start asking "what do I call the skill and what does the body say."

---

## [33:00 - 37:30] Chapter 6 - Real Plugins You Can Install in One Command

[SHOW: Claude Code. The /plugin command.]

> So you've built skills. Now, the fastest way to get powerful fast is to install other people's, and that's what plugins are, remember, the box that skills ship in. And there's an official marketplace built right in.

[SHOW: Run the install command live for a real plugin Tyler already has]

> One command. /plugin install, then the name, at claude-plugins-official. Then reload-plugins. Watch.

```
/plugin install playwright@claude-plugins-official
/reload-plugins
```

[SHOW: Show the newly available namespaced commands from the plugin]

> Done. I just pulled in a whole set of browser-automation skills and tools, and notice they're namespaced, playwright colon something, so they never clash with mine. These are real, on my machine right now. I've got Playwright for browser stuff, Vercel for deploys, Slack, Telegram, all installed the same one-command way.

[SHOW: Briefly show Tyler's Creator Engine repo / a custom pack]

> And you can ship your own. I bundled my content skills into a pack so anyone can install the whole system at once. That's the move, build your skills, then package them as a plugin so other people, or your whole team, get them in one command.

[NOTE: 8/10, this is a "whoa, one command" moment. ALL plugins shown must be real and pre-confirmed installed. Install flow verified: /plugin install <name>@claude-plugins-official then /reload-plugins. Do not invent plugin names.]

---

## [37:30 - 43:30] Chapter 7 - The Payoff: The Same Skill in Claude Cowork

[SHOW: Quit the terminal view. Open the Claude Cowork desktop app.]

> Now the part I promised in the first ten seconds, and the part most people have not seen.

> Everything so far was Claude Code, in the terminal, the developer surface. But Anthropic shipped Claude Cowork this year. It went generally available in April, on Mac and Windows, on every paid plan. Cowork is Claude for the rest of your work, a desktop app, not a terminal. It reads and writes your actual files, works with Excel and Word and PowerPoint, runs tasks for you. Built for people who don't live in a terminal.

> And here's why it matters today. Cowork uses the exact same skill system. The same SKILL.md format. So a skill I wrote for the terminal runs in this completely different app.

[SHOW: In Cowork, the skill being invoked. NOTE TO TYLER: verify the exact invocation UI before filming, see production notes. Demo the standup skill, or an office-flavored skill, on a real doc.]

> Watch. Same standup skill. I'm not in a terminal, I'm in a desktop app looking at my real files. And it runs. Same instructions, same output, totally different surface.

> And for teams this is the unlock. In Cowork, an org owner can push approved skills to the whole company. One person writes the skill, everyone runs it, same quality, no rebuilding.

[CAMERA: Face to camera]

> So sit with that. The file we built in an empty folder, in plain English, runs in Claude Code for developers, on Claude on the web, and in Claude Cowork for everybody else. Write it once. Run it everywhere. That's the whole reason skills are the most important thing to understand right now.

[NOTE: THE UNIQUE PAYOFF AND SCREENSHOT MOMENT. 9/10. CRITICAL: confirm exactly how skills surface and get invoked in the current Cowork build before filming, the UX was not fully documented in research. Have a real custom skill loaded and working in Cowork. If standup is awkward there, use an office-document skill but keep the "same SKILL.md" message. Do NOT fake this, your brand is verifiability.]

---

## [43:30 - 47:00] Chapter 8 - Making Skills Robust (Best Practices)

[SHOW: On-screen list builds one principle at a time]

> You can build them and you understand the whole picture. Here are the principles that separate a skill that works once from one you trust for a year, straight from how Anthropic builds them and how I build mine.

> One. Keep the main file lean. Short body, ideally under a couple hundred lines. Heavy reference detail goes in separate files the skill pulls in only when needed. Progressive disclosure. Lean by default, deep on demand.

> Two. The gotchas are the gold. The most valuable thing in a skill is the context Claude can't guess. Your edge cases, your conventions, the thing that broke last time.

> Three. Ask when something's missing. Use AskUserQuestion like our standup skill did. A skill that asks a clarifying question feels ten times more solid than one that errors out.

> Four. Write to predictable paths. Save output to consistent, documented locations. That's what lets skills cooperate and become a pipeline.

> Five. Put hard rules at the bottom. Never overwrite, always confirm, use real dates. Guardrails prevent the disasters.

> Six, safety. Skills can run scripts and use your tools. Only install skills and plugins from sources you trust, and actually read a skill before you run it. Treat it like any script you're about to run on your machine.

[NOTE: 7/10, tight. One principle every ~40 seconds. This is what makes it a course, not a demo.]

---

## [47:00 - 50:00] CTA

[CAMERA: Direct to lens, energy up]

> Let's bring it home. You understand what a skill is, how it's different from MCP and plugins, the one field that actually matters, you watched me build three live two different ways, install real plugins in one command, and run a skill in both Claude Code and Cowork. That's the complete picture. You're genuinely ahead of most people using this tool.

> Here's what to do next. The fastest way to get good is to build a few and read other people's. So I put together a free starter pack: the skills we built today, the actual SKILL.md files, plus more starters I'd build next, and links to the best community collections so you're never starting from a blank page.

> It's free in my Skool community, link in the description. And I'm building a full Claude Code course in there, so if you join you'll get first access and founding pricing when it opens.

> That's the one thing I'll ask. Grab the pack, build your first skill tonight, and come tell me what it does. I read every post. See you in the next one.

[SHOW: Quick callback montage mirroring the open: the one SKILL.md -> terminal -> Cowork -> the file appearing. Fast cuts, same energy as the cold open.]

---

## Production Notes

### Critical Pre-Production
- [ ] Delete `~/.claude/skills/standup/`, `/hook`, `/wordcount` if they exist - all three builds must be from-scratch
- [ ] Clear or move anything in `~/notes/standups/`
- [ ] **Confirm the exact skill-creator skill** you'll use in Build 2, and that it's installed and working. It is an INSTALLED skill, not a built-in command - say it that way on camera.
- [ ] **VERIFY the current Cowork skill-invocation UX** and have a real custom skill loaded and working in Cowork before Chapter 7. Riskiest segment, do a full dry run.
- [ ] **Pre-confirm every plugin** you show is actually installed: Playwright, Vercel, Slack, Telegram are confirmed on the machine. Install flow: `/plugin install <name>@claude-plugins-official` then `/reload-plugins`. Do NOT invent plugin names.
- [ ] Write the trivial local `wordcount.py` ahead of time so Build 3's script can't break on camera (keep it LOCAL, no network, no API)
- [ ] Pull up the June 3, 2026 "How we use skills" blog + github.com/anthropics/skills in browser tabs
- [ ] Have a rich, SAFE SKILL.md to dissect in Ch3 (use /yt-search or /content, never a file with API keys)
- [ ] OBS scenes: Face Cam, Terminal (Claude Code), VS Code, Finder, Browser, Cowork desktop app

### Accuracy callouts (say these carefully)
- "Anthropic runs hundreds of skills internally" - from the June 3, 2026 blog, real citation, show it on screen.
- Skill creation: there is NO built-in auto-generate command. The two real methods are (1) ask Claude conversationally, (2) an installed skill-creator skill. Frame Build 2 as "a skill you install."
- "Skills can bundle scripts" - TRUE, your own skills do (e.g. /yt-search ships search_youtube.py). A bundled script runs via the Bash tool, it is not a registered/MCP tool.
- Plugins: `/plugin install <name>@claude-plugins-official` then `/reload-plugins` - verified. Only show plugins confirmed installed.
- Cowork: "GA April 2026, Mac and Windows, all paid plans" - verified, safe to state.
- "Over a thousand community skills" / "dozens of tools adopted the standard" - say loosely, do not cite exact figures.

### Sensitive Content Check
- [ ] Never show `~/.claude/.env` or any API keys
- [ ] Dissect only a safe SKILL.md
- [ ] No real/private notes visible in `~/notes/standups/`
- [ ] No confidential docs on screen in Cowork

### Demo Continuity
- The standup skill is the through-line: built in Ch5 (Build 1), then run again in Cowork in Ch7. Same skill, two surfaces. That continuity IS the payoff.

### Energy Curve
| Segment | Energy | Notes |
|---|---|---|
| Cold open (one file, two apps) | 10/10 | Hook + screenshot moment |
| Why this video | 7/10 | Trust build |
| Ch1 What a skill is | 6/10 | Foundational, plant the "bundles a script" line |
| Ch2 Skills vs MCP vs Plugins | 7/10 | The differentiator + the "skill has code" beat |
| Ch3 Anatomy (description is king) | 6-7/10 | Tighter now; the description is the rewatch moment |
| Ch4 Proof | 8/10 | Receipts |
| Ch5 Build three | 7 -> 9/10 | The builds climb; the tests are the money shots |
| Ch6 Real plugins | 8/10 | One-command "whoa" |
| Ch7 Cowork payoff | 9/10 | The unique screenshot moment |
| Ch8 Best practices | 7/10 | Tight and practical |
| CTA | 10/10 | Get the click |

### Common Mistakes to Avoid
1. Don't read the script. Map and riff.
2. The description is the one concept to nail in Ch3, don't bury it.
3. Don't fake the Cowork demo. If it's not ready, push the shoot.
4. Don't re-demo the content pipeline (yt-search/transcribe/yt) - reference, don't rebuild.
5. Answer the AskUserQuestion on camera. Show the loop.
6. No em dashes spoken. ONE CTA, Skool.
7. Three builds: keep each tight, the script (Build 3) must be local so nothing breaks.

### Chapters (paste into description)
- 0:00 One file, two apps (the demo)
- 0:25 Why this video exists
- 2:00 What a Claude Code skill actually is
- 5:00 Skills vs MCP vs plugins
- 9:30 The anatomy: the description is king
- 15:30 Proof: Anthropic runs hundreds of these
- 19:30 Building three skills live
- 33:00 Real plugins you can install in one command
- 37:30 The payoff: the same skill in Claude Cowork
- 43:30 Making your skills robust
- 47:00 Get the free starter pack
