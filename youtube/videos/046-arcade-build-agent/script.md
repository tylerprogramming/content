# Script - Build a Real AI Agent in 7 Minutes: Claude Code + Arcade

Target runtime: 8-10 min. Direct, doable, honest. Tyler's voice: short sentences, person talking, "here's the thing," "right?", admit the limits, drafts before sends.
Format: BUILD-ONE-AGENT. We build ONE specific working agent, start to finish, live. Not a lecture, not a broad "connect all your apps" tour (that's the companion video, 045). No on-screen timer; "about seven minutes" stays as a spoken claim only.
The agent: a morning brief. Reads today's Google Calendar + unread Gmail, summarizes the day, flags which emails need a reply, then drafts those replies in draft/safe mode.

Standing rules: no em dashes, no hype words (insane, crazy, game-changer), no money amounts in the title, no hashtags. Show real runs. Drafts before sends. Tyler is a software engineer, 8 years, IBM and Chase, now AI engineer at Pfizer. Never imply he is not a developer.

[DISCLOSURE: if sponsored/partner with Arcade, say so on camera and in the description.]

---

## [0:00-0:15] COLD OPEN - result first - word for word

[SHOW: the finished agent's output already on screen. A clean morning brief: today's calendar laid out, three emails flagged as "needs a reply," and three drafts sitting ready.]

"This is an AI agent I built. It just read my calendar and my inbox, told me what my day looks like, flagged the three emails that actually need a reply, and drafted all three for me.

Let me build this whole thing from scratch. About seven minutes. Starting now."

[NOTE: keep this tight. No "hey what's up guys," no channel intro. First frame is the result.]

---

## [0:15-0:40] THE STAKES - why this is usually hard

[SHOW: Tyler on camera. Simple text builds: "TOOLS + AUTH". The word AUTH gets circled.]

"A real agent, not a chatbot, one that actually does a job, needs two things. Tools, and permission to use them.

The tools are easy. And I'll be honest, connecting one app to Claude for yourself is easy too. The auth bites when you want an agent doing this on its own, touching your real accounts while you are not sitting there watching it. That is OAuth, tokens, scopes, refresh, per user. I've built these integrations at Fortune 500 companies. That part is genuinely the hard part.

So we're not going to build it. We hand the auth to something else, and spend our time on the agent itself."

---

## [0:45-2:30] FAST SETUP - the means, not the point

[NOTE: keep this section moving. This is plumbing. The viewer is here for the agent, so don't linger.]

### Arcade in one line [0:45-1:15]

[SHOW: arcade.dev landing page. Tagline visible: "Ship agents, not auth infrastructure."]

"The thing I'm using is called Arcade. One line: it's a runtime for agents that handles the auth for you. Their whole pitch is ship agents, not auth infrastructure. Thousands of prebuilt tools across the apps you already use, Gmail, Calendar, Slack, GitHub, all of it. You don't wire up OAuth, it does the per-user OAuth for you. You click authorize once, and it manages the tokens."

[DISCLOSURE: if partner/sponsored, say it here, plainly. "Arcade's sponsoring this one, and I'd use it either way, here's why."]

[NOTE: don't quote a hard tool/server count on camera unless you re-checked it that day. "Thousands" is safe and doesn't age.]

### Build a Gateway [1:15-1:50]

[SHOW: Arcade dashboard. Create a new Gateway. Search and add two tools: Gmail and Google Calendar. Grab the Gateway URL.]

"First I build what Arcade calls a Gateway. That's just a bundle of the tools I want behind one URL. For this agent I only need two things: Gmail and Google Calendar. So I add those two, and I grab the Gateway URL. That's it. That URL is my toolbox."

[NOTE: on-screen, only add Gmail + Calendar. Keep the scope tight so it matches the agent we build. Slack comes later as the "level up."]

### Connect to Claude Code [1:50-2:30]

[SHOW: terminal. Type the command live.]

"Now I plug that toolbox into Claude Code. One command."

```
claude mcp add arcade --transport http "<GATEWAY_URL>"
```

[SHOW: verify it registered.]

```
claude mcp list
```

"And there it is, arcade, connected. Quick honesty note: the first time the agent actually touches Gmail, it's going to pop an OAuth screen and ask me to authorize. That's the good kind of friction. It means my token isn't hardcoded anywhere. I authorize once, and it's done."

[NOTE: trigger and clear the OAuth authorize now, before the build, so the live run doesn't stall on it. Show the authorize screen briefly so viewers see it's real, then start the build clean.]

---

## [2:30-6:30] BUILD THE AGENT LIVE

[SHOW: clean terminal, Claude Code ready.]

"Okay. Let me build the agent."

### The prompt [2:30-3:30]

[NOTE: this is the whole build. The agent IS the prompt. Type it live, say it as you go.]

"An agent is a goal, the tools it's allowed to use, and plain English telling it what to do. We've got the tools connected. So the agent is just this prompt. Here's the exact thing I type."

[SHOW: type this into Claude Code, live.]

```
You are my morning brief agent. Do this in order:

1. Read today's events from my Google Calendar. Give me a short
   rundown of my day, in time order.
2. Read my unread emails from Gmail from the last 24 hours.
3. Tell me which of those actually need a reply from me, and why.
   Skip newsletters, receipts, and notifications.
4. For each email that needs a reply, write a draft reply in my
   voice: short, friendly, direct. Save each one as a Gmail draft.
   Do NOT send anything.

Show me the day summary and the reply list first. Then create the
drafts. If you're unsure whether something needs a reply, ask me,
don't guess.
```

"Read that last part. Save as a draft, do not send. And if you're not sure, ask me. That's the rule for every agent that can touch your real accounts. Drafts first, always. You never let it send on the first run."

### Let it run [3:30-6:30]

[SHOW: Claude Code working. First tool call triggers the Gmail/Calendar authorize if you didn't pre-clear it. Then it reads calendar, reads inbox, thinks.]

[NOTE: speed-ramp the thinking time in the edit so nothing drags, but keep it real. Narrate what's actually happening.]

"Watch what it's doing. It's calling the Calendar tool first. Now it's pulling my unread Gmail. And this is the agent part, right? I didn't tell it which emails to open or how to decide what matters. I gave it the goal and the tools, and it's figuring out the steps.

It's reading through the inbox now. Sorting the stuff that needs me from the stuff that's just noise."

[Dead-air filler options while it runs, pick as needed:]
- "This is the moment that used to take a week of auth setup, by the way. That's the whole point of offloading it."
- "Notice it's doing this as me. It's my real inbox, my real calendar. Not a demo account."
- "It's going to come back with the day first, then the reply list, then the drafts. That order matters, I want to see its reasoning before it writes anything."

"And it's landing."

---

## [6:30-8:00] PAYOFF - the real output

[SHOW: the finished output. Read real lines off the screen.]

"Look at that.

So here's what it gave me. The day, in order: a nine a.m. standup, a call at eleven, a block for filming this afternoon. Then the emails that need me. It flagged three. This one from a viewer asking about the last video. This one about a partnership. And this one where someone's waiting on an answer from me. It skipped the newsletters and the receipts, exactly like I asked.

And then, the drafts."

[SHOW: open the Gmail drafts folder. Three real drafts sitting there. Open one.]

"Three drafts, sitting in my Gmail, ready. Here's one. It's short, it's in my voice, it actually answers the question. Nothing got sent. They're drafts. I read them, I tweak the one that needs it, I hit send myself.

That's a real agent. It read my accounts, made a judgment call about what matters, and did the boring first draft of the work. Built from scratch, in about seven minutes."

[NOTE: be honest if the live run flagged the wrong email or wrote a weak draft. Keep it and say so. "See, that draft's a little stiff, I'd fix that line." Honest beats polished on this channel.]

---

## [8:00-9:00] LEVEL UP - extend it and keep it safe

[SHOW: back to Tyler, or the terminal.]

"Okay, so you've got the shape. Let me show you where this goes, fast.

Adding more is just adding tools. Want it to post the day to Slack every morning? Go back to the Gateway, add the Slack tool, add one line to the prompt: post the summary to my standup channel. Same pattern. You change the goal and the tools, the shape doesn't change.

You can also run it on a schedule, so the brief and the drafts are just waiting for you when you sit down. That's the version I actually use.

And keep it safe, because this touches your real accounts. Three rules. One, drafts before sends, always, until you trust it. Two, Arcade's doing per-user OAuth, so your tokens aren't sitting in a file somewhere, and every action is logged, you can see what it did. Three, start narrow. Two tools, one job. Add more once it's earned it. That's how you use this for real work instead of a toy."

---

## [9:00-end] CTA

[SHOW: warm energy, Tyler to camera, then end card.]

"So here's what I want you to do. Build this one. Not a big system. This one agent. It's the exact prompt on your screen, it takes about seven minutes, and it'll actually save you time tomorrow morning.

I put the whole thing in a free pack you can copy. The exact prompt, the setup, the safety rules, plus my newsletter where I break this stuff down every week. First link in the description, free.tylerai.dev/youtube.

And I've got a free community if you want to build these alongside other people figuring it out too. Linked down there, no pressure.

Two more things. If you want to connect all your apps to Claude Code, not just these two, I made a companion video that's all about that setup, I'll link it. And if you want the full thing, start to finish, there's a whole course. But start with this one agent. Tell me in the comments what you'd have yours do first. I'll see you in the next one."

[End card: subscribe + the companion "connect all your apps" (045) thumbnail.]

---

## Filming notes
- The retention zone is the live build, 2:30 to 6:30. Keep it moving, cut the thinking time in the edit, never fake the output.
- Pre-clear the OAuth authorize before the build so the run is spent on the agent, not waiting on a login screen. Show the authorize screen briefly so viewers know it's real.
- Pre-run the exact morning-brief prompt once before filming to confirm it behaves, and keep a real backup output on hand in case the live run stalls.
- The Fortune 500 / engineer line is authority, not a flex. Use it once in the stakes section, plainly.
- Everything on screen is real: real Gateway, real inbox, real calendar, real drafts. No mockups.
- If the run flags a wrong email or writes a stiff draft, keep it and narrate the fix. Honest is the brand.
- Disclosure: if this is sponsored/partner with Arcade, say it on camera in the setup section and put it in the description.
