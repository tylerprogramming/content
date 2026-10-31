# YouTube Pipeline Status

> **Live pipeline state — the operational source of truth.** What's recording next, what's with the editor, what's queued.
> For full content inventory across all platforms, see `~/content/system/tracker.md`.
>
> **Open this first.** Last updated: 2026-10-27
> 2026-10-27: `063` Claude Duet **packaged** by @packager (kanban `t_9d2d3f5d`): `youtube/videos/063-claude-duet/` (9 files + 2 reference thumbnails, row under FRESH). Earliest shoot Wed 10-28 after the Day 0 pre-build. No ClickUp task yet.
> 2026-10-27: `063` Claude Duet researched by @researcher (kanban `t_93808e4c`): `research/2026-10-26-claude-duet.md` (28 videos, 40-row fact sheet, 3 builds with prompts), breakdown `research/youtube/creator-breakdowns/2026-10-26-claude-duet.md`, 6 transcripts. Packager card waits on it. No package folder, no ClickUp task yet.
> 2026-10-24: `062` ChatGPT Dots vs Hermes Agent packaged by the Researcher → Packager loop (row under FRESH). No ClickUp task yet; Tyler's call.
> Reconciled 2026-09-17: `059` Claude Code Hooks package **deleted** at Tyler's request (folder removed from `youtube/videos/`, was never committed; no ClickUp task existed). `058` OpenAI Agents API added below (was packaged 09-15 but never tracked here).
> **Channel refresh planned 2026-09-20**, not executed: banner/trailer/description/keywords/home layout all still say 2024 (AutoGen/CrewAI) while 24 of the last 25 uploads are Claude Code. Plan with 5 decisions Tyler owes in `channel-refresh-plan-2026-09-20.md` (same folder).
> ClickUp reconciled 2026-09-21: `059` Hostinger 24/7 agent → packaged (first package built end to end by the bot loop; see row). Researcher cron `Content: morning brief` live weekdays 7:45am.
> ClickUp reconciled 2026-09-20: `057` Hermes → publish, scheduled Sun 2026-09-20 1:15pm ET (final 33:24, chapters + SEO done).
> ClickUp reconciled 2026-09-15: `056` DeepSeek → complete (published); `057` Hermes → editing (filmed 2026-09-15 after the first recording failed; Tyler editing).
> ClickUp reconciled 2026-09-12: `050` Build AI Agents marked complete (published); `056` DeepSeek → publish, scheduled Sun 2026-09-13; `057` Hermes → filming, rescoped to ~30 min (see its `STATE.md`).
> ClickUp reconciled 2026-09-07: `045` marked complete; Blotato partnership video due 2026-09-08 (edit back from Sabrina, review + return); `048` parked (Arcade series underperformed); `056` DeepSeek + `057` Hermes set urgent; all 14 stale "Schedule + post" subtasks under published videos closed (Tyler confirmed posted).
> **Also tracked in ClickUp:** YouTube list (id 901710640585), Space "Team Space". Keep both in sync on every stage change — this file is the source of truth. (ClickUp reconciled 2026-07-22: confirmed 021/023/024/025/028/034 complete; marked `026` (scheduled tonight) + 6 already-live back-catalog videos (011/012 + Antigravity, YT Workflow, Build ANYTHING, 23 Concepts) complete; `86e2drehj` social push + `027` remain in progress.)

---

## 📅 Publishing Calendar — target 2x/week (Mon + Thu)

Goal: rebuild cadence. Publish 2x/week; batch-film 2 on Sat/Sun to refill. Editor backlog absorbs gaps.

| Slot | Video | Status |
|---|---|---|
| ✅ published 07-03 | Claude Cowork Full Course | LIVE (`aOECs8oPZ2c`) |
| ✅ published 07-05 | Granola AI (paid) | LIVE (`nFen2thkbmg`) |
| ✅ published ~07-08 | GPT Image 2 vs Nano Banana Pro (`028`) | LIVE (`h5VtHSXY8Hc`), repackaged 07-09 |
| ✅ published 07-15 | Claude Routines (`024`) | LIVE (`T50plh-k3MY`) |
| ✅ published 07-19 | ElevenLabs Flows Agent (`034`) | LIVE (`WJabXRVe8JQ`) |
| ✅ published | AI Video Editor (`026`) | **LIVE** (`AH1ZpX7SD9Y`) |
| ~next slot | YouTube 1-Person Business (`027`) | with editor |
| ~next slot | Automated Publishing (`039`) | film next |

**Weekend rule:** film 2 (batch) on Sat/Sun → publish 2 the next week. Editor has `027` (the YouTube automation) in flight; `026` is LIVE; next to film: `039` Automated Publishing.

---

## 🗓 Scheduled / with editor

| Video | Folder | Stage |
|---|---|---|
| **I Automated My Video Editing With Claude Code** | `026-ai-video-editor/` | **LIVE** (`AH1ZpX7SD9Y`), published. SEO + chapters done. |
| **I Run My Entire YouTube Channel With AI (Watch This)** | `027-youtube-1-person-business/` | With editor as of 2026-07-20. Focused showcase (not the 60-90 min course). Post-edit: /chapters, thumbnail, queue upload. |

---

## ✅ Published (recent)

| Video | Folder | Notes |
|---|---|---|
| The Best AI Image Model for YouTube Thumbnails (I Tested 3) | `028-nano-banana-vs-gpt-image/` (`h5VtHSXY8Hc`) | **LIVE ~2026-07-08. FLOPPED** at ~1.4% CTR / ~50 views on the "NOT DETHRONED" package. Kill-trigger tripped 2026-07-09: title swapped to "The Best AI Image Model for YouTube Thumbnails (I Tested 3)" + thumbnail = `thumbnail_KING_final.jpg` ("The KING" gold text above crowned image, GPT Image 2 remix, LIVE 2026-07-09). Watching CTR. |
| ElevenLabs Flows Agent: "I Automated My Video Ads with Elevenlabs Agent" | `034-elevenlabs-flows/video-2-flows-agent/` (`WJabXRVe8JQ`) | **LIVE 2026-07-19.** Ambassador lane. Social DRAFTED 2026-07-20 + 3 emails added 2026-07-23 in `social/`, awaiting approval. |
| Claude Routines: "I Automated My Life with Claude Routines" | `024-claude-routines-content-system/` (`T50plh-k3MY`) | **LIVE 2026-07-15.** Social DRAFTED 2026-07-23 in `social/` (X, LinkedIn, Community, Skool, IG + 3 emails), awaiting approval to post. |
| Granola AI: "I Connected Granola to Claude Code" | `025-granola-claude-code/` (`nFen2thkbmg`) | **LIVE 2026-07-05** (PAID partnership). 84 views day 1. Social DRAFTED 2026-07-23 in `social/` (5 platforms + 3 emails, disclosure included). **ON HOLD per Tyler 2026-07-23 - do not post yet, revisit later.** |
| Claude Cowork Full Course | `023-claude-cowork-full-course/` (`aOECs8oPZ2c`) | **LIVE 2026-07-03.** 178 views in 3 days - best launch of the June batch. Social DRAFTED 2026-07-23 in `social/` (5 platforms + 3 emails), awaiting approval to post. |
| Claude Cowork Clearly Explained | `021-claude-cowork-clearly-explained/` (`7ND_buIAQfA`) | **LIVE.** Repurposed 2026-06-29: 3 emails + full social (X, LinkedIn, YT Community, IG, 7 Pinterest pins) in `social/`. IG carousel pending Tyler's new look. Nothing scheduled/sent yet. |
| Claude Code Skills: The Only Course You'll Ever Need | `012-skills-full-course/` (`9ZsZgnWrs_E`) | LIVE 2026-06-21. Thumbnail B now (swapped from A, CTR ~3%). Tracking daily — see `analytics/daily-tracker.md`. |
| 3 Skills + Live Build | `011-3-skills-and-build/` | Put out by Tyler himself |

> ✅ Social COPY drafted 2026-07-23 for all live videos (`026`, `024`, `023`, `025`, `028` full sets; `034` emails added; `021`/`011`/`012` already had sets). Each has X, LinkedIn, YT Community, Skool, IG + 3-email drip in its `social/` folder. **Nothing posted yet** — awaiting Tyler's approval + scheduling. ClickUp task `86e2drehj` stays in progress until posts actually go out.
> Older live videos are tracked in `~/content/system/tracker.md` under `youtube/_completed/`.

---

## 🔴 NEXT TO FILM (Tyler's call, 2026-07-06)

The winning lane = **"I Automated My ___ With Claude Code"** (showcase). Mirrors the 2,854-view #1 cohort video. Build 3 more in this exact vein:

| Video | Folder | Status |
|---|---|---|
| **I Automated My Entire Content Pipeline With Claude Code** | `031-automated-content-pipeline/` | Package built 2026-07-06. Showcase: one prompt → a week of content. |
| **I Automated My Email With Claude Code** | `032-automated-email/` | Package built 2026-07-06. Showcase: inbox triage + drafts + sends. |
| **I Automated My YouTube Comments With Claude Code** | `033-automated-yt-comments/` | Package built 2026-07-06. Showcase: monitor + draft + reply via API. |

---

## 🔥 FRESH / FILMING NOW (added 2026-08-28)

| Video | Folder | Status |
|---|---|---|
| How To Build AI Agents in 2026 (5 Steps, No Code) | `videos/050-build-ai-agents-2026/` | ✅ **PUBLISHED (confirmed 2026-09-12).** Recorded 2026-08-29. Built the `social-me` skill live (renamed from social-research on camera), Apify MCP + yt_transcript.py + `grilling` roast. ClickUp `86e2vwgh1` complete. Video id + social status still to log here. |
| DeepSeek Harness: The Open-Source Claude Code (Setup + Features) | `videos/056-deepseek-harness/` | ✅ **PUBLISHED 2026-09-15.** ClickUp `86e30q32d` → complete. Final cut `~/Movies/Camtasia/056 - deepseek harness/056 - deepseek harness - FINAL.mp4`, 17:32. Chapters + description done from a local whisper-large-v3-turbo pass on the delivered render (21 chapters, all verified against YouTube's rules); links all checked 200. Transcript at `transcripts/transcript_056-deepseek-harness.txt`. After publish: thumbnail A/B watch (Concept A primary, B "IT RUNS CLAUDE CODE"), /yt-shorts, /social-copy. |
| Set Up Hermes Agent (Claude Code Users Start Here) | `videos/057-hermes-agent-start-here/` | ✅ **SCHEDULED → publishes Sun 2026-09-20 1:15pm ET.** ClickUp `86e31d3j9` → publish. Final cut `~/Movies/Camtasia/057-previews/057-hermes-agent-FINAL.mp4`, 33:24. 21 chapters from a turbo-whisper pass on the final render, SEO pass in `titles.md`, tags trimmed to 472 chars. Transcript `transcripts/transcript_057-hermes-agent.srt`. Upload title: Set Up Hermes Agent in 30 Minutes (Claude Code Users Start Here). After publish: mark complete, B-test title #3 after day 7, /yt-shorts (Bot Mode clip), /social-copy. Filmed 2026-09-15 (re-shoot; record sheets `RECORD-SHEET-1-10.md` + `RECORD-SHEET-11-18.md`). **RESCOPED 2026-09-12 → ~30 min course**, not 13. Live state in `STATE.md` (read first). Built today: 2 bot profiles (`coder` PR reviewer w/ `code-review` skill, `researcher`), Bot Mode on, gateway multiplexed, all 3 profiles post to Slack, new cron `coder: morning repo check` 8am wkdays → Slack. Verified on camera-ready: desktop→Slack review, bot→bot `message_agent`, Slack→agent DM. Known limits in STATE.md (`@coder` in Slack needs its own app; `message_agent` only in the `Bot Chat` session). Ending beats Tina's Discord build: Bots-tab handoff → real PR → Coder pings Slack. Pokemon/Jarvis demos OUT. Script rewrite to 30 min is the next step. Package: script (v3, 13-min, to supersede), titles, hooks, filming-guide, description, tags, thumbnail brief, `setup-checklist.md`, `STATE.md`. **PACKAGE REBUILT TO v4 (30 min) 2026-09-15** by @packager: `titles.md`, `hooks.md`, `script.md`, `filming-guide.md`, `description.md`, `tags.txt`, `yt-thumbnail.md`, `analysis.md` all rewritten for the 30-min cut; 13-min v3 files archived in `_v3-13min/`. Recommended title: **Set Up Hermes Agent in 30 Minutes (Claude Code Users Start Here)** (64 chars, rules-checked). STATE.md corrected (roster is 4 profiles not 2; local tags `qwen3.8:27b-q8_0` + `gemma4:e4b`; v0.21.3). ⚠️ Three beats in the ending are STILL UNVERIFIED (bot-to-bot reply landing, Coder opening a real PR, the Slack ping) - dry-run before filming, fallbacks in `filming-guide.md` "Verify before you roll". ClickUp `86e31d3j9` (not touched, Tyler's call). Refs transcribed: Tina Huang 29:40 (`transcript_5_N84t1rUU0.txt`), Greg Isenberg (`transcript_hermes_greg.txt`). |
| Run OpenAI's Agents API on Your Own Mac in 3 Steps | `videos/058-openai-agents/` | 📦 **PACKAGED 2026-09-15.** Target 11 to 12 min, ceiling 15. Angle: self-hosted `codex exec-server` on the Mac (0 of 14 competitor videos do it), closing on a cost comparison against the local Hermes agent. Package: titles, hooks, script (10 beats), filming-guide (13-row dry run), description, tags, yt-thumbnail, analysis. Reference: Bart Slodyczka `transcript_JFWq93b4_Oo.txt` (16,207 views). Past-example artifact is **PR #22** (`tylerprogramming/ai`), merged 2026-09-17; `~/dev/ai` pulled to `efaef26` so `openai_agents_058/` is on disk and clean. **Verified on this Mac 2026-09-17:** `codex exec-server` exists with `--remote` / `--environment-id` on `@openai/codex` 0.154.0 (`@latest`, alpha tag not required); `openai` 3.14.1 SDK confirms `beta.agents.sessions.create(environment=...)`, `sessions.events.create`, `sessions.events.stream`, and the self-hosted response fields `environment.id` + `environment.remote_url`. ⚠️ **Dry run NOT done and `~/agents-demo/` does not exist** (no workspace files, no `create_session.py` / `send.py` / `stream.py`) - beats 1, 4, 5, 6 film out of that folder. No timings, so title stays "3 Steps" not "10 Minutes". No ClickUp task (Tyler's call). |
| Create Your First 24/7 Hermes Agent in 20 Minutes (Hostinger VPS) | `videos/059-hostinger-24-7-agent/` | 📦 **PACKAGED 2026-09-21** by the Researcher → Packager loop: Tyler's idea surfaced in the 7:45 content brief as pick 1, reply `1` ran yt-search (66 videos, 4 direct Hermes+VPS competitors), 2 transcripts, a Metics Media creator-breakdown, then kanban `t_7710ff1b` → Packager. 9 files + 2 reference thumbnails. Target 18-20 min, hard ceiling 20:00 (in the title). **Two-day shoot:** sections 2-7 day one, sections 1 (cold open) and 8 (phone proof) the next morning after the job ran overnight. Section 5 = import your Claude Code setup. The job: Coder-style repo audit on `tylerprogramming/ai` delivering to Slack, reply-to-act. Research `research/2026-09-21-24-7-ai-agent-hostinger.md`, breakdown `research/youtube/creator-breakdowns/2026-09-21-metics-media-hermes-hostinger-vps.md`. ClickUp `86e3but4v` → packaged. Film after 058. |
| I Gave ChatGPT Dots 3 Real Jobs | `videos/062-openai-dots/` | ✂️ **EDITED 2026-10-29, approved.** FINAL `~/Movies/Camtasia/062 - openai dots/062 - openai dots - FINAL.mp4` (10:45.6, edit v13: shot-list edit, AI Fiya b-roll at 0:20 and 0:34, real pricing page at 0:56, private info blurred, OCR gate 0 hits). Next: `/yt-chapters`. Was: 🎬 **FILMED 2026-10-26.** Dots only (Hermes comparison dropped; v1 kept as `script-v1-vs-hermes.md`). Script v2 `script.md`, receipts in `receipts.md`. Was: 📦 **PACKAGED 2026-10-24** by @researcher → @packager (kanban `t_fef8791c` → `t_ab09f580`). Tyler paid for Dots 10-24. Target 13 to 14 min, ceiling 15. Angle: his real Dot doing the 3 jobs his Hermes bots already run (7:45 content brief, 9am repo check, Skool prep), side by side with receipts. Beats nobody has filmed: Activity View + the Dot's computer, a Custom Rule "Hand off to you" firing, Dot memory vs an editable `MEMORY.md`. 8 files + `receipts.md` template + 2 reference thumbnails. **Two-day PRE-BUILD before filming** (filming-guide.md, 14 items): fix the Slack delivery error on the researcher + coder crons (both failed 10-23), create the 3 Dot scheduled tasks + 2 Custom Rules, run the hand-off test once off camera, get a PR from Codex and one from Coder, Librarian card for job 3. Dot side unverified until run on his account. Research `research/2026-10-24-openai-dots.md`, breakdown `research/youtube/creator-breakdowns/2026-10-24-openai-dots.md`. No ClickUp task yet. Thumbnails not generated (ask first). |
| I Gave Claude Duet 3 Real Jobs. Here's What Came Back | `videos/063-claude-duet/` | 📦 **PACKAGED 2026-10-27** by @researcher → @packager (kanban `t_93808e4c` → `t_9d2d3f5d`). Duet only, no Hermes on screen. Target 12 min, ceiling 13. Same script shape as 062 (before-you-roll table, beat table, bracketed blanks, receipts). Spine: Build 1 Channel Pulse dashboard (YouTube public + content repo, weekday 6:30am refresh), the unattended refresh is the hook; Build 2 Repo Health sheet runs live and forces the approval card; Build 3 Skool lesson deck checked prompt by prompt against the transcript, plus a phone voice edit. 9 files + 2 reference thumbnails. **PRE-BUILD on Tue 10-27** (filming-guide.md, 11 items): confirm access, GitHub connector reaching the private repo (paste-in fallback), build + schedule Channel Pulse, build the Skool deck, prove the approval card path (Slack DM or email), dry-run Repo Health, usage meter before/after. **Earliest full shoot Wed 2026-10-28** (the hook needs one real 6:30 refresh; Thu 10-29 for two in the history). 17-row "Confirm on your account" list for labels the docs and creators disagree on (sheet artifact type, connections view, Scheduled history, usage label, card layout). Duet-vs-Dots kept as a later option in `analysis.md` section 7, not in the script. Research `research/2026-10-26-claude-duet.md`, breakdown `research/youtube/creator-breakdowns/2026-10-26-claude-duet.md`. No ClickUp task. Thumbnails not generated (ask first). |
| Claude Code Users: Move to Hermes Agent in 10 Minutes (One Command) | no folder yet | 🔬 **RESEARCHED 2026-09-16** by @researcher (kanban t_e74d3be4, card deleted from board mid-run). `research/2026-09-16-hermes-10-minute-guide.md`: 89 long-form Hermes videos ranked, 30 in the 5-15 min lane, 7 titled "in 10 minutes" (median 2,630 views; only Vaibhav Sisinty 183,781 and it is a Hostinger ad). Angle: `hermes import-agent claude-code` on screen (0 of 10 transcripts mention it; dry-run on this Mac would import 55 items: CLAUDE.md, 2 MCP servers, 52 skills), then the 3 things Claude Code lacks: memory across sessions, cron, messaging. Beat plan in section 5 (10 beats, prompts included). Sharbel A. "Hermes + Claude Code" hit 17,950 views in 1 day on 09-15 with zero demos. Decision open: standalone before 057 (recommended) or fold 2 beats into 057. Not packaged, no ClickUp. |

---

## 🎬 RECORD BATCH (packaged 036-041, order set 2026-07-24)

Prompts docs for the batch live in Google Drive → "Tyler AI - YouTube Resources".

| Order | Video | Folder | Status |
|---|---|---|---|
| 1 | Claude Opus 5 (3-way: 5 vs 4.8 vs Fable) | `041-claude-opus-5/` | ✅ **PUBLISHED 2026-08-05** as *Claude Opus 5 Is Half the Price, is it Worth It?* (`J5lkE_jBEko`, https://youtu.be/J5lkE_jBEko). 3-way / 6 tests; real chapters set. Full social in `social/`. **SCHEDULED via Blotato + Resend (max 1 post/platform/day, all times ET):** Fri 8/7 = Email 1 8am, X thread 8am, LinkedIn text 10am, Reel 1 → TikTok/IG/YT Shorts 1pm. Sat 8/8 = Email 2 8am, LinkedIn Reel 1 10am, Reel 2 → TikTok/IG/YT Shorts 1pm. Sun 8/9 = LinkedIn Reel 2 1pm. Mon 8/10 = Carousel (7 slides) → IG + LinkedIn 10am. Manual TODO: 2 Skool posts (Tyler, from `skool.md`). |
| 2 | 17 Claude Code Skills That Run My Business | `040-claude-code-skills-run-my-business/` | ✅ **RE-RECORDED 2026-07-31** (supersedes the 07-28 take) → to edit |
| 3 | I Automated My Publishing With Claude Code | `039-automated-publishing/` | Package complete. **Films next.** |
| 4 | The Simple Claude Code YouTube Workflow | `037-youtube-workflow-simple/` | Package complete. |
| 5 | ~~Build Your First AI Agent (No Code)~~ | `038-build-first-ai-agent/` | 🗄️ **SUPERSEDED 2026-08-31 by `050-build-ai-agents-2026` (recorded 2026-08-29).** Same video, do not film. Archive candidate. |
| backup | ElevenLabs Dubbing v2 | `036-elevenlabs-dubbing-v2/` | Package complete. |

**Reels (039):** 5 reel scripts ready in `039-automated-publishing/reels.md` (fan-out flagship, queue-fills payoff, Pinterest sleeper, not-a-spam-cannon, automate-one-platform). To cut after recording.
**SEO (041):** title locked 2026-07-28 → **"Claude Opus 5 vs Fable 5: I Built the Same App Twice"**. Description + `tags.txt` SEO-optimized. A/B swap at 48-72h if CTR is soft: "Claude Opus 5 Is Half the Price. Is It Half the Model?"
**Shorts (041):** 3 reels **recorded 2026-07-27** (cheaper-Fable value take, website head-to-head, effort-toggle tip). To edit + post. Scripts in `041-claude-opus-5/shorts.md`.
**Shorts (040):** **9 reels, word-for-word scripts** in `040-claude-code-skills-run-my-business/reel-scripts.md` (plan + post order in `shorts.md`), all cuttable from the 07-31 footage: umbrella, anti-fake-demo, what-a-skill-is, 2-min live build, `/yt-search`, `/yt-package` meta, `/social-copy`, cron proof, `/email`, + a bonus closer. Post order 1, 3, 5, 4, 2, 8, 6, 7, 9. ClickUp `86e2ka0y3`. To cut + post.
**Reels recorded (040):** **5 of 9 recorded 2026-08-02** — umbrella, 2-min live build, `/yt-search`, `/yt-package`, `/social-copy`. To edit + post. **Still to record (4):** "What a skill actually is", `/yt-thumbnail`, `/transcribe`, `/email`.
⚠️ **`/skool` does not exist** in `~/.claude/skills/`. The 10th reel is parked over it, and the same gap sits in **Part 3 of the long form (9:30-11:30)** and in the "17" on the on-screen wall. Check the take before it goes to the editor. Tyler's call, deferred 2026-07-31.
**Emails (040 / community):** 5-email Skool onboarding sequence drafted 2026-07-31 in `emails/campaigns/skool-onboarding-2026-07/` (free member → cohort, Harut-derived). Needs the cohort application link, the workshop date, and a real member story before it can send.
**Instagram (040):** 4 carousels rendered 2026-07-29 in `platform/instagram/` (`claude-skills-system`, `first-claude-skill`, `skills-on-a-schedule`, `not-a-demo`) with captions + PDFs. Nothing scheduled yet.

---

## 🔌 Arcade series (045-047) — arcade.dev lane

| Video | Folder | Stage |
|---|---|---|
| **045 Give Claude Code Access to Your Real Apps** | `045-arcade-connect-apps/` | ✅ **COMPLETE 2026-09-07** (Tyler). Final: `~/Movies/Camtasia/045 - arcade.dev/045 - arcade.dev - FINAL.mp4`, 12:00.6. ClickUp `86e2kukfp` closed. |
| **046 Build a Smart AI Agent in 2026** | `046-arcade-build-agent/` | **Reworked to HYBRID 2026-08-10** (retitled from "Real AI Agent in 7 Minutes"). Part 1: build the morning-brief agent in Claude Code (Calendar+Gmail → day summary + flagged replies → drafts). Part 2: move the same job into a small Python script + schedule it, so it runs on its own (the "real agent / in 2026" payoff). ⚠️ **Part 2 needs an Arcade-from-code fact-check + code/scheduler prep before filming** (shared research with 049). ClickUp `86e2kukg1` (in progress). |
| **048 How to Make an MCP Server in 2026 (No Code)** | `048-arcade-make-mcp-server/` | ⏸ **PARKED 2026-09-07** (Tyler: Arcade series underperformed; not filming). plan.md stays on disk. ClickUp `86e2rcmnt` renamed PARKED, priority low. |
| **049 Build Your Own Custom MCP Server with Arcade** | `049-arcade-build-custom-mcp-server/` | **Planning** (plan.md written 2026-08-10). Write + deploy a custom tool as an MCP server (auth + hosting handled). Builder / "you could ship this" lane. ⚠️ **Fact-check Arcade Tool SDK + `arcade deploy` before scripting.** ClickUp `86e2rcmqw`. |
| **047 Arcade — Full Course (~1hr)** | `047-arcade-mcp-course/` | **FINAL DELIVERED 2026-08-19 → chapters + thumbnail + upload.** `~/Movies/Camtasia/047 - arcade.dev full course/047 - arcade.dev full course - FINAL.mp4`, **56:29**, 561 MB. First 2 min rebuilt to the Nate Herk teardown: face-free ~65%, longest bare-face run under 4s (was 18.2s). Seedance cold open + dawn room + kitchen b-roll (3 of 6 generated used), wall cutaway with real brand marks, morning-brief HUD, `code-scroll`, six-module teaser. Camera is a **rounded-rect PIP**, every clip zoom-keyframed to a word. Verified: 0 speech clipped across 351 boundaries, PIP present throughout, seam clean. ⚠️ **description + chapters are STALE** (written against the v1 55:11 cut — every timestamp wrong, first minute completely different). Motion kit recorded in `/yt-edit` → `reference/MOTION-KIT.md`. ClickUp `86e2kukgv`. |

**The arc:** 045 connect apps → 046 build an agent → 048 make a server (no code) → 049 build your own custom server → 047 the course.
**045 ↔ 046 pair:** 045 = connect your apps (the setup), teases 046; 046 = build one real agent (the payoff), references 045 as the companion. 045 + 046 Part 1 can film in one Arcade setup session; 046 Part 2 (code + schedule) needs the from-code fact-check + prep first, so film it after.
**048 ↔ 049 pair:** 048 = assemble a server from prebuilt tools (no code) → teases 049; 049 = write + deploy your own custom tool. Progression: use → build.
**Disclosure:** confirm sponsor/partner status with Arcade before publishing; if sponsored, say so on camera + in the description.

---

## 📦 Queued — package ready, not yet recorded

| Priority | Video | Folder | Lane note |
|---|---|---|---|
| 💡 Idea (to build) | All Claude Features (one big overview) | `(to build)` | Tyler 2026-08-02: **parked Claude Tag (`029`)** for now, leaning toward a full "all Claude features" roundup instead. `029` package still on disk if revived. |
| 🔥 Timely (to build) | Claude Design Just Got a HUGE Update | `(to build → 16)` | New Claude Design version (design-system imports, /design in Claude Code, canvas, round-trip). Ride fresh. |
| 🎙 ElevenLabs (reach) | How to Make AI Voice Sound 100% Human (ElevenLabs) | `(to build)` | Ambassador lane. Big lane (87-101K). PRO-EL framing only (never "free alternatives"). |
| 🎙 ElevenLabs (timely) | ElevenLabs Can Make Full Videos Now (Voice+Image+Video) | `(to build)` | New EL Image+Video launch. Low competition. |
| 🎙 ElevenLabs ($/builder) | I Built an AI Receptionist with ElevenLabs | `(to build)` | ElevenAgents. Hits #1 builder audience ("you could sell this"). Smaller lane, monetization play. |
| Showcase (to build) | I Automated a Month of Content in One Prompt (Claude + Blotato) | `(to build)` | Blotato lane (Koen 31K); founder-tag play. |
| — | Claude Code Email System | `014-claude-code-email-system/` | |
| — | 100+ Pieces of Content Per Week | `015-100-pieces-content-pipeline/` | Overlaps `13` — merge/retire |
| — | Claude Code for Content Creators | `016-claude-code-for-creators/` | Underserved non-dev niche |
| — | Claude Code + Remotion | `017-claude-code-remotion/` | |
| — | Claude Design: 5 Landing Pages | `018-claude-design-5-landing-pages/` | Evergreen slate — needs 4-hr block |
| — | Claude Design: Rebuild Stripe | `019-claude-design-rebuild-stripe/` | Evergreen slate |
| — | Claude Design + Kling Animated Hero | `020-claude-design-kling-animated-hero/` | Evergreen slate — needs Kling credits |

---

## 🗄️ Superseded / archive candidates

| Video | Folder | Why |
|---|---|---|
| Cowork 30-Min Course | `013-claude-cowork-course-30/` | Superseded by the masterclass + clearly-explained versions |
| Build Your First AI Agent (No Code) | `038-build-first-ai-agent/` | Superseded 2026-08-31 by `050-build-ai-agents-2026`, recorded 2026-08-29. Same video. |

> Repo cleaned 2026-06-24: stray root dupes/leftovers archived to `youtube/_archive/`; empty `067-` deleted. Root is now active packages only.

---

## How to use this file

- **Moving a video between stages?** Update it here immediately.
- **"What do I record next?"** → 🔴 NEXT TO FILM section.
- Pair with `system/tracker.md` (inventory) and `research/strategy/2026-05-20-RESTART-plan.md` (90-day priority).
