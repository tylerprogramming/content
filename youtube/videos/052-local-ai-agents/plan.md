# 052 - 100% Local AI Agents (2026 Remake) - Plan

## What this is
A 2026 remake of Tyler's own video "100% LOCAL AI Agents with CrewAI and Ollama"
(25,276 views, published 2024-07, 9:06). The privacy + free + no-API-cost angle still
sells hard; the CrewAI-era tooling is dated. This rebuilds the same promise with current
local models and the current way agents get tools.

## Original stats + what worked
- 25,276 views, 9:06, strong evergreen performer for the channel.
- The winning hook was never CrewAI. It was three words: local, private, free.
  - Local = it runs on your machine, works offline.
  - Private = your data never leaves the laptop (no company file goes to a chatbot).
  - Free = no API keys, no per-token bill, no subscription.
- That demand is still climbing in 2026 (compliance pressure, API-cost fatigue, and a
  widely cited stat that most employees have pasted sensitive company data into personal
  chatbot accounts). See research below.

## What has changed for 2026 (why the remake, tooling-wise)
1. **The model.** In 2024 the local models that could actually call tools were rough.
   In 2026 Qwen3 (Alibaba) is the stable pick for local tool-calling. Qwen3 8B fits in
   ~8GB and calls tools reliably; the 30B-A3B MoE (activates ~3B params) is the sweet spot
   on 16-24GB. gpt-oss 20B and Llama 3.3 are the other common picks.
2. **Ollama grew up.** Ollama now has a native tool-calling API (the same
   function-calling primitive as the big providers), so the model can actually run tools,
   not just chat. This is the piece that was missing in the CrewAI-era video.
3. **The agent approach.** CrewAI's custom per-tool wiring is the dated part. The 2026
   way to give a local agent tools is MCP (Model Context Protocol) - the open standard.
   You define a tool once as an MCP server (filesystem, fetch, a database) and any model
   discovers and calls it, no glue code per model. Qwen3 was trained and evaluated on
   MCP-style agentic tasks, so it pairs cleanly with Ollama.
4. **Framework is optional now.** The remake shows the honest 2026 version: you do NOT
   need a heavy framework to have an agent. Ollama's tool loop + one MCP server is a real
   agent in ~40 lines of Python. (We can name LangGraph/CrewAI as the "if you want more"
   option, but the core build is deliberately minimal.)

## The exact agent we build on screen
**A local file agent.** Point it at a folder of messy documents (notes, receipts, meeting
dumps) and it reads them, pulls out what matters, and writes a clean summary file back to
disk. Everything runs on the laptop.

- **Model:** Qwen3 8B via Ollama (`ollama pull qwen3`). Mention the 30B-A3B upgrade path.
- **Tools:** a filesystem MCP server (read the folder, write the summary). Optionally a
  second read-only tool so the loop is clearly multi-step.
- **Code:** ~40 lines of Python. Ollama tool-calling loop + MCP client. No API key anywhere.
- **The proof beat (open loop):** partway in, Tyler turns off the wifi and the agent keeps
  running. That single moment proves local + private in a way words cannot. Plant it in
  the hook, pay it off in the demo.
- **Task chosen for the privacy angle on purpose:** the folder is the kind of thing you'd
  never paste into a chatbot (personal/work files). That is the whole point.

## The privacy / free angle (the spine)
- Private: unplug the internet, it still works. Your files never leave the machine.
- Free: no API keys, no per-token cost, no monthly bill. You already own the hardware.
- Local: runs on a normal laptop with Ollama, one model pull, done.
- Honest limits (voice): a local 8B model is not GPT-class. It is 70-80% there and you
  nudge it. For private, repetitive file work on your own machine, that is plenty.

## Target audience
- Developers and technical folks who want agents but can't send data to a cloud API
  (work compliance, client data, source code).
- AI-curious people tired of API bills who want to run things for free on their own machine.
- Anyone who did the CrewAI version and wants the current, simpler 2026 build.

## Angle vs the original
- Same promise (100% local, private, free agents), current stack.
- Old: CrewAI + a weak local model, lots of framework glue.
- New: Ollama native tool-calling + Qwen3 + one MCP server, ~40 lines, framework optional.
- Delayed credibility per voice rules: Tyler is a software engineer (8 yrs, IBM, Chase,
  now Pfizer). That comes in late, as the reason he cares about data staying on the machine,
  never as "I'm an expert." Subject stays: using AI to take repetitive file work off your plate.

## Research notes (2026 state, from web search 2026-08-17)
- Qwen3 = most stable local tool-calling series; Qwen3 8B the mid-range default, 30B-A3B
  MoE the 16-24GB sweet spot; gpt-oss 20B the 16GB consensus; Llama 3.3 also supported.
- Ollama native tool-calling API is production-ready for local agent workloads in 2026.
- MCP (Anthropic's open standard) is the 2026 way to give agents tools; define once, any
  model calls it. Qwen-Agent + Ollama both support MCP.
- Privacy driver: survey cited that ~63% of employees who used AI in 2025 pasted sensitive
  company data (including source code) into personal chatbot accounts.
- Sources: localaimaster.com (Ollama models for agents / tool calling / build guide),
  whatllm.org best Ollama models, kdnuggets Qwen3 + MCP, QwenLM/Qwen-Agent (GitHub),
  Ollama tool-calling docs.
