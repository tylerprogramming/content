# Filming Guide - 042 Give Claude Code Access to Your Real Apps in 7 Minutes (Arcade MCP)

A do-this / click-that playbook. Shoot the build once, for real. Keep sends in draft mode first.

[No disclosure needed — Arcade is not sponsored, confirmed 2026-08-13.]

---

## Pre-recording setup (do all of this BEFORE you hit record)

Get these ready so recording is one clean take, not a debugging session.

- [ ] **Arcade account** created and logged in at https://www.arcade.dev/ in a browser tab.
- [ ] **Google account** you're comfortable showing on screen. Consider a demo Gmail with a few realistic-looking emails already in it (a couple that "need a reply," plus newsletters/receipts for contrast).
- [ ] **Slack workspace** you control, with a scratch **#standup** channel. Do NOT use a real team channel.
- [ ] **GitHub account** signed in (even if you only tease it, the auth should be ready).
- [ ] **Claude Code** installed and working in your terminal. Run `claude` once to confirm it launches.
- [ ] **Terminal font bumped up** so it's readable on mobile. Dark theme, clean prompt, no clutter in the working dir.
- [ ] **Remove any existing arcade MCP server** so the `add` is clean on camera: `claude mcp remove arcade` (ignore the error if it isn't there).
- [ ] **Gateway URL** copied somewhere you can grab it, but plan to create the Gateway live for the demo.
- [ ] **On-screen timer** ready (or plan to add a countdown/counter in edit). Start it when you begin building the Gateway.
- [ ] **Screen recording** set to capture terminal + browser. Test that OAuth pop-ups are captured (they sometimes open a new window).
- [ ] **Notifications off.** No Slack DMs, no email toasts, no calendar alerts popping mid-take.
- [ ] Do a **dry run** of the three quick-win prompts once off-camera so you know they behave, then reset (delete the drafts, clear the Slack test message) before the real take.

---

## Section 1 - Cold open (0:00 - 0:15)

**Goal:** show the finished result before you explain anything.

Record this LAST, after you've done the real build, so you can screen-capture the actual outputs (calendar summary, drafted replies, Slack confirmation) and scroll them fast.

> "So this is Claude Code. And right now it just read my calendar, pulled the two emails that need a reply, and drafted them. Then it posted my standup to Slack. All from the terminal, using my real accounts. About seven minutes to set up. Let me show you how."

**On screen:** terminal scroll of the real results.

---

## Section 2 - The pain (0:15 - 0:45)

Talk straight to camera or over a static terminal.

> "Out of the box, Claude Code can't touch your real apps. Normally connecting it means OAuth, tokens, scopes, a little server. I've done this for a living, eight years as an engineer. The auth layer is always the hard part."

**No slides needed.** This is credibility, delivered plainly.

---

## Section 3 - What Arcade is (0:45 - 1:30)

**On screen:** arcade.dev homepage.

1. Point at the tagline: **"Ship agents, not auth infrastructure."**
2. Scroll to the tools / servers catalog.

> "Arcade is an MCP runtime that handles the auth for you. Over seven thousand five hundred prebuilt tools, across eighty one servers. You pick the tools, it does the per-user OAuth."

Keep it to one breath. Don't tour the site.

---

## Section 4 - Connect it live (1:30 - 5:30)

**Start the on-screen timer now.**

### Build the Gateway

1. In Arcade, create a new **Gateway**.
2. Add tools: **Gmail, Google Calendar, Slack, GitHub**.
3. Copy the **Gateway URL**.

> "A Gateway is just a bundle of the tools you pick, behind one URL. I'll add Gmail, Calendar, Slack, GitHub. Copy the URL. That's the thing I need."

**Be honest about tiers** if pricing is visible: there's a free tier and paid tiers.

### Add it to Claude Code

Type this live:

```
claude mcp add arcade --transport http "<YOUR_ARCADE_GATEWAY_URL>"
```

> "One command. Add an MCP server called arcade, HTTP transport, here's the URL. Enter."

### Verify

```
claude mcp list
```

```
claude mcp get arcade
```

> "Let me check it took. There it is. And the detail on it, good."

**Expect:** `arcade` shows in the list; `get` shows the transport and URL.

### First tool use triggers OAuth

Ask for something read-only first:

> "List my Google Calendars."

**Expect:** an OAuth authorize link/pop. Click through Google's real consent screen live, sign in, approve.

> "There's the OAuth pop. One-time part. Google's actual consent screen. Arcade holds the token from here, I never see it, I never paste it anywhere."

**Filling dead air while OAuth loads** (this is where recordings stall, so have this ready):

> "This is the same consent screen you'd build yourself by hand. The difference is I'm not writing the callback handler, the token store, or the refresh logic. That's the afternoon Arcade just gave me back. Every tool authorizes like this once. Slack and GitHub will do the same the first time I use them."

**Expect:** back in the terminal, the calendar list returns. If one Google auth covers multiple Google tools, show what actually happens, don't narrate a fixed outcome.

---

## Section 5 - Quick wins (5:30 - 8:00)

Three actions, one per app. Type each prompt live.

### Gmail (read, then draft-only)

> "What emails came in today that actually need a reply? Just list them, don't do anything yet."

**Expect:** a short list of the real ones, filtering out noise.

> "Draft replies to those two. Don't send. Just create drafts."

**Expect:** drafts created. **Cut to Gmail** and show the drafts sitting unsent.

> "Drafts only. Nothing sent. Let it draft, you approve. That's the pattern."

### Calendar

> "What does my day look like? Give me the short version."

**Expect:** a few-line day summary.

### Slack (scratch channel only)

> "Post a quick standup to my #standup channel: shipped the arcade setup, drafting emails next."

**Expect:** message posts. **Cut to Slack** and show it in the channel, posted as you.

**Honesty beat:**

> "Is it perfect every time? No. Sometimes it grabs the wrong email or you nudge the prompt. Treat it like an assistant you still check, not autopilot."

---

## Section 6 - Why it's safe (8:00 - 9:00)

Back to camera, or show the Arcade dashboard (auth list / logs if available).

Hit three points, plainly:

1. **Per-user OAuth** - your real consent screens, real scopes you approved.
2. **Tokens never hardcoded** - not in your repo, not in a dotfile, Arcade holds them. Safer than the hand-rolled version.
3. **Actions are logged** - there's a trail of what ran as you.

> "Having built these at big companies, that's the part that makes it usable for real work instead of a toy. The auth is the hard part, and they took it off my plate."

---

## Section 7 - CTA (9:00 - end)

**Stop the timer.** End card + community link.

> "From Claude Code that can't touch anything, to Claude Code across your real apps, in about the time it took to watch this. I made a companion video, Build a Real AI Agent in 7 Minutes, where I turn these same tools into an agent. Come hang out in the community, link in the description. Tell me which app you'd connect first. I read every one."

---

## Timing cheat sheet

| Time | Section | On screen | Must-capture |
|---|---|---|---|
| 0:00 - 0:15 | Cold open, result first | Terminal, real results scrolling | Record last from real build |
| 0:15 - 0:45 | The pain | Camera or static terminal | The auth-is-hard credibility line |
| 0:45 - 1:30 | What Arcade is | arcade.dev homepage | Tagline + 7,500 tools / 81 servers |
| 1:30 - 5:30 | Connect it live | Arcade dashboard + terminal | Gateway build, `mcp add`, `mcp list`, OAuth pop. Start timer |
| 5:30 - 8:00 | Quick wins | Terminal + Gmail + Slack | Gmail draft-only, Calendar summary, Slack post |
| 8:00 - 9:00 | Why it's safe | Camera / Arcade dashboard | The three safety points |
| 9:00 - end | CTA | End card + community link | Companion video tease, stop timer |

---

## Commands quick-reference (copy list)

```
claude mcp remove arcade            # pre-record cleanup, ignore error if absent
claude mcp add arcade --transport http "<YOUR_ARCADE_GATEWAY_URL>"
claude mcp list
claude mcp get arcade
```

Prompts to type on camera:
- "List my Google Calendars."
- "What emails came in today that actually need a reply? Just list them, don't do anything yet."
- "Draft replies to those two. Don't send. Just create drafts."
- "What does my day look like? Give me the short version."
- "Post a quick standup to my #standup channel: shipped the arcade setup, drafting emails next."
