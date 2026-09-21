# Creator breakdown: Agentic Lab, "Claude Code Hooks, Explained Simply."

| Field | Value |
|---|---|
| Video | https://www.youtube.com/watch?v=AP7c9YTcaw8 |
| Creator | Agentic Lab (Roman) |
| Views | 30,856 (yt-dlp, 2026-09-16) |
| Duration | 8:32 |
| Uploaded | 2026-08-27 (20 days before this breakdown) |
| Transcript | `~/content/transcripts/transcript_AP7c9YTcaw8.txt` |
| Target | 059, Claude Code hooks |

Chosen because it is the newest hooks-only video with traction (30K in 3 weeks). It is the current ceiling for a "simple" hooks video, and it has no live demo, which is where 059 wins.

## Beat table

| # | Beat | Time | What he does on screen |
|---|---|---|---|
| 1 | Cold open | 0:00 - 0:50 | Talking head. "Hooks are the most powerful feature for coding agents. Yet most people don't understand them. Even Anthropic docs are quite nebulous." Credential: top 3% NeurIPS paper. |
| 2 | Definition | 0:51 - 1:34 | Slide. "A hook is an event that triggers a script. The event answers when should my code run and the script answers what should it do." Example in words only: SessionEnd → spawn agent → summarize session to markdown knowledge base. |
| 3 | Lifecycle | 1:34 - 2:30 | Slide. "Think in terms of the agent life cycle." Lists: user submits a prompt, compaction, subagent spawned, tool called, session begins. Compares to webhooks. |
| 4 | Why hooks | 2:31 - 3:40 | Slide. LLM is probabilistic; CLAUDE.md rules "don't always get followed, especially over a long session." Script is "cheap, instant, identical every time." Quotes docs: hooks make actions "always happen rather than relying on the LLM." Rule: "if the check is binary and mechanical, it should be in a hook. If it needs judgment, leave it at the prompt level." |
| 5 | The four-part prompt | 3:40 - 5:06 | Slide. His template for asking Claude to write a hook: **event, behavior, why, edge case.** "I prefer to eval my hooks rather than predefine every edge case." Tip: "bidirectional prompting", let the model ask you questions. |
| 6 | Example prompt | 5:06 - 6:10 | Slide with the prompt text: "can we create a session end hook which spawns a forked claude -p agent to summarize the session into my knowledge base. Probably on every session. The point is persistent memory of what I've worked on and my patterns. Watch out for knowledge base bloat and don't let sub agents or automations summarize their own sessions." Shows the JSON Claude produced. "You just have Claude eat that complexity." |
| 7 | Event list | 6:10 - 6:31 | Slide, full event list, "pause the video." Lead magnet: one use case per event in his free Skool. |
| 8 | Advanced | 6:31 - 7:39 | Slide. Hooks can trigger HTTP, MCP tool, prompt, or subagent. Hooks inside a skill or custom agent. Matchers ("an if statement at the hook layer"). Hooks that spawn other Claude Code or Codex instances (Stop → red-team agent). |
| 9 | Call to action | 7:39 - 8:32 | "Open your CLAUDE.md, read every line, ask: could this be a hook instead?" Skool link twice. |

Live demos: **0**. Terminal on screen: **0**. Hooks actually run on camera: **0**.

## The rhythm

*Define in one sentence → one concrete example in words → the reason it matters → a prompt template → the prompt → say "Claude handles the complexity" → list of everything else → CTA.* Every beat is a slide with talking head. The technique that works is the **one-sentence definition** ("event that triggers a script; event = when, script = what") and the **binary/mechanical vs judgment** rule. Both are quotable and both are true.

## What works

| Thing | Why |
|---|---|
| "Explained Simply" title on a topic people find murky | He names the pain (docs are nebulous) in the first 10 seconds |
| Event = when, script = what | Sticks. Steal it, credit not needed, it is the docs' own framing |
| The four-part prompt (event, behavior, why, edge case) | Reusable. This is how Tyler should have Claude write every hook on camera |
| "Could this be a hook instead?" CTA | Gives the viewer a job to do after the video |
| 8:32 | Short enough to finish. 30K in 3 weeks on a channel of this size |

## Weaknesses (our openings)

| Weakness | 059 answer |
|---|---|
| Zero demos. The one example (SessionEnd → summarize) is never run | Build 6 hooks live, each one runs, at least 2 fail first and get fixed on camera |
| Says HTTP, MCP, prompt, subagent handler types exist, shows none | Show `prompt` and `agent` hooks on `Stop` actually looping |
| No failure modes. Viewer copies a hook, forgets `chmod +x`, gate is silently off | Show the exit 1 vs exit 2 mistake and the chmod error live |
| No JSON input shown. Viewer does not know the payload shape | `cat` the stdin JSON to a file on the first hook, open it, read the fields |
| Event list is a slide to pause on | Say "33" out loud, show the docs table, then say "you need 6" |
| The example hook is a knowledge base he never shows | Tyler's payoff hook posts to Slack through Hermes, shown landing |
| Audience is generic "coding agents" (Claude Code, Codex, Copilot) | 059 is Claude Code only, current schema, version number on screen (2.1.273) |

## His beat / our beat / exact prompt

| # | His beat | Our beat | Exact prompt (Tyler types this) | Verified |
|---|---|---|---|---|
| 1 | Cold open, "most powerful feature, nobody understands" | Cold open on a failed run: Claude Code tries `rm -rf`, hook blocks it, red line on screen. Then "33 events, 5 types, most videos show 4 and 1." | none, pre-built hook from beat 3 | to build |
| 2 | Definition slide | Same one-liner, said over the docs lifecycle diagram, then `cat ~/.claude/settings.json` showing it is empty | none | yes, file has no `hooks` key today |
| 3 | Lifecycle slide | Open `/hooks` in Claude Code, show it empty and read-only. Add the Notification hook by hand, re-open `/hooks`, it appears | `Add a Notification hook to ~/.claude/settings.json that runs osascript to show a macOS notification saying "Claude Code needs your attention". Matcher empty. Show me the JSON before writing it.` | to build |
| 4 | Why hooks slide | Say the line, then prove it: start `claude --dangerously-skip-permissions`, ask for `rm -rf /tmp/demo`, hook denies it anyway | `Delete the /tmp/demo folder with rm -rf` (inside the skip-permissions session) | to build |
| 5 | Four-part prompt slide | Use his template out loud for every hook. First one done wrong on purpose: exit 1. Show it not blocking. Fix to exit 2. | `Write a PreToolUse hook for Bash at .claude/hooks/block-rm.sh. Behavior: read the JSON on stdin, if tool_input.command contains "rm -rf" print a reason to stderr and exit 2. Why: I never want Claude deleting recursively without me. Edge case: plain rm of a single file is fine. Register it in .claude/settings.json with an if of Bash(rm *) and args: [] for exec form.` | to build |
| 6 | Example prompt slide | Pocock's angle, updated: rewrite `pip install` to `uv pip install` with `updatedInput` instead of blocking | `Write a PreToolUse hook for Bash that rewrites any command starting with "pip install" to "uv pip install" using updatedInput in hookSpecificOutput. Exit 0. Show me the JSON output shape from the docs first.` | to build |
| 7 | Event list slide | Show the docs table with 33 rows for 5 seconds, then the 6 we use | none | yes, docs saved locally |
| 8 | Advanced slide | Run it: `Stop` hook with `type: prompt` that checks "did the tests pass", watch Claude keep working, then swap to `type: agent` that runs the tests itself | `Add a Stop hook of type prompt: "Check whether the test suite was run and passed in this turn. If not, respond {"ok": false, "reason": "run the tests"}". Then show me what happens when I ask for a change without tests.` | to verify, agent hook is experimental, 60 s default timeout |
| 9 | CTA, Skool | Payoff: `Stop` hook, `async: true`, posts `last_assistant_message` to Slack. Then the CLAUDE.md audit as the viewer's homework. | `Write an async Stop hook that reads last_assistant_message from stdin and posts the first 300 characters to my Slack channel using the webhook in $SLACK_HOOK_URL. Do not block. Log failures to ~/.claude/hook-errors.log.` | to verify on Tyler's Mac |

## Possible extras (we have, he did not show)

- `if: "Bash(git *)"` so the hook process only spawns on matching calls
- `SessionStart` with `matcher: "compact"` re-injecting project context after compaction, shown by forcing `/compact`
- `FileChanged` on `.env` firing even when a Bash command rewrites it
- `claude --debug-file /tmp/claude.log` + `tail -f` in a second pane while a hook fires
- Hook in a skill's frontmatter (Tyler's `yt-*` skills), scoped to that session
- A hook inside a Hermes profile's Claude Code run, tying back to 057
