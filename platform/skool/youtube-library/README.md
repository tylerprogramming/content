# YouTube Library: The AI Agency (skool.com/the-ai-agency)

Every long-form YouTube video becomes one lesson in the **YouTube Library** course plus one
scheduled feed post in Attend. The repeatable recipe is the Hermes skill
`youtube-to-skool-library`; this file is the live state.

## Course

- **Course:** YouTube Library, id `31b0709529e1440ea64abf80d6621741`, slug `d8e99302`
- **State:** DRAFT. Tyler publishes in the Skool UI (the API can't change state).
- **Description:** Every video, with the commands, links and files.
- **Cover:** warm-2 (`covers/kie/warm-2.png`, Kie GPT Image 2), uploaded as `covers/youtube-library-cover-warm2.png`
- **Lesson shape:** video, 2 short paragraphs, Resources = step-by-step guide PDF + 2-4 links.
  The full write-up lives in the PDF, not the lesson body.

## Lessons and posts (the last 10 long-form videos)

| # | Lesson (Skool title) | Video | Published | Guide PDF | Post (9am ET) |
|---|---|---|---|---|---|
| 1 | Set Up Hermes Agent in 30 Minutes | `MzwYKfSxToU` | 09-20 | hermes-agent-guide.pdf | Wed Oct 28 |
| 2 | DeepSeek Harness: Full Setup | `3xprBcuJKDA` | 09-13 | deepseek-harness-guide.pdf | Tue Oct 27 |
| 3 | Build an AI Agent in 5 Steps (Claude Code) | `WvxPxQ_XlcQ` | 09-08 | ai-agent-5-steps-guide.pdf | Thu Oct 29 |
| 4 | Give Claude the Keys to Every App You Own | `1KsadAvYE8k` | 08-19 | arcade-mcp-course-guide.pdf | Tue Nov 3 |
| 5 | Claude Code + MCP for Non-Technical Beginners | `uEUP4iHJO1Q` | 08-16 | claude-mcp-beginners-guide.pdf | Fri Oct 30 |
| 6 | YouTube Business That Runs Itself (9 Skills) | `GJQCUcx4roA` | 08-12 | youtube-business-claude-code-guide.pdf | Thu Nov 5 |
| 7 | My 17 Claude Code Skills for Content | `-dEeg0WnJxs` | 08-09 | content-workflow-17-skills-guide.pdf | Wed Nov 4 |
| 8 | Opus 5 vs Opus 4.8 vs Fable 5: Run My Benchmark | `J5lkE_jBEko` | 08-05 | opus-5-benchmark-guide.pdf | Tue Nov 10 |
| 9 | Edit Videos by Talking to Claude Code | `cdvi2ooarDc` | 07-23 | ai-video-editing-guide.pdf | Fri Nov 6 |
| 10 | A Product Ad from One Photo (ElevenLabs Flows) | `WJabXRVe8JQ` | 07-19 | elevenlabs-video-ads-guide.pdf | Wed Nov 11 |

All 10 posts: scheduled through the Attend MCP, 💬 Discussion, email_members off.
Skipped: `AH1ZpX7SD9Y` (private, an earlier upload of #9) and Shorts.

Sources per video: transcript in `~/content/transcripts/transcript_<id>.txt`, live
description in `_sources/<id>.json`, package in `~/content/youtube/videos/NNN-*/`.

## Rule: one lesson and one post per video

`dup_gate.py <id-or-url>` (on the box, read-only) checks the live course, every Attend post and the
feed by YouTube video id. `add_lessons.py` and `schedule_via_attend_mcp.py` run the same check and
re-check right before each write. A "redo" updates the existing lesson in place, never a second one.

## Rule: only videos that are live on the channel

A video goes in the course or gets a post only once it's public on Tyler's channel. Unlisted,
private, scheduled premieres and other channels' videos are blocked by `live_gate.py`:

    # on the Mac (YouTube token is here)
    ~/.hermes/installs/a648e6e8e2b18f2e/environments/186bd88f08444b6d9f67b65a11e80d2b/venv/bin/python \
      check_public.py --json <ids...> > public_check.json
    # then scp public_check.json with add_lessons.py / schedule_via_attend_mcp.py

Both scripts stop before writing anything if a video isn't live, or the check is missing or
older than 60 minutes.

## Files

| file | what |
|---|---|
| `lessons/NN-*.txt` | full lesson write-up (source of truth for the guide) |
| `to_skool_md.py` | lesson .txt -> markdown (sections, code blocks, prompt quotes) |
| `make_guides.py [files]` | lesson .txt -> `guides/*-guide.html`; print to PDF in the browser |
| `briefs-01-05.json`, `briefs-06-10.json` | per-lesson title, brief, guide, links |
| `add_lessons.py` | create new lessons (video + brief + PDF + links), on the box |
| `apply_briefs.py` / `swap_guides.py` | rewrite an existing lesson / replace only its PDF |
| `posts.json` | the 10 post bodies |
| `schedule_via_attend_mcp.py --batch N [--apply]` | schedule a batch through the Attend MCP, cancel matching drafts |
| `set_cover.py` | upload + set the course cover |
| `create_youtube_library.py` | how the course was first created |
| `backups/` | lesson records before the brief rewrite |

## Open for Tyler

- Publish the course (before Tue Oct 27, 9am, when the first post goes out).
- ElevenLabs lesson: is there a promo code? Is the flow template shareable?
- 3 old drafts in Attend from before this work (Oct 21/22/25): approve or cancel.
- YouTube description fixes:
  - 5-step agent: skill link 404s; use `github.com/tylerprogramming/claude-skills/tree/main/social-me`. The Google Doc isn't public.
  - Keys to Every App: the Claude connectors link 404s; use `support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp`.
  - MCP for beginners: no arcade.dev link.
  - YouTube business: the Google Doc and GitHub repo mentioned on camera aren't linked.
  - Content workflow: skills link has no `https://`.
  - AI video editing: the HyperFrames GitHub link promised on camera is missing.
  - ElevenLabs: step-by-step doc and flow template promised on camera are missing; "link + code" but no code.
