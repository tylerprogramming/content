# Filming guide, video 060 (v2)

v1 in `filming-guide-v1.md`. One-page version: `FILMING-CARD.md`. This file is the step list with what you should see at each beat.

## The one thing to know

Everything is pre-done. 9 of 11 beats replay saved results with `uv run show.py <beat>`: no API call, cannot fail, same numbers every take. Two beats run live (3 and 9), each with a replay fallback. If the API is down on filming day you lose nothing, and that becomes part of beat 10.

## Setup (day before, 15 min)

```bash
cd ~/dev/jev-lab
export TYPESAFE_API_KEY="$(grep -E '^(export )?TYPESAFE_API_KEY=' ~/.hermes/.env | head -1 | cut -d= -f2-)"
export OPENROUTER_API_KEY="$(grep -E '^OPENROUTER_API_KEY=' ~/.hermes/.env | cut -d= -f2-)"
for b in why inbox router iphone short judge gate race skills clips fanout jagged health; do uv run show.py $b; done
```

All 13 should print without errors (verified 2026-09-28). Then the interactive hook check, which has **not** been done yet (only headless `claude -p` was tested):

```bash
cd ~/dev/jev-lab/gate-demo && claude
# type: delete the __pycache__ folders in mini_projects
```

Expect a permission prompt labelled `[settings]` with "Jev gate: p(destructive)=0.8x ... Not sure, so you decide." Answer no. Then reset:

```bash
git checkout -- . && git clean -fd -e .claude && rm -f .claude/hooks/jev_gate.log
```

If there is no prompt and it just runs, stop and tell me.

## Filming day (5 min)

```bash
cd ~/dev/jev-lab && uv run health.py
```

GO on both: film beats 3 and 9 live. NO-GO: use the fallbacks, and add one line to beat 10 reading today's `health.py` output.

## Dry run table

| # | Beat | Command | You should see | Fallback |
|---|---|---|---|---|
| 0 | Cold open | `show.py inbox` | 8,490 answers, $0.086, redacted leads list | none needed |
| 1 | Why | `show.py why` | Haiku 1738 ms with a json code fence; Jev 241 ms, 0.99 | none |
| 2 | Fan-out | `show.py fanout` | 184 ms vs 191 ms | none |
| 3 | Inbox LIVE | `uv run inbox_demo.py --limit 50` | about 5 to 8 s, 250 answers | `show.py inbox` |
| 4 | Race | `show.py race` | 6.32 s vs 26.9 s, 74/100 | none |
| 5 | Router | `show.py router` | 133/22/45; the three misroutes | none |
| 6 | Skills | `show.py skills` | Jev 8/8 in 1.87 s, Haiku 7/8 in 12.63 s plus its paragraph | cut the beat |
| 7 | Judge | VS Code on `evaluate_optimizer.py`, then `show.py judge` | LLM PASS 2 / NI 3 on correct code; Jev confidence 0.0 on the buggy one | none |
| 8 | Design bites | `show.py iphone`, then `show.py short` | black phone -> blue 0.82; "stripe not working" 0.43 | none |
| 9 | Gate LIVE | Claude Code in `gate-demo`, prompt below | `ls` allowed; deletes land in "ask" at about 0.82 to 0.84 | `show.py gate` (includes the saved Claude Code run) |
| 10 | Falls over | `show.py jagged`, `show.py health`, status.typesafe.ai | 1.15; 0.39; 09:36 NO-GO, 10:25 GO | none |
| 11 | Fit + CTA | slide + docs page | none | none |

Beat 9 prompt:

```
list the files in mini_projects, then delete the __pycache__ folders, then delete the mini_projects folder entirely
```

## Order to film in

Screens first, face last:
1. All `show.py` beats in one pass (1, 2, 4, 5, 6, 7, 8, 10), big font, one take each.
2. Beat 3 live, then beat 9 live (reset `gate-demo` between takes).
3. Cold open last, once you know which live takes you are keeping.
4. Face lines: the 0:08 intro, the "why" lines in beat 1, the router, judge and gate closers, beat 11.

## On-camera rules

- Say the number the screen shows. Never round in Jev's favor.
- Every latency gets "from my desk".
- Name the creator before redoing their demo, with their clip on screen for 3 s.
- Credit, don't dunk: "LangChain said certainly. Here's what I got."
- Keys are exported off camera. `show.py` never prints a key.
