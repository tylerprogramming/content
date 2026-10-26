# Filming guide, video 060

"Do this, click that." Someone could film from this without reading the script. Narration in blockquotes is suggested, not required. Target 11:00, hard ceiling 13:00.

## The one thing to know before anything else

There is no `TYPESAFE_API_KEY` on this Mac (checked 2026-09-23: not in the shell env, not in `~/.hermes/.env`, not in `~/dev/ai/.env`). Every beat that shows a Jev response depends on getting one. Two ways in, pick one the day before:

| Path | How | Cost | Verified |
|---|---|---|---|
| A. TypeSafe console | console.typesafe.ai, create a key at Settings > Keys. Three sources on 09-23 (learnjev.com, X threads) say the waitlist has ended; the research file (09-23) still says early access. Try it first | $0.042 per Mtok input, output free | no |
| B. OpenRouter | An `OPENROUTER_API_KEY` is already in `~/.hermes/.env`. Point the SDK at it: `TypeSafeClient(api_key=OPENROUTER_KEY, base_url="https://openrouter.ai/api")`, model `typesafe/jev-1.13`. No waitlist, billed to OpenRouter. Per openrouter.ai/docs/guides/community/jev | same price, billed via OpenRouter | no |

If neither works the morning of the shoot: film Hook 3, use the fallbacks in the dry run table, and say on camera that the after numbers are the documented ones.

## Pre-recording setup (the day before)

1. Pull the repo and confirm the before runs.
   ```bash
   cd ~/dev/ai && git pull
   cd mini_projects/agentic_prompts
   uv run evaluate_optimizer.py
   ```
   It needs `OPENAI_API_KEY` in `~/dev/ai/.env` (the helper calls `load_dotenv()`). Note how many loop iterations it takes and the wall time. Write both in `record-prep.md`.

2. Install the SDK and confirm the import names.
   ```bash
   cd ~/dev/ai && uv add typesafe-sdk
   uv run python -c "from typesafe_sdk import Choice, Noul, Score, TypeSafeClient; print('ok')"
   ```
   If the import fails, the class names in `script.md` are wrong; fix them from `docs.typesafe.ai/sdk` and update the script.

3. Write `mini_projects/agentic_prompts/jev_judge.py` from the code block in `script.md` section 4. Copy `generate()` and the task from `evaluate_optimizer.py` so it runs standalone. Run it once:
   ```bash
   time uv run jev_judge.py
   ```
   Screenshot the output. That screenshot is the cold open if the live run misbehaves.

4. Write `hooks/jev_gate.py` from section 6 and add the hook block to `~/dev/ai/.claude/settings.json`. Test it outside Claude Code first:
   ```bash
   echo '{"tool_input":{"command":"rm -rf mini_projects/__pycache__"},"cwd":"/Users/tylerreed/dev/ai"}' | uv run hooks/jev_gate.py; echo "exit $?"
   echo '{"tool_input":{"command":"ls mini_projects"},"cwd":"/Users/tylerreed/dev/ai"}' | uv run hooks/jev_gate.py; echo "exit $?"
   ```
   Expect exit 2 then exit 0. Write the two probabilities in `record-prep.md`. If the `rm` comes back under 0.85, do not raise the threshold to make the demo work; keep the number and say it on camera in section 7.

5. Open Claude Code in `~/dev/ai` and run the prompt from section 6 once. Confirm the block message appears. If hook stdin fields differ from `tool_input.command`, fix `jev_gate.py` from code.claude.com/docs/en/hooks.

6. Optional: install the plugin so section 8 can be live.
   ```bash
   claude plugin marketplace add typesafe-ai/skills
   claude plugin install typesafe@typesafe-ai
   ```

7. Tabs open, in this order: `typesafe.ai/blog/introducing-system-one-models-and-jev`, `docs.typesafe.ai/primitives`, `docs.typesafe.ai/models`, `docs.typesafe.ai/model-jaggedness/jev-1.13`, `docs.typesafe.ai/introduction/coding-agents`, the TechCrunch article, the Latent Space video.

8. Two terminal panes side by side, both in `~/dev/ai/mini_projects/agentic_prompts`. Font big enough that a `real` line reads at 1080p.

9. Export the key in both panes BEFORE rolling. Never type it on camera.

## Dry run table (13 rows)

Every beat that assumes a Jev response has a fallback. Fill the "Real value" column the day before.

| # | Time | Beat | Needs a Jev key | Real value (fill in) | Fallback if no key |
|---|---|---|---|---|---|
| 1 | 0:00 | Cold open, two `real` times side by side | yes | LLM: ___ s, Jev: ___ ms | Film Hook 3 (grep count) instead. Hook 1 and 2 are dead without a run |
| 2 | 0:20 | "the price on that one call is [N]" | yes | ___ | Say the per-million price from the docs page instead of a per-call figure |
| 3 | 0:25 | Jev `usage` block on screen | yes | in / out tokens: ___ | Show the docs quickstart response (392 in / 65 out, per research section 5) and label it "from the docs" |
| 4 | 1:15 | Docs response with three answers | no | n/a | Docs page, always available |
| 5 | 2:30 | `time uv run evaluate_optimizer.py` | no (needs OpenAI key) | ___ s, ___ iterations | None needed. If OpenAI fails, show the pre-recorded run from setup step 1 |
| 6 | 3:00 | `time uv run jev_judge.py`, the payoff | yes | ___ ms, score ___, conf ___ | Show the screenshot from setup step 3 if the live run errors. If no key at all: show the docs Score example (0.57 / 0.43, confidence 0.35) and say "this is their example, not my run." Cut the side-by-side hold to 1 s |
| 7 | 3:20 | Per-call cost math from the usage block | yes | ___ tokens x $0.042/M = ___ | Skip the math. Say "4.2 cents per million input, their price" |
| 8 | 4:40 | Threshold branches added live | no | n/a | Code on screen works with or without a run |
| 9 | 5:30 | "I ran this on [N] examples" | yes | ___ | Say "I have not calibrated it yet, and their docs say you should." Honest, and it sets up section 7 |
| 10 | 6:40 | Bash gate: `ls` passes, `rm` blocked | yes | p(ls) ___, p(rm) ___, ___ ms | Show `jev_gate.py` and the hook JSON, then say "this is the shape; I could not run it without a key." Cut the Claude Code prompt |
| 11 | 7:20 | "the gate call took [N] milliseconds" | yes | ___ | Drop the line |
| 12 | 8:00 | 0.72 + 0.47 = 1.19 | no | n/a | Docs page, always available |
| 13 | 9:15 | "every after number I could not run myself" vs "one run on my machine" | depends | pick one | Say the true one. Both versions are written in the script |

Rows 1, 6 and 10 are the three beats that carry the video. If all three fall back, the video is still filmable but the title should drop "ONE Jev Call" and use title 3 from `titles.md` instead, since there is no call to show.

## Numbered steps

### Step 1: Cold open (0:00 to 0:45)

1. Both panes already run, both `real` lines visible. Start recording on the screen, no face.
2. Read the first two sentences from `hooks.md` Hook 1. Say the real numbers.
3. Zoom the left pane to lines 105 to 113 of `evaluate_optimizer.py`.
4. Cut to camera at 0:08.
5. Cut to the Jev `usage` block at 0:25.

> "So this is the same decision, made twice."

Dead-air fill if a pane needs re-arranging: "So both of these were run about a minute before I hit record. I will run them again live in a second."

### Step 2: What Jev is (0:45 to 1:45)

1. Blog post tab, 3 seconds. Say the founder sentence once.
2. Primitives tab. Read the three types.
3. Models tab. Point at the price row.

> "Those are TypeSafe's numbers. I will tell you which ones I could check."

### Step 3: The before (1:45 to 2:45)

1. VS Code, `evaluate_optimizer.py`, scroll to line 105. Highlight the `Literal`.
2. Open `helpers/json_llm.py`, point at the `except ValidationError`.
3. Left pane:
   ```bash
   time uv run evaluate_optimizer.py
   ```
4. While it runs: "So the generator writes the stack class, the judge reads it, and if it is not PASS we go around again."
5. When it finishes, read the `real` line. Scroll to line 121, `while True:`, hold 2 seconds.

### Step 4: The after (2:45 to 4:00)

1. Split view: `evaluate_optimizer.py` left, `jev_judge.py` right.
2. Read the three `criteria` lines slowly. This is the teaching moment.
3. Right pane:
   ```bash
   time uv run jev_judge.py
   ```
4. Read score, confidence, usage. Do the per-call math out loud from the usage block.
5. Both `real` lines big, hold 3 seconds.

> "Same decision. That is the whole video in one frame."

### Step 5: Three question types (4:00 to 6:00)

1. Camera for the "decision per token" line.
2. Docs quickstart response, three answers.
3. Back to `jev_judge.py`, type the threshold block from the script.
4. Camera for the calibration line. Say the true count.

### Step 6: The Bash gate (6:00 to 8:00)

1. Claude Code open in `~/dev/ai`.
2. Show `.claude/settings.json` hooks block.
3. Show `hooks/jev_gate.py`, scroll slowly.
4. In Claude Code, type:
   ```
   list the files in mini_projects and then delete the __pycache__ folders
   ```
5. Let it run. The `ls` should pass, the `rm` should block. If the `rm` passes, say the probability it returned and move on. Do not re-roll.
6. TechCrunch tab, Vercel paragraph. Say "5 to 18 times, one engineer."

Dead-air fill while Claude thinks: "So the hook is reading the command off stdin, sending it as state with one Noul, and exiting 2 if the probability is over 0.85. That is the whole thing."

### Step 7: Honest limits (8:00 to 9:30)

1. Camera, one line.
2. Jaggedness tab. Scroll to the refund example. Read 0.72, 0.47, 1.19.
3. Scroll the nine-item list. Say "nine" only after the list is on screen.
4. Two-column slide: TypeSafe measured / someone else measured.
5. Latent Space thumbnail, 3 seconds, the "not yet" line.
6. Camera. Say whichever version of row 13 is true.

### Step 8: Where it fits (9:30 to 10:30)

1. Code / Jev / LLM slide.
2. Coding-agents docs page, the quoted sentence.
3. Terminal: the two plugin commands. If the plugin is not installed, show the docs page and skip.

### Step 9: Recap + CTA (10:30 to 11:00)

1. Two `real` lines one more time.
2. Camera. The comment question.
3. End card.

## Timing cheat sheet

| Section | Start | Length | Cut first if over |
|---|---|---|---|
| Cold open | 0:00 | 0:45 | never |
| What Jev is | 0:45 | 1:00 | founder sentence |
| The before | 1:45 | 1:00 | `json_llm.py` detour |
| The after | 2:45 | 1:15 | never |
| Three types | 4:00 | 2:00 | the docs quickstart walk (keep the threshold code) |
| Bash gate | 6:00 | 2:00 | TechCrunch beat |
| Honest limits | 8:00 | 1:30 | never |
| Where it fits | 9:30 | 1:00 | plugin commands |
| Recap + CTA | 10:30 | 0:30 | never |

## On-camera tips

- The two `real` lines are the thumbnail and the payoff. Make them huge, same font, same position, left and right.
- Say "TypeSafe's number" every time you quote a vendor figure. It sounds repetitive in the script and reads as careful on video.
- Never round in Jev's favor. If it is 412 ms, say 412, not "under half a second."
- If the Bash gate lets the `rm` through, that is a better section 7 than the scripted one. Keep rolling.
- Key off camera, both panes, before recording. Check the scrollback.
