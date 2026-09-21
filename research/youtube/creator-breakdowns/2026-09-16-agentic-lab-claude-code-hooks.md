# Creator breakdown: Agentic Lab, "Claude Code Hooks, Explained Simply."

| Field | Value |
|---|---|
| Video | https://youtube.com/watch?v=AP7c9YTcaw8 |
| Channel | Agentic Lab (host: Roman) |
| Views | 30,856 (yt-dlp, 2026-09-16) |
| Likes / comments | 289 / 8 |
| Duration | 8:32 |
| Uploaded | 2026-08-27 |
| Transcript | `~/content/transcripts/transcript_AP7c9YTcaw8.txt` (yt-dlp auto captions, 47 lines) |
| Rank in pull | #1 of 25 for "claude code hooks", 365 days |
| Target video | Claude Code hooks refresh, number not yet assigned. Research: `research/2026-09-16-claude-code-hooks-refresh.md` |

## Beat table

Timestamps from the transcript. Prompts quoted verbatim from captions (auto captions, so "cloud code" = Claude Code, "claw.md" = CLAUDE.md).

| # | Beat | Time | What he does on screen |
|---|---|---|---|
| 1 | Cold open claim | 0:00-0:40 | Talking head. "Hooks are the most powerful feature for coding agents. Yet most people don't really understand them." Calls the Anthropic docs "quite nebulous." Promises: what hooks are, how they relate to agents, "the insane things you can do." |
| 2 | Credential | 0:40-0:51 | "I'm Roman. I published a top 3% paper at NeurIPS." |
| 3 | Definition | 0:51-1:34 | One line: "A hook is an event that triggers a script. The event answers when should my code run and the script answers what should it do." Worked example: SessionEnd fires, script spawns an agent that summarizes the session into a markdown knowledge base. |
| 4 | Lifecycle | 1:34-2:31 | Prose list, no screen: "user submits a prompt, Claude compacts, a subagent is spawned, a tool is called, a session begins." Compares to webhooks. |
| 5 | Why hooks | 2:31-3:40 | "A language model is probabilistic... the rules you write in your CLAUDE.md don't always get followed, especially over a long session. A script is the opposite: cheap, instant, identical every time." Rule of thumb: "if the check is binary and mechanical, it should be in a hook. If it needs judgment, leave it at the prompt level." Quotes the docs: hooks make actions "always happen rather than relying on the LLM to choose to run them." |
| 6 | Four-part prompt frame | 3:40-5:06 | Event, behavior, why, edge case. On edge cases: "I prefer to eval my hooks rather than trying to predefine every single edge case." Tip: "bidirectional prompting", let the model ask you questions first. |
| 7 | The prompt, typed | 5:06-6:10 | His exact prompt: "Can we create a session end hook which spawns a forked claude -p agent to summarize the session into my knowledge base, probably on every session. The point is persistent memory of what I've worked on and my patterns. Watch out for knowledge base bloat and don't let subagents or automations summarize their own sessions." Shows the JSON Claude produces. "You just have Claude eat that complexity for you." |
| 8 | Event list | 6:10-6:31 | Full-screen list. "Pause the video if you want." Says he compiled one use case per event, available in his free community. |
| 9 | Advanced, 3 items | 6:31-7:39 | (a) hooks can trigger HTTP, an MCP tool, a prompt, or a subagent; (b) hooks inside a skill or custom agent only run when that skill is invoked; (c) matchers, e.g. matcher Bash on PreToolUse; (d) hooks that spawn another Claude Code or Codex, e.g. on Stop spawn an agent to red-team the implementation. |
| 10 | Homework + CTA | 7:39-8:32 | "Go open up your CLAUDE.md or your rules files. Read every single line and ask one question: could this be a hook instead?" Then "pick your battles", install some, remove the bloat. Community link twice. |

Counts: 10 beats, 1 typed prompt, 0 hooks executed on screen, 0 artifacts shown, 2 CTAs to the same link.

## Rhythm

| Technique | Where | Reusable? |
|---|---|---|
| Define in one sentence, then one worked example, then the general case | Beats 3-4 | Yes. Event = when, script = what. Steal the sentence shape, not the words. |
| Name the enemy (probabilistic model vs deterministic script) before showing the tool | Beat 5 | Yes. This is why the video works at 30,856 with no demo: the "why" is sharp. |
| Give a prompt template instead of teaching JSON | Beats 6-7 | Yes. "Claude eats the complexity" is the CC-user angle. |
| Defer the full list to a downloadable | Beat 8 | Partial. We should show the list on screen and pick 5, not gate it. |
| End on homework, not a recap | Beat 10 | Yes. "Could this be a hook instead?" is the best line in the video. We do the homework on camera. |

## What works

| Item | Why |
|---|---|
| Length 8:32 | Median of the top 5. Nobody bounces on a hooks explainer this short. |
| "Explained Simply" against "nebulous docs" | Positions against the docs. 2 of the top 5 titles use "explained." |
| One prompt, not a JSON tutorial | The only video in the top 5 that does not open settings.json first. |
| Rule of thumb at 3:18 | "Binary and mechanical = hook, judgment = prompt." Quotable. |

## Weaknesses (our openings)

| Weakness | Opening |
|---|---|
| 0 hooks run on screen | Run 5. Show the blocked command, the log line, the formatted file, the Slack message. |
| Event list is dated (says 21; docs list 33 as of 2026-09-16) | Show the current table from code.claude.com/docs/en/hooks-guide and say the number. |
| "Explained" title | Tyler's rule bans it. Use number + outcome. |
| Advanced section is a list, not a demo | Demo one `prompt` Stop hook and one hook in skill frontmatter. 0 of 25 videos do either. |
| Homework is left to the viewer | Do it live on a real CLAUDE.md. Pick 3 lines, convert them, delete them from the file. |
| Never shows the debug path | Show `claude --debug-file` once when a hook does not fire. Every hooks video has that comment thread. |
| Payoff is a community link | Payoff is the phone buzzing from a Stop hook. |
| No `if` field, no PermissionRequest auto-approve | Both are current docs, both are 0 of 25. One line each. |

## Her beat / our beat / exact prompt

Tyler's machine 2026-09-16: `~/.claude/settings.json` exists, 0 hooks configured. `~/.claude/skills` is symlinked to the skills repo. Slack bot token exists in the Hermes profiles (used by @coder tonight). Everything marked "to build" is not verified yet.

| # | His beat | Our beat | Exact prompt (Tyler types this into Claude Code) | State |
|---|---|---|---|---|
| 1 | Cold open claim | Cold open: phone on camera, Slack buzz "Claude finished: 057 package committed." Cut to terminal. "That was a hook. Eight lines of JSON." | none | to build (Stop hook to Slack) |
| 2 | Credential | Skip. Show the CLAUDE.md instead: "This is my global CLAUDE.md. 40 lines of rules. Half of them Claude forgets by turn 30." | none | ready, `~/.claude/CLAUDE.md` exists |
| 3 | Definition | Same sentence shape, our words: "A hook is a when plus a what. When Claude does X, run this." Then show the docs lifecycle table, say "33 events, you need 5." | none | ready, docs table |
| 4 | Lifecycle | Name the 5: PreToolUse, PostToolUse, Notification, Stop, SessionStart. One line each on when it fires. | none | ready |
| 5 | Why hooks | Keep his enemy framing. Add the docs line: a PreToolUse deny blocks even under `--dangerously-skip-permissions`. "Hooks tighten. They never loosen." | none | ready, hooks-guide "Hooks and permission modes" |
| 6 | Four-part prompt | Same frame, shorter: when, what, why, one edge case. | none | ready |
| 7 | One typed prompt | Hook 1, PreToolUse guard. Type it, show the JSON, then make Claude try to edit `.env` and get blocked. | `Add a PreToolUse hook on Edit and Write that blocks any edit to .env, package-lock.json, or anything under .git/. Put the script in .claude/hooks/protect-files.sh, register it in .claude/settings.json for this project, and exit 2 with a one-line reason so you see why it was blocked. Then try to add a comment to .env so I can watch it fail.` | to build; matches docs example |
| 8 | Event list | Hook 2, PostToolUse formatter. Show the file change on disk. | `Add a PostToolUse hook matching Edit|Write that runs prettier on the edited file path. Use jq to pull tool_input.file_path. Project settings, not global. Then edit any .js file with single quotes and let me see the hook rewrite them.` | to build; matches docs example |
| 9a | Advanced list | Hook 3, `if` field. 0 of 25 videos show this. | `Change the PreToolUse guard so it only spawns when the Bash command starts with git. Use the "if" field with "Bash(git *)". Then run npm test and git status so I can see it fire on one and not the other.` | to build; docs "Filter by tool name and arguments" |
| 9b | Advanced list | Hook 4, `prompt` type Stop hook. Honest line: this one calls Haiku, it costs tokens. | `Add a Stop hook of type prompt that checks whether every task I asked for this turn is done. If not, return ok false with the reason so you keep going. Then give me a two-part task and stop after part one on purpose so I can watch the hook push you.` | to build; docs "Prompt-based hooks" |
| 9c | Advanced list | Hook 5, Notification to Slack, plus a Stop hook that posts to Slack. The 057 ending, again. | `Add a Notification hook with matcher idle_prompt and a Stop hook, both type command, that post a one-line message to my Slack home channel using the bot token in ~/.hermes/profiles/coder/.env. Message format: "Claude Code: <last 80 chars of last_assistant_message>". Global settings so it works in every repo.` | to build; token exists, curl to chat.postMessage verified tonight |
| 10 | Homework CTA | Do the homework live: open `~/.claude/CLAUDE.md`, pick 3 rules, ask Claude which are "binary and mechanical", convert one to a hook, delete the line. | `Read my global CLAUDE.md. For each rule, tell me in a table: binary and mechanical (hook) or needs judgment (stays). Then convert the first hook candidate and delete that line from CLAUDE.md.` | ready, file exists; conversion to build |
| 11 | none | Debug beat, 45 s. Break a hook on purpose (chmod -x), show the error in the transcript, run `claude --debug-file /tmp/claude.log`, fix it. | none | to build |
| 12 | none | Close on the phone buzzing again. "Every hook you saw is in one JSON file. It is in the description." | none | to build |

## Possible extras (not in the reference, all current docs)

| Extra | One line |
|---|---|
| Hooks in skill frontmatter | A hook that only exists while `/yt-package` is running. Tyler's skills repo makes this concrete. 0 of 25 videos. |
| PermissionRequest auto-approve for ExitPlanMode | Docs example. Stop clicking yes on every plan. |
| SessionStart with `compact` matcher | Re-inject "use Bun, run tests before commit" after every compaction. |
| `async: true` | Long test suites in the background. |
| StopFailure with `rate_limit` matcher | The exact failure @packager and @coder hit tonight. Log it, alert on it. |

## Filming notes

- Set all 5 hooks up before filming, verify each fires, then delete them and rebuild on camera. Do not demo on empty state.
- Say the seam when switching from the fresh project settings to the global settings for the Slack hook.
- Length target 12-15 min. Cut the debug beat first if over.
- Title candidates, Tyler's rules (number + outcome, second person, no "Explained", no money): "5 Claude Code Hooks You Should Set Up Today", "Stop Repeating Yourself in CLAUDE.md: 5 Hooks That Enforce It", "Claude Code Hooks: 5 Rules Claude Can Never Break".
