# Script - Build Your First AI Agent (The Easy Way, No Code)

Target runtime: 10-13 min. Warm, direct, doable, honest. Tyler's voice: "so," "here's the thing," "right?", "kind of," admit the limits, make it feel doable.
Format: SHOWCASE. Build ONE real agent live. Not a lecture.
Reminder: no em dashes, no fake money claims, no hashtags. The agent is a Research Agent (topic in, real web research, one-page brief out).

---

## [0:00-0:20] COLD OPEN - word for word

[Visual: quick flash of an intimidating framework diagram / wall of code, then it gets swept off screen. Cut to Tyler.]

"Everyone makes AI agents sound complicated. Frameworks, orchestration, all this stuff that makes you feel like you need a computer science degree.

I built these at Fortune 500 companies, and I'm telling you, the easy version takes about ten minutes.

So let me just show you. We're going to build a real one together, right now, and you can copy the whole thing."

---

## [0:20-1:30] WHAT AN AGENT ACTUALLY IS (kill the intimidation)

[Visual: Tyler on camera. Simple text builds on screen as he says the three parts: a goal / a tool / plain English.]

Talking points, Tyler's voice, keep it tight and warm:
- "So before we build anything, let me clear up what an agent even is, because the word does a lot of damage."
- "Most people hear 'AI agent' and they picture some big technical system with a bunch of moving parts. It's really not that. An agent is kind of just three things."
- Lay out the three, plainly, one line each on screen:
  - "One, a goal. Something you want done."
  - "Two, a tool it's allowed to use. Like searching the web, or reading a file."
  - "Three, you telling it what to do, in plain English."
- The reframe: "That's the whole thing. A regular chatbot just talks back to you. An agent has a job and it can actually go do it, using a tool, and figuring out the steps on its own. That's the only real difference."
- Earned authority, plainly, once: "And look, I've built the heavy, complicated version of this at big companies. Real production agents. So when I tell you that you do not need any of that to start, I mean it. The easy way genuinely gets you most of what you want."
- Set the promise: "So we're going to build one that actually researches a topic for you and writes up a clean summary. You give it a topic, you walk away, you come back to a finished brief. Let's just do it."

---

## [1:30-2:30] WHAT WE'RE BUILDING + THE EASY PATH

[Visual: Tyler, then cut to a clean desktop with Claude Code open. Nothing scary on screen.]

- "Here's the tool we're using. This is Claude Code. Don't let the name scare you, we are not writing code today. Not one line."
- Honest framing of the easy path: "The old way to build an agent was you'd pick a framework, you'd wire up a bunch of pieces, you'd write actual code to connect the tool to the model. That's the part that made it hard to teach, and honestly that's why I stopped teaching it that way."
- "The easy modern way is you just write down what you want the agent to do, in plain English, in a little instructions file. And the AI handles the wiring. That's the whole shift. You describe the job, it does the connecting."
- Name the agent clearly: "So our agent has one job: take a topic, go search the web, read a few real sources, and write me a one-page brief with the key points and links back to where it found them. Simple, useful, and it's a real agent, because it's got a goal and it's using a tool to go get it done."
- "Alright, let me build it in front of you."

---

## [2:30-8:00] THE LIVE BUILD (the payoff - keep it moving)

General direction: build it REAL, on camera, in plain English. Cut Claude's thinking time down in the edit so nothing drags. Narrate what you're doing so a total beginner never feels lost. Do not fake output.

### Step 1 - Make a home for the agent [2:30-3:30]
- "First thing, I'm just going to make a folder for our agent so it has a home. That's it. A folder." [make the folder on screen, name it something plain like research-agent.]
- "Now inside Claude Code, I'm going to create one file. This is the whole agent. It's just an instructions file, plain English, telling it who it is and what to do."
- Start the file live. Say it as you type it, keep it human:
  - "You are a research assistant."
  - "When I give you a topic, search the web for recent, credible sources."
  - "Read them, pull out the key points, and write me a one-page brief."
  - "Include the main takeaways, a few important facts, and a link back to where each point came from."
  - "If you're not sure about something, say so. Don't make things up."
- The teaching beat: "Notice what I just did. I didn't write code. I wrote instructions like I'm talking to a new assistant on their first day. That last line is important, right? I'm telling it, don't make things up, tell me when you're unsure. You want that in every agent you build."

### Step 2 - Give it the tool [3:30-4:30]
- "So it's got its job. Now it needs the one tool it needs to do that job: the ability to search the web. Because without that, it's just guessing from memory, and we don't want that. We want it going out and getting real, current stuff."
- Show turning on / confirming the web tool in plain terms (whatever the on-camera path is: enabling the web search tool). Keep it non-technical: "I'm just letting it use web search. One tool, on. That's the difference between an agent and a chatbot, right there. Now it can actually go do something, not just talk."
- The honest aside: "And this is genuinely all the setup there is. A folder, an instructions file, and one tool turned on. That's the agent. People spend weeks on this the hard way. We're a few minutes in."

### Step 3 - Run it live [4:30-6:30]
- "Okay. Moment of truth. Let me give it a topic and let it go." [Type a real, relatable topic live, for example: "research the best free tools for someone starting a newsletter in 2026."]
- While it runs, narrate what's actually happening so the beginner sees the agent thinking: "Watch this. It's deciding what to search. It's running searches. Now it's reading through the results. This is the agent part, right? I didn't tell it which sites to go to or what exact searches to run. It's figuring out its own steps to hit the goal I gave it."
- Speed-ramp the wait in the edit, but keep enough that it feels real.
- When it lands, open the brief on screen and actually read a couple of real lines from it. Point at the sources: "Look at that. It gave me the main takeaways, a few real facts, and it linked every point back to where it found it, so I can go check. That's a real research brief. From an agent I built in about four minutes."

### Step 4 - The nudge (the honest loop) [6:30-8:00]
- Do NOT pretend it was perfect. This is the trust beat and it's core Tyler.
- "Now here's the part most people won't show you. It's good, but it's not perfect. Look here, this point is a little thin, and I actually want it to focus more on the free tools, not the paid ones."
- Nudge it live, in plain English: "So I just tell it. 'This is close. Cut the paid tools, go deeper on the free ones, and add one line on why each is worth it.' And it goes and fixes it."
- Land the lesson: "That's the whole rhythm of working with an agent, right? It gets you like 80, 90 percent of the way there, fast, and then you nudge it the rest of the way. Never expect it to be a hundred percent on the first try. That's not a flaw, that's just how you use these. You steer, it drives."

---

## [8:00-9:15] WHAT YOU JUST BUILT (zoom out, make it click)

[Visual: back to Tyler, the three-part graphic returns: goal / tool / plain English, now with the agent's real output beside it.]

- "So let's zoom out for a second, because you just built a real AI agent and I want it to actually click."
- Tie it back to the three parts: "Remember the three things? A goal: research this topic. A tool: web search. And plain-English instructions: here's how I want it done. That's all an agent is. You've now got all three, running, in a folder on your computer."
- Make it feel repeatable: "And here's the thing that should get you a little excited. This same exact shape works for almost anything. Want an agent that reads a messy folder and organizes your files? Same three parts. Want one that drafts replies to your emails? Same three parts. You just change the goal and the tool. The pattern doesn't change."
- Seed the ceiling for the builders without scaring the beginners: "This is the simple version, on purpose. You can absolutely take this further, give it more tools, have it talk to your other apps. But you start here. This is the foundation, and it's the same foundation the fancy ones are built on."

---

## [9:15-10:30] HONEST LIMITATIONS (do NOT skip - this is the brand)

[Visual: Tyler straight to camera, no B-roll. The sincerity beat.]

- "Alright, let me be straight with you about what this does and doesn't do, because I'm not going to sell you a fantasy."
- It is not perfect and you have to check it: "It will not be a hundred percent right. It can grab a weak source, it can miss some nuance. So you read what it gives you. You don't just forward it to your boss without looking. It gets you most of the way, you finish the last bit."
- It is not set-it-and-forget-it: "This isn't a robot employee you turn on and never look at again. It's a really fast, really capable assistant. You still steer it. That's the deal."
- Keep it in scope: "And this simple version has limits, right? It's doing one job with one tool. When you need it to do bigger, connected things, there's more to learn. But you do not need any of that to get real value today, and that's the whole point."
- The honest close: "So what did you actually just get? A tool that does the boring 80 percent of a task in a couple minutes, so you can spend your time on the part that actually needs you. That's what an agent is really for. It's leverage, not magic."

---

## [10:30-12:15] BUILD YOUR FIRST ONE + CTA

[Visual: back to warm energy, Tyler to camera, then end card.]

- Lower the bar hard: "So here's what I want you to do. Do not try to build some big complicated system this week. Build one. One small agent that does one annoying thing you do all the time. Research something, sort something, draft something. Just one. That's how you actually learn this, and it takes about ten minutes, you just watched it."
- Hero CTA, one clean ask, the agent IS the doc: "And to make it dead simple, I put the exact agent we just built into a free pack you can copy. The instructions file, the setup, all of it, plus my newsletter where I break this stuff down every week. It's the first link in the description, free.tylerai.dev/youtube. Go grab it, copy the agent, and change the goal to whatever you actually need. It's free."
- Soft secondary, once: "And if you want to build these alongside other people who are figuring it out too, I've got a free community, it's linked down there as well. No pressure."
- Retention loop / genuine close: "But seriously, build one this week. Just one small thing. Tell me in the comments what you'd have your first agent do, I read every one. And I've got a video on how I chain a bunch of these together to run my whole content operation, if you want to see where this goes. I'll see you in the next one."

[End card: subscribe + the "I Automated My Entire Content Pipeline" thumbnail.]

---

## Filming notes
- Energy is warm and reassuring, not hyped. The enemy is intimidation, so every beat should feel like "see, that was easy," not "look how impressive this is."
- The build (2:30-8:00) is the retention zone. Keep it moving, cut the thinking time, but never fake the output. If the live run stumbles, keep it and narrate the nudge. Honest beats polished on this channel.
- The Fortune-500 line is used twice max (cold open + the "what an agent is" section). Keep it plain both times. It's authority, not a flex.
- Every on-screen thing must be REAL: the real folder, the real instructions file, the real brief the agent writes. No mockups.
- The limitations section (9:15) is the only place to slow down and go sincere. It earns the whole video's trust. Don't rush it.
- Pre-run the exact topic prompt once before filming to confirm the agent behaves, and keep a real backup brief on hand in case the live run stalls.
