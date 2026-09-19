# Analysis, video 058: OpenAI Agents API on your own Mac

Built 2026-09-15 from `research/youtube/2026-09-15-openai-agents.md` (@researcher, same day). The research was not redone; this file adds the reference breakdown, two verification holes filled, the angle decision, and the sources. Read the research file for the full YouTube pull and the competitor table.

## Angle decision

| Option from research | Taken? | Why |
|---|---|---|
| 1. Self-host on your own Mac | **Yes, primary** | 0 of 14 videos do it. Docs say the environment "can be a laptop." Extends 057 (same viewer, same "your machine, your files" promise). Films from one build. |
| 3. "You don't need it" (Hermes does this) | Folded in as the closing beat, not the title | The comparison is the withheld payoff at 10:15. Titling on it would spend the search term on Hermes and read as a takedown. Kept as the day-7 B-test title. |
| 2. Three-runtime comparison | Not taken | Needs a real Claude Managed Agents run, adds a day. Parked as title option 3. |

Timing: launch 2026-09-10, package day 5. `packaging-rules.md` says do not cover a launch late. This is not a launch recap; it is a build nobody has filmed plus a comparison nobody has made, so it does not compete with the day-1 explainers or OpenAI's own 276k upload. Cut short (11 to 12 minutes) per the same rule.

## Reference breakdown: Bart Slodyczka, `transcript_JFWq93b4_Oo.txt`

"I Tested OpenAI's New Cloud Agents... What You Need To Know", 12:40, 16,207 views at 5 days (top English creator video on the API). Timestamps are estimated from transcript position across a 12:40 runtime; the transcript has no timecodes.

| Time (est.) | Segment | Purpose |
|---|---|---|
| 0:00 - 0:30 | "OpenAI have just released their agents API." Codex on your computer vs Codex in the cloud, 24/7. | Hook: contrast |
| 0:30 - 1:30 | The speed-to-lead scenario: form, email, research, proposal, calendar. Why cloud beats "only when you are at the computer." | Stakes, business framing |
| 1:30 - 2:30 | platform.openai.com. "Not included in your ChatGPT subscription", add a card, ten dollars of credit. | Setup, cost warning |
| 2:30 - 4:00 | Three concepts: agent, environment, session. Sessions have no memory between them, "that works out in our favor." | Teaching |
| 4:00 - 5:30 | Builds a test agent in the dashboard. Leaves it on Astra, "this is going to be super expensive." Creates an OpenAI-hosted environment. Starts a session, says hi. | Demo, dashboard |
| 5:30 - 7:00 | The "Build in Codex" button installs a ChatGPT plugin that manages the agent from a chat. Renames the agent from ChatGPT. | Demo, the undercovered path |
| 7:00 - 9:30 | Gives ChatGPT the brief plus an n8n MCP (Gmail, calendar list, create event). It writes the prompt and connects the MCP. Test run checks the calendar, drafts, does not send. | Build |
| 9:30 - 11:30 | Connects the form: n8n webhook adds one HTTP node that calls `sessions.create`. Notes that continuing a session from an email reply would need your own DB of session ids. Live test: email lands, slot is correct. | Build, close the loop |
| 11:30 - 12:40 | Second test as "Bob." "We just closed the loop." Comment for a deeper dive, contact details for business owners. | CTA |

### What works
- Opens on the contrast in sentence one: "on your computer" vs "in the cloud, 24/7." No warm-up.
- A business scenario the viewer can picture, then he builds exactly that scenario. The promise and the demo match.
- Honest about money early: "not included in your ChatGPT subscription", "add a billing card", "super expensive" on Astra.
- The "Build in Codex" plugin beat is the fastest on-camera path and nobody else shows it.
- Explains sessions with a ChatGPT analogy ("every new conversation is a new session") and then turns the limitation into a feature for his use case.
- Closes the loop with a second live test under a different name, so the viewer sees it was not staged.

### Weaknesses and gaps (our differentiation)
- OpenAI-hosted environment only. He clicks "keep it as OpenAI hosted" and moves on. Never mentions self-hosting exists.
- No cost numbers. Says "super expensive" and "ten dollars of credit" but never shows the container table or a real bill.
- Never touches the API from code directly. Everything goes through the dashboard, the ChatGPT plugin and n8n. A developer watching learns the product, not the API.
- No comparison to anything. Not Claude Code, not the Agents SDK, not a local agent.
- Session continuation is named as a gap ("we'd have to create a separate database") and left there. We show a second message to the same session in one line.
- Data residency and retention never come up. He is sending customer form data to it.
- Audience is business owners buying automation, not engineers. The CTA is "contact details in the first comment."

### Target audience and assumed level
His: agency and business owners, n8n users, low-code. Assumes you have a ChatGPT plan and have seen n8n.
Ours: developers who already use Claude Code or Codex, saw 057, and want to know whether this API is worth a slot in their stack. Assumes Python, an API key, a terminal. No beginner framing.

## Verification done in this pass (holes the research flagged)

| Claim | Status | Source |
|---|---|---|
| Claude Managed Agents $0.08 per session-hour | **Verified.** "Session runtime $0.08 per session-hour, `running` status duration." Tokens billed separately at model rates. | docs.anthropic.com/en/docs/about-claude/pricing, anthropic.com/pricing |
| `codex exec-server --remote <url> --environment-id <id>`, outbound only, reconnects | **Verified** against the self-hosted doc. Hosts: `api.openai.com` and `wss://codex-cloud-environments.chatgpt.com`. | developers.openai.com self-hosted page |
| Environment key: separate, restricted, all other permissions None, supplied as `CODEX_API_KEY` | **Verified**, same page. |
| `client.beta.agents.sessions.create(agent=..., environment={"type": "self_hosted", "workspace_directory": ...})` | **Verified**, same page (Python example). |
| Follow-up input: `sessions.events.create(session_id, events=[{"type": "agent.session.input.message", ...}])`; a message to an active turn steers it, to an idle session starts a new turn | **Verified**, "Run and continue sessions" doc. |
| Stream states `environment.pending` / `connected` / `failed` | **Verified**, self-hosted doc. |
| App key scopes `api.agents.read`, `api.agents.write`, `api.responses.write`; `OpenAI-Beta: agents=v1` header | **Verified**, quickstart. |
| The 10-minute self-host claim | **Still unverified.** Nothing has been run on this Mac. Title 1 uses "3 Steps" until the dry run produces a time. |
| That `exec-server` ships in the current `@openai/codex@alpha` npm build | **Unverified.** The doc says to install it; nobody on the team has confirmed the subcommand exists on the installed version. Dry run row 1. |
| Exact Python attribute path for `session.environment.remote_url` and the SDK stream method for an existing session | **Unverified.** Docs name the fields; the SDK object shape needs a look. Dry run rows 3 and 5. cURL fallback written. |
| Assistants API retirement 2026-08-26, GPT-Live-1 launch | Not used in the script. Still secondary-source only. |

## Dry run

Not yet done. Record here: date, `codex --version`, minutes from `npm install` to `index.md`, whether anything reconnected, local model tag used for section 8, and whether the local model completed the task.

## What the package deliberately does not do
- No launch recap. Day 5, OpenAI's own 2:18 has 276k.
- No dashboard walkthrough, no "Build in Codex" plugin, no n8n. That is Bart's video and it is good. Shorts candidate only.
- No animated harness explainer. Mathify and Ben BK own that.
- No takedown of OpenAI. The closing table gives the API a real column.

## Shorts (from the research, wide open: 0 shorts on the term in the window)
1. The one command: `codex exec-server` connecting, pending to connected, 30 seconds.
2. The one line that creates an agent: `sessions.create` with `self_hosted`.
3. "It kept the session alive": task 2 updating the file the API wrote in task 1.
4. The cost card: container table, then "or run it here for zero."

## Sources
Research (read first, not redone):
- `research/youtube/2026-09-15-openai-agents.md`
- Raw pulls: `research/2026-09-15-agents-api.{md,json}`, `research/2026-09-15-openai-agents.{md,json}`, `research/2026-09-15-openai-agents-api.{md,json}`, `research/2026-09-15-codex-harness.{md,json}`
- Transcripts: `transcripts/transcript_JFWq93b4_Oo.txt` (Bart, reference), `transcript_2YHa1vhnmK0.txt` (OpenAI launch), `transcript_lHSn7InuflY.txt` (Mathify), `transcript_k_xeuLIwwfQ.txt` (Ben BK), `transcript_Wn-JBHohRYI.txt` (QuantBrasil)

OpenAI (fetched 2026-09-15 in this pass):
- https://openai.com/index/introducing-the-agents-api/
- https://developers.openai.com/api/docs/guides/agents-api/overview
- https://developers.openai.com/api/docs/guides/agents-api/quickstart
- https://developers.openai.com/api/docs/guides/agents-api/sessions
- https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted
- https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted
- https://developers.openai.com/api/docs/pricing (Containers)
- https://community.openai.com/t/introducing-the-agents-api-and-hosted-sandboxes/1396481
- https://github.com/openai/codex

Anthropic (fetched 2026-09-15 in this pass):
- https://docs.anthropic.com/en/docs/about-claude/pricing (Claude Managed Agents, session runtime $0.08/hour)
- https://www.anthropic.com/pricing

Partner guides seen (not used in script):
- https://www.daytona.io/docs/en/guides/openai/openai-agents-api-self-hosted-sandbox/
- https://developers.cloudflare.com/sandbox/tutorials/openai-agents-api/
