# OpenAI Agents API launch: video angles and comparison brief

**Research date:** September 12, 2026  
**Launch date/status:** September 10, 2026; public beta for all developers.[1]

## The one-sentence framing

**The Agents API is not another model endpoint and not the old Agents SDK with a new name. It is “Codex’s managed harness as a service”: OpenAI runs the long-lived agent loop, session state, context compaction, recovery, and subagent orchestration; the developer supplies the task, model, tools, and an optional execution environment.[1][3]**

That is the cleanest opening because it resolves the naming confusion before introducing the product.

## What actually launched — facts

- One `beta.agents.sessions.create` call can define the model and instructions, attach MCP/custom/built-in tools, select an environment, enable subagents, provide the initial task, and begin streaming the run.[3][14]
- The API revolves around four objects: **agent**, **environment**, **session**, and **events/items**. A session is durable and can be continued or steered after the first task.[3]
- OpenAI hosts the harness. Compute can be absent, OpenAI-hosted, or self-hosted/partner-hosted; a self-hosted environment may be a laptop, Docker container, remote sandbox, or Lambda-style runtime.[16]
- Managed features include automatic context compaction, recovery/resume, skills and instructions, MCP and function tools, mid-run steering, programmatic tool calling, and parallel subagents with separate contexts.[1][3][9]
- OpenAI-hosted sandboxes provide Linux, Python, Node.js, CLI tools, package installation, files, skills/plugins, and configurable outbound networking. The default outbound-network setting is enabled unless a template says otherwise; restricted mode uses an exact-domain allowlist.[10]
- The API itself has no additional harness fee during beta. Customers pay model tokens, tools, and—if used—hosted containers. Container rates are per 20-minute session: 1 GB $0.03, 4 GB $0.12, 16 GB $0.48, and 64 GB $1.92.[1][18]
- This is a beta surface (`OpenAI-Beta: agents=v1`), not a GA commitment.[14]

## The comparison people will need

| Product | What it is | Who runs the agent loop/state? | Compute/files | Best fit | Main tradeoff |
|---|---|---|---|---|---|
| **Responses API** | Low-level model-response primitive with built-in tools | Your application, with optional hosted orchestration; state via history, response chaining, or Conversations | Your execution environment; some hosted tools | Maximum control; custom or relatively bounded loops | Highest integration work; you own compaction, recovery, and orchestration choices.[2][19] |
| **Open-source Agents SDK** | Code library/runtime for agents, tools, handoffs, guardrails, sessions, tracing, and sandbox integrations | The SDK inside your application | Your runtime/sandbox integrations | Teams that want reusable agent abstractions but own deployment, storage, approvals, and runtime behavior | More operations and code than Agents API; more control and portability. The Python repo describes support for Responses/Chat Completions and 100+ other LLMs.[2][29] |
| **Agents API** | Managed Codex harness exposed as an API | OpenAI | No sandbox, OpenAI-hosted sandbox, or your/partner sandbox | Long-running embedded agents where low integration effort and managed recovery matter | OpenAI controls the harness and session plane; US-only residency and no ZDR today.[2][3] |
| **AgentKit / Agent Builder** | 2025 product bundle: visual Agent Builder, connectors, ChatKit, and eval tooling built on Responses | Workflow-dependent; Agent Builder was a visual design layer | OpenAI platform/workflow deployment model | Visual collaboration and quick prototypes | Crucial current context: OpenAI is winding down Agent Builder and Evals on November 30, 2026, recommending Agents SDK for code workflows or Workspace Agents for natural-language use cases.[21] |
| **Codex** | OpenAI’s coding-agent product and open-source local CLI/harness | Codex product/CLI | Local computer or Codex cloud, depending on surface | Coding and software engineering directly | It is an end-user agent; Agents API is the developer-facing managed harness derived from it.[1][22] |
| **Hermes / self-hosted harnesses** | Open-source full agent framework/application layer with persistent memory, reusable/self-improving skills, model/provider switching, tools, messaging gateways, cron, and multiple execution backends | You run and own it | Local, Docker, SSH, or remote sandbox backends | Personal/company agent infrastructure, model choice, durable memory, multi-channel operation, custom policy | You own deployment, upgrades, reliability, and security; not the “one API call” path.[23] |

### Critical distinction: “self-hosted sandbox” is not “self-hosted Agents API”

With the self-hosted option, **your box runs `codex exec-server` and executes commands, but OpenAI still runs the harness, model/tool loop, and session state**.[11][16] OpenAI explicitly says self-hosting the sandbox does **not** make the API Zero Data Retention eligible; Agents API data residency is currently US-only.[3] This is the most important correction to likely launch-day misunderstandings.

## Strong video angles, ranked

### 1. **“OpenAI Just Turned Codex Into AWS for Agents”**

**Hook:** Developers no longer rent only model intelligence; they can now rent the operational layer that keeps an agent alive for hours or days.

**Evidence:** OpenAI runs the harness, sessions, compaction, recovery, tool orchestration, and subagents while allowing separate compute placement.[1][3][16] Independent enterprise analysts frame the value as eliminating the queue, state database, sandbox fleet, compaction routine, and retry policy that otherwise block prototypes from becoming unattended systems.[25]

**Why it works:** It makes an abstract “harness” legible as managed infrastructure. The historical analogy is not “new ChatGPT”; it is managed cloud replacing hand-built operational plumbing.

**Interpretation:** The durable moat may move from model APIs to the stateful runtime around them. OpenAI is trying to own the control plane while letting hyperscalers and sandbox vendors compete for the compute plane.

**Watchout:** “AWS for agents” is analogy, not OpenAI language. Say clearly that the API is public beta and narrower than a general cloud.

### 2. **“The Harness Is the Product Now”**

**Hook:** The launch’s biggest claim is that the model is no longer the complete product; compaction, tool loading, subagents, recovery, and cache-aware orchestration materially determine agent performance.

**Evidence:** OpenAI says it will version and improve the harness alongside model launches; automatic compaction carries work across context limits, tool search defers schemas to save tokens and preserve cache, and programmatic tool calling can parallelize/filter tool work in code.[1] The dedicated tool docs say tool search only loads needed tools and appends them to preserve cache, while programmatic tool calling runs generated JavaScript in an isolated V8 environment.[1]

**Interpretation:** This is also a distribution strategy: charge no separate harness fee, improve model consumption and retention, and make the optimized route to OpenAI models the OpenAI-managed runtime.

**Visual:** Layer cake: **model → Responses primitive → SDK/self-built loop → managed Agents API → application/employee experience**.

### 3. **“One API Call Is True—and Misleading”**

**Hook:** Yes, one call starts a production-shaped agent session. No, one call does not make a production system.

**Evidence:** The quickstart creates a session, provisions a sandbox, supplies a task, and streams events in one call.[14] But the same docs require correct API-key scopes, stream/webhook recovery, environment lifecycle handling, cleanup, artifact persistence, and checking actual tool outcomes. They explicitly warn that a completed turn does not guarantee every tool succeeded and that an `idle` event alone does not mean success.[14] In the beta, trace retrieval/export is not in the public API and usage values are best-effort, may be null, and are not a final bill.[27]

**Interpretation:** OpenAI has removed agent-loop infrastructure, not application engineering. The remaining hard parts are permissions, domain tools, evaluation, human approval, data boundaries, and product UX.

**Best contrarian title:** **“I Read the Fine Print on OpenAI’s ‘Production-Ready Agent in One Call’”**

### 4. **“Bring Your Own Sandbox Does Not Mean Bring Your Own Agent”**

**Hook:** The headline sounds hybrid-cloud friendly, but the control plane remains OpenAI.

**Evidence:** Your environment executes shell commands and holds files; OpenAI’s external harness decides the model/tool loop and maintains state.[11][16] Even a self-hosted environment cannot enable ZDR, and residency remains US-only.[3]

**Interpretation:** This is useful isolation and compute flexibility, but not full sovereignty. Regulated workloads and multi-model strategies may still prefer an independent SDK/harness; InfoWorld’s analysts independently identify lock-in, governance, and negotiation leverage as the main enterprise concerns.[25]

**Balanced counterpoint:** The same separation can reduce blast radius: keep proprietary code/data in your VPC while outsourcing the difficult control loop. Do not present it as fake self-hosting; present it as **split hosting**.

### 5. **“Responses API vs Agents SDK vs Agents API: Stop Using the Names Interchangeably”**

**Hook:** OpenAI now has three valid runtime levels, not three versions of the same thing.

**Evidence:** OpenAI’s own comparison labels integration effort low/medium/high and divides them by who owns execution and state: Agents API for managed long-running sessions, SDK for code-first custom workflows, Responses for direct model control.[2]

**Simple rule:**
1. Use **Responses** when the loop itself is your product or the task is bounded.
2. Use **Agents SDK** when you want abstractions but must own storage, approvals, models, and runtime.
3. Use **Agents API** when managed durability and reduced operations outweigh control-plane lock-in.

**Interpretation:** The API is not automatically the successor to Responses or SDK. It is a higher-level deployment choice.

### 6. **“Agent Builder Is Already Dying—So Is This API Another Assistants Moment?”**

**Hook:** OpenAI launched AgentKit’s visual Agent Builder in October 2025, then announced its November 30, 2026 shutdown less than a year later.[21]

**Evidence:** The current AgentKit post explicitly says OpenAI is winding down Agent Builder and Evals and points code workflows to the Agents SDK.[21] The new Agents API is also explicitly beta.[14]

**Interpretation:** Stateful APIs create higher migration cost than stateless model calls, so product-churn risk deserves weight. This does not prove Agents API will be retired; it makes portability, export paths, and contract stability legitimate buying criteria. A Hacker News commenter explicitly connected this concern to being “burned” by the Assistants-to-Responses transition.[24]

**Fair framing:** This angle should be a question, not a prediction. OpenAI’s open-source Codex base lowers conceptual opacity, but it does not make hosted session state portable.

### 7. **“Free Harness, Expensive Agents”**

**Hook:** The API layer costs $0, but autonomous work can multiply model and container usage invisibly.

**Evidence:** Agents may make several model calls; reasoning tokens are output tokens; subagents make additional calls; reported usage can lag or be null.[27] Containers are billed per 20-minute session, and the OpenAI launch forum itself warned newcomers to calculate container costs carefully.[18][28]

**Interpretation:** “No additional fee” is an adoption subsidy and bundling strategy, not “free agents.” The correct KPI is cost per successful task, not cost per API call.

**Suggested demo:** Run the same job three ways—single Responses loop, Agents API without subagents, Agents API with four subagents—and compare latency, total tokens, container intervals, and result quality. Do not claim a winner before measuring.

### 8. **“Codex Is Escaping the IDE”**

**Hook:** OpenAI’s showcase is less about code generation than about turning the Codex pattern into a general digital worker.

**Evidence:** Official examples include a Slack teammate, SRE incident responder, read-only data analyst, GitHub issue investigator, and bulk contract/invoice reviewer.[3] The document-review demo mounts a policy as a skill, delegates documents to specialists, writes artifacts, and leaves approvals to humans.[26]

**Interpretation:** Coding agents won because files, shells, tests, and artifacts create a verifiable work loop. OpenAI is generalizing that loop to operations, analysis, and compliance—not merely exposing Codex coding autocomplete.

### 9. **“Managed Harness vs Hermes: Convenience vs Agency”**

**Hook:** Agents API sells a managed session; Hermes-like systems sell an agent you operate and extend.

**Evidence:** Agents API owns the control plane and durable session but is currently OpenAI-hosted, US-only, and non-ZDR.[3] Hermes is MIT-licensed, provider-agnostic, runs across local/cloud backends and messaging surfaces, and adds persistent cross-session memory, reusable/self-improving skills, scheduling, plugins, and model switching.[23]

**Interpretation:** These are adjacent, not exact substitutes. Agents API is a component for developers embedding long-running agents into products. Hermes is a self-hostable agent application/framework and personal/company control plane. A useful architecture could even put an Agents API session behind a broader independent orchestrator—but every dependent task would still inherit OpenAI’s control-plane and data-policy constraints.

**Best balanced title:** **“Would I Replace My Self-Hosted Agent With OpenAI’s New API?”**

## Practical demos that reveal the product instead of repeating the launch post

### Demo A — same task, three abstraction levels

Ask each runtime to inspect a small repository, reproduce a seeded bug, and write a report without editing source:

- Responses API: implement the loop and state manually.
- Agents SDK: use its runner/session and local sandbox.
- Agents API: create a managed session with the same sandbox and task.

Measure code written by the developer, recovery after disconnect, trace quality, tokens, elapsed time, and ease of resuming. This directly tests OpenAI’s low/medium/high integration claim.[2]

### Demo B — “self-hosted” packet boundary

Run `codex exec-server` in a Docker container, keep sensitive source files there, and diagram which actions happen locally versus at OpenAI. Then quote the non-ZDR rule on screen.[11][3] This is more educational than a generic quickstart.

### Demo C — subagents: speedup or token bonfire?

Use four independent release-note files and compare sequential review with two/four subagents. The API defaults to six concurrent subagents excluding the coordinator, shares one filesystem among them, and warns agents editing the same files must coordinate.[9] Show both wall-clock time and aggregate usage.

### Demo D — policy skill + human gate

Adapt OpenAI’s invoice/contract example: mount a read-only policy skill, delegate reviews, write JSON artifacts, and require human approval. The official sample explicitly never lets the agent approve payments and notes retained activity is not a complete audit of specialist work.[26] That creates a strong “useful, but not magically compliant” segment.

### Demo E — cost trap

Start a 1 GB hosted sandbox, continue work across turns, and track the 20-minute billing intervals. Compare deleting promptly versus allowing keep-alives; hosted sandboxes may be deleted after an hour without activity/keep-alives, and that timeout is not configurable.[10][18]

## Launch claims worth quoting—with caveats

- OpenAI: “production-ready agent in a single API call.”[1] **Caveat:** this describes session creation and managed infrastructure, not completed security/evals/approval/product work.
- OpenAI: same harness and infrastructure behind Codex.[1] **Caveat:** it is powered by the open-source Codex harness, but the managed service and stored state are not themselves an open deployment.[1][22]
- Ciridae customer quote: evaluation score reportedly improved from 0.71 to 0.85 and subagent-flow latency fell 4×.[1] **Caveat:** launch-partner testimonial, not independent benchmark.
- SafetyKit customer quote: 60% lower cost per case after migration.[1] **Caveat:** no public workload, baseline, or audit in the launch material.
- Hypha customer quote: 86% fewer failed agent responses after separating harness from sandbox.[1] **Caveat:** customer-reported and undefined denominator/methodology.

**Editorial rule:** Call all three “customer-reported launch results,” never “benchmarks” or “OpenAI proved.”

## What developers are reacting to

A Hacker News launch thread reached roughly 341 points and 177 comments when retrieved on September 12; that is a useful qualitative sample, not representative polling.[24]

Recurring themes in that thread:

1. **Genuine confusion about API vs SDK.** The top discussion asks why one would choose the API when the SDK in a sandbox seems better.[24]
2. **Convenience has a real market.** Defenders compare managed agents to cloud infrastructure: security patching, uptime, scaling, recovery, and OPEX instead of building everything.[24]
3. **Lock-in is the dominant objection.** Commenters want model interchangeability and ownership of state, especially while no model/harness winner is clear.[24]
4. **Self-hosters say the basic pattern already works.** Examples in the thread include Codex in QEMU, Slack bots on VMs, and Hermes in a remote Docker container; several commenters argue that local control is the point.[24]
5. **Others say good harnesses are deceptively hard.** Several developers describe context, indefinite waits, async tools, human interaction, recovery, and evolving model APIs as the rabbit hole OpenAI is selling away.[24]
6. **Security skepticism is heightened.** One prominent comment immediately questions whether restricted network access is trustworthy; this should be treated as concern, not evidence of a current Agents API escape.[24]

Independent InfoWorld analysis reaches a similar split: faster production deployment and fewer moving parts versus control-plane/model lock-in, lack of ZDR, US-only residency, and weaker fit for regulated or multi-model enterprises.[25]

## Recommended narrative spine for a 10–14 minute video

1. **Cold open:** “OpenAI did not launch another agent framework. It launched the managed operating layer behind Codex.”
2. **30-second architecture:** application → OpenAI harness/session → optional sandbox; emphasize that harness and sandbox are separate.
3. **Name decoder:** Responses vs Agents SDK vs Agents API vs AgentKit vs Codex.
4. **Show one-call quickstart:** create a durable session and stream work.
5. **Show what OpenAI actually owns:** compaction, recovery, subagents, tool loading, traces.
6. **Run the honest demo:** disconnect/reconnect or subagent comparison; report cost and tool success, not just final prose.
7. **Fine print:** beta, non-ZDR, US-only, best-effort usage, hosted-container pricing, default network access.
8. **Contrarian decision:** managed convenience is valuable, but “self-hosted sandbox” does not remove platform lock-in.
9. **Who should use it:** OpenAI-first SaaS teams needing long-running embedded agents.
10. **Who should wait/use SDK/self-host:** regulated data, model switching, custom deterministic control, long-lived platform state, or agent infrastructure as core IP.
11. **Close:** “The question is no longer whether agents need a harness. It is whether the harness should belong to your model vendor.”

## Title and thumbnail options

1. **OpenAI Just Turned Codex Into an API** — thumbnail: `CODEX → YOUR APP`
2. **The Agent Framework Era Is Over?** — thumbnail: `ONE API CALL`
3. **OpenAI’s Agents API: The Fine Print** — thumbnail: `NOT REALLY SELF-HOSTED`
4. **Responses vs Agents SDK vs Agents API** — thumbnail: `WHICH ONE?`
5. **Would I Replace My Self-Hosted Agent With This?** — thumbnail: `OPENAI vs HERMES`
6. **The Harness Is the Product Now** — thumbnail: `MODELS AREN’T ENOUGH`
7. **OpenAI Made Agent Infrastructure “Free”** — thumbnail: `$0*` with `*TOKENS + TOOLS + COMPUTE`

## Bottom-line assessment

**Fact:** Agents API is the highest-level and lowest-integration option in OpenAI’s agent stack, offering a managed Codex harness, durable sessions, compaction/recovery, tools, sandboxes, and subagents.[2][3]

**Interpretation:** It is a credible answer to the hardest undifferentiated parts of production agents and will be attractive to OpenAI-first product teams. Its strongest advantage—OpenAI owning and continuously tuning the stateful harness—is also its deepest risk: control-plane lock-in, opaque portability, and current data-governance limits. The strongest video is therefore not “agents are easy now,” but **“OpenAI has productized the harness; here is exactly what you gain, what you still build, and what you give up.”**

## Sources

[1] https://developers.openai.com/api/docs/guides/agents-api/overview — Agents API overview
[2] https://openai.com/index/introducing-the-agents-api — Introducing the Agents API
[3] https://developers.openai.com/api/docs/guides/agents-api/quickstart — Agents API quickstart
[9] https://developers.openai.com/api/docs/guides/agents-api/sessions/events — Events and items
[10] https://developers.openai.com/api/docs/guides/agents-api/tools/functions — Function tools
[11] https://developers.openai.com/api/docs/guides/agents-api/observability — Observability and usage
[14] https://developers.openai.com/api/docs/guides/agents-api/tools/mcp — MCP connections
[16] https://developers.openai.com/api/docs/guides/agents-api/sessions/manage — Manage sessions
[18] https://developers.openai.com/api/docs/guides/agents — OpenAI agents overview and runtime comparison
[19] https://developers.openai.com/api/docs/guides/migrate-to-responses — Migrate to the Responses API
