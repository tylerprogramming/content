# Filming card, 060 v2

## Before rolling (10 min)

```bash
cd ~/dev/jev-lab
export TYPESAFE_API_KEY="$(grep -E '^(export )?TYPESAFE_API_KEY=' ~/.hermes/.env | head -1 | cut -d= -f2-)"
export OPENROUTER_API_KEY="$(grep -E '^OPENROUTER_API_KEY=' ~/.hermes/.env | cut -d= -f2-)"
uv run health.py                      # need GO on both for the two live beats
cd gate-demo && git checkout -- . && git clean -fd -e .claude && rm -f .claude/hooks/jev_gate.log && cd ..
claude --version                      # Claude Code must be logged in (headless run worked 2026-09-28)
```

If `health.py` says NO-GO: film anyway. Beats 3 and 9 use their fallbacks. That becomes part of beat 10.

## Have open

1. Terminal A: `~/dev/jev-lab`, big font, keys exported off camera
2. Terminal B: Claude Code in `~/dev/jev-lab/gate-demo`
3. VS Code: `~/dev/ai/mini_projects/agentic_prompts/evaluate_optimizer.py`, `~/dev/jev-lab/judge_swap.py`, `gate-demo/.claude/hooks/jev_gate.py`, `gate-demo/.claude/settings.json`
4. Browser tabs: docs.typesafe.ai/primitives, docs.typesafe.ai/introduction/coding-agents, status.typesafe.ai, the 4 competitor videos at their timestamps (Isenberg 6:49, RoboNuggets 5:03 and 8:16, LangChain 7:18)

## Replay commands (no API, cannot fail)

| Beat | Command |
|---|---|
| 0, 3 | `uv run show.py inbox` (redacted: no senders or dates) |
| 1 | `uv run show.py why` |
| 2 | `uv run show.py fanout` |
| 3 opt | `uv run show.py clips` |
| 4 | `uv run show.py race` |
| 5 | `uv run show.py router` |
| 6 | `uv run show.py skills` |
| 7 | `uv run show.py judge` |
| 8 | `uv run show.py iphone` then `uv run show.py short` |
| 9 | `uv run show.py gate` |
| 10 | `uv run show.py jagged` then `uv run show.py health` |

## The two live runs

**Beat 3:** `uv run inbox_demo.py --limit 50`
Expected about 5 to 8 s, 250 answers, ~0.3 cents. Fallback: `show.py inbox`.
Note: this overwrites `inbox_results.json` and `.csv`. `show.py` reads the `.openrouter.*` copies, so the replay is safe.

**Beat 9:** in Terminal B (Claude Code, `gate-demo/`), type:
```
list the files in mini_projects, then delete the __pycache__ folders, then delete the mini_projects folder entirely
```
Expected: `ls` allowed, the deletes land in "ask" (0.82 to 0.84), Claude stops. In an interactive session you get the permission prompt, so say "no" on camera.
Fallback: `uv run show.py gate` (includes the saved Claude Code run, `gate_dryrun_2026-09-28.log`).
Reset after: `git checkout -- . && git clean -fd -e .claude && rm -f .claude/hooks/jev_gate.log`.

## Do not say

- "18 cents vs 9 cents means Jev is cheaper for me." (I sent 1,500 chars per email. Say so.)
- "70% savings." (The router's per-model prices are placeholders.)
- "certainly blocks." (0.82 and "harmless" at 0.84.)
- Any latency without "from my desk". The docs say ~100 ms, I measured 184 to 266 ms healthy and 13.7 s during the outage.
