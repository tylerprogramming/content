# Claude Code hooks: research refresh (2026-09-16)

Supersedes `research/youtube/claude-code-hooks/report.md` (2026-03-22, 1 KB). That report's three "top videos" were general Claude Code explainers, not hooks videos, and its gaps section was about prompt "hook templates" (attention hooks), not Claude Code lifecycle hooks. Both are corrected below. Requested by Tyler via @hermes. No video number assigned yet.

Inputs
- Sibling file from the same request, written in parallel by my Bot Chat session: `research/youtube/2026-09-16-claude-code-hooks.md`. It has the docs event and field tables in more depth, the 059 hook-by-hook plan, and a secondary Copilot-hooks transcript. Read both; this file is the shorter one.
- YouTube pull: `research/2026-09-16-claude-code-hooks.md` + `.json` (yt-dlp, query "claude code hooks", 365 days, 120 raw results, 25 kept)
- Reference transcript: `transcripts/transcript_AP7c9YTcaw8.txt` (Agentic Lab, 8:32)
- Docs checked live 2026-09-16: https://code.claude.com/docs/en/hooks-guide and https://code.claude.com/docs/en/hooks
- Prior art: `youtube/ideas/claude-code-course/ep13-hooks-automation/` (parked, 12-min script, 8 sections)
- Creator breakdown: `research/youtube/creator-breakdowns/2026-09-16-agentic-lab-claude-code-hooks.md`

## 1. Competitive pull

Query "claude code hooks", title must contain the keywords, last 365 days. 25 long-form, 0 Shorts. Top 12 by views:

| # | Title | Channel | Views | Duration | Uploaded |
|---|---|---|---:|---|---|
| 1 | Claude Code Hooks, Explained Simply. | Agentic Lab | 30,856 | 8:32 | 2026-08-27 |
| 2 | Mastering Claude Code Hooks: A Complete Guide to Essential Settings | Gary Chen | 19,234 | 19:57 | 2026-08-16 |
| 3 | 5 Claude Code Hooks That Save Me Hours Every Day | TechWhistle | 12,130 | 6:32 | 2026-03-21 |
| 4 | Claude Code Hooks: Get Notified When Tasks Finish | Joe Rhew | 10,657 | 14:42 | 2026-03-05 |
| 5 | Claude Code Hooks explained in 5 minutes | shanraisshan | 8,996 | 5:00 | 2026-02-05 |
| 6 | 2 useful Claude Code Hooks (Chinese) | YAHA | 1,570 | 8:31 | 2026-02-19 |
| 7 | Claude Code Hooks: Consistent Prompts & Workflow Automation | MLTut | 1,347 | 5:35 | 2025-12-01 |
| 8 | Block Dangerous Commands with PreToolUse | StonerStack | 1,081 | 14:38 | 2026-08-09 |
| 9 | PostToolUse Hook to Clean and Summarize Tool Output | MLTut | 1,078 | 4:37 | 2025-12-08 |
| 10 | Claude Code Hooks, Explained & Demoed | TechXion | 1,043 | 12:07 | 2026-04-26 |
| 11 | Master jq for Claude Code Hooks | MLTut | 992 | 4:48 | 2025-12-03 |
| 12 | Build a Bash Command Logger Step-by-Step | MLTut | 901 | 4:25 | 2025-12-05 |

Full 25 with likes/comments in `2026-09-16-claude-code-hooks.md`.

Three videos the title filter or the 365-day window dropped. Verified by direct yt-dlp lookup 2026-09-16:

| Title | Channel | Views | Duration | Uploaded | Why it matters |
|---|---|---:|---|---|---|
| Hooks in Claude Code | Claude (official) | 358,375 | 3:21 | 2026-05-07 | Anthropic owns the 3-minute "what is a hook." Do not remake it. |
| I'm HOOKED on Claude Code Hooks: Advanced Agentic Coding | IndyDevDan | 123,653 | 30:50 | 2025-07-07 | Biggest long-form. 14 months old, predates `prompt`/`agent`/`http` hooks, `if`, async, and most of today's events. |
| I Can SEE EVERYTHING: Claude Code Hooks for Multi Agent Observability | IndyDevDan | 31,711 | 20:08 | 2025-07-14 | Observability angle, also dated. |

Corrected ceiling: a current, demo-first long-form hooks video has not been made since IndyDevDan's 2025 one, and that one did 123,653.

### What the numbers say

| Signal | Count |
|---|---|
| Videos over 10,000 views | 4 of 25 |
| Videos over 1,000 views | 12 of 25 |
| Videos under 500 views | 12 of 25 |
| Uploads in last 120 days | 7 (1 over 1,000 views) |
| Median duration, top 5 | 8:32 |
| Longest in top 5 | 19:57 (Gary Chen, #2) |
| Top 5 videos that end on a real artifact | 0 (Agentic Lab ends on a CTA to a free community; the rest are settings walkthroughs) |

Read: mid-demand, evergreen term. The strict title-match pull caps at 30,856, but the official 3:21 explainer did 358,375 and IndyDevDan's 2025 deep dive did 123,653, so the audience is there for a long-form video when it is current and demo-first. Nobody has done a 10-20 minute video that builds hooks on a real repo and shows the artifacts (log file, blocked command, formatted file, Slack ping) on screen. That is the open lane.

### Title patterns in the top 5

| Pattern | Titles using it |
|---|---|
| "Explained" / "Explained Simply" / "in 5 minutes" | 2 |
| Number + outcome ("5 Hooks That Save Me Hours") | 1 |
| Single use case ("Get Notified When Tasks Finish") | 1 |
| "Complete Guide" | 1 |

Tyler's rule: no "Explained" in titles, no money, second person. That removes 2 of the top 5 patterns and leaves number + outcome and single use case. Both fit.

## 2. Reference transcript: structure breakdown

Agentic Lab, "Claude Code Hooks, Explained Simply." 30,856 views, 8:32, uploaded 2026-08-27. Transcript at `transcripts/transcript_AP7c9YTcaw8.txt` (yt-dlp auto captions, 47 lines). Full beat table with his exact prompt, rhythm, weaknesses, and our-beat plan in the creator breakdown file. Summary here.

| # | Beat | Time | What he does |
|---|---|---|---|
| 1 | Cold open | 0:00-0:40 | Claim: hooks are the most powerful feature, most people do not understand them, the docs are "nebulous". |
| 2 | Credential | 0:40-0:51 | "Top 3% paper at NeurIPS." |
| 3 | Definition | 0:51-1:34 | "A hook is an event that triggers a script." Event = when, script = what. Example: SessionEnd summarizes the session into a markdown knowledge base. |
| 4 | Lifecycle | 1:34-2:31 | Lists events in prose: prompt submitted, compaction, subagent spawned, tool called, session begins. Compares to webhooks. |
| 5 | Why | 2:31-3:40 | LLM is probabilistic, CLAUDE.md rules get ignored in long sessions, scripts are deterministic. Rule: "if the check is binary and mechanical, it should be in a hook." Quotes the docs line "always happen rather than relying on the LLM to choose." |
| 6 | Four-part prompt | 3:40-5:06 | Event, behavior, why, edge case. Says he evals hooks rather than pre-defining edge cases. |
| 7 | The prompt, live | 5:06-6:10 | Types one prompt and lets Claude write the JSON. "Claude eats the complexity." |
| 8 | Event list | 6:10-6:31 | Shows a list on screen, "pause the video." Points to the free community for one use case per event. |
| 9 | Advanced | 6:31-7:39 | Four new things: hooks can call HTTP, MCP tool, prompt, or spawn a subagent. Hooks inside a skill or custom agent. Matchers. Hooks that spawn other Claude Code or Codex instances (red-team on Stop). |
| 10 | Homework + CTA | 7:39-8:32 | "Open your CLAUDE.md, read every line, ask: could this be a hook instead?" Then the community link. |

Demos on screen: 1 (the prompt in beat 7). Artifacts shown: 0. He never runs a hook, never shows a blocked command, a log file, or a notification landing. The video is an explainer with one typed prompt.

## 3. Fact check against current docs (2026-09-16)

Checked live. Cite these on camera, not the old ep13 script.

| Claim | Status | Source |
|---|---|---|
| Hooks are "user-defined shell commands" that run at lifecycle points | True, and now incomplete: 5 handler types exist (`command`, `http`, `mcp_tool`, `prompt`, `agent`) | hooks-guide, "How hooks work" |
| Event list | 33 events documented. The old ep13 script names 4 (PreToolUse, PostToolUse, Notification, Stop). Agentic Lab says "21" on screen (his list is dated). | hooks-guide lifecycle table |
| Core events for a video | SessionStart, UserPromptSubmit, PreToolUse, PermissionRequest, PostToolUse, PostToolUseFailure, Notification, Stop, StopFailure, SubagentStart/Stop, PreCompact/PostCompact, SessionEnd | same |
| Newer events worth one line each | FileChanged, CwdChanged, ConfigChange, WorktreeCreate/Remove, PreModelSwitch/PostModelSwitch, InstructionsLoaded, TaskCreated/Completed, TeammateIdle, Setup, PostToolBatch, MessageDisplay, Elicitation | same |
| Config location | `~/.claude/settings.json` (all projects), `.claude/settings.json` (project, committable), `.claude/settings.local.json` (gitignored), plugin `hooks/hooks.json`, skill frontmatter, subagent frontmatter | hooks-guide, "Configure hook location" |
| Matcher syntax | `"Edit|Write"` pipe alternation; comma also works on v2.1.191+; regex allowed; `mcp__server__tool` naming for MCP tools; empty matcher fires on all | hooks-guide, "Filter hooks with matchers" |
| `if` field | New. Permission-rule syntax like `"Bash(git *)"` so the hook process only spawns when the tool call matches. Tool events only. | hooks-guide, "Filter by tool name and arguments" |
| Exit codes | 0 = no objection (PreToolUse still goes through normal permissions); 2 = block, stderr goes to Claude; other = non-blocking error | hooks-guide, "Hook output" |
| JSON output | `hookSpecificOutput.permissionDecision` of `allow`, `deny`, `ask` (and `defer` in `-p` mode). Must be nested under `hookSpecificOutput`; top-level is silently ignored. | hooks-guide, "Structured JSON output" |
| Hooks vs permission modes | PreToolUse `deny` blocks even under `--dangerously-skip-permissions`. `allow` cannot loosen deny rules. Hooks tighten, never loosen. | hooks-guide, "Hooks and permission modes" |
| Notification matchers | `permission_prompt` fires after ~6 s idle; `idle_prompt` after ~60 s; plus `auth_success`, `elicitation_*`, `agent_needs_input`, `agent_completed`, `quota_auto_resume_*` | hooks-guide, notification table |
| Stop hook block cap | Overridden after 8 consecutive blocks without progress; check `stop_hook_active` in input; raise with `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` | hooks-guide, "Stop hook hits the block cap" |
| Timeouts | command/http/mcp_tool 10 min default; 30 s for UserPromptSubmit and model-switch events; prompt 30 s; agent 60 s; SessionEnd shares 1.5 s | hooks-guide, "Limitations" |
| Async hooks | `"async": true` runs in background | hooks reference |
| Multiple hooks on one event | All run in parallel; most restrictive decision wins (deny > defer > ask > allow); one deny does not stop siblings | hooks-guide, "Combine results" |
| `/hooks` menu | Read-only browser; edit JSON directly or ask Claude | hooks-guide, step 2 |
| Debug | `claude --debug-file /tmp/claude.log`, or `/debug` mid-session; Ctrl+O transcript view | hooks-guide, "Debug techniques" |
| Agent hooks | Marked experimental in docs. Say so if shown. | hooks-guide, "Agent-based hooks" |

Things in the old ep13 script that are now wrong or stale
- "Hooks are NOT AI. They don't use tokens." True for `command` hooks only. `prompt` and `agent` hooks call a model (Haiku by default). Rewrite that line as "command hooks use zero tokens; the two model-backed types exist for judgment calls."
- 4 events named. Docs list 33. Do not try to cover them; pick 5 and say "there are 33, here are the 5 you will use."
- No mention of `if`, HTTP hooks, hooks in skill frontmatter, or PermissionRequest auto-approve. All four are current and none of the 25 competitor videos cover `if` or skill-frontmatter hooks.

## 4. Corrected gaps (replaces the 03-22 gaps section)

The 03-22 report's gaps were about prompt hook templates and A/B testing prompts. Wrong feature. Real gaps in the 25-video set:

| Gap | Evidence |
|---|---|
| Nobody builds hooks on a real repo and shows the artifact | Top 5: 0 artifacts on screen. Agentic Lab shows one typed prompt. Gary Chen (19:57) is a settings walkthrough. |
| Nobody covers `if`, hooks in skill frontmatter, or PermissionRequest auto-approve | 0 of 25 titles or descriptions mention them |
| Nobody connects hooks to a chat surface | Joe Rhew (10,657) does desktop notifications only. No Slack, no phone. |
| Nobody covers the model-backed types honestly | Agentic Lab names them in one line (6:31). No demo of a `prompt` Stop hook anywhere in the set. |
| Nobody shows the debug path | 0 of 25 show `--debug-file` or the transcript view. Every hooks video has a "hook not firing" comment thread. |
| The 12 under-500-view videos are all "explained" or "tutorial" with no specific outcome in the title | Title pattern, see section 1 |

## 5. Angle for the video

Claude Code users who already have a CLAUDE.md full of rules. Take Agentic Lab's homework line (open your CLAUDE.md, ask "could this be a hook") and actually do it on camera on `~/content` or a real repo: 5 hooks, each one shown firing, ending on a Stop hook that posts to Slack so the phone buzzes when Claude is done. That ending is the same "three surfaces" close as 057 and none of the 25 have it.

Tyler's machine today: `~/.claude/settings.json` has 0 hooks configured (checked 2026-09-16). Every demo is "to build" until he sets them up. Details in the creator breakdown, section "Her beat / our beat".

Length target: 12-15 min. The top 5 median is 8:32 and the 19:57 video did 19,234, so 15 is not a penalty. Ep13's 12-min structure is a usable skeleton if the 4-event framing is replaced.

## 6. Prior art

`youtube/ideas/claude-code-course/ep13-hooks-automation/` (parked). 12-min script, 8 sections: intro, what are hooks, first hook, auto-format demo, logging hook, protection hook, settings.json, combining, course wrap. Demos match the docs guide examples (Prettier PostToolUse, Bash logger, protect-files PreToolUse). Reusable: sections 3-5 map straight onto the docs' current examples. Not reusable: intro claim "not AI, no tokens" (see fact check), course-finale framing, 4-event list.

## 7. Files

| File | What |
|---|---|
| `research/2026-09-16-claude-code-hooks-refresh.md` | This file |
| `research/2026-09-16-claude-code-hooks.md` + `.json` | Raw yt-dlp pull, 25 videos |
| `research/youtube/creator-breakdowns/2026-09-16-agentic-lab-claude-code-hooks.md` | Beat table, prompts, our-beat plan |
| `transcripts/transcript_AP7c9YTcaw8.txt` | Agentic Lab, 8:32 |
| `research/_raw/vtt_to_transcript.py` | yt-dlp vtt to transcript converter (used because the transcript API install was blocked in unattended mode) |

Not fetched: Gary Chen transcript (rLNGSDYkK-w). Only a zh-TW auto-translation track exists, no English captions. Marked unverified for structure; view count and duration are from yt-dlp and stand.
