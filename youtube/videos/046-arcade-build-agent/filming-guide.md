# Filming Guide - Build a Real AI Agent in 7 Minutes: Claude Code + Arcade

Do-this / click-that playbook for shooting 043. The point of this video is ONE agent, built start to finish, with a visible 7-minute timer. Everything on screen is real. Drafts before sends, always.

[DISCLOSURE: if this is sponsored/partner with Arcade, say it on camera in the setup section AND put it in the description.]

---

## Pre-recording setup (do all of this BEFORE you hit record)

1. **Clean the desktop.** One terminal, one browser. Big readable font in the terminal (18pt+). Hide personal bookmarks and notifications.
2. **Pick the demo account.** Use a real Gmail + Google Calendar you're comfortable showing on camera, or a lightly-staged one with real-looking unread emails. You want at least: 2-3 emails that genuinely need a reply, plus some newsletters/receipts it should skip. Put 2-3 real events on today's calendar.
3. **Build the Arcade Gateway ahead of time** (you'll re-show the key steps on camera, but have a working one ready as backup):
   - Log in at arcade.dev, create a new Gateway.
   - Add exactly two tools: **Gmail** and **Google Calendar**. Nothing else yet (Slack is the "level up" beat).
   - Copy the Gateway URL. Keep it pasteable.
4. **Pre-clear the OAuth authorize OFF the timer.** Connect the gateway to Claude Code (command below), then run one small tool call so Gmail/Calendar throws the OAuth authorize screen. Authorize it. Do a quick screen-capture of that authorize screen so you can show it during setup without stalling the live build. After this, the 7-minute build runs clean.
5. **Pre-run the exact morning-brief prompt once** to confirm the agent behaves on this account. Save the real output as a backup in case the live run stalls.
6. **Reset for the take.** Empty the terminal scrollback. If you want the drafts to be created fresh on camera, delete the drafts the pre-run created so the drafts folder is empty when you start.
7. **Timer.** Have a 7:00 timer graphic ready to drop in the corner in the edit, OR a real on-screen timer you start at the build. It should be visible and it should be honest.

---

## Timing cheat sheet

| Time | Section | On screen | Timer |
|---|---|---|---|
| 0:00-0:15 | Cold open (result) | Finished brief + 3 drafts | off |
| 0:15-0:45 | The stakes | Tyler, "TOOLS + AUTH" text | off |
| 0:45-1:15 | What Arcade is | arcade.dev, tagline | off |
| 1:15-1:50 | Build the Gateway | Arcade dashboard, add Gmail + Calendar | off |
| 1:50-2:30 | Connect to Claude Code | terminal: mcp add + list + authorize screen | off |
| 2:30-3:30 | The prompt | terminal, type the prompt live | START (7:00) |
| 3:30-6:30 | Let it run | Claude Code working, narrate | running |
| 6:30-8:00 | Payoff | real output + open the drafts | STOP |
| 8:00-9:00 | Level up | add Slack / schedule / safety | off |
| 9:00-end | CTA | Tyler + end card | off |

---

## Step-by-step

### 1. Cold open (result first)
Have the finished brief and the three drafts already on screen. First words, no intro:

> "This is an AI agent I built. It just read my calendar and my inbox, told me what my day looks like, flagged the three emails that actually need a reply, and drafted all three for me. Let me build this whole thing from scratch. About seven minutes. Starting now."

### 2. The stakes
Straight to camera. Build the text "TOOLS + AUTH", circle AUTH.

> "A real agent needs two things. Tools, and permission to use them. The tools are easy. It's the permission that stops everyone. I've built these at Fortune 500 companies. The auth is the hard part. So we're not going to build it."

### 3. What Arcade is (keep it to ~30s)
Show arcade.dev with the tagline visible.

> "It's a runtime for agents that handles the auth for you. Ship agents, not auth infrastructure. Seven thousand five hundred prebuilt tools, eighty-one servers. You click authorize once, it manages the tokens."

[If sponsored, disclose here, plainly.]

### 4. Build the Gateway
On the Arcade dashboard: create Gateway, add Gmail, add Google Calendar, copy the URL.

> "A Gateway is just a bundle of tools behind one URL. For this agent I need two: Gmail and Calendar. Add those, grab the URL. That's my toolbox."

### 5. Connect to Claude Code
In the terminal, type live:

```
claude mcp add arcade --transport http "<GATEWAY_URL>"
```

Then verify:

```
claude mcp list
```

> "One command. And there it is, arcade, connected. First time it touches Gmail it'll ask me to authorize. That's the good kind of friction, my token isn't hardcoded anywhere."

Cut in your pre-captured authorize screen here so viewers see it's real, without stalling.

### 6. Build the agent live (START THE TIMER)
Start the 7:00 timer. Type this exact prompt into Claude Code, live:

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

> "An agent is a goal, its tools, and plain English. The tools are connected, so the agent is just this prompt. And read the last part: save as a draft, do not send. Drafts first, always."

### 7. Let it run (narrate, don't go silent)
Speed-ramp the thinking time in the edit but keep it real. Narrate the actual tool calls.

> "It's calling Calendar first. Now it's pulling my unread Gmail. This is the agent part, I gave it the goal and the tools, it's figuring out the steps."

**Dead-air fillers while it runs:**
- "This is the moment that used to be a week of auth setup."
- "It's doing this as me, real inbox, real calendar, not a demo account."
- "It'll come back with the day, then the reply list, then the drafts. That order matters, I want its reasoning before it writes anything."

### 8. Payoff (STOP THE TIMER)
When it lands, stop the timer, note the time.

> "Look at that. Stop the timer."

Walk the real output: the day in order, the emails it flagged and why, the ones it skipped. Then open the Gmail drafts folder and open one draft.

> "Three drafts, sitting in my Gmail, ready. Short, in my voice, actually answers the question. Nothing got sent. I read them, tweak, and send myself."

[If it flagged wrong or wrote something stiff, KEEP IT and say so. Honest beats polished.]

### 9. Level up
Cover three quick extensions, then safety:
- Add Slack: back to the Gateway, add the Slack tool, one line in the prompt to post the summary.
- Schedule it so the brief is waiting when you sit down.
- Safety: drafts before sends; per-user OAuth so tokens aren't in a file and actions are logged; start narrow, two tools one job.

### 10. CTA
Warm, one clean ask.

> "Build this one agent. It's the exact prompt on screen, about seven minutes. I put the whole thing in a free pack you can copy, first link in the description, free.tylerai.dev/youtube. Free community's linked too. Want to connect all your apps, not just these two? Companion video's linked. Tell me in the comments what you'd have yours do first."

End card: subscribe + the companion 042 thumbnail.

---

## What to expect / gotchas
- **First tool call = OAuth popup.** Pre-clear it off-timer (see setup step 4) or the build stalls on a login screen.
- **It may ask a clarifying question** ("should I reply to X?") because the prompt tells it to ask when unsure. That's good, it's honest, keep it in.
- **Draft creation is separate from reading.** Confirm on the pre-run that it actually saves Gmail drafts and does not send. If the tool set only allows read, note it and adjust the Gateway.
- **Time drift.** If the live run goes past 7:00, that's fine, be honest about it. Do not fake the timer. The promise is "about seven minutes."
- **Backup ready.** If the live run fails, cut to the pre-run real output and say "here's the run I did earlier, same prompt."
