# OpenAI Agents API — Video Research Brief

**Research date:** September 12, 2026  
**Launch date:** September 10, 2026  
**Status:** Public beta

## Executive take

OpenAI’s new Agents API is a managed agent runtime, not another model endpoint. It exposes the Codex harness—the loop that manages model calls, tools, context, subagents, and recovery—as a cloud API. Developers still specify the model, instructions, tools, and execution environment, but OpenAI operates the orchestration layer.[2][1]

The cleanest video thesis is:

> **OpenAI is no longer just selling model calls. It now offers to run the agent loop for you.**

That is the real distinction from the Responses API and the open-source Agents SDK. Responses gives developers model-and-tool primitives and leaves them responsible for the workflow. The Agents SDK runs an agent loop inside the developer’s application. The Agents API runs a versioned Codex harness as a managed service.[18][1]

The trade is straightforward: less orchestration and infrastructure code in exchange for a more opinionated OpenAI runtime, more vendor dependence, beta instability, and important current data-governance limits.[1][23]

## What actually launched

OpenAI released the Agents API to all developers in public beta on September 10, 2026. OpenAI says the API uses the same harness and infrastructure behind Codex and is intended for reliable work that can run for hours or days.[2]

The API has four central abstractions:

1. **Agent** — reusable configuration containing model, instructions, tools, MCP connections, reasoning settings, and optional multi-agent settings.
2. **Environment** — optional execution space where the agent can run commands, work with files, and load skills or plugins.
3. **Session** — durable conversation and work state that can continue across turns.
4. **Events and items** — real-time lifecycle/output events plus persisted messages, tool calls, and results.[1][4]

This is a meaningful layer above a raw inference call. OpenAI manages session state, orchestration, automatic context compaction, subagent coordination, and recovery. The application sends work, reacts to events, handles any client-side function calls, and retrieves results or artifacts.[1][9][10]

## How a run works

A typical flow is:

1. Create or reuse an agent configuration.
2. Create a session with `environment.type` set to `none`, `openai_hosted`, or `self_hosted`.
3. Include initial input or send an input event later.
4. Consume server-sent events while the harness plans, calls tools, delegates work, and produces output.
5. If the session enters `requires_action`, the application supplies a function result or connects a self-hosted environment.
6. Inspect the root turn’s outcome and saved items; an idle session or completed stream alone does not prove all tools succeeded.
7. Continue the same session with follow-up input, or delete it when finished.[3][9][16]

Streams do not replay missed events. OpenAI’s recovery pattern is to reconnect, retrieve the persisted session/items, reconcile by item ID, and then apply buffered live updates.[9]

Webhooks are available for session-level changes such as created, action required, in progress, idle, and failed. They are intended for long-running work where an application should not hold an event stream open.[17]

## Minimal Python shape

The current quickstart uses the beta SDK surface and `gpt-6-astra` in its examples:[3]

```python
from openai import OpenAI

with OpenAI() as client:
    with client.beta.agents.sessions.create(
        agent={
            "model": "gpt-6-astra",
            "instructions": "Complete the task and verify the result.",
        },
        environment={"type": "openai_hosted"},
        input="Inspect the supplied files and write a concise report.",
        stream=True,
    ) as events:
        for event in events:
            print(event.model_dump_json())
```

Direct HTTP calls use `/v1/agents/sessions` and require the beta header `OpenAI-Beta: agents=v1`; current OpenAI SDKs add the header automatically.[3][9]

## What the managed harness adds

### Durable work and context compaction

The session persists conversation and work across turns. As the context approaches its limit, the harness automatically compacts older context so the agent can continue across multiple context windows without the developer writing a summarization or truncation strategy.[1][2]

This is one of the strongest reasons the product exists. A production agent loop otherwise needs its own state store, context policy, retry/recovery logic, and lifecycle management.[23]

### Tools

The API supports custom function tools, web search, MCP servers, tool search, and programmatic tool calling. Function tools pause the session with a required action; the application executes the function and sends back a result linked by `turn_id` and `call_id`.[2][10]

MCP connections can originate from OpenAI’s service, from the attached environment over HTTP, or from a stdio process inside the environment. This makes it possible to reach public services, private-network services, or locally installed tools without forcing every integration into the same network model.[14]

Tool search can defer loading definitions until they are relevant, reducing context overhead. Programmatic tool calling lets an agent combine, filter, chain, or parallelize operations in code before returning only useful information to model context.[2]

### Multi-agent delegation

Multi-agent support is enabled explicitly. The coordinator receives built-in orchestration tools for creating, messaging, waiting for, and interrupting subagents. Each subagent has its own model context, while all agents in a session share the same environment and filesystem.[8]

The default concurrency limit is six subagents, excluding the coordinator, and the developer can set a smaller positive limit. A notable beta limitation is that subagents inherit MCP, web search, files, and command-line access but do **not** support application function tools.[8]

### Skills and plugins

The environment can load skills—folders containing reusable instructions and supporting resources—and plugins that bundle skills with MCP configuration. Plugins can be mounted into self-hosted environments or uploaded as ZIP archives to OpenAI-hosted sandboxes.[15]

This is important because the API is not only exposing a model loop; it is exposing the broader Codex-style pattern of a filesystem, shell, reusable skills, MCP tools, and long-lived context.[1][15]

## Environment choices

### No environment

Use `environment.type: "none"` when the agent only needs hosted tools, remote MCP, or application functions and does not need shell commands or a filesystem.[4]

### OpenAI-hosted sandbox

OpenAI provisions a Linux workspace with Python, Node.js, and command-line tools. A session can install pinned packages, run setup commands, receive input files, load skills/plugins, and publish immutable files from `/workspace/outputs` as artifacts.[6]

Outbound networking can be enabled, disabled, or restricted to 1–100 exact hostnames. Each session receives a separate workspace; files survive across turns while the sandbox exists. An inactive hosted sandbox can be deleted after one hour, and that timeout is not configurable.[6]

### Self-hosted sandbox

The harness still runs at OpenAI, but command execution happens in infrastructure the developer controls. The developer starts a Codex executor and connects it to the session. This is useful for private networks, custom images, specialized compute, or an existing sandbox provider.[4][7]

Self-hosting the sandbox does **not** mean self-hosting the orchestration layer. It moves file and command execution, not the model calls, session state, or Codex harness. That boundary is central to both the product’s appeal and its lock-in risk.[1][7][23]

## Pricing

OpenAI says there is no separate Agents API platform fee. Customers pay the normal price for all model tokens, built-in tools, and any hosted sandbox use.[2]

Current OpenAI container pricing is:

| Sandbox memory | Price per 20-minute container session |
|---:|---:|
| 1 GB | $0.03 |
| 4 GB | $0.12 |
| 16 GB | $0.48 |
| 64 GB | $1.92 |

Model usage is charged separately at the selected model’s API rate, and web search or other paid tools add their own charges.[21][6]

The cost risk is not an Agents API surcharge; it is autonomous volume. One user task may create several root-agent model calls, subagent calls, retries, tool calls, context compactions, and sandbox time. OpenAI’s usage records are currently best-effort, can be null or revised, and do not expose every cache-write detail needed to calculate an exact model charge from session usage alone.[11]

## Security and data controls

Agent-generated code can access every file, credential, and network destination available to its environment. OpenAI recommends isolated compute, separate environments for workloads that must not share data, restricted outbound networking, and dedicated projects.[13]

The application API key should remain outside the sandbox. A self-hosted executor uses a restricted environment key that can connect the environment but cannot authorize other API actions. The agent can still read that environment key, so long-lived third-party credentials should stay behind a broker or trusted proxy rather than being injected into model-visible code or environment variables.[13]

The biggest current enterprise limitation is data handling: the Agents API supports data residency only in the United States and does not support Zero Data Retention. Choosing a self-hosted sandbox does not make it ZDR-eligible.[1]

This makes the beta a poor fit for workloads that require non-US residency or stateless/ZDR operation. The Responses API can support stateless patterns with `store: false` and encrypted reasoning items, so teams with strict retention requirements may need to stay at that lower-level API.[19]

## Observability limitations

The API exposes sessions, turns, saved items, events, and per-turn usage. OpenAI also provides a tracing dashboard showing recorded model generations, tool calls, subagent activity, duration, and status.[11][12]

However, the public beta does not expose trace retrieval or external trace exporters through the customer API. Detailed dashboard trace endpoints are not a supported API surface. Usage can be incomplete, and the API does not tell the customer whether command output was truncated.[11][12]

Operationally, `agent.session.idle` only means the session is ready for input. A completed turn can still include failed tool calls. Production code must inspect the turn and tool results rather than treating an idle or completed lifecycle event as proof of task success.[9][17]

## Comparison: which OpenAI layer owns what?

| Option | Core abstraction | Who owns the loop? | Best fit | Main trade-off |
|---|---|---|---|---|
| **Responses API** | Model response/items | Your application | Custom workflows, direct control, ZDR-compatible stateless patterns | Most orchestration work |
| **Agents SDK** | Agent run in TypeScript/Python | SDK inside your application | Typed, code-first workflows with custom storage, approvals, and runtime behavior | You deploy and operate it |
| **Agents API** | Durable managed agent session | OpenAI’s Codex harness | Long-running agents, managed recovery/compaction, optional sandboxes, subagents | Less control, more lock-in, beta/data limits |

OpenAI’s own guidance frames Responses as the direct-control layer and the Agents SDK as the application-owned agent runtime. The new API adds the fully managed Codex runtime above those layers.[18][1]

The former Assistants API is not the correct comparison target for a new build: it was officially sunset on August 26, 2026, and OpenAI directs migrations to Responses and Conversations.[22]

AgentKit is also different. It was a broader product suite including Agent Builder, Connector Registry, ChatKit, and eval tooling. OpenAI later announced that Agent Builder and the Evals product would be wound down, with availability ending after November 30, 2026. The new Agents API is a code/API runtime, not a visual workflow builder.[20]

## What is genuinely new versus repackaged

### Genuinely new as a product surface

- The Codex harness operated as a public managed API.
- Durable agent sessions with managed compaction and recovery.
- An explicit split between OpenAI-hosted orchestration and a selectable execution environment.
- Native subagent lifecycle and concurrency controls in the managed runtime.
- Codex-style skills/plugins and environment artifacts integrated into the API.[1][8][15]

### Existing pieces now unified

- Models and inference still come from the Responses infrastructure.
- Web search, custom functions, MCP, shell/container concepts, and streaming already existed in other OpenAI surfaces.
- The open-source Agents SDK already provided an agent loop, handoffs, tools, tracing, and guardrails inside application code.[18][19]

The launch is therefore less “OpenAI invented agents” and more “OpenAI productized its internal agent harness as managed infrastructure.”

## Early evidence—and how to present it honestly

OpenAI’s launch page includes selected customer reports: Ciridae says its evaluation score rose from 0.71 to 0.85 and its subagent flow became four times faster; SafetyKit reports a 60% reduction in cost per case; Hypha reports an 86% reduction in failed responses after separating the harness from the sandbox.[2]

These are useful launch anecdotes, not independent benchmarks. They have different workloads, no published common test protocol, and should be labeled as customer-reported results rather than typical expected gains.

Early developer discussion is split along the predictable boundary: supporters emphasize that maintaining context, memory, retries, and environments is difficult; skeptics prefer the Responses API or an open-source harness because a managed loop reduces model portability and control.[24] InfoWorld’s launch coverage similarly frames the product as a reduction in engineering effort paired with vendor-lock-in concerns.[23]

## Strongest video angle

### Recommended framing

**“OpenAI Just Turned Codex Into an API—Should You Stop Building Your Own Agent Harness?”**

This gives the video a real decision rather than a feature list:

1. Show the old architecture: Responses API + custom loop + database + queue + sandbox + retries + compaction.
2. Replace that stack with one Agents API session.
3. Demonstrate that the execution environment can still be OpenAI-hosted or self-hosted.
4. Show a function call pausing in `requires_action` and the application returning a result.
5. Enable two subagents and visualize their separate events.
6. End with the costs: control, vendor dependence, US-only residency, no ZDR, and incomplete beta observability.

The punchline is balanced: the API can remove a large amount of undifferentiated runtime work, but it does not remove the need for product-specific tools, permissions, evaluations, human approvals, cost controls, or result verification.

## Demo ideas, ranked

### 1. GitHub issue investigator — best overall

Give the agent a small repository and a bug report. Ask it to reproduce the issue, delegate an independent root-cause review, patch the code, run tests, and publish a report artifact. This exercises the sandbox, filesystem, shell, subagents, streaming events, and artifacts in one understandable story.

### 2. Research agent with parallel source tracks — easiest to explain

Ask a coordinator to delegate market, technical, and risk research to separate subagents, then combine them with citations. This makes subagent events visually obvious, but it is less differentiated from existing research-agent demos.

### 3. Support-case investigator with an application function — best architecture lesson

Use remote MCP for documentation, a client-side `get_customer` function, and no sandbox. Show the session entering `requires_action`, your server applying authorization, and the agent continuing after the tool result. This demonstrates that managed orchestration does not mean surrendering every sensitive operation.

### 4. Hosted-versus-self-hosted sandbox comparison — strongest contrarian follow-up

Run the same file-processing task in an OpenAI-hosted sandbox and a local/container executor. Compare setup, latency, logs, data boundaries, artifact handling, and cost. Emphasize that the harness remains hosted by OpenAI in both cases.

## Claims to avoid

- Do not call it a replacement for the Responses API; it is a higher-level option built around managed orchestration.
- Do not say self-hosted means fully local or ZDR; only command/file execution moves to your infrastructure.[1][7]
- Do not describe customer quotes as independent benchmarks.[2]
- Do not promise deterministic completion; the docs explicitly require inspection of turn and tool outcomes.[9][17]
- Do not imply the API is generally available; it is a beta surface and still uses a beta header.[2][3]
- Do not assume the tracing dashboard has a supported export API.[11][12]

## Suggested titles

1. **OpenAI Just Turned Codex Into an API**
2. **Stop Building Agent Loops? OpenAI’s New Agents API Explained**
3. **OpenAI Agents API vs Agents SDK vs Responses API**
4. **The Codex Harness Is Now an API—Here’s the Catch**
5. **I Built an Agent With OpenAI’s Brand-New Managed Runtime**

## Suggested 10-minute structure

- **0:00 — Hook:** “OpenAI will now run the agent loop, not just the model.”
- **0:35 — What launched:** public beta, Codex harness, durable sessions.
- **1:30 — Why agent harnesses are hard:** state, tools, sandboxes, retries, context.
- **2:30 — Architecture:** agent, environment, session, events/items.
- **4:00 — Live demo:** repo issue or research workflow.
- **6:30 — The three OpenAI layers:** Responses vs SDK vs Agents API.
- **7:45 — Pricing and runaway-work risk.**
- **8:30 — Security and data limits:** US-only, no ZDR, sandbox boundary.
- **9:20 — Verdict:** who should use the beta and who should wait.

## Bottom-line verdict

The Agents API is important because it turns OpenAI’s accumulated Codex-runtime engineering into a managed product. It is compelling for teams whose differentiation is in their tools, data, and workflow—not in maintaining an agent harness. It is less attractive for teams that need model portability, full control of orchestration, non-US data residency, ZDR, or a stable generally available API.

For a video, the strongest story is not “OpenAI launched another agents framework.” It is: **OpenAI has drawn a new infrastructure boundary. Developers can keep the tools and even the sandbox, while renting the reasoning loop, context management, recovery, and subagent coordination. Whether that is leverage or lock-in is the decision viewers need help making.**

## Sources

[1] https://developers.openai.com/api/docs/guides/agents-api/overview — Agents API overview
[2] https://openai.com/index/introducing-the-agents-api — Introducing the Agents API
[3] https://developers.openai.com/api/docs/guides/agents-api/quickstart — Agents API quickstart
[4] https://developers.openai.com/api/docs/guides/agents-api/architecture — Agents API architecture
[6] https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted — OpenAI-hosted sandboxes
[7] https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted — Self-hosted sandboxes
[8] https://developers.openai.com/api/docs/guides/agents-api/multi-agent — Multi-agent
[9] https://developers.openai.com/api/docs/guides/agents-api/sessions/events — Events and items
[10] https://developers.openai.com/api/docs/guides/agents-api/tools/functions — Function tools
[11] https://developers.openai.com/api/docs/guides/agents-api/observability — Observability and usage
[12] https://developers.openai.com/api/docs/guides/agents-api/tracing — Tracing
[13] https://developers.openai.com/api/docs/guides/agents-api/environments/security — Sandbox security
[14] https://developers.openai.com/api/docs/guides/agents-api/tools/mcp — MCP connections
[15] https://developers.openai.com/api/docs/guides/agents-api/tools/plugins — Agents API plugins
[16] https://developers.openai.com/api/docs/guides/agents-api/sessions/manage — Manage sessions
[17] https://developers.openai.com/api/docs/guides/agents-api/sessions/webhooks — Session webhooks
[18] https://developers.openai.com/api/docs/guides/agents — OpenAI agents overview and runtime comparison
[19] https://developers.openai.com/api/docs/guides/migrate-to-responses — Migrate to the Responses API
[20] https://openai.com/index/introducing-agentkit — Introducing AgentKit
[21] https://developers.openai.com/api/docs/pricing — OpenAI API pricing
[22] https://developers.openai.com/api/docs/assistants/migration — Assistants migration guide
[23] https://www.infoworld.com/article/4221163/openai-launches-managed-agents-api-to-simplify-enterprise-ai-agent-development.html — InfoWorld: OpenAI launches managed Agents API
[24] https://news.ycombinator.com/item?id=49649213 — Hacker News discussion: OpenAI Agents API
