# OpenAI Agents API — technical research brief

**Status:** Public beta, announced September 10, 2026. This is a managed API for the Codex agent harness—not the older Agents SDK and not a thin alias for the Responses API.[1][2]

## What it is

The Agents API runs the model/tool loop inside an OpenAI-managed Codex harness and durably maintains agent sessions. The application chooses an agent configuration, tools, and an optional execution environment; OpenAI handles session orchestration, automatic context compaction, subagent coordination, and harness recovery.[1][3]

The boundary is important:

- **Agents API:** OpenAI runs the Codex harness; state is stored as sessions, turns, and items; environments may be OpenAI-hosted, self-hosted, or absent.
- **Agents SDK:** the SDK runs the loop inside your application, and your application owns deployment/runtime and storage choices.
- **Responses API:** direct model responses with application-managed history/chaining or Conversations; it is the lower-level integration surface.[2]

## Resource model

| Object/resource | Role |
|---|---|
| **Agent** | Reusable or inline configuration: `model`, `instructions`, `tools`, reasoning/output controls, and `multi_agent`. A stored agent can be referenced by `agent_id`; an inline `agent` object can override it for one session. Supplied objects/arrays replace, rather than merge with, saved values.[4] |
| **Environment** | Optional execution target. `none` has no shell/files; `openai_hosted` provisions a managed Linux sandbox; `self_hosted` connects the managed harness to customer-controlled compute.[3][10][11] |
| **Session** | Durable conversation and saved-work container. The create endpoint is `POST /v1/agents/sessions`; without `agent_id`, an inline agent needs a model. The response object is `agent.session` and includes agent/environment snapshots, `status`, `required_actions`, usage, timestamps, metadata, and vault IDs.[5][15] |
| **Turn** | One cycle of work. Input sent while idle starts a new root turn; input during an active turn steers that same turn. Turns are asynchronous and have completed/failed/cancelled outcomes.[5] |
| **Event** | Live state/output update or client input. Clients post input to `/v1/agents/sessions/{session_id}/events` and consume an SSE stream from that session.[5][6] |
| **Item** | Durable message or tool/coordination record. Root session items and per-subagent items can be listed later; turns and items use cursor pagination.[6] |
| **Subagent** | Delegated worker with its own context and turn/item history. Coordinator and subagents share the session environment/filesystem.[9] |
| **Artifact** | Immutable published copy of a file produced by an OpenAI-hosted sandbox, normally from `/workspace/outputs`; artifacts survive environment expiration and are downloaded via session artifact endpoints.[13] |
| **Vault** | Separate credential store for service-origin MCP connections; credentials are not embedded in reusable agent definitions.[8] |

## Request/response lifecycle

1. **Configure and create.** Call `POST /v1/agents/sessions` with `environment`, either `agent` and/or `agent_id`, optional initial `input`, optional `vault_ids`/metadata, and optional `stream`. Requests require `OpenAI-Beta: agents=v1`; SDKs add it automatically. Project keys need `api.agents.read`, `api.agents.write`, and `api.responses.write`.[14][15]
2. **Environment readiness.** With `openai_hosted`, OpenAI provisions the sandbox asynchronously. With `self_hosted`, the application starts `codex exec-server` using the session environment ID/remote URL and a restricted environment key. With `none`, no executor is involved.[3][10][11]
3. **Turn execution.** Initial input starts work after the environment is ready. Typical stream events include session/environment state, `agent.session.turn.created`, `.in_progress`, item add/done events, output deltas, and one of `agent.session.turn.completed|failed|cancelled` for the root turn.[5][6]
4. **Required actions.** A function call or disconnected self-hosted environment puts the session into `requires_action`. Retrieve the session and inspect `required_actions`; return a tool result with the exact `turn_id` and `call_id`, or connect the requested environment. The harness then continues the existing turn.[5][7]
5. **Completion and persistence.** Treat a root turn terminal event—not `agent.session.idle` or stream closure—as its outcome. Even a completed turn can contain failed tools, so inspect items/output. List saved items/turns later, and download published artifacts if applicable.[5][6][13]
6. **Continue, steer, cancel, or delete.** Post `agent.session.input.message`; it steers the active turn or starts a new one when idle. Post `agent.session.input.cancel` to stop only the active turn while preserving the session. Delete the session separately when finished.[5]

## Streaming and recovery

`stream: true` on session creation returns SSE events for the first turn. For later work, subscribe to `GET /v1/agents/sessions/{id}/events?stream=true` **before** posting the next input so early events are not missed. Text rendering should correlate `item_id`, `output_index`, and `content_index`, append `agent.session.turn.output_text.delta`, then replace the buffer with `.done` text when provided.[6]

Streams do **not** replay missed events. Official recovery is: open a replacement stream and buffer it; retrieve the session and saved items; rebuild local state keyed by item ID; apply buffered updates while dropping updates for already-final items; then resume live handling. Saved items recover completed work but not every missed intermediate event.[6]

For application function tools, persist side-effecting results keyed by session/turn/call and resubmit the stored result with the same IDs after reconnecting; do not blindly execute a possibly-successful side effect twice.[7]

## Steering

There is no separate steering endpoint: steering is ordinary `agent.session.input.message` submitted while a root turn is active. The same event sent to an idle session creates a new turn with the existing conversation and work. The docs recommend opening the event stream first.[5]

## Tools and integrations

- **Environment tools:** with a sandbox, the harness has built-in command execution/Bash and apply-patch/file work. `environment: none` removes those capabilities.[3]
- **Web search:** add `{ "type": "web_search" }`; modes are `live` (default), `cached`, or `disabled`, with optional domain and location constraints. Prompting for search does not enable it by itself.[16]
- **Function tools:** JSON-Schema definitions in `agent.tools`; the application executes calls and posts `agent.session.input.tool_result`. Attaching an environment does not automatically execute application functions there.[7]
- **MCP:** HTTP connections can originate at OpenAI (`service`, default; no environment) or the environment; stdio MCP runs in the environment. `allowed_tools`, `required`, inline per-session auth, or attached vault credentials control discovery/startup/authentication.[8]
- **Programmatic tool calling / tool search:** supported as agent tools; deferred function loading uses `defer_loading: true` plus `tool_search`.[3][7]
- **Skills/plugins:** environments can expose skill/capability directories; plugins package skills plus MCP configuration. Hosted sandboxes can receive plugin ZIPs or environment templates.[10]

## Subagents

Enable delegation at session creation with `agent.multi_agent.enabled: true`; `max_concurrent_subagents` defaults to **6**, excluding the coordinator. The harness injects create/message/wait/interrupt coordination tools automatically. Subagents have isolated model context but share one environment and filesystem, and can run concurrently.[9]

Subagents inherit configured MCP tools/credentials/allowlists, web-search settings, environment files, and command-line tools. They **do not support application function tools**. Observe them via `agent.session.subagent.created` and coordination item types such as `create_subagent_call`, `send_subagent_input_call`, `wait_for_subagents_call`, and `interrupt_subagent_call`; per-subagent item history is retrievable, but the stream is not a complete inter-agent transcript.[9]

## Context compaction

The managed harness automatically summarizes prior work to manage the model context window and can resume a durable session where it left off.[2][3] **Uncertain/undocumented:** the launch guide and public reference examined do not expose a session-level compaction endpoint, threshold, policy control, compaction event, or exact summary schema for Agents API. Do not import the separate Responses API `/responses/compact` semantics into this API without confirmation.

## Environments and sandbox behavior

- **`none`:** useful for model/tool-only tasks; no Bash, apply-patch, workspace files, or executor MCP. Remote service-origin MCP and application functions still work.[3]
- **`openai_hosted`:** managed Linux workspace at `/workspace` with Python, Node.js, and CLI tools. Configure packages, setup commands, initial files, env vars, skills/plugins, templates, and network access (`disabled`, restricted exact-host allowlist, or enabled). Save publishable outputs under `/workspace/outputs`.[10][13]
- **`self_hosted`:** laptop/container/remote sandbox/private-network compute. Run `codex exec-server`, which makes outbound connections to OpenAI and executes harness-requested commands. Each session gets its own environment ID; your application owns provisioning, reconnection, storage, shutdown, and file durability.[11][12]

A session can outlive self-hosted compute. A replacement executor using the same environment ID does not restore files unless the provider storage/snapshot does. Input-time connection waits last up to five minutes; timed-out input is not durably queued, and a late connection does not replay it. Deleting a session neither stops self-hosted compute nor emits a deletion webhook.[12]

## Minimal Python example

```python
from openai import OpenAI

client = OpenAI()
with client.beta.agents.sessions.create(
    agent={
        "model": "gpt-6-astra",
        "instructions": "Write clean code, run it, and report actual output.",
        "multi_agent": {"enabled": True, "max_concurrent_subagents": 2},
    },
    environment={"type": "openai_hosted"},
    input="Create tree.py, run it, and show the directory tree.",
    stream=True,
) as events:
    for event in events:
        print(event.to_json(indent=None), flush=True)
```

For a follow-up or mid-turn correction, save the session ID and post:

```python
client.beta.agents.sessions.events.create(
    session_id,
    events=[{
        "type": "agent.session.input.message",
        "input": [{
            "role": "user",
            "content": [{"type": "input_text", "text": "Exclude hidden files."}],
        }],
    }],
)
```

These shapes match the official Python quickstart/session guide; they were not executed here because no API credential or billable test was requested.[5][14]

## Languages, models, and availability

Official quickstart examples are provided for **Python, JavaScript, Go, Java, Ruby, and raw HTTP/cURL**; SDK calls live under the beta Agents namespace.[5][14]

The official launch and core guides consistently demonstrate **`gpt-6-astra`**. The create-session schema treats `model` as a string rather than publishing an exhaustive compatibility enum.[4][15] **Uncertain:** I found no authoritative, exhaustive Agents API model-support matrix in the launch material or guide set. One official provider guide also contains a `gpt-5.6-sol` manifest example, but that is not enough to claim a complete supported-model list; validate the intended model against the current Models/API reference before deployment.[17]

The launch says public beta is available to all developers. Pricing is the selected model’s normal API token rates plus standard charges for OpenAI tools and hosted containers; there is no separate Agents API fee.[1][3]

## Practical cautions

- Persist session IDs; they are the durable conversation handle.[5]
- Subscribe before posting input, and never infer success from idle/EOF alone.[5][6]
- Make external side effects idempotent by `(session_id, turn_id, call_id)`.[7]
- Coordinator and subagents share files; avoid concurrent edits to the same files.[9]
- Keep the broad application key outside sandboxes; self-hosted executors should receive only restricted environment keys.[11]
- Treat automatic compaction/recovery as managed behavior, not as the Responses API’s explicit compaction contract.[2][3]

## Sources

[1] https://openai.com/index/introducing-the-agents-api — Introducing the Agents API
[2] https://developers.openai.com/api/docs/guides/agents — Agents runtime comparison
[3] https://developers.openai.com/api/docs/guides/agents-api/overview — Agents API overview
[4] https://developers.openai.com/api/docs/guides/agents-api/configuration — Configuring Agents
[5] https://developers.openai.com/api/docs/guides/agents-api/sessions — Run and continue sessions
[6] https://developers.openai.com/api/docs/guides/agents-api/sessions/events — Events and items
[7] https://developers.openai.com/api/docs/guides/agents-api/tools/functions — Function tools
[8] https://developers.openai.com/api/docs/guides/agents-api/tools/mcp — MCP connections
[9] https://developers.openai.com/api/docs/guides/agents-api/multi-agent — Multi-agent
[10] https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted — OpenAI-hosted sandboxes
[11] https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted — Self-hosted sandboxes
[12] https://developers.openai.com/api/docs/guides/agents-api/environments/lifecycle — Sandbox lifecycle
[13] https://developers.openai.com/api/docs/guides/agents-api/environments/files — Files and artifacts
[14] https://developers.openai.com/api/docs/guides/agents-api/quickstart — Agents API quickstart
[15] https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/methods/create — Create an agent session reference
[16] https://developers.openai.com/api/docs/guides/agents-api/tools/web-search — Web search
[17] https://developers.openai.com/api/docs/guides/agents-api/environments/providers/digitalocean — DigitalOcean sandbox provider guide
