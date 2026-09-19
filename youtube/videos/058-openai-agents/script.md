# Script, video 058: Run OpenAI's Agents API on Your Own Mac in 3 Steps

**Target runtime:** 10 to 11 minutes. Hard ceiling 15. Setup (old beats 4 and 5) is pre-run and shown connected, which bought back a minute. If a section runs long, cut beat 2 first.
**Version:** v3, 2026-09-19 (v2 same day). Tyler ran the full self-hosted path end to end on this Mac; all VERIFY markers resolved. Three terminals are up and connected before rolling. Supersedes v1 (09-15), which had the agent write `04_self_hosted.py` live. That file exists now. v2 shows it working instead.

Every fact here traces to `research/2026-09-15-agents-api.md`, the OpenAI docs in `analysis.md`, or a run on this Mac on 09-19. Tyler ran the whole path on this Mac before filming; nothing here is unverified.

Structure follows the Tina Huang breakdown (`research/youtube/creator-breakdowns/2026-09-12-tina-huang-hermes-fundamentals.md`): every beat is tell it, show a real past example that already exists on this Mac, then do a new one live. Never demo on empty state. Say the seam. End on the build, not the recap.

Voice: Tyler's. "So" openers, short sentences, hedge instead of hype. No em dashes.

**Verified on this Mac 2026-09-19 before writing.** Read off the machine, not remembered:

| Claim in the script | How it was checked |
|---|---|
| PR #22 merged 2026-09-17, three demos on main | `gh pr view 22` |
| `04_self_hosted.py` and `self_hosted/` kit exist, uncommitted | `git status` in `~/dev/ai/openai_agents_058` |
| `01_hosted_sandbox.py` ran clean today | Tyler ran it |
| `04` ran, executor connected, `send.py` got a `final_answer` on the notes folder | Tyler ran it, session `sess_025e1b...` |
| `session.environment.id` and `.remote_url` are the attribute names | SDK source, `openai/types/beta/environment.py` |
| `events.stream(session_id)` does not replay history | Watcher started after executor stayed silent until the first message |
| Plain `python` is not on the path | `python not found` on the first try |
| zsh globs `?` in an unquoted message | `no matches found: folder?` |
| `codex` was not installed globally before today; alpha is `0.156.0-alpha.7` | `which codex`, `npm view` |
| gpt-6-astra standard rate: $10 in, $1 cached, $50 out per 1M | pricing page 09-19 |
| 1 GB container: $0.03 per 20 min | pricing page, Containers row |

**All previously open checks resolved by Tyler's end-to-end run on this Mac, 2026-09-19.**

## The past example, used all the way through

`github.com/tylerprogramming/ai/pull/22`, "058: OpenAI Agents API demos", merged 09-17. Opened by Coder (the Hermes bot) from a kanban card. Three scripts, all run against the live API: `01_hosted_sandbox.py` (hosted sandbox, primes.py, sum 129), `02_function_tools.py` (no sandbox at all, `lookup_member`, two turns on one session), `03_subagents.py` (three subagents). Then, after the merge, `04_self_hosted.py` and the `self_hosted/` kit, written on this Mac and run once against a notes folder. That is the seam: the PR is the past, the kit is today, and the video runs the kit.

## Beat table (the map for filming)

| # | Beat | Time | What's on screen | Tell / Show past / Do live |
|---|---|---|---|---|
| 1 | Hook: a file changes, the agent is not here | 0:00 - 0:35 | Split: `codex exec-server` connected on the left, `todo.md` open on the right. A line appears. Then PR #22. | Show: the edit landing (recorded first). Show past: PR #22, three demos, all hosted. Tell: docs say "can be a laptop," three steps. |
| 2 | What they shipped, and the three places code can run | 0:35 - 1:45 | Launch post. Four-primitive list. `01` in the editor on the `openai_hosted` line. `02` on the `none` line. | Tell: harness behind an API. Show past: demo 1's line and its transcript, demo 2's `none`. Tell: three types, partners are the third one. Cut first if long. |
| 3 | Step 0: two keys, one install | 1:45 - 3:00 | API keys page. Agents tab, environment key. Terminal `npm install`. `self_hosted/README.md` two-keys section. | Tell: app key vs environment key, why. Show past: the README table Coder wrote. Do live: make the key, install codex alpha. |
| 4 | Steps 1 and 2: already running, walk it back | 3:00 - 4:30 | Three panes up and connected before rolling. Editor split `01` / `04` for the one changed line. Pane C scrollback: the three ids. Pane A: executor. Pane B: `CONNECTED`. | Tell: one line changed, the three ids, one command, outbound only, watcher goes first. Show: it is connected. No live setup; the setup is the boring minute. |
| 6 | Step 3: send work, on the notes folder | 4:30 - 6:00 | `send.py`. Stream: `ls`, `cat`, `final_answer`. Second message edits `todo.md`. `cat` it. | Tell: sending work, session stays alive. Show past: demo 1's `primes.py` in `/workspace/outputs`, gone in an hour. Do live: a read, then a write that stays. |
| 6b | The folder has rules | 6:00 - 6:30 | `workspace/AGENTS.md`. Ask it to delete the meeting note. It refuses. | Tell: one AGENTS.md in every folder; Claude Code, Hermes, and now this all read it. Do live: the refusal. |
| 7 | What it costs, and where it stops | 6:30 - 7:30 | `sessions.py cost`. Pricing page Containers row. Overview limits. | Tell: no API fee, tokens, containers. Show past: demo 1's cost block from this morning. Do live: `sessions.py cost` on the self-hosted session, read the number. |
| 8 | **The build: the API works in my real repo** | 7:30 - 9:15 | THE SEAM. `cd ~/dev/ai/openai_agents_058`. New session, new executor. Agent reads `common.py`, writes a test, runs it here. Second message on the same session. `git status`. | Tell: same three steps, real folder. Show past: the four demos and the kit as they sit. Do live: the agent writes `tests/test_cost.py` and runs it on this Mac. |
| 9 | The same folder, the local agent, for zero | 9:15 - 10:15 | Hermes desktop, Coder, local model tag. Same folder. Two-column overlay. | Tell: I already run an agent here. Show past: PR #22 and the kit, both written by Coder. Do live: Coder does the notes task on a local model. Then the "reach for which" table. |
| 10 | CTA | 10:15 - 10:45 | Camera. End card, 057 left. | Tell: everything is in the repo. Ask what they pointed it at. 057 is the other half. |

---

## Beat 1 [0:00 - 0:35] Hook: a file changes, the agent is not here

[SHOW: no camera. Split screen. Left: terminal, `codex exec-server` connected. Right: `~/agents-demo/workspace/todo.md` open in the editor, seven items.]

Watch the file on the right.

[SHOW: a new line appears at the bottom: `- [ ] buy stamps`]

That line just landed on my Mac. The agent that wrote it is not on my Mac. It is running in OpenAI's cloud, on the same harness that runs Codex. The only thing on my machine is one command, and it is the one on the left.

[SHOW: browser, github.com/tylerprogramming/ai/pull/22, merged, the file list: `01_hosted_sandbox.py`, `02_function_tools.py`, `03_subagents.py`]

This is a PR one of my agents opened on my repo this week. Three demos against this API, all in OpenAI's hosted sandbox, all run, merged. And every video I found on this API does the same thing. Runs it in their box.

[SHOW: OpenAI docs, self-hosted page, the line "The environment can be a laptop, a container, or a remote sandbox"]

But the docs say the environment can be a laptop. Nobody has done that on camera. So that is this video. Three steps, and at the end I point it at my real repo and have it write and run a test on this machine.

[SHOW: camera]

And right before that I put the cost of this next to the agent I already run on this same Mac for free, because I think that comparison is the whole decision.

---

## Beat 2 [0:35 - 1:45] What they shipped, and the three places code can run

[SHOW: openai.com launch post, the headline "Build and run cloud agents with the Codex harness, fully managed by OpenAI"]

So quick version, because three other videos already explain this part well.

If you use Claude Code or Codex, you already know what a harness is. It is the loop. It calls the model, runs the tool, reads the result, calls the model again. It compacts the context when it gets long. It retries when something breaks. The model is one piece of that. The loop is the rest.

[SHOW: the overview doc, the list: context compaction, tool search, subagents, steering, resume]

On September tenth OpenAI took the harness that runs Codex and put it behind an API. You send a task. They run the loop. They keep the session alive, they compact, they recover if it drops. You bring the tools and you pick where the code runs.

[SHOW: the four primitives as a simple list: Agent, Environment, Session, Events]

Four things. An agent is the model plus instructions plus tools. An environment is where it runs commands and touches files. A session is one running instance with its own conversation. Events are how you watch it work.

[SHOW: editor, `openai_agents_058/01_hosted_sandbox.py`, cursor on `environment={"type": "openai_hosted"}`]

Here is what that looks like when it already ran. Demo one from the PR. One call. That environment line is the one to look at: `openai_hosted`. OpenAI spun up a box, the agent wrote `primes.py` in it, ran it, reported 129, the sum of the first ten primes. About a minute.

[SHOW: the README's "What to expect" for demo 1, the `READY environment`, `CONNECTED environment`, `final_answer` lines]

That box is theirs. The file is in it. An hour after the last keep-alive, the box is gone.

[SHOW: `02_function_tools.py`, cursor on `environment={"type": "none"}`]

And this is demo two, and it is the one people skip. Environment type `none`. No computer at all. The harness runs with nothing but a function I wrote to call. Tokens only.

[SHOW: simple three-row overlay: `none` / `openai_hosted` / `self_hosted`]

So there are exactly three environment types. None, which is demo two. OpenAI hosted, which is one and three. And self hosted, which is a machine where you run one command. You will see a list of partners on the launch post, Modal, Cloudflare, Vercel, nine of them. Those are not a fourth type. They are self hosted with the machine rented from them. Same command, same key, their box instead of yours.

That third one, on my own box, is this video.

---

## Beat 3 [1:45 - 3:00] Step 0: two keys and one install

[SHOW: platform.openai.com, API keys page]

So, setup. There are two keys, and the docs are strict about keeping them apart, and I think they are right to be.

Two programs are going to talk to OpenAI. My Python scripts, which create sessions and send messages. And the executor, which runs the agent's commands on my Mac. Each one needs a key.

The scripts use my normal key. It needs agents read, agents write, and responses write, and a default project key has all three. It is the key the PR demos ran on. Nothing new.

[SHOW: editor, `self_hosted/README.md`, the "Two keys, and why" section]

The executor gets a second, weaker key. Because the agent's commands run right next to that process, and code the agent writes could read whatever is there. So this key can do exactly one thing: connect an environment. It cannot create sessions, call models, or read anything.

[SHOW: Agents tab, creating the environment key, every other permission None]

You make it on the Agents tab. Every other permission to None. Copy it once. It goes in your shell, in the one terminal that runs the executor. Not in `.env`, because `.env` is what the scripts read and they need the normal one.

[NOTE: blur both keys. Put the app key in `.env` and export the environment key off camera before rolling.]

And one install.

[SHOW: terminal]

```
npm install -g @openai/codex@alpha
codex exec-server --help
```

That is the Codex CLI, alpha channel. It is what has the `exec-server` command. Stable does not have it yet. The install does not take long, so I will let it run and move on.

[SHOW: `ls ~/agents-demo/workspace`, seven files: six notes and `AGENTS.md`]

Then a folder for the agent to work in. Six markdown notes, a to-do list, a meeting, two ideas, groceries, a reading list. Nothing special. And one more file in there I will come back to.

---

## Beat 4 [3:00 - 4:30] Steps 1 and 2: it is already running, here is what you are looking at

[NOTE: three terminals up and connected BEFORE you roll. Pane A: `codex exec-server`, connected. Pane B: `stream.py`, showing `CONNECTED environment`. Pane C: shell in `self_hosted/`, prompt empty, with the `04_self_hosted.py` output still in scrollback so the three values and the exec-server line can be scrolled to.]

[SHOW: all three panes]

So I have this running already, because the two setup steps take a minute and I would rather spend the minute on what they mean. Three terminals. Left is the executor, that is step two. Middle is the event stream, so we can watch it work. Right is where I send it work. Let me walk you back through how these got here.

[SHOW: editor split. Left: `01_hosted_sandbox.py`. Right: `04_self_hosted.py`. Cursor on `openai_hosted` on the left, then the `self_hosted` line on the right.]

Step one is the same call demo one made. One line changes.

```python
environment={"type": "self_hosted", "workspace_directory": str(WORKSPACE)},
```

Type went from `openai_hosted` to `self_hosted`, and it takes a path. A real folder on my disk. That is the line that makes this different from every other video on this API.

And one more difference. Demo one sent the task in the same call. This one sends nothing. It cannot, because there is no environment yet. Something on my side has to show up first.

[SHOW: pane C, scroll up to the `04_self_hosted.py` output. Three values, then the exec-server command with them filled in.]

That is what running it printed. Three things the API generated. A session id, an environment id, and a remote URL. You do not look these up, they come back from the call. And under them, the exact command for step two with the values already in it.

[SHOW: pane A, the executor command at the top, then whatever it printed on connect]

Step two is that command, pasted. One process on my Mac.

```
codex exec-server --remote "<remote url>" --environment-id "<environment id>"
```

[NOTE: the environment key is exported in pane A off camera. Blur the URL and id if legible.]

[SHOW: pane B, `CONNECTED environment`]

And the stream saw it connect. That is my Mac telling OpenAI, I am the room this agent works in.

One thing about order, because it bit me. The stream does not replay. It shows events from the moment you attach. So the watcher goes up before the executor, or you miss the connect.

And what happened on the network matters. The executor dialed out. Two hosts, api.openai.com to register, and a websocket to their environments endpoint for commands. Nothing came in. No port is open on this machine. If the connection drops it reconnects on its own.

[SHOW: camera]

So that is the whole trick. Their loop, my disk. Now let's give it something to do.

---

## Beat 6 [4:30 - 6:00] Step 3: send work, on the notes folder

[SHOW: editor, `self_hosted/send.py`, the `events.create` call]

So now the useful part. Sending it work. It is one event, type `agent.session.input.message`, with the text. I kept it as a tiny script because I am going to send more than one message to the same session, and that matters in a minute.

[SHOW: README, demo 1 expected output: `$ /bin/bash -lc ...`, `python3 /workspace/outputs/primes.py`]

Same shape as demo one. It ran `ls`, it looked for an `AGENTS.md` like Codex does locally, it wrote a file, it ran it. The difference is where. That was `/workspace/outputs` in their box. This is my folder.

First task.

[SHOW: type]

```
uv run python send.py <session id> "What is in this folder? One line per file."
```

[NOTE: quote the message. zsh treats `?` as a glob and errors. It bit me on the dry run.]

[SHOW: the watcher pane. `$` lines go by, `ls`, `cat`. Then `final_answer:` with the six notes.]

Watch the stream, because every one of those commands is running here. That `ls` is my folder. When it reads a file, that is my file. The model is in their cloud. The hands are on my Mac.

Now a write.

[SHOW: type]

```
uv run python send.py <session id> 'Add "buy stamps" to the to-do list.'
```

[SHOW: stream. Then `cat ~/agents-demo/workspace/todo.md`. The new line at the bottom.]

And there it is. That is the shot from the cold open. And unlike `primes.py`, this one does not disappear in an hour, because it is on my disk.

That is the three steps. Create the session pointed at your folder. Run the executor. Send work.

[SHOW: camera]

Honest note. It is a beta. On my runs the executor connected and stayed connected, but it is a beta.


---

## Beat 6b [6:00 - 6:30] The folder has rules

[SHOW: `~/agents-demo/workspace/AGENTS.md`, nine lines]

That other file I mentioned. `AGENTS.md`. Codex reads it before it acts, and this harness is Codex. It says: to-dos go at the bottom, never delete a line, do not edit past meetings, do not delete files.

I have one of these in every folder I work in. Claude Code reads it. Hermes reads it. Now this reads it. One file, three agents, same rules. That is the part I did not expect to like this much.

[SHOW: type]

```
uv run python send.py <session id> "Delete the meeting note, it is old."
```

[SHOW: the stream. It should refuse, or ask, and cite the rule.]


So the notes did not change. That is the file doing its job, and it is the same file across three tools.

---

## Beat 7 [6:30 - 7:30] What it costs, and where it stops

[SHOW: terminal, the tail of this morning's `01_hosted_sandbox.py` run, the `--- cost estimate ---` block]

So, cost. Because I promised, and because it changes what you would do next.

Every one of these scripts prints an estimate at the end now. Tokens from the session's usage, priced off the pricing page, and container time rounded up to twenty-minute blocks. That is demo one this morning. Tokens, plus three cents for the box.

[SHOW: type]

```
uv run python sessions.py cost <session id>
```

[SHOW: the block. `container: none (self_hosted)`.]


Same thing for the session we just ran. Container line is gone, because the box is mine. What is left is tokens. And gpt-6-astra is not a cheap model. Ten dollars in, fifty out, per million. Bart, who has the biggest English video on this, left it on Astra and said on camera "this is going to be super expensive." So the container line was never the big line. The tokens are. `MODEL` is one line in `common.py` if you want to drop to something cheaper.

[SHOW: developers.openai.com pricing page, the Containers row: 1 GB $0.03, 4 GB $0.12, 16 GB $0.48, 64 GB $1.92 per 20 minutes]

For the record, that is the hosted rate you are skipping. Five minute minimum, and the box gets deleted after an hour idle, which you cannot change.

[SHOW: the overview doc, the limits]

Two limits I would want to know before I built on it.

One, US-only data residency. Two, no zero data retention, and that includes when the sandbox is your own machine. The files are on your disk. The conversation is not.

[SHOW: camera]

That second one is the thing for me. I ran this against a folder of my own notes. The notes stayed here. Everything the model read from them went there. For a demo folder, fine. For what I am about to do, my public repo with demo code in it, fine. For my content repo, I would not.

---

## Beat 8 [7:30 - 9:15] The build: the API works in my real repo

[NOTE: SAY THE SEAM. Everything up to here was a folder made for this video. Now cut to the real repo and name it.]

[SHOW: camera]

Right, I am switching folders. Everything so far was a clean folder I made for this video, six notes and nothing else. This is my actual repo, the one that PR merged into. Because reading six fake notes proves the plumbing and nothing else. If this is real, it should be able to do a job in a codebase.

[SHOW: terminal, `cd ~/dev/ai/openai_agents_058 && ls`. Four demos, `common.py`, `self_hosted/`, `README.md`.]

Same three steps. New session, pointed here instead of the notes folder.

[SHOW: `uv run python self_hosted/create_session.py ~/dev/ai/openai_agents_058`. Three values.]

[NOTE: the second session needs its own executor. Ctrl-C the first one, run `codex exec-server` again with the new URL and id. Watcher first, again. Show the flip once, fast. Do not narrate it twice.]

[SHOW: watcher shows `CONNECTED environment`]

Connected again. Now the task. `common.py` has a `print_cost` function that does the pricing math you just saw, and it has no test. So.

[SHOW: type]

```
uv run python self_hosted/send.py <session id> "Read common.py. Write tests/test_cost.py using unittest that checks the token math in print_cost with a fake session object: 1000 input tokens, 200 cached, 500 output. Run it with uv run python -m unittest and show me the output. Do not change common.py."
```

[SHOW: the stream. `cat common.py`. A write to `tests/test_cost.py`. Then `$ uv run python -m unittest ...` and the result.]

Watch it read first, then write, then run. And that run is on this Mac. That is `uv` in my venv executing a test the agent just wrote.


Now the thing the other videos skip. This session is still alive. So I keep talking to it.

[SHOW: type]

```
uv run python self_hosted/send.py <session id> "Add a second test for the container math: 25 minutes elapsed on openai_hosted should be 2 blocks, six cents. Run both."
```

[SHOW: the stream. The file updates, the test runs, two tests pass.]

Same session, same conversation. It remembers what the file is. It did not read `common.py` again.

[SHOW: terminal, `git status`. One new folder: `tests/`.]

So look at what just happened. A harness in OpenAI's cloud read my repo, wrote a test, and ran it, on my disk, in my venv. I will commit that after this and the message will say who wrote it.

[NOTE: do not commit on camera. Tyler commits by hand after the take.]

---

## Beat 9 [9:15 - 10:15] The same folder, the local agent, for zero

[SHOW: Hermes desktop, Bots tab, Coder selected]

So here is the comparison I said I would make.

This is the agent I already run on this machine. I set it up in the last video, so I will not redo that. Same shape as what we just used. A loop, tools, memory, skills, scheduled jobs. It runs here. The model can be local.

[SHOW: PR #22, the author line. Then the `self_hosted/` folder in Finder.]

And the past example is the PR itself, and the kit. Coder wrote the three PR scripts off a card on my board. Then it wrote `04` and the whole `self_hosted/` folder you just watched me run. So the thing the cloud agent worked in today was built by the local one.

[SHOW: type into Coder's chat, pointed at the notes folder]

```
Read every markdown file in ~/agents-demo/workspace and write index.md with one line per file: the filename and a one-sentence summary.
```

[SHOW: it runs. The file appears. Show the model tag, a local Ollama model.]


Same folder. Same kind of result. The model was local, so the cost line is zero, and nothing left this machine.

[SHOW: camera]

Now I do not think that makes the Agents API pointless, and I want to be fair.

[SHOW: two-column overlay]

| Reach for the Agents API when | Reach for the local agent when |
|---|---|
| It has to run when your machine is off, and you do not want to babysit it | It is your files, on your machine, and you want them to stay there |
| You want OpenAI to own the loop, the compaction, the recovery, at scale | You want a local model, or you want to switch models |
| You are shipping this to a team or a product, not just yourself | You want it free and you are fine owning the uptime |

The API is a managed harness. That is the whole product. If you want someone else running the loop for a thing you ship to other people, that is real, and self hosted makes it a lot more usable than the hosted box alone. If you want an agent for you, on your computer, you kind of already have one, and it does not send your notes anywhere.

For me, it is both. This one for things I would ship. That one for my own machine. Today they worked on the same folder.

---

## Beat 10 [10:15 - 10:45] CTA

[SHOW: camera]

So that is the Agents API on your own Mac. Three steps, one command on your side, and a test in my repo that the API wrote and ran here.

All four demos, the `self_hosted/` kit, the sample notes folder, and an `EXAMPLES.md` with more things to send it are in the repo and in the free community, link below. If you build something on this, I want to know what you pointed it at. Tell me in the comments, I read every one.

And if you have not set up the local one yet, the last video is the full setup. Thirty minutes, and it is the other half of this.

[SHOW: end card, 057 on the left]

See you in the next one.
