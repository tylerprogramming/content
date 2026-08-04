# Filming guide

Everything here is real and already working on your machine. Nothing needs
mocking. The risk in this video is not that a demo fails, it is that a demo is
slow, so the timings below tell you what to cut.

---

## Pre-recording setup

**The night before**

1. `cd ~/jarvis && git status` should be clean. You are filming the
   `public-prep` branch.
2. Delete the test reports so the documents panel starts believable:
   `rm -f reports/2026-08-0*.md reports/index.md && jarvis index`
   Then run `jarvis agent morning` and `jarvis agent radar` once so the panel
   has two real, current reports rather than week-old ones.
3. **Start Kokoro:** `jarvis voice start`, then confirm `jarvis voice status`
   says up. It does not survive a reboot and the voice chain fails over to
   ElevenLabs silently, so if you skip this the "free local voice" demo is
   quietly a lie.
4. `jarvis doctor` and screenshot it. You want local whisper: yes, kokoro: yes.

**Right before recording**

- Browser at `localhost:4747`, hard refresh, hide bookmarks bar.
- Terminal font up to at least 16pt. Everything you type gets read on a phone.
- Editor open with three files in tabs, in this order:
  `agents/postmortem.md`, `~/content/BRAIN/youtube/brain.md`, `data/vitals.json`
- Close Slack, mail, notifications. The HUD is dark, popups are bright.
- Quiet the terminal prompt if it shows a long path.

**Have ready to paste**

```
how am I tracking this week?
```
```
what did radar find this morning?
```
```bash
jarvis voice install --native
jarvis voice start
jarvis doctor
npm run setup
```

---

## Step 1 - Hook (0:00, target 30s)

**What you do:** Start on `brain.md` already open, not on the HUD. Scroll
slowly to a rule with a `[confirmed YYYY-MM-DD]` stamp.

**What you say:** Hook A from `hooks.md`, word for word.

**Watch out:** If no rule in `brain.md` has a recent confirmed stamp, run
`jarvis agent postmortem` the day before so there is a genuine one. Do not
hand-write the line. The entire hook is that you did not write it.

---

## Step 2 - The HUD tour (0:30, target 90s)

**What you do:** Cut to the browser, full screen. Let it sit for two seconds
before you talk. Move the mouse slowly across each panel as you name it. Hover
one agent so the tooltip shows.

**What you say:** Left rail top to bottom, then the ring, then the bar. Then
the OpenPaw concession.

**Watch out:** Do not click anything yet. This is orientation only.

---

## Step 3 - Ask it something (2:00, target 2m30s)

**What you do:** Click the command bar, paste `how am I tracking this week?`,
press enter.

**What happens:** A `log` line shows the brain, then a tool chip appears saying
`Read`, then text streams in. Takes about 15 to 25 seconds total.

**Dead air filler:** While the tool chip is up, say the "it went and read the
actual file, it is not guessing" line. That is the most important sentence in
this section and it lands better while the evidence is on screen.

**Then:** Click the mic, say the radar question out loud, and let it transcribe.

**Watch out:** The mic needs browser permission. Grant it once before you
record or the prompt shows up on camera. Also confirm `jarvis doctor` said
local whisper yes, otherwise this silently uses the browser and your claim is
wrong.

---

## Step 4 - Agents are markdown (4:30, target 2m30s)

**What you do:** Switch to the editor, `agents/postmortem.md`. Scroll from the
frontmatter down through the steps. Then split-screen with `brain.md`.

**What you say:** "It is a markdown file, that is the whole thing." Then the
schedule line, then the reboot point, then the playbook step.

**Watch out:** This is the thesis of the video. Slow down, do not rush to the
next demo. If the edit needs to lose 60 seconds, take them from Step 5, not
here.

---

## Step 5 - Run radar live (7:00, target 2m30s on screen)

**What you do:** Back to the HUD. Click RADAR on the ring.

**What happens:** The dot lights up. The sweep takes about **3 minutes 20
seconds** for 10 channels, then the agent writes a report and it appears in the
documents panel.

**How to handle it:** Do not sit through it. Say the relative-velocity
explanation while it starts, then cut. Rejoin when the report appears. In the
edit this should feel like 40 seconds.

**Then:** Click the report in the documents panel, scroll the modal.

**Watch out:** If you want a guaranteed breakout on screen, check
`data/radar.json` beforehand. If breakouts is 0 that day, the demo is flat, so
either film it on a day it is not, or fall back to opening yesterday's report.

---

## Step 6 - Voice (9:30, target 90s)

**What you do:** Terminal. Run `jarvis voice status` to show it is up. If you
want to show the install, run `jarvis voice install --native` on a second
machine or in a throwaway copy, because on this one it is already installed and
will just say "already downloaded."

Then trigger a spoken reply in the HUD and let it play.

**What you say:** The Docker versus native point, then the honest ElevenLabs
comparison.

**Watch out:** Kokoro takes about 1.2 seconds to generate a few seconds of
speech, so there is a beat of silence before it talks. Do not talk over it.

---

## Step 7 - The bugs (11:00, target 2m)

**What you do:** Mostly talking head, with the `jarvis doctor` screenshot on
screen when you mention the status light lying.

**What you say:** The three bugs, in order, in plain language. Tilde not
expanded, status checked the binary not the model, temp filenames colliding.

**Watch out:** Do not turn this into a code review. No one needs the diff. The
point is "it told me it was fine and it was not," and the lesson is test end to
end.

---

## Step 8 - Get it running (13:00, target 90s)

**What you do:** Terminal, `npm run setup`, let the first two questions show,
then cut. Do not film your real answers.

**What you say:** Free, public domain, Claude Code recommended but Ollama works.
Then the community line, once, plainly.

**Watch out:** Do not show `.env` or `config.json` on screen. Your ElevenLabs
key is in one and your channel config is in the other.

---

## Step 9 - Close (14:30, target 60s)

Talking head. The loop, the "one agent and one text file" line, then the
comments question.

---

## Timing cheat sheet

| Section | Target | Running |
|---|---|---|
| Hook | 0:30 | 0:30 |
| What it is | 1:30 | 2:00 |
| Ask it something | 2:30 | 4:30 |
| Agents are markdown | 2:30 | 7:00 |
| Run radar live | 2:30 | 9:30 |
| Voice | 1:30 | 11:00 |
| The bugs | 2:00 | 13:00 |
| Get it running | 1:30 | 14:30 |
| Close | 1:00 | 15:30 |

If you are over, cut from radar first, then the HUD tour. Never cut the
playbook step or the bugs.

---

## On camera

- **When something breaks, keep it.** This video's credibility rests on the
  bugs section. A live failure that you narrate is worth more than a clean
  take.
- **The HUD is the visual asset nobody else has.** Chase's thumbnail has no
  product shot because his system is invisible. Yours is on screen and moving.
  Use wide shots of it between sections.
- **Energy:** this is a walkthrough, not a launch. Conversational, hands on the
  keyboard, thinking out loud.
- **Do not oversell the loop.** It is one agent writing to one file. Saying
  exactly that is more impressive than "self-improving AI," and it is true.

## Files to have open

`agents/postmortem.md`, `~/content/BRAIN/youtube/brain.md`, `data/vitals.json`,
a terminal in `~/jarvis`, and the browser on `localhost:4747`.
