# Script — DeepSeek Harness: The Open-Source Claude Code (Setup + Features)

Target: ~11-13 min. Honest, engineer POV, short sentences. `[SHOW: ...]` = on screen. `[NOTE: ...]` = production. No em dashes, no money in the spoken hook (fine to say "free"). Cover it while the term is hot.

Reference: NeuralNine (222k) covered plugins, trajectory, creator mode, providers. He did NOT cover subagents or the desktop app. Those are our differentiators - the subagent beat is the hero.

---

## [0:00 - 0:25] Hook

Half of YouTube is telling you DeepSeek Harness is the end of Claude Code.

[SHOW: fast montage of those thumbnails, then cut to Tyler]

It's not. But it is the most interesting thing to happen to coding agents this year, and it hit over two hundred thousand GitHub stars in about two weeks.

[SHOW: the repo star count]

It's open source, it runs any model including free local ones, and it can run Claude Code for you as a subagent.

[NOTE: no intro card, no "hey guys". Hard cut.]

---

## [0:25 - 1:25] What a harness actually is

Quick thing first, because the word is doing a lot of work and nobody explains it.

A model on its own does almost nothing. DeepSeek, Claude, any of them. Text in, text out. It can't read a file. It can't run a command. It can't remember what you said a minute ago. It can't even decide to stop.

[SHOW: plain box labeled MODEL, text in one side, out the other]

So everything you think of as a coding agent is not the model. It's the code wrapped around it. The loop that calls the model, runs the tool it asked for, feeds the result back, and goes again. The tools themselves. What gets loaded into context and what gets cut. Permissions. The interface you're looking at.

[SHOW: labeled rings building around the box as you name them]

That wrapper is the harness. The model is the engine. The harness is the rest of the car.

[NOTE: land this line clean. Say it once, never again.]

And you already use one. Claude Code is a harness. Codex is a harness. Cursor is a harness. Sometimes literally the same model underneath, and they feel completely different. That difference isn't the model. That's the harness.

[SHOW: three logos, one model box under all of them]

The catch is you can't open any of them. You get the finished car.

[SHOW: cut to the dsh UI]

This one, every part is a piece you can pull out. That's what "everything is a plugin" means here. The model, the tools, the agent loop, even the sidebar. Eighty six of them running in the default setup, and I can turn any of them off.

Alright. Let's run it.

[NOTE: straight into the terminal. No transition, no "so in this video we'll cover".]

---

## [1:25 - 2:30] Install it (and the desktop caveat)

Let's get it running. The easy way is one command.

[SHOW: terminal]
```
npx @deepseek-ai/dsh web
```

That launches the web interface at localhost:3080. That is the whole install. If you'd rather build from source you can, but for trying it, npx is enough.

[SHOW: the web UI opening at 127.0.0.1:3080]

Now, one thing you will see people talk about: a DeepSeek Harness desktop app. Quick heads up, and this matters. That desktop app is not official. It is a community wrapper. A few people took the real web UI and wrapped it in a desktop shell so it feels native and stays in your tray.

[SHOW: one of the GitHub desktop-wrapper repos]

It is genuinely convenient, no terminal, one-click updates. Just know it is third party, not from DeepSeek. I would start with the official web version, then grab a wrapper if you want the app feel.

---

## [3:30 - 5:00] Give it a model (including free + local)

First run, it asks for a DeepSeek API key. Watch what I do with it.

[SHOW: the first-run dialog, click "Configure later"]

Skip it. You never actually need one. Because models in this thing are not special, they are just a plugin, and that plugin holds a list of providers. And there are exactly two kinds.

[SHOW: on-screen split - "Knows about it: 1 key" / "Never heard of it: 3 fields"]

Kind one, a provider it already ships. It knows the endpoint, the protocol, the model list. You give it a key and you are done. Kind two, a provider it has never heard of. Your own box, a private gateway, whatever. You describe it in three fields. No code, no plugin to write.

Let's do one of each.

[SHOW: Settings > Models > Add provider > openrouter]

First one, OpenRouter. It is in the list already, so this is one dropdown and one key.

[SHOW: scroll the provider dropdown slowly - 39 options]

Look at how long that list is. Anthropic, OpenAI, Google, Groq, Bedrock, Together, xAI, all of it shipped.

[SHOW: openrouter.ai]

Quick note on OpenRouter, because it is the easiest option. OpenRouter is one account and one API key that gives you access to hundreds of models across every provider. Instead of making a separate account and key for each company, you make one, you add credit to it, and OpenRouter routes your request to whatever model you pick and takes a small cut.

And I do not even have to paste a key here. It supports signing in.

[SHOW: the OAuth flow - "open this page to continue signing in", the code, the verification page]

[NOTE: do NOT refresh the browser during this or the login is abandoned]

Now let's pick a model. And I am going to use DeepSeek's own model, through OpenRouter, inside DeepSeek's harness.

[SHOW: model picker, select deepseek/deepseek-v4-flash]

DeepSeek V4 Flash. A million tokens of context, and it is cents per million tokens, so this whole video is going to cost me almost nothing.

[NOTE: optional 10s, cut if pacing is tight]
There is also a free tier in here.

[SHOW: scroll the picker to the :free models]

Seventeen free models that support tool calling. They are heavily rate limited though, twenty requests a minute, so for an agent loop that is going to stall out. I am using the cheap DeepSeek route instead. But it is there.

One detail I liked: the key does not go in the config file. The config holds a reference, the secret goes to a separate credential store. So you can actually commit your harness config.

Now the free one. And this is a different button, which matters.

[SHOW: Settings > Models > Add custom provider]

Ollama is not in that catalog. So it goes in as a custom provider. Three fields.

[SHOW: fill the form - blank key, display name Ollama, base URL, protocol]

No API key, because it is my machine. Name it Ollama. Base URL is localhost eleven four three four slash v1. Protocol is openai-completions, which is the default.

[SHOW: click "Fetch available models"]

And then this. Fetch available models. It goes and asks my Ollama server what it has, live.

[SHOW: qwen3.8 appears, select it, set capacity to 64000]

There is my local model. I set the context window to match what I started Ollama with, save.

[SHOW: switch the composer model dropdown from the cloud model to the local one]

And now I am running a coding agent completely locally. No API key, no per-token cost, nothing leaving my machine. And notice I did not restart anything, it re-reads that config per request.

That is the "free Claude Code" thing people are talking about, and it is real.

[SHOW: click "Open config file", show the YAML both forms wrote]

One last thing here. Every click I just made wrote these lines. The UI is a form over a config file, and the config file is the truth.

[NOTE: honest beat] One limitation: as far as I can tell you cannot plug in your ChatGPT subscription like some tools let you. API keys or local. Fine, just know it.

---

## [5:00 - 6:45] Feature 1 — See everything (Trajectory)

Okay, let me show you the first thing that actually impressed me. Let's give it a real task.

[SHOW: point it at a workspace, type a task]
```
Create a simple Flask to-do app.
```

It works, fine. But watch this. Go to the Trajectory view.

[SHOW: the Trajectory tab, the graphical step timeline]

This is every single thing the agent did. The system prompt, your prompt, the context it loaded, its thinking, every tool call, the exact payload, the result, how long each step took.

[SHOW: click into a tool call, show payload + result]

This is the opposite of Claude Code, where the thinking is hidden. Here you can see and replay literally everything. If you have ever wanted to know why an agent did something, this is it. As an engineer, this is the feature I did not know I wanted. You can even export the whole session as a log file.

---

## [6:45 - 8:30] Feature 2 — It builds its own tools (Creator mode)

Now the one that sounds fake until you see it. Creator mode.

[SHOW: switch agent preset to Creator mode]

There is a mode specifically for building plugins by talking. So instead of writing a plugin, I describe it.

[SHOW: type in creator mode]
```
Add a plugin for a calculator overlay in the bottom right. A simple GUI calculator.
```

[SHOW: it loads the Cordis plugin skill, builds it, asks to confirm]

Watch. It pulls in its own plugin-development skill, writes the plugin, and asks me to approve it. I click approve, and now there is a working calculator living in my agent. That I never coded. I just described it.

[SHOW: the calculator working in the corner]

Is it polished? No. This is a preview, the buttons were even unlabeled on my first try. But think about what just happened. The agent extended itself. You can persist these, and over time there is going to be a whole plugin ecosystem. That is a genuinely new idea.

[NOTE: keep the honesty - "rough but real" is the tone. Do not oversell.]

---

## [8:30 - 10:30] The hero — make it run Claude Code (subagents)

Okay. This is the part I actually made this video for, and almost nobody is showing it.

DeepSeek Harness can call Claude Code as a subagent.

[SHOW: diagram - dsh in the middle, arrow out to Claude Code, result coming back]

So instead of replacing Claude Code, it can orchestrate it. It hands a task off to Claude Code, waits, reads what comes back, and keeps going. Same with Codex.

Here is how you turn it on. Harness ships subagent provider plugins, and they are disabled by default. So you enable the plugin.

[SHOW: enable the subagent / Claude Code provider plugin in the config]

It delegates to the Claude Code binary that is already on your PATH. So if you have Claude Code installed, Harness can just call it.

[SHOW: in a session, delegate a task to Claude Code, show the tool call handing off and the result folding back in]

And now, watch. I ask it to delegate this piece to Claude Code. It makes the call, Claude Code does the work, and the result comes back into my Harness session, and it keeps reasoning on top of it.

That reframes the whole thing. This is not Harness versus Claude Code. Harness becomes an orchestration layer above Claude Code. You keep the tool you trust for hard coding, and you get all this transparency and the model choice around it. That is the combination I would actually run.

---

## [10:30 - 12:00] Where it fits + honest verdict

So let me be straight with you, engineer to whoever is watching.

[SHOW: a simple "who it's for" card]

Is this replacing Claude Code today? No. It is a developer preview. It is rough in places, the plugin toggling is still config files, some of it is fiddly. If you just want to ship code, Claude Code is still smoother.

But. If you care about seeing exactly what your agent does, running any model including free local ones, and composing tools instead of being locked in, this is the most exciting thing out right now. And the fact that it can drive Claude Code means you do not even have to choose.

[SHOW: recap card - open source / any model + local / everything a plugin / creator mode / runs Claude Code]

Open source. Any model, including free and local. Everything is a plugin. It builds its own tools. And it can run Claude Code for you. That is DeepSeek Harness.

[NOTE: CTA short, one destination]

If you want the exact commands, the provider setup, and how I wired the subagent, they are in the free community, link below. And tell me in the comments if you want a full build where I orchestrate Claude Code with this on a real project. That is probably my next one.

That is it. Go play with it while it is early. See you in the next one.

[SHOW: end card]
