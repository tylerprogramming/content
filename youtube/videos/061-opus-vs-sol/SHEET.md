# 061 Opus 5.5 vs GPT-6 Sol: the full sheet

Generated 2026-09-23. Everything below is on disk under `~/content/youtube/videos/061-opus-vs-sol/`.

## Done

- Two Hermes profiles: `opus` on `claude-opus-5-5` (anthropic), `sol` on `gpt-6-sol` (openai-codex, your subscription). Same SOUL, same skills, same Slack.
- Both on the daily 8am repo-check cron (`37d92d30a26b`, `dd90ba69981f`), delivering to Slack, message opens with `[model id]`. First fire 2026-09-24 08:00.
- 7 use cases run on both models, 14 of 14 complete, artifacts below.
- Ad visuals built: `runs/3-ad-visual.html`, `runs/3-ad-concepts.html`.
- Public harness committed to `~/dev/ai/mini_projects/opus_vs_sol_061/` (prompts, setup.sh, run-all.sh, README with results). No data in it. Not pushed.
- Week-in-AI research: `~/content/research/youtube/2026-09-23-week-in-ai-youtube.md` (20 terms, 219 videos).
- Herk's 10 use cases transcribed: `~/content/transcripts/transcript_eF3yeJuifoQ.txt`.

## Needs to complete

| What | Who | When |
|---|---|---|
| Row 8, the bill: read both Slack cards, compare invoices | me | after 8am 09-24, then again 09-26 for the 3-day thread |
| Judge #1 website and #4 game by eye | you | before filming |
| Package 061 (titles, hooks, script, filming guide) | Packager | after row 8 |
| ClickUp + status.md row for 061 | me | with the package |
| Reinstall the Hermes browser tool (`hermes tools` → Browser Automation) | you | before filming anything that uses the in-app browser |
| Push `~/dev/ai` and `~/content` | you | when you say |

## Every comparison, where it is

| # | Case | Opus 5.5 | GPT-6 Sol | How to compare |
|---|---|---|---|---|
| 1 | Website design | `runs/opus/1-website/landing.html` | `runs/sol/1-website/landing.html` | open both `landing.html` in a browser, side by side |
| 2 | Code review | `runs/opus/2-review/out.txt` (text, final answer at the bottom) | `runs/sol/2-review/out.txt` (text, final answer at the bottom) | read both `out.txt` bottoms; the two lead findings |
| 3 | Attend ad | `runs/opus/3-ad/out.txt` (text, final answer at the bottom) | `runs/sol/3-ad/out.txt` (text, final answer at the bottom) | `runs/3-ad-visual.html` (both scripts as posts) and `runs/3-ad-concepts.html` (three concepts) |
| 4 | Game | `runs/opus/4-game/game.html` | `runs/sol/4-game/game.html` | open both `game.html`, play each |
| 5 | Analytics | `runs/opus/5-videos/out.txt` (text, final answer at the bottom) | `runs/sol/5-videos/out.txt` (text, final answer at the bottom) | read both `out.txt` bottoms; look for the 10 to 20 min finding |
| 6 | Reel | `runs/opus/6-reel/reel-opus.mp4` | `runs/sol/6-reel/reel-sol.mp4` | play `reel-opus.mp4` then `reel-sol.mp4` |
| 7 | Brief | `runs/opus/7-brief/out.txt` (text, final answer at the bottom) | `runs/sol/7-brief/out.txt` (text, final answer at the bottom) | read both `out.txt` bottoms; the 3 picks |
| 8 | Bill | Slack card 09-24 08:00 | Slack card 09-24 08:00 | the thread, and `hermes -p <profile> cron list` |

Results as read so far: Opus took 5, 7, 3. Sol took 2. Reel tied. Website and game are yours.

## The 8 prompts, verbatim (same text to both models)

Each was sent as `hermes -p <profile> chat -q "Work in this folder and write every file there: <case folder>\n\n<prompt>"` from `inputs/`.

### 1. Website design  (`prompts/1-website.md`)

```
Build a landing page for Attend, a CRM for Skool community owners: it tracks members, DMs, churn risk, and course progress, and sends a morning brief to Slack. One page, one CTA ("Start free"), dark theme, mobile first. Plain HTML + CSS in a single file at ./landing.html. No frameworks, no placeholder lorem ipsum: write real copy. Open it in a browser when done and tell me the one line you are least sure about.
```

### 2. Code review  (`prompts/2-review.md`)

```
Review the most recent commit on tylerprogramming/skoolos using the code-review skill. Fetch it with gh. File and line for every finding, quote the code. Lead with the one finding that matters. Do not post anything to GitHub.
```

### 3. Attend ad  (`prompts/3-ad.md`)

```
Read attend-ad-swipe.md in this folder. It is my swipe file of ad scripts that worked for Attend, a CRM for Skool community owners. Write ONE new 30-second video ad script for Attend in that same structure. Hook in the first 3 seconds, one pain, one proof line, one CTA. No em dashes, no hype words (insane, crazy, game-changer), no prices. Under 90 words. Then in one line tell me which existing script in the swipe file it is closest to and why yours is different.
```

### 4. Game  (`prompts/4-game.md`)

```
Build a browser game in a single ./game.html: you are a support agent, emails slide in from the right, each needs one of four labels (billing, technical, sales, spam) before it reaches the left edge. Keyboard 1-4 to label. Score, lives, speed ramps every 10. Real-sounding email subjects, at least 20. Plain HTML/JS/CSS, no libraries. Open it in a browser and play one round yourself, then tell me your score.
```

### 5. Analytics  (`prompts/5-videos.md`)

```
analytics-50-videos.json in this folder is my YouTube channel's last 28 days from the Analytics API: month.perVideo has every video with views, avgViewPct, avgViewDuration, durationSeconds, isShort. Read it. Tell me, with numbers from the file: (1) what video length holds retention best on this channel and what length loses it, (2) the three title patterns that are winning, (3) five specific videos I should make next, each with a title under 70 characters, no money in titles, no em dashes. Do not ask me anything first.
```

### 6. Reel  (`prompts/6-reel.md`)

```
057-final.mp4 in this folder is a 33-minute video; transcript_057-hermes-agent.srt is its transcript. Cut a 45-second vertical (9:16) reel from the section 28:20 to 31:20 where bots hand work to each other. Use the hyperframes skills: a title card, burned-in captions from the SRT, one lower-third. Run hyperframes check --strict and fix anything it flags, then render to ./reel-{model}.mp4. Report the check result and the render time.
```

### 7. Brief  (`prompts/7-brief.md`)

```
Run the content-brief skill using ONLY the files in this folder (status.md, analytics-50-videos.json, video-ideas.md). Produce the morning brief in the exact output shape from the skill, under 900 characters, 3 openings, ending with "Reply with a number." Numbers only from the files.
```

### 8. The bill

Not a prompt. The cron prompt both profiles run daily:

```
You are Coder. Check tylerprogramming/skoolos and tylerprogramming/jarvis-public: commits in the last 24h, failed CI, open PRs. Review any commit over 30 lines with the code-review skill. Lead with the one thing that matters. Start your message with your model id in brackets. If everything is green say exactly: All green. Nothing needs you.
```

Compare: token usage per run from each profile's session, and the Anthropic invoice vs the ChatGPT subscription (flat).
