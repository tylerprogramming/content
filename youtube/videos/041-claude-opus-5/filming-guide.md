# Filming Guide: Claude Opus 5 (is it really better?)

**Date:** 2026-07-24 (film tomorrow)
**Estimated filming time:** One focused session. Talking head plus three builds: one pre-recorded opener (Design to code) and two split-screen head-to-heads (Opus 5 vs Fable 5).
**Golden rule:** The builds are REAL and NOTHING is staged to fail. The whole angle is "I actually built real things with it and it just worked." There is no on-camera break to engineer. Your job is to capture clean, honest builds and show the cost. If a build has a rough moment, that is fine and honest, but you are not manufacturing a failure anywhere.

---

## The Single Most Important Prep Step

**Pre-record the opener and dry-run BOTH head-to-head builds the night before, on both models, and capture clean backup takes.** These models are non-deterministic, so the exact output changes run to run. You want a known-good recording of each build in the can before you ever roll the "real" take, so you are never stuck if a live run goes sideways. Also capture the real token counts and dollar costs from both head-to-heads the night before as a backup, in case the live numbers are noisy.

Pre-flight checklist:
- [ ] Claude Code updated to the version that exposes Opus 5.
- [ ] Confirm the exact model id string in Anthropic's docs (looks like `claude-opus-5`, but verify - it launched today). Screenshot the docs page.
- [ ] Both Opus 5 and Fable 5 selectable and confirmed reachable/working.
- [ ] The design screenshot for the opener is ready to drop in.
- [ ] The landing-page brief is written and ready to paste (see below).
- [ ] The browser-game spec is written and ready to paste (see below).
- [ ] Know exactly where the effort toggle lives and how to change it on camera.
- [ ] Pre-record the Design-to-code opener and confirm you have a clean take.
- [ ] Dry-run head-to-head #1 (landing page) on Opus 5 and Fable. Record outputs, token counts, costs. Keep the recordings as backup.
- [ ] Dry-run head-to-head #2 (game) on Opus 5 and Fable. Record outputs, token counts, costs. Note which outcome you got (tie, or Fable slightly cleaner) so the narration matches.
- [ ] Tabs open and ready: Anthropic announcement (anthropic.com/news/claude-opus-5), Anthropic pricing/model page, OpenRouter (openrouter.ai/anthropic/claude-opus-5).

---

## Pre-Recording Setup

### Terminal and environment
- Terminal font large enough to read on a phone. Bump the font size before filming.
- Clean working directory. Only the demo projects visible. No clutter.
- The model selector and the effort level need to be visible or easy to show on camera.
- For the split-screen builds, decide your layout up front: Opus 5 on the left, Fable on the right, consistent for both head-to-heads so viewers can track it.
- No secrets on screen. No API keys, no tokens, no `.env` contents, no private paths. Scan before you open any file.

### Recording setup
- Screen recording at clean resolution, cursor visible, windows sized so both the command and output fit.
- For split screen, either record both panes in one frame, or record each separately and composite in the edit. Composited is usually cleaner and lets you sync the start.
- Teleprompter loaded with the word-for-word cold open and the CTA.
- Talking-head and screen-capture audio levels checked once up front.
- Turn off all notifications (Slack, Mail, Messages, calendar). A notification popping mid-build kills the take.

### On-screen safety (read this)
- Never show repo secrets, tokens, keys, or `.env` files. If you open a skill file to show a real automation is real, scan it first.
- Blur anything sensitive that slips into frame (private paths, other repo names, browser tabs).
- The builds write real files locally, which is safe to show. Just keep private paths and other repos out of frame.

### Accuracy on camera (do not skip)
- Say out loud that you recorded this on launch day and that people should verify the model id in Anthropic's docs before copying code. This one line protects you if the string changes.
- Prices to state: Opus 5 is $5 in / $25 out per million. Fable 5 is $10 / $50. Opus 5 is the same price as Opus 4.8 (free upgrade). Do not put these in the title, only say them in the video.

---

## Per-Section Capture Notes

### Cold open (0:00-0:30)
- Talking head, word for word from the teleprompter.
- Drop in a 2-second teaser flash of the two split-screen builds to come, as a hook. Pull it from the pre-recorded builds and cut it in during the edit.
- Do not explain anything yet. Just the two camps, "neither matched what I saw," and the promise.

### What launched and what it costs (0:30-1:30)
- Talking head plus a quick scroll of Anthropic's announcement page (the benchmark charts live here for a two-second glance).
- Show the OpenRouter Opus 5 page for the clean pricing table (Opus 5 $5/$25 vs Fable $10/$50).
- Editor can drop in a clean price table: Opus 5 $5/$25, Fable 5 $10/$50, Opus 4.8 same as Opus 5.
- Keep it tight. This section trims first if you run long. No benchmark theater.

### The honest part - doubters vs what I saw (1:30-2:30)
- Talking head. Show your real folder of skills / automations so the viewer sees these are real.
- Then show a real skill running clean, all the way to a finished result, on Opus 5. This is the visual proof of "it did not break for me." Nothing staged, just a normal successful run.
- This is the pivot from "here is the news" to "here is what actually happened when I used it." Sell the honesty, do not oversell it. You are reporting your result, not dunking on the doubters.

### OPENER - Design to working code (2:30-3:30) [PRE-RECORDED]
- Pre-recorded, single Opus 5, effort medium.
- Drop the design screenshot into the prompt so the viewer sees the input:

```
Here is a screenshot of a landing page design. Rebuild it as a working front end
that matches the layout, spacing, colors, typography, and button styles as closely
as you can. Clean semantic HTML and modern CSS (flexbox/grid), fully responsive down
to mobile, no framework, one file. When done, show it running so I can compare it
side by side with the screenshot.
```

- Show the rendered result next to the original design screenshot, side by side. Let the match land.

> Suggested narration: "I took a screenshot of a design and dropped it in on Opus 5. No spec, just the image. And watch what comes back. Clean, working code. That is the thing that surprised me most in the first hour. It just works."

### HEAD-TO-HEAD #1 - landing page + cost (3:30-6:30) [BUILD, split screen]
- Same brief to both models, kicked off together, split screen (Opus 5 left, Fable right).
- Paste the brief so the viewer can read it:

```
Build a complete, polished landing page for a SaaS product called "PostPilot" that
helps solo creators schedule social posts to every platform from one place. One
self-contained HTML file, inline CSS, no frameworks, fully responsive.

In order: a sticky nav with logo and a "Start free" button; a hero with a bold
headline, one-line subhead, a primary CTA, and a simple product mockup; a row of 3
feature cards with icons; a "how it works" section with 3 numbered steps; a pricing
section with 3 tiers (Free, Pro, Team) with the middle tier highlighted; one short
testimonial; and a footer.

Design direction: modern, clean, generous whitespace, one confident accent color,
real visual hierarchy, subtle hover states. Make it look like a real product a
startup would ship, not a template. Build it and show it running.
```

- Narrate the dead air while both build. Talk through what each is scaffolding, structure choices, speed, whether either asks questions. Point out that neither is arguing or stalling (the thing the doubters warned about, not happening here).
- Show both finished pages side by side. Be honest about how close they are.
- Put the two token counts and costs side by side. Fill in the REAL numbers from the live runs (or the dry-run backup if live is noisy). Do the multiplication on screen:

```
Opus 5:  ~[N] tokens  →  $[X]   ($5 in / $25 out)
Fable 5: ~[N] tokens  →  $[X]   ($10 in / $50 out)   ~2x
```

> Suggested narration: "If I hid the labels, I would have a hard time telling you which came from the expensive model. And one of them cost about twice as much. For everyday front-end work, you may not need the expensive one. That part of the hype is real."

- **This is the COST story.** The punchline is comparable quality at roughly half the price.

### HEAD-TO-HEAD #2 - browser game + quality (6:30-9:30) [BUILD, split screen]
- Same spec to both models, split screen, same layout as #1. This is the harder, flashier build and the segment to slow down on.
- Paste the game spec so the viewer can read it:

```
Build a complete, playable browser game in a single self-contained HTML file, no
external libraries. A physics-based "merge" game (Suika / Watermelon style):

- Circles of increasing size drop from the top into an open-topped container.
- I move to choose the drop position, then click to drop.
- When two of the same size touch, they merge into the next size up with a little pop.
- Everything has gravity, bounces, and collides with realistic-feeling physics.
- Score increases on every merge; show the score and the next piece.
- If the pile overflows the top, game over with a restart button.

Make it feel good to play: smooth motion, satisfying merges, clean minimal visuals.
Write the physics yourself in vanilla JS. Build it, then let me play it in the browser.
```

- Narrate the dead air while both build. Talk through the physics approach, collision/merge handling, whether either self-checks. This build takes longer, let it breathe.
- **Actually play both games on camera.** Drop pieces, let them merge, let them bounce. This is the wow segment and the honest quality probe.
- Two honest outcomes, use whichever is true on the day (you will know from the dry run):
  - **They tie:** both run, both feel good, Fable's premium buys nothing even here. Then the cost gap is the punchline.
  - **Fable a bit cleaner:** both run, Fable's physics/polish are a touch smoother. That is the one place the expensive model still earns its price. The cost gap becomes the honest tradeoff.
- Show the cost side by side again either way:

```
Opus 5:  ~[N] tokens  →  $[X]
Fable 5: ~[N] tokens  →  $[X]   ~2x
```

> Suggested narration (tie): "They both run, they both feel right. Even on the hard build, Fable's premium is not buying me anything I can feel."
> Suggested narration (Fable cleaner): "They both run, but Fable's feels a little more polished. It is not night and day, but I can feel it. That is the one place the expensive model still earns its price."

- **Say what is actually true this run. Do not force either line.** The honesty is the point.

### The effort toggle (9:30-10:30)
- Talking head plus the effort setting on screen. Change it on camera (low / medium / high / extra-high) so the viewer sees where it lives.
- Frame it POSITIVELY: it is your dial to control cost and quality, not a fix for anything broken. Medium for everyday work to keep cost down, turn it up for the genuinely hard jobs.
- Put the one-liner on screen: "Effort is your dial. Turn it down to save, turn it up for the hard stuff."

### Honest verdict + CTA (10:30-12:00)
- Talking head plus a simple two-column "use Opus 5 when / use Fable when" graphic.
- Hit the beats: Opus 5 is the new default (free upgrade, half the cost, comparable on everyday work); you probably do not need Fable for everyday building anymore; Fable still wins the absolute hardest long-horizon jobs; fair nod to both the hype camp and the doubter camp, then your honest "it worked for me."
- Do not overclaim. "We will know more in a couple weeks" is a fine, honest thing to say.
- Show the two finished builds one more time, side by side.
- Soft Skool CTA: the exact brief, the game spec, and your effort settings are in the free community so people can run the same head-to-head. Link in description: https://www.skool.com/the-ai-agency
- Subscribe ask framed around "building real things with Claude instead of just reading the benchmarks is most of what I do here."

---

## Filling Dead Air While It Builds

The split-screen builds take time. Do not sit in silence. Good things to talk through while a build runs:
- What each model is scaffolding right now, step by step, and the structure it chose.
- How fast each one is moving, and whether either is asking questions or stalling.
- Why you set the effort where you did.
- The price math (narrate the cost while it works, especially on head-to-head #1).
- A quick honest aside about the doubter camp: "this is exactly where people said it would argue or stop, and it is just working."
- If a build runs long, you can tighten the wait in the edit, but keep the real runtime honest (do not imply it was instant if it was not).

---

## On-Camera Tips: Split-Screen Comparison

- Keep the layout consistent: Opus 5 left, Fable right, for BOTH head-to-heads. Viewers should not have to relearn the frame.
- Start both runs as close to simultaneously as you can (or composite them to start together in the edit) so the comparison feels fair.
- When you reveal results, put them literally side by side and give the viewer a beat to look before you talk.
- Narrate the cost while the build is still going, so the money math does not feel bolted on at the end.
- Be honest in the reveal. If they tie, say they tie. If Fable is a bit better, say so. The whole video's credibility rides on you calling it straight.

---

## Timing Cheat Sheet

| Section | Target | Format |
|---------|--------|--------|
| Cold open | 0:30 | Talking head (word for word) + 2s teaser flash |
| What launched + cost | 1:00 | Talking head + pricing tabs + price table |
| The honest part | 1:00 | Talking head + real skill running clean |
| Opener (design to code) | 1:00 | **Pre-recorded build** |
| Head-to-head #1 (landing page + cost) | 3:00 | **BUILD split screen**, Opus 5 vs Fable |
| Head-to-head #2 (game + quality) | 3:00 | **BUILD split screen**, Opus 5 vs Fable |
| Effort toggle | 1:00 | Talking head + toggle on screen |
| Verdict + CTA | 1:30 | Talking head + two-column graphic |
| **Total** | **~12:00** | Trim "what launched" + "verdict" first to hit ~11 |

**If you must cut for time:** tighten the launch recap and the verdict. Never cut the two head-to-head builds or their cost math. Those are the spine, and nothing in them is staged to fail.
