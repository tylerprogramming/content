# Every Claude Code Feature - Research Doc

**Purpose:** Reference/fact catalog for a YouTube video roughly titled "Every Claude Code Feature" / "All Claude Code Features."
**Compiled:** 2026-08-02
**Method:** Fetched the official docs at code.claude.com (overview, CLI reference, memory, MCP, hooks, skills, subagents, checkpointing, permission modes, model config, commands, agent SDK, and the What's New digests) plus supplementing knowledge. Version references reflect Claude Code v2.1.x (mid-2026). Source URLs at the bottom.

This is a reference doc, not a script. Every feature below has: what it is, why it matters, and a quick command/example.

> Note on accuracy: the docs changed a few things people still get wrong. Custom slash commands have been **merged into skills** (a `.claude/commands/deploy.md` file and a `.claude/skills/deploy/SKILL.md` both create `/deploy`). The `/agents` interactive wizard was **removed** in v2.1.198 (you now ask Claude or edit `.claude/agents/` directly). Both are called out below.

---

## 0. The mental model (say this early in the video)

Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your dev tools. The same engine runs across five "surfaces": **Terminal (CLI), VS Code, JetBrains, Desktop app, and Web (claude.ai/code)**. Your CLAUDE.md files, settings, skills, and MCP servers work across all of them. That "one engine, many surfaces" idea is the spine of the whole feature set.

Install (native, recommended):
```bash
curl -fsSL https://claude.ai/install.sh | bash   # macOS/Linux/WSL
# Windows PowerShell: irm https://claude.ai/install.ps1 | iex
# Homebrew: brew install --cask claude-code
```

---

## 1. Core CLI

**Interactive mode (the REPL).** Run `claude` in a project to start a session. Full terminal UI with real-time feedback, slash commands, the permission system, and all built-in tools.
- Why it matters: this is the default way to work. Everything else is a variation on it.
- `cd your-project && claude` or `claude "explain this codebase"` to open with a first prompt.

**Headless / print mode (`-p`).** `claude -p "query"` runs a query, prints the result, and exits. Non-interactive, built for scripting and CI.
- Why it matters: this is what makes Claude Code composable and Unix-friendly. You can pipe into it and chain it with other tools.
```bash
tail -200 app.log | claude -p "Slack me if you see anomalies"
git diff main --name-only | claude -p "review these changed files for security issues"
```

**`--output-format`.** `text` (default), `json` (full structured result after completion), or `stream-json` (streaming events for real-time processing). `--input-format` accepts `text` or `stream-json`.
```bash
claude -p --output-format json "analyze performance"
```
- Why it matters: `json` gives you a machine-readable result with cost/usage/model fields. This is the backbone of automation.

**`--json-schema`.** Constrain the final output to a JSON Schema you supply, validated after the workflow runs.
```bash
claude -p --json-schema '{"type":"object","properties":{...}}' "extract the API endpoints"
```

**Resuming sessions.**
- `claude -c` / `claude --continue`: reload the most recent conversation in the current directory.
- `claude -r "<id-or-name>" "query"` / `claude --resume`: resume a specific session (or open a picker).
- `--fork-session`: resume but branch to a new session ID instead of reusing the old one.
- `-n "name"` / `--name`: name a session; `--session-id <uuid>` to pin an ID.
- Why it matters: sessions persist. You can walk away and come back, or fork to try a second approach.

**Budget and turn limits (headless).** `--max-turns 3`, `--max-budget-usd 5.00` cap agentic turns and spend in `-p` mode.

**Other notable CLI subcommands:** `claude update`, `claude doctor` (diagnostics), `claude mcp ...` (MCP management), `claude plugin ...`, `claude setup-token` (long-lived OAuth token for CI), `claude auth login/logout/status`, `claude install [version]`.

---

## 2. CLAUDE.md and memory

**CLAUDE.md (project memory).** A markdown file Claude reads at the start of every session. Put build/test commands, conventions, architecture, and "always do X" rules here. Lives at `./CLAUDE.md` or `./.claude/CLAUDE.md`, committed to the repo so the whole team gets it.
- Why it matters: it is the single biggest lever on how well Claude works in your repo.
- `/init` generates a starting CLAUDE.md by analyzing your codebase (or suggests improvements if one exists).

**Scope hierarchy** (loaded broadest to most specific):
| Scope | Location |
|---|---|
| Managed policy (org) | `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS), `/etc/claude-code/CLAUDE.md` (Linux) |
| User (personal, all projects) | `~/.claude/CLAUDE.md` |
| Project (team) | `./CLAUDE.md` or `./.claude/CLAUDE.md` |
| Local (private, gitignored) | `./CLAUDE.local.md` |

Files are walked up the directory tree and concatenated; subdirectory CLAUDE.md files load on demand when Claude touches files there.

**Imports (`@path`).** `@docs/git-instructions.md` inlines another file at launch (relative or absolute paths, up to 4 hops deep). Wrap in backticks to reference a path without importing it. Also how you make Claude read an existing `AGENTS.md`: put `@AGENTS.md` at the top of CLAUDE.md.

**`.claude/rules/`.** Split instructions into topic files. Path-scoped rules with `paths:` frontmatter load only when Claude works on matching files, saving context.
```markdown
---
paths: ["src/api/**/*.ts"]
---
# API rules: validate all inputs, use the standard error format
```

**Auto memory (Claude writes it).** On by default. Claude saves its own learnings (build commands, debugging insights, preferences) to `~/.claude/projects/<project>/memory/MEMORY.md` and topic files, and reloads them every session. You see "Saved N memories" / "Recalled N memories" in the UI.
- Why it matters: Claude gets better at your repo over time without you writing anything.
- Toggle in `/memory`; disable per-project with `"autoMemoryEnabled": false`.

**`/memory` and the `#` shortcut.** `/memory` lists and opens all memory files and toggles auto memory. Telling Claude "remember that we use pnpm not npm" saves to auto memory; "add this to CLAUDE.md" edits the file. Run `/context` to confirm what actually loaded.

---

## 3. Slash commands (built-in + custom)

**Built-in commands** (fixed logic). A partial but useful list to show on screen:
`/help`, `/clear` (new empty context; aliases `/reset`, `/new`), `/compact` (summarize to free context), `/context` (visualize context usage), `/init`, `/model`, `/effort`, `/fast`, `/memory`, `/rewind`, `/hooks`, `/mcp`, `/permissions`, `/plan`, `/resume`, `/config` (alias `/settings`), `/status`, `/usage` (alias `/cost`), `/tasks`, `/agents`, `/skills`, `/plugin`, `/add-dir`, `/cd`, `/diff`, `/export`, `/copy`, `/login`, `/logout`, `/vim`, `/keybindings`, `/feedback`, `/doctor` (alias `/checkup`), `/branch`, `/fork`, `/goal`, `/desktop` (alias `/app`), `/mobile`, `/ide`, `/install-github-app`.

**Bundled skills** (prompt-based, orchestrated by Claude). Marked "Skill" in the docs: `/code-review`, `/verify`, `/run`, `/debug`, `/batch`, `/loop`, `/deep-research`, `/dataviz`, `/claude-api`, `/doctor`, `/fewer-permission-prompts`. Disable all except `/doctor` with `disableBundledSkills`.

**Custom slash commands = skills now.** A file at `.claude/commands/deploy.md` still works and creates `/deploy`. The recommended form is a skill (see next section). Project commands live in `.claude/commands/` or `.claude/skills/`; user commands in `~/.claude/commands/` or `~/.claude/skills/`. Arguments via `$ARGUMENTS`, `$0`/`$1`, and named args; frontmatter controls invocation.
- Why it matters: your team can ship `/review-pr`, `/deploy-staging`, `/commit` as version-controlled files.

---

## 4. Skills (SKILL.md)

**What it is.** A `SKILL.md` file (YAML frontmatter + markdown instructions) in a directory. Claude loads it automatically when relevant, or you invoke it with `/skill-name`. Follows the open Agent Skills standard (agentskills.io).
- Why it matters: this is the main extension mechanism. Unlike CLAUDE.md, a skill's body only loads when used, so long reference material costs almost no context until you need it.

**Where they live:**
| Location | Path | Applies to |
|---|---|---|
| Personal | `~/.claude/skills/<name>/SKILL.md` | all your projects |
| Project | `.claude/skills/<name>/SKILL.md` | this project |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | where plugin is enabled |

**Minimal example:**
```yaml
---
description: Summarizes uncommitted changes and flags risks. Use when the user asks what changed or wants a commit message.
---
## Current changes
!`git diff HEAD`
## Instructions
Summarize the diff in 2-3 bullets, then list risks.
```

**Key frontmatter:** `description` (how Claude decides to use it), `disable-model-invocation: true` (only you can trigger it, e.g. `/deploy`), `user-invocable: false` (only Claude), `allowed-tools` (pre-approve tools for the invoking turn), `context: fork` (run in an isolated subagent), `agent:` (which subagent type), `model` / `effort`, `paths:` (auto-load only for matching files), `argument-hint`.

**Dynamic context injection.** `` !`command` `` runs a shell command before the skill reaches Claude and inlines the output. `${CLAUDE_SKILL_DIR}` and `${CLAUDE_PROJECT_DIR}` resolve bundled script paths.

**Supporting files.** A skill directory can bundle scripts, templates, and reference docs that load only when referenced. Great demo: a Python script that generates an interactive HTML codebase visualization.

**skill-creator plugin** runs evals (should-trigger / output-quality A/B) so you can measure whether a skill actually helps.

---

## 5. MCP (Model Context Protocol)

**What it is.** An open standard for connecting Claude Code to external tools and data (GitHub, Sentry, Postgres, Notion, Slack, Figma, your own servers).
- Why it matters: instead of pasting data from another tool into chat, Claude reads and acts on that system directly.

**Adding servers:**
```bash
# Remote HTTP (recommended for cloud services)
claude mcp add --transport http notion https://mcp.notion.com/mcp
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_PAT"

# Local stdio (runs a process on your machine; note the -- separator)
claude mcp add --env AIRTABLE_API_KEY=KEY --transport stdio airtable -- npx -y airtable-mcp-server

# From raw JSON
claude mcp add-json weather '{"type":"http","url":"https://api.weather.com/mcp"}'
```
Transports: **http** (recommended), **sse** (deprecated), **stdio** (local), **ws** (WebSocket, config-only).

**Managing:** `claude mcp list` (shows health: Connected / Needs auth / Failed), `claude mcp get <name>`, `claude mcp remove <name>`, and `/mcp` inside a session (status, tool counts, OAuth login, disable a server without removing it).

**Scopes:** `local` (default, this project, private, in `~/.claude.json`), `project` (shared via `.mcp.json` committed to the repo), `user` (all your projects). Precedence: local > project > user > plugin servers > claude.ai connectors.

**Auth.** OAuth 2.0 supported; run `/mcp` to sign in, or from the shell `claude mcp login <name>` / `claude mcp logout <name>` (added v2.1.186). Pre-configured client IDs, fixed callback ports, dynamic `headersHelper`, and scope pinning are all supported.

**Connectors.** If you signed in with a claude.ai account, MCP servers you added in claude.ai (connectors from claude.ai/directory) show up automatically in Claude Code.

**Import from Claude Desktop:** `claude mcp add-from-claude-desktop`.

**Notable 2026 behavior:** MCP tool calls that run past two minutes auto-move to a background task so the session stays usable. Claude Code can also act as an MCP server, and MCP servers can push messages into a session via **channels**.

---

## 6. Subagents / the Agent tool / custom agents

**What they are.** Specialized assistants that run in their own context window with a custom system prompt, tool restrictions, and independent permissions. The main agent delegates via the Agent (Task) tool; the subagent works and returns only a summary.
- Why it matters: keeps noisy work (searching, log reading, big file dumps) out of your main context, and lets you route cheap work to Haiku.

**Built-in subagents:**
- **Explore** - fast, read-only, for search/codebase understanding (Write/Edit denied).
- **Plan** - read-only research agent used during plan mode.
- **general-purpose** - full tool access, multi-step tasks.
- Plus helpers: `statusline-setup`, `claude-code-guide`, `claude` (background sessions).

**Custom agents** live in `.claude/agents/` (project) or `~/.claude/agents/` (user) as markdown + frontmatter:
```markdown
---
name: code-improver
description: Scans files and suggests improvements. Use after writing or modifying code.
tools: Read, Grep, Glob
model: sonnet
---
You are a code improvement specialist. For each issue, explain it, show current code, provide an improved version.
```
Frontmatter: `name`, `description`, `tools`, `model`, `permissionMode`, plus optional persistent `memory` and preloaded `skills`.
- Note: the `/agents` creation wizard was removed in v2.1.198. Ask Claude to write the file or edit `.claude/agents/` directly.

**Foreground vs background.** As of Week 27 (v2.1.195+), subagents run in the **background by default** so Claude keeps working while they run. Subagents can spawn their own subagents (chains capped at 5 levels deep).

**Related orchestration:**
- **Dynamic workflows** (`/batch`, ultracode): Claude writes a script that orchestrates dozens to hundreds of subagents.
- **Agent teams**: multiple sessions that communicate.
- **Agent view** (`claude agents`): one screen showing every session (running / blocked on you / done).

---

## 7. Hooks

**What they are.** User-defined shell commands (or HTTP/prompt/agent calls) that Claude Code runs at fixed lifecycle events. Deterministic control: the thing always happens instead of relying on the model to choose it.
- Why it matters: auto-format after every edit, block edits to protected files, enforce policy users can't bypass, inject context, send notifications.

Configured in a `hooks` block in `settings.json` (`~/.claude/settings.json`, `.claude/settings.json`, `.claude/settings.local.json`, managed, or plugin/skill/agent frontmatter). Browse with `/hooks` (read-only menu).

**Lifecycle events (exhaustive-ish list):**
`SessionStart`, `Setup`, `UserPromptSubmit`, `UserPromptExpansion`, `PreToolUse`, `PermissionRequest`, `PermissionDenied`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `Notification`, `MessageDisplay`, `SubagentStart`, `SubagentStop`, `TaskCreated`, `TaskCompleted`, `Stop`, `StopFailure`, `TeammateIdle`, `InstructionsLoaded`, `ConfigChange`, `CwdChanged`, `DirectoryAdded`, `FileChanged`, `WorktreeCreate`, `WorktreeRemove`, `PreCompact`, `PostCompact`, `Elicitation`, `ElicitationResult`, `SessionEnd`.

**Example: auto-format after edits.**
```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write" }] }
    ]
  }
}
```
Hooks talk back via exit codes (exit 0 = proceed, exit 2 = block with stderr fed to Claude) or structured JSON on stdout. Matchers filter by tool name (`Bash`, `Edit|Write`, `mcp__github__.*`); the `if` field filters by tool + arguments (`Bash(git *)`).

**Hook types:** `command` (default), `http` (POST to a URL), `mcp_tool`, `prompt` (a Claude model returns a yes/no decision), `agent` (a subagent verifies against the actual codebase, e.g. "run the tests before allowing Stop").

---

## 8. Plan mode

**What it is.** A permission mode where Claude researches and proposes changes without editing anything, then presents a plan for approval.
- Why it matters: for anything non-trivial, planning first is the single biggest quality win. It reads files and runs read-only commands, writes a plan, and waits.

Enter with `Shift+Tab` (cycles default -> acceptEdits -> plan), prefix a single prompt with `/plan`, or start with `claude --permission-mode plan`. When the plan is ready you choose: auto-accept edits, manually approve each edit, refine with Ultraplan on the web, or keep planning. `Ctrl+G` opens the plan in your editor. Approving a plan auto-names the session.

**opusplan** alias runs Opus during planning, then Sonnet for execution.

---

## 9. Background tasks / long-running commands

- **Background agents:** `claude --bg "investigate the flaky test"` starts a session that runs detached and returns immediately; monitor with `claude agents`, `claude attach <id>`, `claude logs <id>`, `claude stop <id>`.
- **`--exec`:** run a shell command as a PTY-backed background job (`claude --bg --exec 'pytest -x'`).
- **`/tasks`:** list background work and subagent tasks in a session.
- **Auto-backgrounding:** MCP tool calls over 2 minutes and forked skills move to the background automatically.
- **`/loop`:** repeat a prompt on an interval within a session (polling). **Monitor tool** streams background events into the conversation so Claude can tail logs and react live.
- Why it matters: kick off long jobs, keep working, get pulled back when they finish.

---

## 10. Checkpoints / rewind

**What it is.** Claude Code automatically snapshots your code before each prompt. `/rewind` (or double-`Esc` on an empty prompt) opens a menu of every prompt in the session.
- Why it matters: a session-level undo so you can attempt ambitious changes knowing you can revert.

Menu options: Restore code and conversation, Restore conversation only, Restore code only, **Summarize from here** / **Summarize up to here** (compress context to free the window). Keeps snapshots for the 100 most recent checkpoints; persists with the session so you can rewind after resuming; deleted with the session after 30 days.

**Limitations to state honestly on camera:** does NOT undo files changed by bash commands (`rm`, `mv`, `cp`), does NOT restore background-subagent edits, does NOT track external/other-session changes, and skips symlinked/hard-linked paths. It is "local undo," not a replacement for git.

---

## 11. Permissions and settings

**Permission modes** (cycle with `Shift+Tab`; the "review every action" mode is labeled **Manual**, config value `default`):
| Mode | Runs without asking | Best for |
|---|---|---|
| `default` (Manual) | reads only | sensitive work |
| `acceptEdits` | reads + file edits + common fs commands (mkdir, touch, mv, cp) | iterating on code you review after |
| `plan` | reads (+ classifier-approved commands) | exploring before changing |
| `auto` | everything, with background safety checks | long tasks, fewer prompts |
| `dontAsk` | only pre-approved tools | locked-down CI |
| `bypassPermissions` | everything | isolated containers/VMs only |

**Auto mode** (2026 flagship, GA on all plans) deserves its own beat: a separate classifier model reviews each risky action before it runs, blocking escalations, unrecognized infrastructure, and prompt-injection-driven actions while letting safe work through. Blocks things like `curl | bash`, force push, prod deploys, `rm -rf` on unresolved variables, and exfiltration of secrets; allows local edits, dependency installs, read-only HTTP, and pushes to your repo's branches. Falls back to prompting after repeated blocks.

**Permission rules** (in settings): `allow`, `ask`, `deny`. Syntax like `Bash(git log *)`, `Edit(*.ts)`, `Agent(model:opus)`. `/permissions` manages them; `/fewer-permission-prompts` scans your transcripts and proposes an allowlist. Deny rules always win, even over hook "allow" and bypass mode.

**Settings files & precedence:** managed policy > `--settings` > `.claude/settings.local.json` (personal, gitignored) > `.claude/settings.json` (project, committed) > `~/.claude/settings.json` (user). `/config` (alias `/settings`) opens the UI or sets values inline. `--setting-sources`, `--safe-mode` (disable all customizations for troubleshooting), and `--bare` (skip auto-discovery of hooks/skills/plugins/MCP) are useful debugging flags.

**Protected paths.** Writes to `.git`, `.claude`, shell rc files, `.mcp.json`, `.npmrc`, etc. are never auto-approved except in bypass mode.

---

## 12. Models & thinking

**Model selection.** `/model` (picker, or `/model sonnet` directly; Enter saves as default, `s` = session only), `--model` flag, `ANTHROPIC_MODEL` env var, or the `model` setting.

**Aliases:** `sonnet`, `opus`, `haiku`, `fable`, `best`, `default`, plus `sonnet[1m]` / `opus[1m]` (1M-token context) and `opusplan` (Opus to plan, Sonnet to execute). Current mid-2026 resolution on the Anthropic API: `opus` -> Opus 5, `sonnet` -> Sonnet 5. **Fable 5** is the most capable model for long autonomous sessions (`/model fable`). Pin exact versions with full names like `claude-opus-5`.

**Effort levels** (`/effort` or `--effort`): `low`, `medium`, `high`, `xhigh`, `max`, plus `ultracode` (sends xhigh AND orchestrates dynamic workflows). Effort controls **adaptive reasoning** - the model decides per step whether and how much to think. Default is `high` on most models. Slider also appears in `/model`.

**Extended / adaptive thinking.** Fable 5, Sonnet 5, and Opus 4.7+ always use adaptive reasoning (thinking is optional per step). `Ctrl+O` toggles verbose mode to see reasoning as gray italic text. **`ultrathink`**: type it anywhere in a prompt for deeper reasoning on that one turn without changing your effort setting (other phrases like "think hard" are NOT special keywords).

**Fast mode** (`/fast`): lower-latency responses. **`--fallback-model`**: up to three fallbacks tried in order when the primary is overloaded.

---

## 13. Image input, web search, web fetch

- **Image input.** Paste or drag an image (screenshot, error, mockup, diagram) into the prompt. Claude reads it. Great for "here's the broken UI, fix it" and design-to-code.
- **Web search.** Built-in WebSearch tool; Claude searches the live web when a task needs current info. Session cap defaults to 200 searches (tunable).
- **Web fetch.** Built-in WebFetch tool pulls a URL, converts to markdown, and reads it. Handy for "read these docs and implement against them."
- **`/deep-research`.** Bundled skill that fans out web searches, fetches sources, and synthesizes a cited report.

---

## 14. Git & GitHub integration

- **Git in-session.** Claude stages changes, writes commit messages, creates branches, and opens PRs directly. `claude "commit my changes with a descriptive message"`.
- **GitHub Actions / GitLab CI/CD.** Automate PR review and issue triage in CI. `/install-github-app` sets up the GitHub app.
- **Code Review.** `/code-review [--fix] [--comment] [target]` reviews a diff for correctness bugs and cleanup; automatic review on every PR is available via GitHub Code Review.
- **`/autofix-pr`.** Spawns a session that watches a PR and pushes fixes when CI fails.
- **`gh` CLI.** Claude uses `gh` for GitHub operations when available.
- **Worktrees.** `claude -w feature-auth` (add `--tmux`) runs parallel sessions in isolated git worktrees.
- **`/diff`** opens an interactive diff viewer; **`/branch`** and **`--fork-session`** branch a conversation to try alternatives.

---

## 15. Surfaces: IDEs, Desktop, Web, Mobile, Slack, Chrome

- **VS Code / Cursor extension.** Inline diffs, @-mentions, plan review, conversation history in the editor. Mode selector at the bottom of the prompt box.
- **JetBrains plugin.** IntelliJ, PyCharm, WebStorm, etc. Runs the CLI in the IDE terminal with interactive diff viewing.
- **Desktop app** (macOS/Windows/Linux beta). Visual diffs, multiple sessions side by side, an in-app browser, scheduled tasks, and cloud sessions. `/desktop` hands a terminal session off to it.
- **Web** (claude.ai/code). No local setup, run long tasks and parallel tasks in the browser, work on repos you don't have locally. `claude --cloud "fix the login bug"` starts a web session from the terminal; `claude --teleport` pulls a web session into your local terminal.
- **Mobile** (Claude app iOS/Android). Kick off and monitor tasks, push notifications when a task finishes.
- **Remote Control.** `claude remote-control` continues a local session from your phone or any browser.
- **Slack.** Mention `@Claude` with a bug report, get a PR back. `/install-slack-app`.
- **Chrome / Claude in Chrome** (`claude --chrome`, GA in 2026). Debug live web apps: Claude drives the browser, reads console/network, interacts with pages.
- **Computer use** (research preview in the CLI). Claude opens native apps and clicks through UI to verify changes.
- **Channels.** Push events from Telegram, Discord, iMessage, or your own webhooks into a running session.

---

## 16. Output styles, status line, other customization

- **Output styles.** Change how Claude communicates (e.g. a **Proactive** style for more autonomous behavior while keeping prompts). Configure via output-styles files.
- **Status line.** `/statusline` customizes the bottom status bar (a `statusline-setup` agent helps configure it); show git branch, model, cost, whatever you script.
- **Themes.** Custom color themes buildable and shippable via `/theme` or a plugin.
- **Keybindings.** `/keybindings` edits `~/.claude/keybindings.json`; `/vim` enables vim keybindings; `vimInsertModeRemaps` maps `jj` to Escape.
- **Plugins.** Package skills, subagents, hooks, and MCP servers together and share them. `/plugin`, `claude plugin install <name>@<marketplace>`, `/plugin marketplace add ...`. Official marketplace: `claude-plugins-official`. Load ad-hoc with `--plugin-dir` (dir or .zip) or `--plugin-url`.
- **Focus / recap.** `/focus` shows only the last prompt and final response; session recap shows what happened while a terminal was unfocused.

---

## 17. The Claude Agent SDK (brief)

**What it is.** The same tools, agent loop, and context management that power Claude Code, available as a **library in Python and TypeScript** so you can build your own agents in your own process.
- **How it differs from the CLI:** the CLI is the interactive terminal app for daily use; the Agent SDK is for building production agents with full control over orchestration, tool access, and permissions. It loads the same `.claude/` skills, commands, memory, subagents, hooks, and MCP config.
- To drive the same loop from another language, run the CLI as a subprocess with `-p --output-format json`.
- Not to be confused with the **Client SDK** (raw Anthropic API, you write the tool loop) or **Managed Agents** (hosted, Anthropic runs the sandbox).
- Install: `npm i @anthropic-ai/claude-agent-sdk` or `pip install claude-agent-sdk`. Requires API-key auth for third-party products (no claude.ai login).

---

## 18. Other notable capabilities (grab-bag)

- **`/goal`.** Set a completion condition and Claude keeps working across turns until it holds.
- **`/context`.** Visualize context-window usage as a colored grid (Memory files, Skills, MCP tools, conversation).
- **`/usage` (`/cost`).** Breaks down what drives your plan limits by skill, subagent, plugin, and MCP server.
- **`/compact`.** Manually summarize to free context; hooks can re-inject context after compaction.
- **Routines.** Scheduled cloud agents (cron, GitHub events, or API triggers) that run on Anthropic infrastructure even when your machine is off. Create with `/schedule`. Desktop scheduled tasks run locally instead.
- **Ultraplan / Ultrareview.** Cloud plan authoring with browser review; a fleet of bug-hunting agents (`/ultrareview`, `claude ultrareview` in CI).
- **Artifacts.** Turn a session's output into a live, shareable page on claude.ai; as of Week 29 an artifact can call each viewer's MCP connectors for live data.
- **Sandboxing.** A sandboxed Bash tool with filesystem/network isolation.
- **Advisor tool** (`--advisor opus`, `/advisor`) escalates hard decisions to a stronger model.
- **Voice dictation, accessibility (screen reader mode), fullscreen rendering.**

---

## MOST DEMO-WORTHY FEATURES (the "I didn't know it could do that" list)

Pick 8-12 of these for the video. Ordered roughly by wow-per-second.

1. **Plan mode + rewind together.** Plan a big change, let it run, hit `/rewind` (or double-Esc) to snap the code back if you don't like it. The safety net is the story.
2. **Auto mode.** A classifier approves safe actions and blocks dangerous ones (force push, `curl | bash`, secret exfiltration) so you get long autonomous runs without blanket `--dangerously-skip-permissions`. This is the flagship 2026 feature.
3. **Skills with a bundled script.** Show the codebase-visualizer skill: ask "visualize this codebase," Claude runs a bundled Python script, and an interactive HTML tree opens in the browser. Skills can do things a prompt alone can't.
4. **MCP in one command.** `claude mcp add --transport http sentry https://mcp.sentry.dev/mcp`, then "what are the most common errors in the last 24 hours?" Live production data in chat, no copy-paste.
5. **Headless + pipe.** `tail -200 app.log | claude -p "Slack me if you see anomalies"`. Claude Code as a Unix citizen surprises people.
6. **Background agents / agent view.** `claude --bg "fix the flaky test"`, keep working, watch it in `claude agents`. Parallel agents on one screen.
7. **Subagents preserving context.** Delegate a noisy search to Explore; the main context stays clean. Show the `/context` grid before/after.
8. **Hooks that enforce rules.** A PreToolUse hook that blocks edits to `.env`, or a PostToolUse hook that auto-formats every edit. Deterministic guardrails.
9. **Image input to working code.** Paste a screenshot of a broken UI or a design mockup and get a fix/implementation.
10. **`claude --cloud` / teleport.** Start a task on the web (or from the terminal), continue on your phone, pull it back to the terminal with `claude --teleport`. Same session, many surfaces.
11. **Claude in Chrome / computer use.** Claude drives a real browser to reproduce and verify a bug, reading console and network.
12. **`/rewind` "summarize from here."** Compress a verbose debugging session mid-stream to reclaim context without losing your original instructions.

Bonus if you want a laugh: `/radio` (Claude FM lo-fi radio).

---

## WHAT'S GENUINELY NEW / RECENT (so the video feels current)

Sourced from the What's New digests, newest first (Q2-Q3 2026):

- **Week 29 (Jul 13-17):** Artifacts can call each viewer's MCP connectors for live data; **screen reader mode** (`claude --ax-screen-reader`); **`/fork`** copies a conversation into a new background session (in-session fork is now `/subtask`); MCP calls over 2 min auto-background; session-wide caps on web searches and subagent spawns.
- **Week 28 (Jul 6-10):** **In-app browser on Desktop**; **`/doctor`** is now a full setup checkup that can fix issues (alias `/checkup`); auto mode blocks transcript tampering and unresolved-variable `rm -rf`.
- **Week 27 (Jun 29-Jul 3):** **Claude Sonnet 5** becomes the default (1M-token context, adaptive thinking on by default); **Claude in Chrome GA**; **subagents run in the background by default**; **Claude Desktop on Linux** beta.
- **Week 26 (Jun 22-26):** **`claude mcp login` / `logout`** from the shell; shell mode responds to command output; `/rewind` can resume from before a `/clear`.
- **Week 25 (Jun 15-19):** **Artifacts** beta; deny/ask rules match tool parameters (`Agent(model:opus)`); `/config key=value` from the prompt; auto mode blocks destructive git.
- **Week 24 (Jun 8-12):** `/cd` mid-session; subagents spawn subagents (5 deep); `--safe-mode`; `fallbackModel` (up to three).
- **Week 22 (May 25-29):** **Claude Opus 4.8** default for Max/Enterprise/API; **dynamic workflows** (dozens-to-hundreds of subagents); security-guidance plugin.
- **Week 20-21 (May):** **Agent view** (`claude agents`); **`/goal`**; **auto mode on Pro**; **`/code-review`** command; `/usage` breakdown.
- **Week 16-17 (Apr):** **Opus 4.7** + **`xhigh` effort** and the `/effort` slider; **Routines** (scheduled cloud agents); **`/ultrareview`** and **Ultraplan**; mobile push notifications; CLI moved to native binaries.
- **Week 13-14 (Mar):** **Auto mode** research preview (the classifier permission system); **computer use** in the CLI; conditional `if` hooks; native PowerShell tool for Windows.

Headline for the video: the two things that most change day-to-day work in 2026 are **auto mode** (autonomous but safe) and the **skills = commands** consolidation, on top of **Sonnet 5 / Opus 5 / Fable 5** with adaptive thinking.

---

## Sources

- Overview: https://code.claude.com/docs/en/overview
- Docs index (all 174 pages): https://code.claude.com/docs/llms.txt
- CLI reference: https://code.claude.com/docs/en/cli-reference
- Memory / CLAUDE.md: https://code.claude.com/docs/en/memory
- Skills: https://code.claude.com/docs/en/skills
- Commands (built-in + bundled skills): https://code.claude.com/docs/en/commands
- MCP: https://code.claude.com/docs/en/mcp  (quickstart: https://code.claude.com/docs/en/mcp-quickstart)
- Subagents: https://code.claude.com/docs/en/sub-agents
- Hooks guide: https://code.claude.com/docs/en/hooks-guide  (reference: https://code.claude.com/docs/en/hooks)
- Permission modes: https://code.claude.com/docs/en/permission-modes  (permissions: https://code.claude.com/docs/en/permissions)
- Model config: https://code.claude.com/docs/en/model-config
- Checkpointing / rewind: https://code.claude.com/docs/en/checkpointing
- Plan mode: https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode
- Agent SDK: https://code.claude.com/docs/en/agent-sdk/overview
- Headless: https://code.claude.com/docs/en/headless
- Settings: https://code.claude.com/docs/en/settings
- Output styles: https://code.claude.com/docs/en/output-styles  |  Status line: https://code.claude.com/docs/en/statusline
- Plugins: https://code.claude.com/docs/en/plugins
- Agent view: https://code.claude.com/docs/en/agent-view  |  Worktrees: https://code.claude.com/docs/en/worktrees
- What's New index: https://code.claude.com/docs/en/whats-new/index  (Week 29: https://code.claude.com/docs/en/whats-new/2026-w29)
