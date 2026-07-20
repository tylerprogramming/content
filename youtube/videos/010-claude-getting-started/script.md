# How to Get Started with Claude Code — Full Script

---

## [0:00 - 0:30] Hook

[SCREEN: Quick montage — terminal opening, Claude Code running, countdown timer app appearing in browser]

> Claude Code is the most powerful AI coding tool right now, but most people never get past the install screen. The terminal freaks them out. Today I'm going to fix that. In the next ten minutes, you're going to install Claude Code and build your first app — even if you've never opened a terminal in your life. Let's go.

[NOTE: Hard cut, high energy from frame one. Flash the finished countdown timer app at the end of the montage to tease the payoff.]

---
 
## [0:30 - 1:30] What is Claude Code?

[SCREEN: Tyler talking to camera]

> So what actually is Claude Code? It's made by Anthropic — the company behind Claude. And it's an AI coding agent that runs directly in your terminal. That means it's not a chatbot you talk to in a browser. It lives on your computer. It can read your entire codebase, write code across multiple files, run commands, handle git — it can actually do things.

> Think of it as a senior software engineer sitting inside your computer, waiting for instructions. You tell it what you want, and it builds it. The reason people are going crazy about it right now is because the models have gotten so good that the output is legitimately impressive. We're talking full apps, not toy demos.

> But to use it, you need to be comfortable with one thing — the terminal. And I know that word just scared half of you. So let's fix that.

[NOTE: Keep this tight — 60 seconds max. The goal is just enough context so they understand WHY they're about to install something.]

---

## [1:30 - 2:30] Don't Be Afraid of the Terminal

[SCREEN: Tyler talking to camera, then cut to terminal]

> I know the terminal looks like a hacker movie. Black screen, blinking cursor, feels like you're about to accidentally delete your entire computer. You're not. I promise.

> The terminal is just a text-based way to talk to your computer. Instead of clicking folders and icons, you type commands. That's it. You only need to know like three things to get started — how to open it, how to navigate to a folder, and how to type a command.

[SCREEN: Open Terminal app on Mac]

> On Mac, just search for "Terminal" in Spotlight — Command+Space, type Terminal, hit enter. On Windows, search for "Command Prompt" or "PowerShell." Either works.

[SCREEN: Show a blank terminal]

> See? It's just a blank screen with a cursor. Not scary. If I type `ls` and hit enter, it shows me the files in my current folder. If I type `pwd`, it tells me where I am on my computer. That's literally all you need to know for now. Claude Code handles the rest.

> Alright, let's install this thing.

[NOTE: This section is critical for true beginners. Don't rush it. Let the blank terminal sit on screen for a beat so they can see it's just... a text box.]

---

## [2:30 - 3:30] What Do You Need to Pay For?

[SCREEN: Tyler talking to camera]

> Before we install, let's talk about what this costs — because Claude Code is not free. You need a Claude subscription. There are a few options.

> The cheapest way in is Claude Pro at twenty bucks a month. That gives you access to Claude Code with the Sonnet model, which is honestly great for most things. If you're just getting started, this is what I'd recommend.

> If you want more power and higher usage limits, there's Claude Max at a hundred dollars a month. That gets you the Opus model — which is the smartest one — plus way more usage before you hit any limits. There's also a two hundred dollar tier if you're really pushing it.

> There's also an API option where you pay per token — per use, basically — but I wouldn't recommend that for beginners. Subscriptions are simpler and more predictable. Start with Pro, upgrade if you need to.

[NOTE: Keep this section tight — 60 seconds. Don't get bogged down in pricing details. The goal is just "you need Pro at minimum, here's what the tiers are."]

---

## [3:30 - 5:00] Installation

[SCREEN: Terminal open]

> Alright, installing Claude Code is stupid easy now. You don't need to install Node, you don't need npm, none of that. It's one command.

> On Mac or Linux, open your terminal and paste this:

[SCREEN: Tyler types `curl -fsSL https://claude.ai/install.sh | bash`]

> `curl -fsSL https://claude.ai/install.sh | bash`. That's it. One line. It downloads and installs everything.

> On Windows, open PowerShell and paste this instead:

[SCREEN: Show the Windows command on a text overlay]

> `irm https://claude.ai/install.ps1 | iex`. Same idea, just the Windows version.

[SCREEN: Installation running, finishing quickly]

> Once it's done, type `claude` and hit enter.

[SCREEN: Claude Code starting up for the first time]

> It's going to ask you a couple things. First, pick your text style — I always go dark mode. Then it asks how you want to connect your account. Sign in through the browser. It'll open a page, you log into your Claude account, authorize it, and boom — you're in.

[SCREEN: Show the success screen — Claude Code prompt ready]

> That's it. You now have Claude Code installed. One command to install, type claude to start. If you're using VS Code, you can also open a terminal right inside VS Code with Control+Backtick on Windows or Command+Backtick on Mac, and run Claude Code there. Same thing, just embedded in your editor.

[NOTE: Much simpler than the old npm flow. No common gotchas to mention anymore — the native installer handles everything.]

---

## [5:00 - 7:30] Your First App

[SCREEN: Terminal with Claude Code running]

> Alright, the moment you've been waiting for. Let's build something. First, I need a folder for my project. I'm going to type these commands — don't worry about memorizing them, they'll be in the description.

[SCREEN: Tyler types commands]

> `mkdir my-first-app` — that creates a new folder. `cd my-first-app` — that moves me into it. Then `git init` — this sets up version control. Claude Code works best when you have git set up. Then I type `claude` to start it up, and it asks me to trust this folder. I'll press one to confirm.

[SCREEN: Claude Code ready for input]

> Now here's the fun part. I'm just going to tell Claude what I want.

[SCREEN: Tyler types the prompt]

> "Create a beautiful countdown timer to New Year's Eve 2027. Make it full-screen with a dark background, animated numbers, and a confetti explosion when it hits zero. Also give me the ability to add more countdowns to the page."

[SCREEN: Claude starts working — creating files, writing code]

> Watch this. Claude is reading my prompt, figuring out what files to create, and writing all the code. HTML for the structure, CSS for the styling and animations, JavaScript for the countdown logic. I didn't write a single line of this.

[SCREEN: Speed up Claude generating at 2-3x, then cut to real-time when it finishes]

> It's done. Let me open this in a browser.

[SCREEN: Open the HTML file in browser — countdown timer running with animations]

> Look at that. A full-screen animated countdown timer. Numbers ticking down, smooth animations, dark background. And if I scroll through the code Claude wrote — it's clean. Proper structure, comments, responsive design.

> You just built your first app with Claude Code. That's how fast it is. One sentence in, working app out.

[SCREEN: Tyler talking to camera, genuine excitement]

> Now obviously this is a simple example. But the process is exactly the same whether you're building a countdown timer or a full SaaS app. You tell Claude what you want, it builds it. The difference is just how detailed your instructions are. And I have a whole video on that — I'll link it at the end.

---

## [7:30 - 10:00] Key Things to Know

[SCREEN: Tyler talking to camera]

> Before you go off building, there are five things you need to know about Claude Code. These will save you a ton of headaches.

> Number one — Plan Mode. If you press Shift+Tab, you toggle plan mode on and off.

[SCREEN: Show Shift+Tab in terminal, mode indicator changing]

> When plan mode is on, Claude thinks and plans but doesn't write any code. It'll ask you questions, outline an approach, and wait for your approval before doing anything. For anything beyond a simple one-file project, always start in plan mode. Trust me on this.

> Number two — Permissions. Claude is going to ask your permission before it runs certain commands.

[SCREEN: Show a permission prompt from Claude]

> It'll say something like "I want to run npm install, is that okay?" You can allow it once, allow it always for that command, or deny it. When you're starting out, I'd say allow things one at a time so you can see what it's doing. As you get comfortable, you can loosen that up.

> Number three — Slash commands. There are a few commands built into Claude Code that you should know.

[SCREEN: Show each command being typed]

> `/clear` — this wipes your conversation history and gives you a fresh start. Super useful when things get messy. `/compact` — this compresses your conversation to save context space. `/help` — shows you all available commands.

> Number four — Context. As you talk to Claude, the conversation fills up a context window. Think of it like RAM — there's a limit. If your conversation gets really long and Claude starts acting weird or forgetting things, that's probably why. Just type `/clear` and start fresh. Your files are still there, nothing is lost.

> And number five — the Escape key. If Claude is doing something and you want to stop it, just press Escape. It cancels whatever it's currently doing. Good to know in case it starts going in a direction you don't want.

---

## [10:00 - 11:00] What's Next + Outro

[SCREEN: Tyler talking to camera]

> Alright, you now have Claude Code installed, you've built your first app, and you know the five things that matter. You're ahead of ninety percent of people who are still just reading about this stuff.

> But here's the thing — what we built today was simple on purpose. If you want to build real, serious apps with Claude Code, you need a system. You need to know how to plan properly, how to build feature by feature, how to test, and eventually how to let Claude build entire apps autonomously while you walk away.

> I made a whole video on exactly that. It's the complete Claude Code workflow — from planning to autonomous building. I'll link it right here and in the description. Think of today's video as part one and that video as part two.

> If this helped you, hit subscribe — I put out videos on Claude Code, AI tools, and practical workflows every week. And if you build something after watching this, drop it in the comments. I actually read all of them and I love seeing what people create.

> I'll see you in the next one.

[SCREEN: End screen with subscribe button, link to workflow video, related video cards]

[NOTE: Total spoken word count ~1,700 words. At 150 wpm this lands around 11 minutes. The screen recording sections add time with pauses, so actual runtime will be 11-13 minutes.]
