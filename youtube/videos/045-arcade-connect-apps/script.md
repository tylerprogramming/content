# Script - 045 Give Claude Code Access to Your Real Apps in 7 Minutes (Arcade MCP)

Target length: 8 to 10 minutes.
Voice: Tyler talking to a friend over his shoulder. Short sentences. No hype. No em dashes. Software engineer, lean into the auth angle.

[DISCLOSURE: if this is a sponsored/partner video with Arcade, say so on camera and in the description.]

[NOTE: Do the whole build once, on camera, for real. Keep any send or destructive action in draft or safe mode first. Have a scratch Slack channel and a throwaway-ish Gmail context ready so nothing embarrassing shows.]

---

## 0:00 - 0:15 | Cold open, result first

[SHOW: terminal already open, Claude Code running. Screen recording of the finished result scrolling: calendar summary, drafted email replies, a Slack post confirmation.]

This is Claude Code. Watch what it just did.

It read my calendar, pulled the two emails that actually need a reply, and drafted them. Then it posted my standup to Slack.

All from the terminal. On my real accounts. A few minutes to set up, and I never touched an OAuth token. Let me show you.

[NOTE: Get right into it. No "hey guys, welcome back." First words are the demo. Keep this to ~12 seconds, tight. The whole hook is the result on screen.]

---

## 0:15 - 0:45 | The pain

[SHOW: Tyler on camera, or terminal with Claude Code sitting there, unable to do anything with real apps.]

Here's the honest version. Claude Code can already reach outside tools. You can add an MCP server, you can flip on a connector, and for one app, for yourself, that part is genuinely easy. I'm not going to pretend it isn't.

The auth is where it gets real. The second you want a bunch of apps, or you want to build something other people log into, or you want an agent doing this while you are not at your desk, you are the one holding it. Setting up the OAuth, storing the tokens, refreshing them, walking each user through their own consent, a little server to keep it all running.

I've done this for a living. Eight years as a software engineer, at IBM, at Chase, now doing AI work at Pfizer. That auth layer is always the part that eats the afternoon.

So the trick isn't writing better auth code. It's not writing it at all.

---

## 0:45 - 1:30 | What Arcade is, one breath

[SHOW: arcade.dev homepage. Highlight the tagline "Ship agents, not auth infrastructure." Then the tools/servers count.]

That's what Arcade does. In one breath: Arcade is an MCP runtime that handles the auth for you.

Their tagline is "ship agents, not auth infrastructure." That's the whole idea.

[SHOW: the tools catalog, scroll it a bit.]

They give you thousands of prebuilt MCP tools across the apps you already use. Gmail, Calendar, Drive, Slack, GitHub, Notion, Salesforce, a lot more.

You don't build the connection. You pick the tools you want, and Arcade does the per-user OAuth for you. You click authorize once, and it manages the tokens after that.

There's a free tier to start, then paid plans if you grow into it. Let me connect it.

[NOTE: Keep this section tight. It should feel like one exhale, not a product tour. Don't quote a hard tool count on camera unless you re-check it that day. "Thousands" is safe.]

---

## ~1:00 - 4:30 | Connect it live

[SHOW: Arcade dashboard. Start a small on-screen timer here so the "7 minutes" is honest.]

Okay. Step one, over in Arcade, I'm going to build what they call a Gateway.

A Gateway is just a bundle of the tools you pick, behind one URL. That's the whole concept. You choose your tools, you get a URL, that URL is what Claude talks to.

[SHOW: creating the Gateway, selecting tools. Click Gmail, Google Calendar, Slack, GitHub.]

So I'll add Gmail. Google Calendar. Slack. And GitHub. Four to start. You can always add more later.

[SHOW: the generated Gateway URL. Note free vs paid tiers honestly if visible.]

And there's my Gateway URL. That's the thing I need. I'll copy it.

[NOTE: Be honest on screen about tiers. There's a free tier and paid tiers. Don't oversell.]

Now the connection. This is the easy part. One command in Claude Code.

[SHOW: terminal, type the command out live so people see it.]

```
claude mcp add arcade --transport http "<YOUR_ARCADE_GATEWAY_URL>"
```

That's it. I'm telling Claude Code, add an MCP server called arcade, it's an HTTP transport, here's the URL. Enter.

[SHOW: confirmation that arcade was added.]

Let me verify it took.

```
claude mcp list
```

[SHOW: arcade in the list.]

There it is. And if I want the detail on it:

```
claude mcp get arcade
```

[SHOW: the details for the arcade server.]

Good. So the server is connected. But I haven't authorized any of my accounts yet. That happens the first time Claude actually uses a tool.

[SHOW: run a first, harmless read. Ask Claude to list your calendars or read your latest email subject line.]

So I'll ask it to do something small first. Something read-only.

> "List my Google Calendars."

[SHOW: the OAuth authorize prompt / link appears. Click through the Google consent screen live.]

And there's the OAuth pop. This is the one-time part. It's sending me to Google's actual consent screen, I sign in, I approve the scopes, and Arcade holds the token from here on. I never see it. I never paste it anywhere.

[NOTE: While the OAuth page loads, fill the dead air. Say something like: "This is the exact same consent screen you'd build yourself if you were doing this by hand. The difference is I'm not writing the callback handler, the token store, or the refresh logic. That's the afternoon Arcade just gave me back."]

[SHOW: back in the terminal, the calendar list comes through.]

And we're connected. Each tool authorizes the same way, once. Slack will do it, GitHub will do it, the first time I use them.

[NOTE: If you selected multiple Google tools, one Google auth may cover them. Show what actually happens, don't script an outcome.]

---

## 5:30 - 8:00 | Quick wins across tools

[SHOW: terminal, Claude Code. Do three quick actions, one per app, to show breadth.]

Alright. It's connected. Now let me show you what this actually buys you. Three quick things, across three apps.

**One, Gmail.**

[SHOW: prompt and result.]

> "What emails came in today that actually need a reply? Just list them, don't do anything yet."

[SHOW: Claude reads the inbox and lists the ones that matter.]

So it read my inbox and pulled out the ones that need me. Not the newsletters. Not the receipts. The ones a human has to answer.

Now watch. I'll have it act, but safely.

> "Draft replies to those two. Don't send. Just create drafts."

[SHOW: Claude creating drafts. Then open Gmail and show the drafts sitting there.]

Drafts only. Nothing sent. I'll open Gmail and there they are, waiting for me to read and hit send. That's the pattern I'd tell anyone to use. Let it draft, you approve.

**Two, Calendar.**

[SHOW: prompt and result.]

> "What does my day look like? Give me the short version."

[SHOW: the day summary.]

Reads the calendar, gives me the day in a few lines. Simple, but that plus the email triage is basically a morning brief.

**Three, Slack.**

[SHOW: prompt. Post to a scratch channel, not a real team channel.]

> "Post a quick standup to my #standup channel: shipped the arcade setup, drafting emails next."

[SHOW: Slack, the message appears in the channel.]

And there it is in Slack. Posted as me.

[NOTE: Use a personal or test workspace and a scratch channel. Don't spam a real team.]

So, three different apps, three real actions, one setup. And I could just as easily have had it summarize open GitHub issues, or file one to ClickUp. Same idea. The tools are already there.

[NOTE: Keep expectations honest. It's not always perfect. Say something like: "Is it perfect every time? No. Sometimes it grabs the wrong email or you have to nudge the prompt. Treat it like a capable assistant you still check, not autopilot."]

---

## ~6:30 | Wait, doesn't Claude already have connectors?

[SHOW: quick cut to Claude's connectors screen, then back to the terminal.]

Quick one, because someone is typing it right now. Yes, Claude has built-in connectors. If you just want Claude to touch your own accounts, use them. They are great.

You reach for Arcade when it is more than that. When you are building for other people, so each user connects their own accounts, not yours. When it is your own agent, not just chatting inside Claude. Or when you want the auth run like production. That is the line, and that is where the next video goes.

[NOTE: ~20 seconds. It lands harder here, right after they watched it work, than it would up front.]

---

## 8:00 - 9:00 | Why it's safe

[SHOW: back to camera, or the Arcade dashboard showing auth/logs if available.]

Now, the question I'd ask as an engineer. Is this safe? Because you just watched me hand Claude my email and my Slack.

Three things matter here.

One, it's per-user OAuth. It's using my real Google and Slack consent screens, with real scopes I approved. Same as any app you've ever signed into.

Two, the tokens are never hardcoded. I never see them, they're not in my repo, they're not in a config file on my machine. Arcade holds them. That's actually safer than the version most people hack together, where the token ends up in a dotfile somewhere.

Three, the actions are logged. There's a trail of what ran as me.

[NOTE: This is Tyler's credibility wedge. Deliver it plainly, from experience, not as a sales point.]

For me, having built these integrations at big companies, that's the part that makes it usable for real work instead of a toy. The auth is the hard part, and it's the part they took off my plate.

---

## 9:00 - end | CTA

[SHOW: Tyler on camera. End card / community link.]

So that's it. You go from Claude Code that can't touch anything, to Claude Code working across your real apps, in about the time it took to watch this.

If you want to go further, I made a companion video, "Build a Real AI Agent in 7 Minutes," where I take these same connected tools and actually turn them into an agent that runs a workflow. I'll link it right here.

And if you're building this stuff, come hang out in the community. Link's in the description. Tell me which app you'd connect first. I read every one.

I'll see you in the next one.

[NOTE: Soft close. No hard sell. End on the question.]
