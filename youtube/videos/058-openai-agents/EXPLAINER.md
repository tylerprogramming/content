# 058 Explainer: what the Agents API is, and what you are doing on camera

Written for Tyler to read before filming. Not a script. Every fact below was pulled from OpenAI's
docs on 2026-09-17 and checked against this Mac. Sources at the bottom.

---

## Part 1: What OpenAI actually shipped

### The one-sentence version

The Agents API is the Codex harness, rented out as a managed service. You send a task, OpenAI runs
the agent loop, and you choose which computer the agent's hands are on.

### Why that is a real product and not a wrapper

When you run Claude Code or Codex locally, the model is only one piece. Around it sits a loop that
calls the model, runs the tool, reads the result, calls the model again, compacts the context when
it gets long, and retries when something breaks. That loop is the harness, and it is most of the
engineering.

OpenAI's docs call it exactly that. From the architecture page: "Harness: The OpenAI-hosted Codex
instance that runs the model and tool loop and maintains the agent's session."

The overview page lists what the managed harness does for you:

- runs commands and code in a sandbox
- applies relevant skills and instructions
- connects to external data through tools or MCP
- lets you steer the agent while it works
- summarizes previous work to manage its context window
- breaks work into subtasks and delegates to subagents
- resumes a session where it left off

So the product is: you do not write the loop. That is the whole pitch.

### The four concepts

Straight from the overview page, these are the four things:

| Concept | What it is | In practice |
|---|---|---|
| **Agent** | The model, instructions, tools, and MCP servers | A dict you pass at create time |
| **Environment** | Where the agent runs commands and touches files | The line this video is about |
| **Session** | A durable instance of an agent that works on tasks | Has an id, stays alive, remembers |
| **Events and items** | Inputs you send and output produced | The stream you watch |

The one worth slowing down on is **session**, because it is the difference between this and a
normal API call. A session is durable. It keeps the conversation and the saved work. You send a
second message to the same session and it picks up where it was. From the sessions doc: "A message
sent to an idle session starts a new turn. A message sent during an active turn steers that turn."

That second half matters. Steering a running agent is a first-class feature, not a hack.

### The environment is the fork in the road

There are **three** environment types, not two. The script currently says three "choices" but frames
them as hosted / partner / your machine, which is slightly off. The actual types are:

| `environment.type` | What happens | Cost on top of tokens |
|---|---|---|
| `none` | No sandbox at all. The agent answers and calls your function tools, but has no shell and no files. | Nothing |
| `openai_hosted` | OpenAI provisions a Linux box with Python, Node, and CLI tools. Working dir is `/workspace`. | Container rate |
| `self_hosted` | You run one command on a machine you own. The harness treats that machine as the environment. | Nothing |

The nine partners (Modal, Cloudflare, Vercel, Daytona, Blaxel, E2B, Runloop, DigitalOcean, OCI) are
not a separate type. They are `self_hosted` with the "machine you own" being rented from them. Worth
saying correctly on camera, because a developer will notice.

Note that demo 2 in your PR already uses `none`. That is a good teaching beat you are currently not
using: the harness works with no computer at all.

---

## Part 2: What you are doing on camera, exactly

The video is the `self_hosted` path, because 0 of the 14 competitor videos do it. Everyone else
clicks "keep it OpenAI hosted" and moves on.

### The mental model to say out loud

**Their loop, your disk.** The model and the agent loop run in OpenAI's cloud. The shell commands and
the file writes happen on your Mac. One outbound WebSocket connects the two.

### The three steps

**Step 0, setup (two keys and one install).**

Two separate keys, and the docs are strict about it:

- Your **app key** (`OPENAI_API_KEY`) needs `api.agents.read`, `api.agents.write`, and
  `api.responses.write`. A normal project key has all three. This one lives in your Python script
  and stays out of the sandbox.
- An **environment key**, created on the Agents tab under Environments, with every other permission
  set to **None**. This is what the executor on your Mac holds, passed in as `CODEX_API_KEY`.

Why two: agent-generated code can read the environment key. The docs say it plainly, and the reason
the restriction exists is that the key can only connect an environment and authorize nothing else.
That is a genuinely good security design point and it is worth thirty seconds.

Then one install: `npm install -g @openai/codex@alpha`.

**Step 1, create the session pointed at your Mac.**

```python
session = client.beta.agents.sessions.create(
    agent={"model": "gpt-6-astra", "instructions": "..."},
    environment={
        "type": "self_hosted",
        "workspace_directory": "/Users/tylerreed/agents-demo/workspace",
    },
)
```

One line differs from demo 1 in your PR: `openai_hosted` becomes `self_hosted` plus a real path.

It returns three things you need: `session.id`, `session.environment.id`, and
`session.environment.remote_url`. The docs say to pass the remote URL "unchanged, including when
reconnecting."

At this point the session exists and is **waiting**. The stream shows
`agent.session.environment.pending`. Nothing can happen yet, because the agent has no hands.

**Step 2, run the executor.**

```bash
export CODEX_API_KEY="<environment key>"
codex exec-server \
  --remote "<remote_url>" \
  --environment-id "<environment id>"
```

This is the whole trick. The executor registers over `https://api.openai.com`, then opens a
WebSocket to `wss://codex-cloud-environments.chatgpt.com` for commands and results. Both outbound.
Nothing opens a port on your Mac. The docs confirm it reconnects on its own if the connection drops.

The stream flips `pending` to `agent.session.environment.connected`. That flip is your shot.

**Step 3, send it work.**

```python
client.beta.agents.sessions.events.create(
    session_id,
    events=[{"type": "agent.session.input.message",
             "input": [{"role": "user",
                        "content": [{"type": "input_text", "text": text}]}]}],
)
```

Then watch the event stream. Every `ls`, every `cat`, every file write is running on your Mac.

**The payoff beat.** The session stays alive, so you send a second message and it continues without
re-reading everything. That is the thing Bart explicitly names as a gap in his video and leaves
unsolved (he says you would need "a separate database" of session ids). You do it in one line.

### The closing comparison

Same folder, same task, run by the local Hermes agent on Ollama. Cost zero, nothing leaves the Mac.
Then the honest two-column table: reach for the Agents API when it must run while your machine is
off or you are shipping to other people; reach for the local one when it is your files and you want
them to stay yours.

---

## Part 3: The numbers, verified

**Container pricing** (only applies to `openai_hosted`, which is what you are removing):

| Container | Per 20-minute session |
|---|---:|
| 1 GB | $0.03 |
| 4 GB | $0.12 |
| 16 GB | $0.48 |
| 64 GB | $1.92 |

Plus, verbatim from the pricing page: "Eligible container sessions will be billed by the minute,
with a 5-minute minimum per session."

**There is no fee for the API itself.** Model usage bills at normal API rates, tools at standard
rates. That is the overview page's Pricing section.

**Model cost is the real line, not the container.** `gpt-6-astra` standard short context is $10.00
per 1M input and $50.00 per 1M output. That is why Bart says "this is going to be super expensive"
on camera. Self-hosting removes the $0.03, not the $50. Say that honestly or the video looks like
it is selling a saving that is not there.

**The two limits**, verbatim from the overview page: "The Agents API currently supports data
residency only in the United States and does not support Zero Data Retention (ZDR). Choosing a
self-hosted sandbox does not make the Agents API ZDR-eligible."

That second sentence is the strongest line in your video. Your files stay on your disk. The
conversation does not. Nobody else is saying it.

---

## Part 4: What is still not verified

Everything in Parts 1 through 3 is confirmed against the docs or this machine. These are not:

| Claim | State |
|---|---|
| The whole self-hosted flow end to end | **Never run on this Mac.** No session created, no executor connected, no task sent. |
| Connect time is faster than the hosted box's 20 to 30 s | Unmeasured. The "watch how long" line has no number behind it. |
| "Mine reconnected once during the dry run" (beat 6) | **Placeholder for an event that has not happened.** Cut it or replace it with the truth. |
| Hosted sandbox deleted after an hour idle | In your PR README but **not on any doc page I could find.** The openai-hosted doc only says files persist "while its sandbox exists". Soften to "sandboxes expire" unless you find the source. |
| The agent writes a usable `04_self_hosted.py` | Unattempted. This is beat 8, the climax. |
| Local Ollama model does the index task cleanly | Unattempted. |

**Two script references point at things that do not exist:**

1. Beats 1 and 3 say to show the README's "Not done" section. There is no "Not done" heading in the
   merged README. The equivalent content is the last bullet under "Things worth saying on camera"
   (line 106): self-hosting "needs the key from the dashboard Agents tab." Re-point those SHOW
   markers at that line.
2. The README's file table lists `CLAUDE.md`, which is not in the merged folder. If you show the
   table on camera, that row is a visible error.

---

## Sources

OpenAI docs, fetched 2026-09-17:
- Overview: https://developers.openai.com/api/docs/guides/agents-api/overview
- Architecture: https://developers.openai.com/api/docs/guides/agents-api/architecture
- Self-hosted sandboxes: https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted
- OpenAI-hosted sandboxes: https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted
- Sandbox lifecycle: https://developers.openai.com/api/docs/guides/agents-api/environments/lifecycle
- Run and continue sessions: https://developers.openai.com/api/docs/guides/agents-api/sessions
- Pricing: https://developers.openai.com/api/docs/pricing

Verified on this Mac 2026-09-17:
- `@openai/codex` 0.154.0 (`@latest`) has `codex exec-server` with `--remote`, `--environment-id`,
  `--remote-transport`. The alpha tag is not required.
- `openai` 3.14.1 exposes `beta.agents.sessions.create`, `.events.create`, `.events.stream`, and the
  self-hosted response carries `environment.id` and `environment.remote_url`.
