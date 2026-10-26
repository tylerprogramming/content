# Research: Claude Code hooks (video 059)

**Date:** 2026-09-16
**For:** 059, Claude Code users (Tyler's core audience)
**Supersedes:** `research/youtube/claude-code-hooks/report.md` (2026-03-22, 1 KB, see section 6 for what was wrong in it)
**Docs pulled today:** `research/youtube/claude-code-hooks/docs/hooks.md` (reference, 328 KB, 3,840 lines) and `docs/hooks-guide.md` (guide, 83 KB), both from code.claude.com on 2026-09-16
**Transcripts:** `transcripts/transcript_AP7c9YTcaw8.txt` (Agentic Lab, 8:32), `transcripts/transcript_03CfGf9iw_U.txt` (Burke Holland, 19:30, Copilot hooks not Claude Code; secondary only)
**Prior art in repo:** `youtube/ideas/claude-code-course/ep13-hooks-automation/` (13-min course finale, 6 files, never filmed; stale in 3 places, section 6)
**Tyler's machine:** Claude Code 2.1.273, jq 1.7.1 at /usr/bin/jq, `~/.claude/settings.json` has no `hooks` key, `~/.claude/hooks/` does not exist. Clean slate for filming.

---

## 0. Read this first

| Fact | Number | Consequence |
|---|---:|---|
| Biggest hooks-specific video | 358,375 (Claude official, 3:21, 2026-05-07) | Anthropic owns the 3-minute "what is a hook". Do not remake it. |
| Biggest long-form hooks video | 123,653 (IndyDevDan, 30:50, 2025-07-07) | 14 months old. Predates prompt hooks, agent hooks, HTTP hooks, `if` field, async, FileChanged, and 19 of today's 33 events. |
| Newest hooks video with traction | 30,856 (Agentic Lab, 8:32, 2026-08-27) | Talk over slides, zero live demo. That is the opening. |
| Hook events in the docs today | 33 (counted from the reference lifecycle table 2026-09-16) | Every existing video lists 5 to 9. The count itself is a hook. |
| Handler types today | 5 (`command`, `http`, `mcp_tool`, `prompt`, `agent`) | Every existing video covers 1 (`command`). |

Read on the field: the term is evergreen, not a news wave. Demand is steady (25 videos in the search, 10 over 10K). The two videos over 100K are a plain-language explainer (Simon Scrapes, 875K, covers hooks as one concept of many) and IndyDevDan's 2025 deep dive. Nobody has filmed a current, demo-first, Claude Code-only hooks video since the feature grew from 9 events to 33 and from 1 handler type to 5. 059 is that video: build 5 to 6 real hooks on camera, on Tyler's real projects, against the 2026-09 docs.

---

## 1. What hooks are today (verified against code.claude.com, 2026-09-16)

### Definition
User-defined shell commands, HTTP endpoints, MCP tool calls, LLM prompts, or subagents that run automatically at points in Claude Code's lifecycle. Same events fire in terminal, IDE extensions, Desktop app, and cloud sessions.

### The three-level config shape (this is the whole mental model)

```json
{
  "hooks": {
    "PreToolUse": [                       // 1. event
      {
        "matcher": "Bash",                // 2. matcher group (filters by tool name here)
        "hooks": [                        // 3. handlers
          {
            "type": "command",
            "if": "Bash(rm *)",           // optional, permission-rule syntax, narrows further
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh",
            "args": []                    // exec form, no shell
          }
        ]
      }
    ]
  }
}
```

### Where hooks live

| Location | Scope | Shareable |
|---|---|---|
| `~/.claude/settings.json` | all projects | no |
| `.claude/settings.json` | one project | yes, commit it |
| `.claude/settings.local.json` | one project | no, gitignored |
| managed policy settings | org | admin |
| plugin `hooks/hooks.json` | when plugin enabled | yes |
| skill frontmatter | rest of session after skill invoked | yes |
| subagent frontmatter | while that subagent runs | yes |

Hooks merge across levels. `disableAllHooks: true` turns them off. `/hooks` menu is **read-only** now (browse, inspect source file, no editing).

### The 33 events (cadence)

| Cadence | Events |
|---|---|
| Per session | `SessionStart`, `SessionEnd`, `Setup` |
| Per turn | `UserPromptSubmit`, `UserPromptExpansion`, `Stop`, `StopFailure` |
| Per tool call | `PreToolUse`, `PermissionRequest`, `PermissionDenied`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch` |
| Subagents / tasks | `SubagentStart`, `SubagentStop`, `TaskCreated`, `TaskCompleted`, `TeammateIdle` |
| Context | `PreCompact`, `PostCompact`, `InstructionsLoaded` |
| Environment | `CwdChanged`, `DirectoryAdded`, `FileChanged`, `ConfigChange`, `WorktreeCreate`, `WorktreeRemove` |
| Model | `PreModelSwitch`, `PostModelSwitch` |
| MCP | `Elicitation`, `ElicitationResult` |
| UI | `Notification`, `MessageDisplay` |

The 6 that matter for a first video: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SessionStart`, `Notification`. Mention the count, show the table, then go deep on 6.

### Input: JSON on stdin (not env vars)

Common fields every event gets: `session_id`, `prompt_id`, `transcript_path`, `cwd`, `scratchpad_dir`, `permission_mode`, `effort`, `hook_event_name`. Inside a subagent also `agent_id`, `agent_type`.

```json
{
  "session_id": "abc123",
  "cwd": "/Users/tylerreed/dev/jarvis",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": { "command": "npm test", "description": "Run test suite" },
  "tool_use_id": "toolu_01ABC123..."
}
```

`PostToolUse` adds `tool_response`. `UserPromptSubmit` adds `prompt`. `Stop` adds `stop_hook_active`, `last_assistant_message`, `background_tasks`, `session_crons`. `SessionStart` adds `source` (`startup|resume|clear|compact|fork`). File-tool paths are always absolute.

### Output: exit codes and JSON

| Exit | Meaning |
|---|---|
| 0 | no objection. Stdout is plain text → added to Claude's context only on `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart`, `PostModelSwitch`. Stdout that starts `{` and ends `}` is parsed as JSON. |
| 2 | block. Stderr becomes the reason. Only exit code that blocks on its own. |
| 1 or other | non-blocking error, action proceeds, transcript shows `<hook> hook error`. **Common mistake: exit 1 does not block.** |

Exit 2 per event: `PreToolUse` blocks the tool call, `UserPromptSubmit` erases the prompt, `Stop` keeps Claude working, `PostToolUse` cannot block (tool already ran) but Claude sees stderr.

JSON output (exit 0, print an object):

```json
{ "hookSpecificOutput": { "hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "..." } }
{ "hookSpecificOutput": { "hookEventName": "PreToolUse", "permissionDecision": "allow" } }
{ "hookSpecificOutput": { "hookEventName": "PostToolUse", "additionalContext": "This file is generated. Edit src/schema.ts instead." } }
{ "decision": "block", "reason": "Tests must pass before stopping" }
{ "continue": false, "stopReason": "Build failed" }
```

`permissionDecision` values: `allow | deny | ask | defer`. `updatedInput` under `hookSpecificOutput` rewrites tool arguments before they run. Output strings capped at 10,000 chars. Multiple hooks run in parallel; most restrictive wins (`deny > defer > ask > allow`).

### Hooks beat permission modes
`PreToolUse` fires before any permission check, in every mode including `bypassPermissions` and `--dangerously-skip-permissions`. A hook `deny` cannot be bypassed by changing mode. A hook `allow` cannot loosen a settings deny rule. One-way ratchet. This is the strongest single sentence in the video.

### The 5 handler types

| Type | What runs | Default timeout | Notes |
|---|---|---|---|
| `command` | shell command, JSON on stdin | 10 min (30 s for UserPromptSubmit) | `async: true` runs in background, result delivered next turn |
| `http` | POST JSON to a URL | 10 min | cannot block via status code, must return 2xx + JSON |
| `mcp_tool` | tool on a connected MCP server | 10 min | text output treated like stdout |
| `prompt` | single-turn Haiku call, returns `{"ok": true/false, "reason"}` | 30 s | judgment calls. `Stop` + prompt hook = "did you finish?" loop |
| `agent` | subagent with Read/Grep/Glob, up to 50 turns | 60 s | experimental. `$ARGUMENTS` placeholder gets the JSON input |

Rule of thumb from docs and creators: binary and mechanical → `command`. Needs judgment → `prompt`. Needs to look at files → `agent`.

### Things that ship now that no video shows
- `if` field: `"if": "Bash(git *)"` or `"Edit(*.ts)"` so the process only spawns when the call matches. Best-effort; use permissions for hard deny.
- `async: true` on command hooks. Test suite runs in background, result lands on next turn.
- `once: true` removes a hook after first successful run (skill hooks).
- `FileChanged` with a `matcher` of literal filenames, fires whoever wrote the file.
- `SessionStart` with `matcher: "compact"` to re-inject context after compaction.
- `CLAUDE_ENV_FILE`: SessionStart/CwdChanged hooks write env vars that Bash picks up.
- `Stop` hook input has `last_assistant_message`, so a read-aloud or Slack-post hook needs no transcript parsing.
- Stop hook block cap: 8 consecutive blocks, then Claude Code overrides. Check `stop_hook_active`.
- `terminalSequence` output field for desktop notifications (hooks have no `/dev/tty`).
- `/goal` is a built-in session-scoped prompt Stop hook.
- Debug: `claude --debug-file /tmp/claude.log` then `tail -f`. Or `/debug` mid-session. `Ctrl+O` transcript view.

### Gotchas worth showing on camera (each is a failed run the viewer will hit)
1. Script not executable → `Failed with non-blocking status code: /bin/sh: ... No such file or directory`, and the gate is silently off. `chmod +x`.
2. Exit 1 does not block. Exit 2 does.
3. `permissionDecision` at the top level of JSON is silently ignored. Must be inside `hookSpecificOutput`.
4. Shell profile that echoes on startup breaks JSON parsing (output no longer starts with `{`).
5. Matcher `mcp__memory` matches nothing (exact string). Need `mcp__memory__.*`.
6. `PostToolUse` on `Edit|Write` does not fire when a Bash command rewrites the file. Use `FileChanged`.
7. `@file` references in a prompt never fire `PreToolUse` on `Read`.

---

## 2. YouTube landscape (yt-dlp pull, 2026-09-16, query "claude code hooks", 25 results)

| Views | Dur | Date | Channel | Title | Hooks-only? |
|------:|-----|------|---------|-------|---|
| 875,835 | 27:24 | unverified | Simon Scrapes | Every Claude Code Concept Explained for Normal People | no, one concept of many |
| 490,493 | 46:13 | unverified | John Kim | How I use Claude Code (Meta L7 Senior Staff Engineer Tips) | no |
| 358,375 | 3:21 | 2026-05-07 | Claude (official) | Hooks in Claude Code | yes |
| 123,653 | 30:50 | 2025-07-07 | IndyDevDan | I'm HOOKED on Claude Code Hooks: Advanced Agentic Coding | yes |
| 80,254 | 19:38 | 2026-09-07 | Tech With Tim | Claude Code: The Advanced Guide (99% of Devs Skip These Features) | no, section |
| 59,196 | 27:29 | 2026-01-19 | IndyDevDan | The Claude Code Feature Senior Engineers KEEP MISSING | yes (hooks) |
| 49,742 | 6:51 | 2026-02-25 | Matt Pocock | How to actually force Claude Code to use the right CLI (don't use CLAUDE.md) | yes, one hook |
| 43,311 | 2:43 | 2025-07-12 | Better Stack | How Claude Code Hooks Save Me HOURS Daily | yes |
| 35,258 | 19:30 | 2026-04-14 | Burke Holland | Completely understand hooks in less than 20 minutes | Copilot hooks, not CC |
| 30,856 | 8:32 | 2026-08-27 | Agentic Lab | Claude Code Hooks, Explained Simply. | yes |
| 20,691 | 22:23 | 2026-01-05 | IndyDevDan | Claude Code is Amazing... Until It DELETES Production | yes, safety |
| 20,614 | 64:58 | 2026-05-12 | CampusX | Hooks in Claude Code, Full Theory + Practical Use | yes, 1 hr |
| 16,083 | 11:53 | unverified | Greg Baugues | Claude Code - Getting Started with Hooks | yes |
| 12,130 | 6:32 | unverified | TechWhistle | 5 Claude Code Hooks That Save Me Hours Every Day | yes |
| 11,080 | 5:29 | unverified | Web Dev Cody | Claude Code hooks are Officially Awesome | yes |
| 10,660 | 14:43 | unverified | Joe Rhew | Claude Code Hooks: Get Notified When Tasks Finish | yes |

Below 10K: shanraisshan 8,996 (5:01), Adam Goodyer 4,721 (8:38), Mervin Praison 4,537, QuantBrasil 4,392 (33 min), JorgeConsulting 3,937, Code Playbook 2,025, TechXion 1,043, AI Terminal 487 ("All 9 Events", already wrong).

### Patterns in what works
| Pattern | Evidence |
|---|---|
| Title states the promise as time saved or danger avoided | Better Stack "Save Me HOURS" 43K at 2:43; IndyDevDan "DELETES Production" 20K |
| One hook, one problem, short | Matt Pocock 49K at 6:51: a single PreToolUse hook that rewrites `npm` to `pnpm`. Title says the hook is the fix, not CLAUDE.md |
| "Explained simply" framing | Agentic Lab 30K at 8:32 in 3 weeks |
| Long-form deep dive by a known engineer | IndyDevDan 123K at 30 min, 59K at 27 min |
| Hooks pitched against CLAUDE.md rules | Pocock, Agentic Lab, CampusX all say the same line: rules get ignored over a long session, hooks do not |

### Gaps (our openings)
| Gap | Who has it |
|---|---|
| No video shows the current event count (33) or any of the 5 handler types beyond `command` | all |
| No video shows `prompt` or `agent` hooks running | all |
| No video shows `if`, `async`, `FileChanged`, `SessionStart compact`, `last_assistant_message` | all |
| The two 2026 hooks-only videos with traction (Agentic Lab, Claude official) have zero live terminal demos | Agentic Lab, Claude |
| IndyDevDan's 123K video is 14 months stale on schema | IndyDevDan |
| Nobody shows the failure modes (exit 1, chmod, top-level `permissionDecision`) | all |
| Nobody films hooks on a real multi-project setup with a Slack/Hermes payoff | all |

---

## 3. Angle for 059

**Working thesis:** Claude Code hooks grew from 9 events to 33 and from 1 handler type to 5 while everyone was busy with skills and subagents. Build 6 hooks live, on real projects, each one solving a thing Tyler actually hit. End with the hook that talks to Hermes.

Six live builds, ordered easy to hard, each one a beat:

| # | Hook | Event | Type | Proves | Where to film |
|---|---|---|---|---|---|
| 1 | Desktop notification when Claude needs input | `Notification` | command | the shape of a hook, `/hooks` read-only menu | `~/.claude/settings.json` |
| 2 | Block `rm -rf` and edits to `.env` | `PreToolUse` `Bash` + `Edit\|Write`, `if: "Bash(rm *)"` | command, exit 2 then JSON deny | hooks beat `--dangerously-skip-permissions`; show exit 1 failing first | a dev repo (`~/dev/jarvis` or `~/content`) |
| 3 | Force `uv` over `pip`, rewrite the command | `PreToolUse` `Bash` | command, `updatedInput` | hooks can rewrite, not just block (Pocock's angle, updated) | Python project |
| 4 | Log every Bash command with timestamp | `PostToolUse` `Bash` | command, `jq` | stdin JSON, `tool_response` | any |
| 5 | Don't let Claude stop until tests pass | `Stop` | `prompt` hook, then `agent` hook | the 2 LLM handler types nobody shows; `stop_hook_active`; 8-block cap | project with a test suite |
| 6 | Post `last_assistant_message` to Slack via Hermes | `Stop` | command, `async: true` | payoff. Ties to 057. Uses `~/.hermes/scripts` or a curl to the Slack webhook | to verify on Tyler's Mac |

Every hook gets written by asking Claude to write it (Agentic Lab's four-part prompt: event, behavior, why, edge case), then opened and read line by line. That is the "engineering is not dead, you moved up a layer" beat and it keeps the video honest for an engineer audience.

**Unverified before filming:** beat 6 (Slack from a hook), beat 5 `agent` hook timing (60 s default, experimental), whether `~/dev/jarvis` has a test suite fast enough for beat 5.

**Verified on Tyler's Mac 2026-09-16 (Claude Code 2.1.273), demo files in `/tmp/hooks-demo-059/`:**

| Test | Result |
|---|---|
| `PreToolUse` `Bash` hook, `if: "Bash(rm *)"`, `exit 2`, under `claude -p --dangerously-skip-permissions` | Blocked. Transcript: `PreToolUse:Bash hook error: [...block-rm.sh]: Blocked by hook: recursive delete not allowed`. Directory survived. Payload showed `"permission_mode": "bypassPermissions"`. |
| Same hook with `exit 1` | Not blocked. Claude ran `rm -rf`, reported "exit 0, directory gone". Directory deleted. |
| stdin payload captured | `{"hook_event_name":"PreToolUse","tool_name":"Bash","tool_input":{"command":"rm -rf ...","description":"Remove the scratch directory"},"permission_mode":"bypassPermissions"}` |
| Bonus for the script | Claude noticed it could route around the hook with `rmdir` and declined on its own. Good on-camera moment: the hook blocked the pattern, the model respected the intent. |

---

## 4. Title and thumbnail inputs

Titles must pass `yt-title-check`. Raw material, not final:

- Claude Code Hooks Went From 9 Events to 33 (Build 6 Live)
- The 5 Claude Code Hook Types (Everyone Only Uses One)
- Claude Code Hooks in 2026: Build 6 That Actually Run
- Stop Putting Rules in CLAUDE.md. Use a Hook.
- I Built 6 Claude Code Hooks on Camera (2 Failed First)

Thumbnail concepts: a settings.json block with one line highlighted `"permissionDecision": "deny"` and a red BLOCKED terminal line; or the number 33 large over the lifecycle diagram; or split terminal showing `rm -rf` on the left and the block on the right.

---

## 5. Creator breakdown

- `research/youtube/creator-breakdowns/2026-09-16-agentic-lab-claude-code-hooks.md` (Agentic Lab, 8:32, 30,856 views). Beat table with his exact prompt, rhythm, weaknesses, and a 12-row his-beat / our-beat / exact-prompt plan.
- Sibling research from the same request: `research/2026-09-16-claude-code-hooks-refresh.md` (competitive table, docs fact-check table, corrected gaps, prior-art notes on ep13).

---

## 6. Corrections to prior material

### Old report (2026-03-22)
Its "Gaps" section described "hook templates for prompting" and "high-conversion hooks", meaning YouTube video hooks, not Claude Code lifecycle hooks. Wrong topic. The "Top Videos" list was three general Claude Code videos, none hooks-specific. Discard.

### ep13 course script (`youtube/ideas/claude-code-course/ep13-hooks-automation/script.md`)
Stale in 3 places that would fail on camera:
1. Scripts read `$TOOL_INPUT_FILE_PATH` and `$TOOL_INPUT_COMMAND` env vars. **Hooks receive JSON on stdin.** Use `jq -r '.tool_input.file_path'`.
2. settings.json shape has `"command"` directly on the matcher object. **Real shape needs the nested `"hooks": [{"type": "command", "command": ...}]` array.** The ep13 JSON would not register.
3. "Use `/hooks` to set one up interactively." **`/hooks` is read-only now.** Edit JSON or ask Claude.
Also lists 4 events (there are 33) and says "hooks are NOT AI" (true for `command`, false for `prompt` and `agent`). The section structure (format, log, protect) is still a good spine.

Decision needed from Tyler: 059 replaces ep13 as the hooks video, or ep13 stays parked for the course and 059 is standalone. This file assumes standalone.
