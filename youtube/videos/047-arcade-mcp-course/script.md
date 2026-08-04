# Script - 044 Arcade MCP Course

**Target length:** ~28-32 minutes, chaptered.
**Core message, repeat it so it lands:** one gateway, three surfaces, same tools.
**Surfaces:** Claude Code (terminal), Claude Cowork/Desktop, claude.ai (web).

[DISCLOSURE: if sponsored/partner with Arcade, say so on camera and in the description.]

Voice reminders: person talking, short sentences. Open on the problem or the result, plainly. Admit limits. Draft before send. No em dashes. No hype words. Concrete before abstract.

Timestamps are speaking-target ranges. Real chapter times get set in /yt-chapters after the edit.

---

## THE RESULT + PROMISE (0:00 - 2:30)

[SHOW: fast three-way montage cut, terminal then Cowork then browser, same tools moving in each]

Watch this. Same tools, three places.

In the terminal, Claude Code just read my calendar and drafted two replies. Here, on my desktop in Cowork, the same Claude went through my inbox. And here, in the browser, on claude.ai, it pulled the open issues in my repo and posted a standup to Slack.

[NOTE: hold each of the three clips about two seconds so the viewer registers "same tools, different app"]

Here's the thing. I set that up one time. I built one connection, and then those same tools showed up in all three. One gateway, three surfaces, same tools. That's the whole idea, and I'm going to say it a lot, because it's the point.

[SHOW: cut to talking head]

So here's what this course is. We're going to build one thing called an Arcade Gateway. It's a bundle of prebuilt tools, Gmail, Calendar, Slack, GitHub, behind a single URL. Then we plug that one URL into Claude Code, into Cowork on the desktop, and into claude.ai in the browser. Connect once, works everywhere.

Then we don't just set it up and leave. We do three real walkthroughs, one on each surface. A morning-brief agent in the terminal. Inbox triage on the desktop. And a repo-to-Slack standup from the browser.

[SHOW: on-screen chapter list / lower-third of the six modules]

Here's the map. Module zero, why the auth is actually the hard part. Module one, we build the gateway. Module two, we connect all three surfaces. Modules three, four, and five are the real walkthroughs. And module six is which surface to use when, plus the safety piece, because this touches your real accounts.

One quick note before we start. Everything that sends, an email, a Slack message, I keep in draft or preview first. I'll show you the send, but nothing goes out until I look at it. Okay. Let's get into it.

[NOTE: RECAP BEAT - "One gateway, three surfaces. That's the spine. Let's talk about why this is even hard."]

---

## MODULE 0 - WHY THE AUTH IS THE HARD PART (2:30 - 4:30)

[SHOW: talking head, then a simple diagram, Claude on one side, your apps on the other, a wall labeled "auth" in the middle]

So let me tell you why this isn't already built in.

Claude is great. But out of the box, it can't touch your real apps. It can't read your Gmail. It can't see your calendar. It can't post to your Slack. And the reason isn't Claude being weak. The reason is the auth.

I've been a software engineer for about eight years. IBM, Chase, now I'm an AI engineer at Pfizer. And I've built these integrations, connecting software to people's real accounts, more times than I can count. I'll tell you straight, the auth is the hard part. Not the feature. The auth.

Because to let something act as you in Gmail, you need OAuth. You need tokens. You need the right scopes. You need to refresh those tokens when they expire. You need to store them somewhere safe and never leak them. That's the actual work. That's the part that takes days, and it's the part that gets you in trouble if you do it wrong.

[SHOW: the "auth wall" in the diagram gets replaced by a box labeled "Arcade"]

So here's where Arcade comes in. Arcade is an MCP runtime. Their tagline is "ship agents, not auth infrastructure," and that's exactly it. It handles the per-user OAuth for you. You click authorize once per tool, and it manages the tokens from there. You never see them. You never store them.

And it's not a small thing. Arcade has over 7,500 prebuilt tools across 81 servers. Gmail, Google Calendar, Drive, Slack, Teams, GitHub, Notion, Asana, all of it, already built. You're not writing a server. You're plugging into ones that exist.

[NOTE: this is the credible wedge. Don't oversell. State it and move on.]

That's the wedge for me. I'm not excited because it's easy. I'm interested because it removes the exact part that's genuinely hard and genuinely risky. And it takes real actions as you, with an audit trail, which we'll get to.

[NOTE: RECAP BEAT - "So the hard part is auth, and Arcade takes it off your plate. Let's go build the gateway."]

---

## MODULE 1 - BUILD THE ARCADE GATEWAY (4:30 - 9:00)

[SHOW: screen recording, arcade.dev, signing in]

Okay, module one. Let's build the gateway. This is the one thing we build, and everything else plugs into it.

Head to arcade.dev and make an account. I've already got one, so I'll sign in.

[SHOW: the dashboard, navigating to create a gateway]

Now, what is a gateway? Simple. A gateway is your chosen bundle of tools behind one URL. You pick which apps you want Claude to reach, Arcade wraps them up, and gives you a single address. That address is the thing you'll paste into all three surfaces later.

So let's make one. I'll create a new gateway and give it a name. I'll call mine something obvious so I recognize it later.

[SHOW: the tool picker, selecting Gmail, Google Calendar, Slack, GitHub]

Now I pick my tools. For this course I'm going to keep it to four, because these are the ones most people actually want. Gmail. Google Calendar. Slack. And GitHub.

[NOTE: click each one deliberately, let the viewer see them get added]

Gmail so Claude can read and draft email. Calendar so it knows my day. Slack so it can post updates. GitHub so it can see my repo. You can add way more later, there are thousands, but start small. Pick what you'll actually use.

[SHOW: the gateway saved, the gateway URL displayed]

And there it is. That's my gateway URL. This one address now represents all four of those tools. I'm going to copy it, and honestly, I'd keep it somewhere handy because you'll paste it three times.

[NOTE: on screen, blur or use a throwaway gateway if the URL is sensitive. Say this out loud.]

Quick honest note on pricing, because I'm not going to pretend it's all free. Arcade has a free tier, and it's enough to follow this whole course. When you connect to Claude's desktop and web apps later, those custom connectors have their own limit on Claude's side. On the free Claude plan you get one custom connector. Pro, Max, Team, and Enterprise give you more. So if you're on free Claude, you can still do this, you just pick the one surface you care about most for the connector. Claude Code doesn't count against that, so the terminal is always open to you.

[NOTE: RECAP BEAT - "So we have one gateway, four tools, one URL. Now we plug that URL into all three Claudes."]

---

## MODULE 2 - CONNECT ALL THREE SURFACES (9:00 - 15:00)

[SHOW: talking head, then a three-panel graphic, Code / Cowork / Web]

This is the heart of it. We have one gateway URL. We're going to connect it three times, once in each surface. And I want you to notice how it's the same URL every time. That's the whole point.

### Claude Code (terminal)

[SHOW: terminal]

Let's start in Claude Code, the terminal. This is one command.

```
claude mcp add arcade --transport http "<GATEWAY_URL>"
```

That's it. `claude mcp add`, I name it arcade, I tell it the transport is http, and I paste my gateway URL in quotes.

[SHOW: run it, then run the list command]

Now let me verify it's there.

```
claude mcp list
```

And there's arcade in the list. I can also get the detail on it.

```
claude mcp get arcade
```

[SHOW: first tool call triggering the OAuth authorize popup]

Now here's the auth part, the part Arcade handles. The first time I actually use a tool, it pops an OAuth authorize screen for that account. So if I ask it to check Gmail, it says "authorize Gmail," I click through my Google login, and I'm done. I do that once per tool. I never touch a token. That's Arcade doing the hard part.

[NOTE: actually trigger one authorize on camera so people see it's real and not scary]

Claude Code is connected. That's surface one.

### Claude Cowork / Desktop

[SHOW: Cowork desktop app, opening Settings]

Now the desktop. This is Claude Cowork, the desktop app. Same gateway, different door. And notice, no command here. This is all clicks, which is kind of the point of the desktop app.

I go to Settings. Then Customize. Then Connectors. Then Add custom connector.

[SHOW: the Add custom connector dialog, pasting the URL]

I paste the exact same gateway URL. The one I used in the terminal. I save it, and then I authorize, same OAuth flow as before.

[SHOW: the tools now appearing available in Cowork]

And now watch. The same tools show up here. Gmail, Calendar, Slack, GitHub. I didn't rebuild anything. I pasted one URL.

[NOTE: this is the "aha" moment of the whole course. Let it breathe. Point at the tools list.]

One thing worth saying. These custom connectors run from Anthropic's cloud, not from your laptop. That's why the gateway has to be a public URL, and Arcade's is public, so it just works. You're not exposing your own machine.

That's surface two.

### Web (claude.ai)

[SHOW: browser, claude.ai, Settings]

Now the browser. claude.ai. No install, nothing on your machine at all. And it's the exact same flow as the desktop.

Settings. Customize. Connectors. Add custom connector.

[SHOW: pasting the same URL in the browser]

Same URL. A third time. Paste, save, authorize.

[SHOW: tools available in the web app]

And there they are again. Same tools, in the browser, from anywhere. If I'm on a different computer, or honestly on my phone later, this connector follows my account.

[SHOW: talking head, three-panel graphic all lit up]

So stop and look at what just happened. One gateway. Three surfaces. Same tools. Terminal, desktop, browser. I built the connection once and it's live in all three. That's the sentence I want you to walk away with.

[NOTE: RECAP BEAT - "Setup's done. From here it's all real work. Three walkthroughs, one on each surface. Let's start in the terminal."]

---

## MODULE 3 - WALKTHROUGH 1: MORNING BRIEF IN CLAUDE CODE (15:00 - 20:00)

[SHOW: terminal, clean, a 7-minute timer in the corner starts]

Walkthrough one. In Claude Code. We're building a morning-brief agent. Gmail plus Calendar. And I'm putting a timer on screen, because the whole idea from Arcade is you go from nothing to something useful in one sitting.

Setup is nothing, honestly, because we already connected it. So let's just do it. Here's the exact prompt.

[NOTE: type this prompt live, don't paste, so it feels real]

> **Prompt:** "Look at my Google Calendar for today and my unread Gmail from the last 24 hours. Give me a short brief: what meetings I have and when, and which emails actually need a reply from me. Rank the emails by how much they need me. Don't send anything."

[SHOW: Claude authorizing Calendar if it hasn't, then pulling events, then pulling email]

So it's reading my calendar first. It's pulling today's events. Now it's going through unread Gmail. And notice I told it not to send anything. I always start read-only. Look before you act.

[SHOW: the brief output, meetings listed, emails ranked]

And there's my brief. Three meetings, laid out with times. And a ranked list of emails, the two at the top are the ones that actually need me, the rest are noise. That's genuinely useful, and that's just reading.

Now let's take an action. Still safe though. Here's the next prompt.

> **Prompt:** "Draft replies to the top two emails only. Keep them short and in my voice. Save them as drafts in Gmail. Do not send."

[SHOW: Claude drafting, then confirming the drafts are saved in Gmail]

It's drafting the two replies. And I said save as drafts, do not send. So it's writing them and dropping them into my Gmail drafts folder. Nothing left my account.

[SHOW: switching to Gmail, showing the two drafts sitting there]

And there they are. Two drafts, waiting for me. I read them, I tweak if I need to, I hit send myself. This is the pattern I want you to internalize. The agent gets you to 80, maybe 90 percent, and you do the last step. Draft first, always.

[SHOW: timer, still under seven minutes]

And look at the timer. We went from nothing to a working morning-brief agent that reads my day and drafts my replies, in under seven minutes. That's surface one doing real work.

[NOTE: RECAP BEAT - "That was the terminal, for building. Now the desktop, for people who don't live in a terminal. Same tools."]

---

## MODULE 4 - WALKTHROUGH 2: INBOX TRIAGE IN COWORK (20:00 - 25:00)

[SHOW: Cowork desktop app, clean]

Walkthrough two. In Cowork, the desktop app. And here's why this surface matters. Not everyone lives in a terminal. Cowork is the friendly version, same Arcade tools underneath, but it's a desktop app with a normal interface and it can work with your files. So this is the one to send to someone on your team who isn't going to open a command line.

Setup, again, is nothing, because we already pasted the URL here in module two. So let's triage an inbox.

> **Prompt:** "Go through my unread email. Group it into three buckets: needs a reply from me, just needs me to read it, and can be ignored. For the 'needs a reply' bucket, write a short draft reply for each in my voice and save them as Gmail drafts. Don't send anything."

[SHOW: Cowork working through the inbox, grouping, then drafting]

So it's reading unread email, same as before, but watch it sort into the three buckets. Needs a reply. Just read. Ignore. That sorting alone is most of what inbox triage actually is.

[SHOW: the drafts being created]

And for the ones that need me, it's writing drafts and saving them, not sending. Same safety rule as the terminal. Draft first.

Now let me show the thing Cowork does that the terminal doesn't do as naturally. A file task.

> **Prompt:** "Take the key points from the 'needs a reply' emails and save them as a short markdown file called triage-notes.md in my Documents folder, with a bullet per email and the person's name."

[SHOW: Cowork writing the file to disk, then opening it]

So now it's taking what it found and writing it to an actual file on my desktop. There's the file. Bullets, names, the points I need. That's the Cowork difference, it reaches your apps through Arcade and your local files at the same time.

[SHOW: talking head brief cut]

So to be honest about the limits, it's not perfect. It'll misjudge which emails matter sometimes, and the draft voice needs nudging. But that's fine, because I'm reviewing everything before it goes anywhere. Same tools as the terminal, friendlier surface, plus files. That's surface two.

[NOTE: RECAP BEAT - "Terminal for building, desktop for everyday work with files. Now the browser, for when you're not even at your machine."]

---

## MODULE 5 - WALKTHROUGH 3: REPO TO SLACK STANDUP IN THE WEB APP (25:00 - 29:00)

[SHOW: browser, claude.ai, maybe framed like a different/borrowed computer]

Walkthrough three. In the browser. claude.ai. And the point of this one is you're not at your machine. Nothing is installed. But because the connector lives on your account, the same tools are right here. GitHub and Slack this time.

Let's do a repo-to-Slack standup.

> **Prompt:** "Look at the open issues and recent commits in my GitHub repo [REPO NAME] from the last day. Summarize what changed and what's still open in three or four bullets. Draft a short standup message for our Slack #standup channel. Show me the draft first, don't post it yet."

[SHOW: claude.ai authorizing GitHub if needed, pulling issues and commits]

So it's reaching GitHub through the same gateway. Pulling open issues. Pulling recent commits. And it's summarizing what actually moved.

[SHOW: the drafted standup message]

There's the standup draft. What I shipped, what's still open, short and clean. And I told it to show me first, not post. So let me read it.

[NOTE: actually read it on camera, tweak one word so it's clearly a review step]

Good. Now I'll let it post.

> **Prompt:** "That looks good. Post it to the #standup channel now."

[SHOW: the message posting to Slack, then switch to Slack to show it landed]

And it posts to Slack. Let me flip over to Slack, and there it is in the channel. From a browser. On a machine with nothing installed.

[SHOW: talking head]

That's the payoff of surface three. Zero setup on the device. The connector follows you. If you're traveling, on a borrowed laptop, whatever, the same tools are one login away.

[NOTE: RECAP BEAT - "So that's all three, doing real work: terminal, desktop, browser, one gateway. Let's talk about when to use which, and whether this is actually safe."]

---

## MODULE 6 - WHICH SURFACE WHEN + SAFETY + CTA (29:00 - 31:30)

[SHOW: three-panel graphic with a one-line label under each]

Okay. You've got the same tools in three places. So when do you use which? Here's how I think about it.

Claude Code, the terminal, is for building and automating. It's scriptable, it's fast, it's where I set up repeatable agents. If you write code, this is home.

Cowork, the desktop, is for everyday work, especially anything that touches your files. It's the one I'd hand to someone on my team who doesn't want a terminal. Same power, friendlier door.

And the web app is for quick things from anywhere, with zero setup. Not at your machine? That's the web app.

Same tools underneath, all three. You're just picking the door that fits the moment.

[SHOW: talking head, a little slower here, this is the trust part]

Now the part I care about most, because this touches your real accounts. Is this safe?

Here's why I'm comfortable with it, as someone who's built this stuff for a living. It's per-user OAuth. You authorize each tool as yourself, once. The tokens are never hardcoded, you never see them, they're not sitting in some config file waiting to leak. And every action is logged, so there's an audit trail of what the agent did as you.

That combination, real per-user auth, no exposed tokens, and a log of every action, is the difference between a demo and something you'd actually run on your real work. That's what makes this usable, not just a toy.

And I'll keep saying the honest part. Keep sends in draft first. Review before it acts. The agent gets you most of the way, you do the last step.

[SHOW: talking head, close]

So here's the whole idea, one more time. One gateway, three surfaces, same tools. You stop thinking about building a separate integration for every app in every place. You build the connection once, and you assemble what you need from prebuilt tools, wherever Claude happens to be.

If you set this up, I really want to know what you connect first and which surface you use it on. Tell me in the comments, I read them. Links to Arcade and the docs are below.

And if you want the walkthroughs and the templates I use, they're in the community, link's in the description. Go build something small first. Pick one tool, one surface, and just try it. That's it. I'll see you in the next one.

[SHOW: end screen, companion short + one more video]

[NOTE: if this is a partner video, restate the disclosure on camera before the end screen.]
