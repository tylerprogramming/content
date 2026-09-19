# Filming guide, video 058: Run OpenAI's Agents API on Your Own Mac in 3 Steps

The "do this, click that" version. Film from this without reading the script. Target 11 to 12 minutes. Hard ceiling 15.

**Version:** v2, 2026-09-19. Matches `script.md` v2. The v1 guide had you write `create_session.py`, `send.py`, and `stream.py` by hand and had the agent write `04_self_hosted.py` live. All of that exists now in `~/dev/ai/openai_agents_058/self_hosted/`. Nothing here asks you to write code. Beat 8 is a test the agent writes and runs.

Beat numbers match the beat table in `script.md`. Every beat is tell, show past, do live. The past example for the whole video is `github.com/tylerprogramming/ai/pull/22` (merged 09-17) plus the `self_hosted/` kit written after it. Have both open before you roll.

---

## Verify before you roll (the dry run)

Tyler ran the full path end to end on this Mac on 09-19 and it worked. The rows below are the morning-of re-check, not open questions. Rows 2 and 3 no longer matter (setup is pre-run, not shown live).

| # | Beat | Check | How | If it fails |
|---|---|---|---|---|
| 1 | 3 | `codex exec-server --help` works on the installed build | Run it. Note `codex --version`. | `npm install -g @openai/codex@0.156.0-alpha.7` and retry. If no build has it, block the video. |
| 2 | 5 | Does the watcher print `PENDING environment` when started before the executor? | Start `stream.py`, wait 5 seconds, then start the executor. Watch the pane. | If nothing prints until `CONNECTED`, cut the pending line from the script. The flip still lands. |
| 3 | 5 | What the executor prints on connect, and how long the flip takes | Time it from enter to `CONNECTED`. | If it is not clearly under the hosted 20 to 30 seconds, drop "watch what happens when the box is already here." |
| 4 | 6 | The write task actually edits `todo.md` | Send the "buy stamps" message. `cat` the file. | Simplify: "Append the line `- [ ] buy stamps` to todo.md." |
| 5 | 6b | The harness refuses the delete | Send "Delete the meeting note, it is old." Check the file still exists. | If it deletes, `cp` the note back from the repo and cut beat 6b. Do not keep a beat the tool did not earn. |
| 6 | 7 | `sessions.py cost <id>` shows token usage right after a turn | Run it 10 seconds after `final_answer`. | If `usage not reported yet`, wait 60 seconds and run again. Say the number on screen or say nothing. |
| 7 | 7 | The cost block at the end of `01_hosted_sandbox.py` | Run demo 1 the morning of. Keep the terminal scrollback. | If usage is None, `sessions.py cost` on that id a minute later. |
| 8 | 8 | Second session pointed at the repo connects | Ctrl-C executor and watcher. `create_session.py ~/dev/ai/openai_agents_058`. Watcher, then executor. | Same fixes as rows 2 and 3. |
| 9 | 8 | The agent writes a correct `tests/test_cost.py` and runs it | Send the beat 8 task. Read the file. It must assert 0.0332 for the token case. | Wrong number: send a second message pointing at the mistake. That is a better beat. Two failures: fall back to "Write a docstring for every function in common.py that lacks one." `git checkout . && rm -rf tests` between attempts. Do not fake the file. |
| 10 | 8 | Second message adds the container test without re-reading `common.py` | Watch the stream for `cat common.py`. | If it re-reads, fine. Just do not say "it did not read it again." |
| 11 | 9 | Coder on a local model does the `index.md` task cleanly | Run it once in Hermes on the local model. Note the model tag. | If it needs a cloud model, say so on camera and show the cost. |
| 12 | all | Time the whole thing | From `npm install` to the test passing in beat 8. | Under 10 minutes: the "in 10 Minutes" title variant is honest. If not, stay on "3 Steps". |
| 13 | 6 | Did anything reconnect or drop? | Note it. | Replace the beta sentence at the end of beat 6 with what happened, or keep it as written if nothing dropped. |

Time the dry run. Write the number in `analysis.md` under "Dry run." After the dry run, reset both folders (see setup step 1 and 2 below).

---

## Pre-recording setup

1. Notes folder: `~/agents-demo/workspace/` must have all seven files, six notes plus `AGENTS.md`. Re-copy from `~/dev/ai/openai_agents_058/self_hosted/workspace/` if in doubt. Undo any dry-run edits (`buy stamps`, `index.md`).
2. Real folder: `~/dev/ai/openai_agents_058`. The kit files can be committed or not, your call, but `tests/` must not exist. `rm -rf tests` if the dry run left it.
3. `.env` in the repo has `OPENAI_API_KEY`. Never on screen.
4. Environment key made on the dashboard Agents tab and exported as `CODEX_API_KEY` in pane A only, off camera. Never on screen. Check pane A's scrollback before every take.
5. `npm install -g @openai/codex@alpha` done. Beat 3 runs it again on camera; it is idempotent.
6. `uv sync` done in the repo.
7. Terminal: one window, three panes, all starting in `~/dev/ai/openai_agents_058/self_hosted`:
   - Pane A (left): the executor. `CODEX_API_KEY` exported here.
   - Pane B (right top): the watcher, `stream.py`.
   - Pane C (right bottom): commands. `04_self_hosted.py`, `send.py`, `sessions.py`, `git status`.
8. Editor tabs ready, in this order: `01_hosted_sandbox.py`, `02_function_tools.py`, `04_self_hosted.py`, `self_hosted/send.py`, `self_hosted/README.md`, `~/agents-demo/workspace/todo.md`, `~/agents-demo/workspace/AGENTS.md`.
9. Browser tabs, in order:
   - github.com/tylerprogramming/ai/pull/22 (Files tab)
   - openai.com/index/introducing-the-agents-api
   - developers.openai.com/api/docs/guides/agents-api/overview
   - developers.openai.com/api/docs/guides/agents-api/environments/self-hosted
   - developers.openai.com/api/docs/pricing (scrolled to Containers)
   - platform.openai.com Agents tab
10. Hermes desktop open, Bots tab, Coder profile, local model selected. Beat 9.
11. Beat 1 shot: record it first, on its own. Full flow through beat 6's write task with `todo.md` open in the editor, so the take is "line appears." Restore `todo.md` before the beat 6 take.
12. Every script is `uv run python`. Never bare `python`. It is not on the path and it will fail on camera.
13. Every message to `send.py` is quoted. zsh globs `?` and `*`.

---

## Panes and commands, in order

Beat 3, pane C:

```
npm install -g @openai/codex@alpha
codex exec-server --help
ls ~/agents-demo/workspace
```

BEFORE ROLLING (beats 4 and 5 are pre-run; you show them connected, you do not build them on camera):

Pane C, from the repo root:

```
cd ~/dev/ai/openai_agents_058
uv run python 04_self_hosted.py
```

Leave the output in scrollback (you scroll to it in beat 4). Copy the exec-server line and the session id.

Pane B (watcher goes up FIRST, the stream does not replay):

```
cd ~/dev/ai/openai_agents_058/self_hosted
uv run python stream.py <session id>
```

Pane A (environment key exported here, off camera):

```
codex exec-server --remote "<remote url>" --environment-id "<environment id>"
```

Confirm pane B shows `CONNECTED environment`. Then `cd self_hosted` in pane C and clear to an empty prompt. Roll.

Beat 6, pane C:

```
cd self_hosted
uv run python send.py <session id> "What is in this folder? One line per file."
uv run python send.py <session id> 'Add "buy stamps" to the to-do list.'
cat ~/agents-demo/workspace/todo.md
```

Beat 6b, pane C:

```
uv run python send.py <session id> "Delete the meeting note, it is old."
```

Beat 7, pane C:

```
uv run python sessions.py cost <session id>
```

Beat 8. Ctrl-C pane A and pane B. Pane C:

```
uv run python create_session.py ~/dev/ai/openai_agents_058
```

Pane B with the new id, then pane A with the new URL and environment id. Then pane C:

```
uv run python send.py <id> "Read common.py. Write tests/test_cost.py using unittest that checks the token math in print_cost with a fake session object: 1000 input tokens, 200 cached, 500 output. Run it with uv run python -m unittest and show me the output. Do not change common.py."
uv run python send.py <id> "Add a second test for the container math: 25 minutes elapsed on openai_hosted should be 2 blocks, six cents. Run both."
cd .. && git status
```

Expected numbers: tokens (800 x 10 + 200 x 1 + 500 x 50) / 1,000,000 = 0.0332. Container: 25 min is 2 blocks at $0.03 = $0.06.

After the take, cleanup in pane C:

```
uv run python sessions.py delete <first session id>
uv run python sessions.py delete <second session id>
```

Ctrl-C panes A and B.

---

## Beats

### Beat 1. Hook: a file changes, the agent is not here (0:00 - 0:35)

Record the line-landing shot as a separate take, first.

- Pane A already connected. `todo.md` open in the editor on the right, seven items.
- From a hidden pane, send the "buy stamps" message. Do not show the send.
- Let the line land. Hold two seconds.

> Watch the file on the right. That line just landed on my Mac. The agent that wrote it is not on my Mac.

- Cut to PR #22, Files tab. Point at the three scripts. It is merged. There is no "Not done" section anymore; do not scroll for one.
- Cut to the self-hosted doc, the "can be a laptop" line.
- Camera for the promise: three steps, and at the end it writes and runs a test in my real repo.

Dead air filler: "Every video I found runs this in OpenAI's hosted box. It is fine. It is just not the interesting mode."

### Beat 2. What they shipped, and the three places code can run (0:35 - 1:45)

- Launch post headline on screen.
- Overview doc, scroll to the harness feature list. Do not read it. Point at compaction and subagents.
- Four primitives as an overlay: Agent, Environment, Session, Events.
- Show past: editor on `01_hosted_sandbox.py`, cursor on `"type": "openai_hosted"`. Then the README "What to expect" block for demo 1, point at `CONNECTED environment` and `final_answer` 129.
- Editor: `02_function_tools.py`, cursor on `"type": "none"`. New in v2. Say it is no computer at all.
- Three-row overlay: `none` / `openai_hosted` / `self_hosted`. Say partners are the third row, not a fourth. Three names is enough, do not list all nine.

> The model is one piece. The loop is the rest. On September tenth they put the loop behind an API.

Cut this beat first if over time. Keep the `01` shot and the three-row overlay even if you cut the rest; beat 4 needs the viewer to have seen `openai_hosted` once.

### Beat 3. Step 0: keys and install (1:45 - 3:00)

- API keys page. Then `self_hosted/README.md` scrolled to "Two keys, and why." Say two programs talk to OpenAI, so two keys.
- Agents tab. Create the environment key, everything else None. Blur. Or make it off camera and show the list view.

> Any code the agent runs can read this one. So the point is it cannot do anything except connect an environment.

- Pane C: the beat 3 commands. Point at `exec-server --help` existing.
- `ls ~/agents-demo/workspace`. Seven files. Say "one more file I will come back to."

### Beat 4. Step 1: create the session (3:00 - 4:30)

- Editor split: `01` left, `04` right. Cursor on `openai_hosted` then on the `self_hosted` line.
- Point at the absence of `input=` in `04`. Say why: nothing to run it on yet.

> One line changes. That line is the whole difference between this and every other video on this API.

- Pane C: `uv run python 04_self_hosted.py`. Let the output sit two seconds.
- Point at the three values, then the filled-in exec-server command. Say you do not look these up, they come back from the call.

### Beat 5. Step 2: the executor (4:30 - 5:45)

- Pane B first. `stream.py`. Say it goes first because the stream does not replay.
- Show past: README line "READY environment then CONNECTED environment, roughly 20 to 30 seconds." Say that was the hosted box building itself.
- Pane A: paste the command from beat 4. Enter.
- Cut to pane B on `CONNECTED environment`. This is the shot. Hold it.

> Pending to connected. That is my Mac telling OpenAI, I am the room this agent works in.

- Network sentence over a still of pane A: outbound only, two hosts, no inbound port, reconnects on its own.
- Camera: "Their loop, my disk."

Dead air filler while it connects: "Two hosts. api.openai.com to register, and a websocket for the commands. That is it."

### Beat 6. Step 3: send work (5:45 - 7:15)

- Editor: `send.py`, the `events.create` block, ten seconds, do not walk every line.
- Show past: README demo 1 output, the `$ /bin/bash -lc` line and `python3 /workspace/outputs/primes.py`. Say same shape, different disk.
- Pane C: the read message. Pane B: `$` lines, then `final_answer`.

> That ls is my folder. When it reads a file, that is my file.

- Pane C: the write message. Pane B: the edit. Then `cat todo.md`. Say it does not vanish in an hour like `primes.py`.
- Camera: the beta note, replaced with whatever happened on the dry run.

### Beat 6b. The folder has rules (7:15 - 7:45)

- Editor: `workspace/AGENTS.md`. Read two of the rules out loud. Say Codex reads it, Hermes reads it, Claude Code has the same idea.
- Pane C: the delete message. Pane B: the refusal.
- One sentence: same file, three tools. Move.

Cut this beat if the refusal is not clean on the dry run.

### Beat 7. Cost and limits (7:45 - 8:45)

- Terminal scrollback from this morning's demo 1 run, the `--- cost estimate ---` block. Or a screenshot from the dry run if you did not keep the terminal.
- Pane C: `sessions.py cost <id>`. Read what is there. Point at `container: none (self_hosted)`.
- Say: no API fee, tokens at model rate, self-hosted removes the container row, tokens are the big line. `MODEL` is one line in `common.py`.
- Pricing page, Containers row, as the "what you are skipping" shot.
- Overview doc: US-only data residency, no zero data retention even self-hosted.

> The files are on your disk. The conversation is not.

- Camera: the demo folder was fine, the public demo repo is fine, the content repo would not be.

### Beat 8. The build: the API works in my real repo (8:45 - 10:30)

This is the seam and the payoff. Say the seam on camera:

> Right, I am switching folders. Everything so far was a clean folder I made for this video. This is my actual repo, the one that PR merged into.

- Pane C: `cd .. && ls`. Four demos, `common.py`, `self_hosted/`, `README.md`.
- `create_session.py` with the repo path. Three values print.
- Ctrl-C A and B. Restart B with the new id, A with the new values. Flip once, fast. Do not narrate it again.
- Pane C: the test task (exact text above). Pane B: `cat common.py`, write to `tests/test_cost.py`, `$ uv run python -m unittest`, output.

> Watch it read first, then write, then run. That run is on this Mac.

- Editor: open `tests/test_cost.py`. Scroll once, slowly. Let it be the shot.
- Pane C: the second message. Pane B: update, run, two pass.

> Same session, same conversation. It remembers what the file is.

- Pane C: `git status`. One new folder.

> A harness in OpenAI's cloud read my repo, wrote a test, and ran it, on my disk, in my venv.

- Do not commit on camera. Commit by hand after the take and say in the message who wrote it.

### Beat 9. Same folder, local, zero (10:30 - 11:30)

- Hermes desktop, Bots tab, Coder selected. Show the local model tag.
- Show past: PR #22 author line. Then Finder on `self_hosted/`. Say Coder wrote the PR and the kit you just watched run.
- Same kind of task, notes folder:
```
Read every markdown file in ~/agents-demo/workspace and write index.md with one line per file: the filename and a one-sentence summary.
```
- Show the model tag it used.
- Overlay the two-column "reach for which" table from the script.

> This one for things I would ship. That one for my own machine. Today they worked on the same folder.

Do not trash the API. The fair read is: managed harness for things you ship, local agent for you.

### Beat 10. CTA (11:30 - 12:00)

- Camera. Four demos, the kit, the notes folder, `EXAMPLES.md`, all in the repo and the community. Ask what they pointed it at. Point at 057 as the other half.
- End card with 057 on the left.

---

## Timing cheat sheet

| Beat | Section | Target | Cut first? |
|---|---|---|---|
| 1 | Hook | 0:35 | never |
| 2 | What they shipped | 1:10 | yes, first, but keep the `01` shot and the three-row overlay |
| 3 | Step 0 keys and install | 1:15 | trim the key explanation to the README scroll |
| 4 | Step 1 create session | 1:30 | no |
| 5 | Step 2 executor | 1:15 | trim the network sentence |
| 6 | Step 3 send work | 1:30 | second, drop the read task and go straight to the write |
| 6b | The folder has rules | 0:30 | third, or if the refusal is not clean |
| 7 | Cost and limits | 1:00 | trim the pricing page |
| 8 | The build | 1:45 | no, it is the payoff |
| 9 | Local comparison | 1:00 | trim the table to two rows |
| 10 | CTA | 0:30 | no |
| | **Total** | **12:00** | |

---

## On-camera tips

- Three panes, always visible. The viewer should see the executor, the stream, and the command at once. That is the proof.
- Every beat points at PR #22 or the kit once. If you find yourself demoing on empty state, stop and pull one of them up.
- Never say "cloud agent" without saying "on my Mac" in the same breath for the first half. The title promise is the location.
- When a file changes, stop talking for two seconds. Let it be the shot. Beat 1, beat 6, beat 8.
- Say `uv run python` out loud once in beat 4 and never again. Viewers will see it in every command.
- When a stream pane is scrolling, stop talking. Let the `$` lines be the audio.
- Beat 5's flip is the thumbnail moment. Frame pane B large for it.
- Say the seam in beat 8 out loud. Cutting from the notes folder to the real repo without saying so reads as a continuity error. Saying it reads as honest.
- If anything errors on camera, read the error out loud and fix it. A real error beats a clean retake for this audience.
- Do not read the docs aloud. Point, paraphrase, move.
- The cost section is one terminal block, one table, and three sentences. Only say numbers that are on screen.
- On the comparison, be the engineer who runs both. "I run both" is the line that keeps this from being a takedown.
- One "right?" per section at most.
- No em dashes in overlays. No "insane", no "game-changer".
- The environment key is the one thing that must never be visible. Check pane A's scrollback before every take.
