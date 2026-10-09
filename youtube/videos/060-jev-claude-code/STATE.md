# STATE, 060 (updated 2026-09-28)

## Direction

v2: "every Jev demo, rerun on my own data." Pre-done: `show.py` replays saved real results; 2 live beats with fallbacks. Judge swap kept as beat 7 (Tyler: option b). Inbox redacted on screen (option b). v1 script kept at `script-v1.md`.

## Verified on this Mac, 2026-09-28

| Thing | Result | Proof |
|---|---|---|
| TypeSafe key | works, `jev-1.13.0` | `~/.hermes/.env` |
| OpenRouter key | works, `typesafe/jev-1.13-20260917` | `~/.hermes/.env` |
| Gmail read | re-authed, 1,700 emails pulled (Aug 7 to Sep 28) | `jev-lab/emails.jsonl` (gitignored) |
| Inbox classifier | 1,698/1,700 answered, 8,490 answers, $0.086 list | `inbox_results.openrouter.*` |
| Race vs Haiku 4.5 | 6.3 s vs 26.9 s, $0.0039 vs $0.078, 74/100 agree | `creator_examples.json` |
| Router, 200 real prompts | 133/22/45, 44 low-conf; context changes 32, not the 3 misroutes | `router_results.json`, `router_ctx_results.json` |
| Skill picker, 115 Hermes skills | Jev 8/8, Haiku 7/8 (wrote a paragraph) | `creator_examples.json` |
| Judge swap vs gpt-5.4-mini | LLM flips PASS/NI on correct code (2/3); Jev conf 0.0 on the buggy one | `judge_swap.json` |
| PreToolUse hook in Claude Code | `claude -p` in `gate-demo/`: ls allowed, 2 deletes "ask" at 0.84/0.82, Claude stopped | `gate-demo/.claude/hooks/jev_gate.log` |
| Creator examples | iphone, fraud, lead, logs, diff, pii, short, clips | `creator_examples.json` |
| Outage | 09:36 NO-GO (13.7 s median, 503s), 10:25 GO | `health_log.jsonl` |

## Not verified / open

- Hook in an **interactive** Claude Code session (only `-p` tested). "ask" should show the permission prompt; confirm in the dry run.
- Router's dollar saving: per-model costs in `router_demo.py` are placeholders. Do not say a percentage.
- `fraud`, `lead`, `logs`, `diff` examples ran but are not in the v2 script (spare B-roll).
- Title: **recommended "Jev in Claude Code: 5 Real Tests, 1 BREAKS"** (PASS). Shortlist and lint in `titles.md`.
- `titles.md`, `hooks.md`, `description.md`, `filming-guide.md` rewritten for v2 on 2026-09-28; v1 copies kept as `*-v1.md`. `yt-thumbnail.md` and `tags.txt` are still v1.

## Costs so far

OpenRouter key: $0.0886 by ~09:05 (usage endpoint), plus the race, skills, judge and router reruns after. TypeSafe direct: not checked.
