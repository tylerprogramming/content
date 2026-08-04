# Filming Guide - 044 Arcade MCP Course

A module-by-module playbook: what to do, what to click, exact commands, and what to expect. Narration to say out loud is in blockquotes. Everything that sends stays in draft/safe mode first.

---

## Pre-recording setup (do ALL of this before you hit record)

Accounts and logins:
- [ ] Signed into arcade.dev in the browser.
- [ ] Signed into Google (the Gmail + Calendar you'll demo with). Use a demo/clean account if you don't want your real inbox on camera.
- [ ] Signed into Slack, and know which channel you'll post to (create a private #standup test channel so you don't spam a real team).
- [ ] Signed into GitHub, pick the repo you'll reference. Have 1-2 open issues and a recent commit so there's something to summarize.
- [ ] Signed into claude.ai in the browser.
- [ ] Claude Cowork / Desktop app installed and signed in.
- [ ] Claude Code installed and working in a terminal (`claude --version` runs).

Build the gateway BEFORE recording the walkthroughs (you record building it in Module 1, but have a working one ready so the walkthroughs don't stall):
- [ ] Arcade Gateway created with Gmail, Google Calendar, Slack, GitHub.
- [ ] Gateway URL copied to a scratch note you can paste from quickly.
- [ ] Decide: show the real URL or blur it. If real, use a throwaway gateway you delete after.

Safety / draft modes:
- [ ] Plan every prompt to say "don't send" / "save as draft" / "show me first."
- [ ] Have your Gmail Drafts folder ready to switch to on camera.
- [ ] Test channel in Slack ready.

Screen hygiene:
- [ ] Close noisy tabs, notifications off (do-not-disturb), clean terminal theme, readable font size (18pt+).
- [ ] Have a visible 7-minute timer ready for Module 3 (phone, or an on-screen timer added in edit).
- [ ] Do a throwaway dry run of each walkthrough once so you know it works and OAuth is already authorized where you want it pre-authorized (or leave one authorize on camera on purpose in Module 2).

---

## THE RESULT + PROMISE (0:00 - 2:30)

Shoot this AFTER you've recorded everything else, so you have real clips to montage. Grab ~2s each of: terminal drafting, Cowork triaging, browser posting to Slack.

> "Watch this. Same tools, three places... I set that up one time. One gateway, three surfaces, same tools."

Then talking head: state the promise and read the six-module chapter list (put it on screen as a lower-third). End with the draft-first honesty note.

Dead-air filler while clips load in edit: none needed, this is edited montage.

---

## MODULE 0 - Why the auth is the hard part (2:30 - 4:30)

Mostly talking head + one simple diagram (Claude | auth wall | your apps, then the wall becomes an "Arcade" box).

Say, in your own words:
> "Claude can't touch your real apps out of the box, and the reason isn't Claude. It's the auth. OAuth, tokens, scopes, refresh. I've built these for eight years and that's the hard part."
> "Arcade is an MCP runtime. Ship agents, not auth infrastructure. It does the per-user OAuth for you. 7,500-plus prebuilt tools across 81 servers."

No screen recording required here. Keep it tight, this is the "why," not the "how."

---

## MODULE 1 - Build the Arcade Gateway (4:30 - 9:00)

Screen recording of arcade.dev.

Do this, on camera:
1. Go to arcade.dev, sign in.
2. Create a new Gateway. Name it something obvious.
3. Add tools: Gmail, Google Calendar, Slack, GitHub. Click each deliberately.
4. Save the gateway.
5. Copy the Gateway URL.

> "A gateway is your chosen bundle of tools behind one URL. Pick the apps, Arcade wraps them, you get one address. That address is what we paste into all three surfaces."

Pricing honesty beat (say it, don't skip it):
> "There's a free tier, enough for this whole course. When we connect Claude's desktop and web apps later, Claude limits custom connectors: free plan is one custom connector, Pro/Max/Team/Enterprise give you more. Claude Code doesn't count against that, so the terminal is always open."

What to expect: the tool list is large; use search inside Arcade to find each app fast. If a tool asks you to pre-select scopes, take the defaults for the demo.

Dead-air filler while the gateway saves:
> "While that saves, keep this URL handy, we're going to paste it three separate times."

---

## MODULE 2 - Connect all three surfaces (9:00 - 15:00)

This is the money module. Same URL, three doors. Emphasize "same URL" out loud each time.

### Surface 1 - Claude Code (terminal)

```
claude mcp add arcade --transport http "<GATEWAY_URL>"
```

Verify:

```
claude mcp list
claude mcp get arcade
```

Trigger the OAuth authorize ON CAMERA (ask it to check Gmail, let the authorize popup appear, click through). This proves it's real.

> "One command. `claude mcp add`, name it arcade, transport http, paste the URL. Verify with `claude mcp list`. First time I use a tool it pops an OAuth authorize, I click once, I never touch a token."

What to expect: `claude mcp list` shows `arcade` with an http transport. First tool call opens a browser authorize window.

### Surface 2 - Claude Cowork / Desktop

Clicks, no command:

```
Settings > Customize > Connectors > Add custom connector > paste GATEWAY_URL > Save > Authorize
```

> "Same gateway, different door. No command here, just clicks. Settings, Customize, Connectors, Add custom connector, paste the same URL, save, authorize."

Point at the tools list once they appear:
> "Same tools show up. I didn't rebuild anything. I pasted one URL."

Say the public-URL note:
> "These connectors run from Anthropic's cloud, not your laptop, so the gateway has to be a public URL, and Arcade's is."

What to expect: after saving, the connector appears in the list; tools become available in the composer/tool menu. May prompt OAuth on first use.

### Surface 3 - Web (claude.ai)

Same flow in the browser:

```
Settings > Customize > Connectors > Add custom connector > paste GATEWAY_URL > Save > Authorize
```

> "Third time, same URL. Nothing installed. Paste, save, authorize. Same tools, in the browser, from anywhere."

Land the core line with the three-panel graphic all lit:
> "One gateway. Three surfaces. Same tools. I built the connection once and it's live in all three."

What to expect: identical to desktop. On free Claude you may hit the one-connector limit; if so, note it and pick the surface you care about.

---

## MODULE 3 - Walkthrough 1: Morning brief in Claude Code (15:00 - 20:00)

Start the visible 7-minute timer. Terminal.

Prompt 1 (type live, read-only):
> "Look at my Google Calendar for today and my unread Gmail from the last 24 hours. Give me a short brief: what meetings I have and when, and which emails actually need a reply from me. Rank the emails by how much they need me. Don't send anything."

Prompt 2 (action, still safe):
> "Draft replies to the top two emails only. Keep them short and in my voice. Save them as drafts in Gmail. Do not send."

Then switch to Gmail Drafts on camera and show the two drafts sitting there.

> "The agent gets you to 80, 90 percent, you do the last step. Draft first, always."

Show timer still under seven minutes.

What to expect: may re-authorize Calendar/Gmail if not pre-authorized. Ranking is a judgment call and won't be perfect, that's fine, say so. Drafts appear in Gmail Drafts, not Sent.

Dead-air filler while it reads email:
> "While it's going through the inbox, notice I told it not to send anything. I always start read-only. Look before you act."

---

## MODULE 4 - Walkthrough 2: Inbox triage in Cowork (20:00 - 25:00)

Cowork desktop app.

Prompt 1 (triage + draft):
> "Go through my unread email. Group it into three buckets: needs a reply from me, just needs me to read it, and can be ignored. For the 'needs a reply' bucket, write a short draft reply for each in my voice and save them as Gmail drafts. Don't send anything."

Prompt 2 (the file task, the Cowork differentiator):
> "Take the key points from the 'needs a reply' emails and save them as a short markdown file called triage-notes.md in my Documents folder, with a bullet per email and the person's name."

Open the written file on camera to show it landed on disk.

> "That's the Cowork difference. It reaches your apps through Arcade and your local files at the same time."

Admit limits on camera:
> "It'll misjudge which emails matter sometimes, and the draft voice needs nudging. Fine, because I review everything before it goes anywhere."

What to expect: Cowork will ask before writing files / may show a permission step, click allow. Drafts land in Gmail Drafts. The markdown file appears in Documents.

Dead-air filler while it sorts:
> "Sorting the inbox into those three buckets is honestly most of what triage even is."

---

## MODULE 5 - Walkthrough 3: Repo to Slack standup in the web app (25:00 - 29:00)

Browser, claude.ai. Frame it as "not at my machine."

Prompt 1 (draft, don't post):
> "Look at the open issues and recent commits in my GitHub repo [REPO NAME] from the last day. Summarize what changed and what's still open in three or four bullets. Draft a short standup message for our Slack #standup channel. Show me the draft first, don't post it yet."

Read the draft on camera, tweak one word (make the review step visible).

Prompt 2 (post):
> "That looks good. Post it to the #standup channel now."

Switch to Slack and show the message landed in the channel.

> "From a browser. On a machine with nothing installed. The connector follows your account."

What to expect: may authorize GitHub and/or Slack on first use. Use your private #standup test channel. If the repo is private, make sure the GitHub tool authorized the right account/org.

Dead-air filler while it pulls GitHub:
> "It's reaching GitHub through the same gateway we built once. Same URL as the terminal and the desktop."

---

## MODULE 6 - Which surface when + safety + CTA (29:00 - 31:30)

Talking head, slower on the safety part. Three-panel graphic with one-line labels.

Which surface when:
> "Code, the terminal, for building and automating, scriptable. Cowork, the desktop, for everyday work and anything touching your files, and the one to hand a non-terminal teammate. Web, for quick things from anywhere, zero setup."

Safety (this is the trust beat, don't rush):
> "Per-user OAuth. You authorize as yourself, once. Tokens are never hardcoded, you never see them. Every action is logged, so there's an audit trail. Real auth, no exposed tokens, a log of every action, that's the difference between a demo and something you run on real work."

Close on the core line + CTA:
> "One gateway, three surfaces, same tools. Build the connection once, assemble what you need from prebuilt tools wherever Claude is. Tell me in the comments what you connect first and on which surface, I read them. Links below. Pick one tool, one surface, and just try it."

If partner/sponsored: restate the disclosure on camera before the end screen.

---

## Timing cheat sheet

| Module | Segment | Surface | Target time | Running total |
|---|---|---|---|---|
| Intro | Result montage + promise + chapters | All | 2:30 | 2:30 |
| 0 | Why the auth is the hard part | Talking head | 2:00 | 4:30 |
| 1 | Build the Arcade Gateway | arcade.dev | 4:30 | 9:00 |
| 2 | Connect all three surfaces | Code + Cowork + Web | 6:00 | 15:00 |
| 3 | Walkthrough 1: morning brief | Claude Code | 5:00 | 20:00 |
| 4 | Walkthrough 2: inbox triage + file | Cowork | 5:00 | 25:00 |
| 5 | Walkthrough 3: repo to Slack standup | Web | 4:00 | 29:00 |
| 6 | Which surface when + safety + CTA | Talking head | 2:30 | 31:30 |

Target total: ~28-32 minutes. If long, trim Module 0 and tighten the recaps between modules; keep all three walkthroughs intact, they're the value.

---

## Recap beats (say a version of these between modules so the spine lands)

- After Intro: "One gateway, three surfaces. That's the spine."
- After M0: "The hard part is auth. Arcade takes it off your plate."
- After M1: "One gateway, four tools, one URL."
- After M2: "Setup's done. From here it's all real work."
- After M3: "Terminal for building. Now the desktop."
- After M4: "Desktop for everyday work with files. Now the browser."
- After M5: "All three doing real work. Now, which one when, and is it safe."
