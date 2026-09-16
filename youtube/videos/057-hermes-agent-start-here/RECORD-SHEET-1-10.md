# 057 Record Sheet, sections 1 to 10 (0:00 to ~10:30)

Film from this page. Tina-shaped: her cadence, your facts. Left = what you say. Right = what is on screen / what you click.
Rules: no em dashes, no hype words, "so" openers are fine. If a count is spoken, count it on camera.

Pre-roll (before you press record)
- Phone: screen record Slack, 8:02 Attend card and Coder's "All green" card. AirDrop to Mac.
- Desktop open on Bots tab, 4 avatars showing (Hermes, Coder, Researcher, Packager).
- Fresh-install machine decided: `mv ~/.hermes ~/.hermes.bak` on this Mac, or second Mac.
- Claude Code open in a terminal, ready for the bio prompt.
- `~/.hermes/memories/` open in Finder, both files ready to open in your editor.
- Capabilities pane: ClickUp shows connected (61 tools).

---

## 1. Hook (0:00 to 0:45)

| Say | Do |
|---|---|
| Welcome to the Hermes Agent setup guide for Claude Code users. Setting up your Hermes Agent correctly is so important. It's the difference between having a terrible time versus being able to build something sustainable that you can build on top of and that becomes more useful every day. | Camera |
| It's been a few weeks now that I've been using Hermes Agent consistently. Here's my multi-agent system doing research and reviewing code while I'm chatting with it, using local models to keep things free and private. And here's the morning brief it sent to my phone before I opened my laptop. | Cut: Bots tab with 4 bots → Coder's review verdict → phone, 8:02 Attend card |
| So in this video I'm going to walk you through my whole Hermes setup, and tips and tricks along the way that can make a really big difference for your experience. And I'll be giving you the exact prompts and commands so you can build yours the same way. Now without further ado, let's go. | Camera |

## 2. Outline + hardware (0:45 to 2:55)

| Say | Do |
|---|---|
| Alright, outline for today's video. We're going to start off with talking about hardware choices, where your Hermes Agent is going to live. Then I'll walk you through the download and setup process. We'll walk through the major features: memory, skills, cron jobs, and profiles, including how to set each one up properly. I'll also talk about how to use open source models. And finally, after you've got the fundamentals, I want to give you a taste of the multi-agent side, how powerful that can be, especially in combination with Claude Code if you're building software. | Outline card on screen |
| By the way, if you're wondering whether this replaces Claude Code, it doesn't. I still use Claude Code every day. Hermes has become the one that's always running alongside it. You'll see where the line is. | Camera |
| Okay, let's start off with talking about hardware. For me, I primarily run my Hermes Agent on my Mac Studio. It's on 24/7. This is powerful enough for me to run some pretty great local AI models, and I only reach for a cloud model when I need to do something really heavy. This is a good balance for me. | Camera, Mac Studio in shot |
| But do not fear if you don't happen to have a Mac Studio. You can have a very powerful Hermes setup with other options. I'd say there are four primary options. The first is a dedicated local machine, like a Mac Studio. The second is a VPS, a virtual private server, which is basically renting a computer in the cloud. These can be as cheap as five or six dollars and be on 24/7 as well. The third option is any old computer or laptop you have lying around. Just wipe it and leave it on. And finally, if you don't want to spend any money, you can use your own personal computer. But if you're going to do this, I highly recommend you use Docker, which containerizes your agent so it doesn't go bananas on the rest of your machine. | Four-option card (post) |
| I'm not going to go into too much detail on each of these, because the setup is the same on all of them. Let's move on to the next step, which is setting up our Hermes Agent. | Camera |

## 3. Install (2:55 to 4:25)

| Say | Do |
|---|---|
| So to set up Hermes Agent, you want to go to hermes-agent dot nousresearch dot com, and you have two different options. You can install it via the desktop app, or you can install it via the terminal. Most tutorials I see go through the terminal route. So I want to show you the desktop app, which is a great option if you don't want to type stuff into a terminal. But if you're going terminal, it's super easy as well. Just click copy, stick it into your terminal, and go through the onboarding sequence. | Browser: hermes-agent.nousresearch.com |
| (fill while it runs) It grabs its own Python, the code, and a launcher. Everything lands in one folder, dot hermes, in your home. Same install on a laptop or a five dollar server. | Terminal, paste and run: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| So click download for macOS. Alright, once you have it open, it looks like this. A clean Hermes Agent. This interface probably looks very familiar. It's very similar to your normal chatbot interfaces. | Download → open desktop app |
| And the first thing you want to do is come over here and look at the different models. There are some models already here because I have keys set up. This is going to look different depending on what you already have. So you can just choose what you have. And if you don't have anything, you can choose edit models and click add provider. Here you can connect to any provider you have. If you have a ChatGPT or Claude subscription, you can just log into that and use it here. If you want to go fully local, that also works. I'll show you later in the video how to set up your local model. But if you don't have any kind of subscription, the easiest option is probably the Nous Portal. It's a monthly subscription that gets you access to hundreds of different models. | Composer model picker → Edit models → Add provider → Nous Portal sign in |

## 4. Say hi (4:25 to 4:30)

| Say | Do |
|---|---|
| And once you have that connected, you can just start off by saying hi. | Type `hi` |
| There you go. Just had your first interaction with Hermes Agent. | Let it answer |

## 5. Tell it about yourself (4:30 to 6:00)

| Say | Do |
|---|---|
| Now let's continue talking with the agent for a bit. The first thing I actually recommend you do is tell your agent a little bit about yourself. Now, instead of typing it, what I like to do is go to Claude Code, which already knows me, and just write: | Switch to Claude Code |
| | In Claude Code: `Write a short paragraph about me I can hand to a new AI assistant: who I am, what I build, how I like things written. Plain text.` |
| So it'll tell me about myself, which I can just copy. | Copy the paragraph |
| | Paste into Hermes, add on a new line: `Here's a bit about myself. Please remember this.` |
| There you go. And you can see it says running memory, because it's actually going to remember this. | Point at the memory tool call in the transcript |
| Now before I show you where that went, watch this. | |
| | Type: `Given what you now know about me, what would you not bother explaining to me?` |
| It skipped what an agent is, skipped how Claude Code works, and kept it short, because I told it to once. Ten seconds in and it already talks to me differently. | Let it answer, read one line |

## 6. Where memory lives (6:00 to 7:30)

| Say | Do |
|---|---|
| Now you may be asking, how is it remembering it? Where is it storing this information? Great question. Let me show you. I'm actually going to jump now to my Mac Studio, which has my proper Hermes Agent running. I reinstalled it fresh just to show you the download, but let's see what it looks like once it knows you. | Cut to the mature install. Say the seam. |
| Okay, this is the Mac Studio. Let me show you where Hermes stores its memories. If you go to Finder, it's under your user, then dot hermes, then memories. | Terminal: `open ~/.hermes/memories/` |
| And you can see there are two files here. | Count them on camera |
| This one, USER dot MD, is what it knows about the user, me. It's literally human readable. You can read it yourself, exactly what Hermes knows about you. | Open USER.md in your editor. Scroll slowly. |
| It's just a markdown file. And since it's just a file, I can edit it. | Delete one line, type one line, save |
| If it learned something wrong, I delete the line. If I want it to always know something, I type it in. | |
| And there's also a MEMORY dot MD file, where it saves information that's crucial to your current setup. Things it figured out on its own. | Open MEMORY.md. Point at the bots line, the cron line, a tool pitfall line. |
| This is the built-in Hermes memory. You don't have to do anything here. I'll talk more about the memory system and how to make it better a little later in the video. | |

## 7. Settings tour (7:30 to 8:00)

| Say | Do |
|---|---|
| By the way, there are a lot of things you can do just from this desktop app. It's so convenient. If you go to your settings over here, there's a lot you can configure. | Cmd+, |
| Your model. Personality. Appearance. Workspace. Safety. | Scroll, 20 seconds |
| Memory and context. See these two numbers? Those are the size limits on the two files you just saw. I'll explain why they're small later, it's actually the smart part. | Stop on Memory & Context, point at the two caps |
| And this row at the top, because I've got four agents, every setting here is per agent. I mostly leave it default, it looks pretty good. And with that, let's move on to the major Hermes features. | Point at the Applies to chips |

## 8. Tools (8:00 to 9:00)

| Say | Do |
|---|---|
| Okay, so there are four major features I think are important for you to understand. The first one is tools. Tools are pre-configured infrastructure managed by Nous Research, the creators of Hermes, to do things like search the web, read files, run commands, browse a site, look at an image. It's not something you build yourself. For example, I can ask: | New chat |
| | Type: `Search the web for what changed in the latest Hermes Agent release and give me the three things a Claude Code user would care about.` |
| So we see it uses a search function and pulls the results. If you click on Capabilities over here, and look at Tools, you can see everything Hermes natively has. This is already very powerful. | Left rail → Capabilities → Tools tab. Scroll: terminal, browser, web search, vision, image, memory, delegate. |
| If you've used Claude Code, this is the same idea as its tool set, but wider. It can drive a browser and look at a screenshot out of the box. | |

## 9. Integrations and messaging (9:00 to 10:00)

| Say | Do |
|---|---|
| But Hermes can do more than this, because it also has what are called integrations. Integrations let Hermes call on other third-party software. It's what lets you connect different providers for models, Nous Portal, Anthropic, OpenAI, Ollama. And it lets you connect to messaging platforms. Over here I have Slack connected. | Settings → Messaging. Slack shows connected. |
| This is how I get alerts and talk to Hermes from my phone. So here's Hermes sending me my morning brief. | Cut to phone: 8:02 Attend card (same clip as the hook) |
| Good morning, here's what's happening in my product today. That's a little taste of what you can build with these integrations. It's also where my code reviews land. | |
| By the way, if you want to connect Slack, or Telegram, or any other chat app, it's really easy. You can start a new session and just ask your Hermes Agent, hey, can you help me connect to Telegram? And if you click on Messaging, you can see all the different messaging apps you can connect to. | Back to Messaging pane |
| Telegram is literally a QR code. Scan it, it makes the bot and detects your user ID. I use Slack because I already live there, and it works on my phone. | Point at Telegram, Create with QR |

## 10. MCP (10:00 to 10:30)

| Say | Do |
|---|---|
| Nous Research and Hermes support a lot of these integrations already, and they're super easy to use. And if it happens that Hermes doesn't have a native integration, you can use what's called MCP to give your agent additional third-party tools. Same thing Claude Code uses, so if you've got MCP servers set up there, they work here. | Capabilities → Capabilities tab, MCP list. ClickUp row: connected, 61 tools. |
| The way you connect one is, as you'd probably guess, really easy. You just say, hey, help me connect to the ClickUp MCP, and follow the instructions. I'm not going to go into more detail on MCPs and plugins, that's a bit more advanced, maybe a next video. | Point at the ClickUp row |
| Now let's move on to the second feature. Also the feature that made Hermes famous to begin with, which is skills. | Camera, transition to §11 |
