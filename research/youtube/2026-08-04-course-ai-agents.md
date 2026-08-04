# Course: Build AI Agents (Standalone) - Outline

**Type:** Course OUTLINE (structure only, not a script)
**Compiled:** 2026-08-04 (expanded from the ~88 min v1 to a full 2+ hour course)
**Target runtime:** ~2:20:00 (140 min), intro + 20 lessons + outro
**Audience:** People who already use an AI chat tool and keep hearing "agents" but have never built one. Business owners, creators, operators, and technically-curious beginners. No framework experience assumed. Tyler is a software engineer, so the promise is honest: "I build the heavy production version at a Fortune 500, and I am going to show you the version anyone can start today, then take you all the way to the frameworks and the paid-service version, and be straight about where it breaks."
**Stance:** Broadly useful and vendor-neutral on the concepts (a model in a loop with tools and a goal works anywhere). Concrete demos use Claude / Claude Code for the agent and Arcade for tools + auth, because that is Tyler's stack. Say once, early: the shape is the same on any model or runtime; we are just picking one to make it real. The frameworks lesson (L16) shows the same agent in Pydantic AI, LangGraph, and the Claude Agent SDK so the concepts stay portable.
**Voice/rules:** no em dashes, no money amounts in titles, no hype words (insane, crazy, game-changer, magic), drafts before sends, show real runs, admit limits. Honest over impressive. Tyler is a software engineer (8 yrs, IBM/Chase, now AI engineer at Pfizer) - never imply otherwise. The Fortune-500 line is authority, not a flex; use it sparingly.

**Format note (say this early):** film it LESSON BY LESSON, each with its own screen recording, stitched with chapter cards. Chapters go in the description so viewers can jump to any lesson. Do not attempt one pass. This is a long course; the chapter list is the navigation.

**Disclosure:** if the Arcade portion is sponsored/partner, say so on camera in the tools lesson (L4) and in the description.

---

## By the end of this course you can...

- Explain what an AI agent actually is in one sentence: a model running in a loop, with tools and a goal, deciding its own steps, versus a single prompt that just answers once.
- Decide honestly when a task is worth an agent and when a plain prompt or a script is the better call.
- Describe the agent loop in detail (plan, act, observe, decide) and how planning changes an agent's behavior.
- Build your first working agent with no code: one plain-English instructions file plus one tool.
- Give an agent real tools over MCP, and understand why auth (OAuth, tokens, scopes) is the real wall, with Arcade as the fix.
- Design good tools for an agent (clear names, tight inputs, honest errors) and know why bad tools cause most agent failures.
- Give an agent memory: short-term (the current run) versus long-term (an instructions/memory file it reads every time), and know when each matters.
- Test an agent: make it verify its own work, write simple evals, and catch failures before they reach a user.
- Build eight complete agents start to finish: research-brief, morning-brief, inbox triage, a research assistant that saves an artifact, repo triage to a ClickUp task, a content-repurposing agent, a customer-support/FAQ agent, and a scheduled monitoring agent.
- Rebuild one of your agents in a real framework (Pydantic AI, LangGraph, or the Claude Agent SDK) and know which to reach for.
- Decide when multiple agents help and when a single agent is simpler and better.
- Name where agents fail, tell real failure stories, and put real guardrails on them: approval, reversibility, logging, and cost control.
- Deploy an agent: put it on a schedule, monitor it, and control cost as a first-class concern.
- Understand what it takes to run an agent as a paid service: scoping, pricing, delivering, and maintaining it.

---

## The running timeline (sums to ~2:20:00)

| Time | Section | Min |
|---|---|---|
| 0:00 | INTRO | 4 |
| 0:04 | L1 - Who this is for + what an agent actually is | 6 |
| 0:10 | L2 - When you should and should NOT build an agent | 5 |
| 0:15 | L3 - The agent loop in detail (plan, act, observe, decide) | 7 |
| 0:22 | L4 - Tools, MCP, and the auth problem | 8 |
| 0:30 | L5 - Tool design: giving an agent good tools | 5 |
| 0:35 | L6 - Memory: short-term vs long-term | 6 |
| 0:41 | L7 - Self-verification and evals: how to test an agent | 8 |
| 0:49 | L8 - Agent 1: build your first agent, no code (research-brief) | 7 |
| 0:56 | L9 - Agent 2: the morning-brief agent, end to end | 11 |
| 1:07 | L10 - Agent 3: inbox triage | 5 |
| 1:12 | L11 - Agent 4: research assistant that saves an artifact | 5 |
| 1:17 | L12 - Agent 5: repo triage to a ClickUp task | 6 |
| 1:23 | L13 - Agent 6: content-repurposing agent | 6 |
| 1:29 | L14 - Agent 7: customer-support / FAQ agent | 5 |
| 1:34 | L15 - Agent 8: scheduled monitoring agent | 5 |
| 1:39 | L16 - Frameworks with hands-on (Pydantic AI, LangGraph, Claude Agent SDK, Arcade) | 8 |
| 1:47 | L17 - Multi-agent and orchestration: when it helps, when it hurts | 7 |
| 1:54 | L18 - Where agents fail and how to keep them safe | 7 |
| 2:01 | L19 - Deploy, schedule, monitor, control cost | 7 |
| 2:08 | L20 - Running an agent as a paid service | 7 |
| 2:15 | OUTRO | 5 |
| 2:20 | END | |

---

# INTRO (0:00 - 0:04) ~4 min

**By the end of the intro you can:** say what you are going to build and why this course refuses to hype it.

### Cold open + what you will build (0:00, 4 min)
Open on a result, not a channel intro: the finished morning-brief agent already on screen (the day laid out, three emails flagged, three drafts sitting ready). One line on who is teaching (software engineer by day, builds this heavy version at a Fortune 500, runs a channel and community, uses this daily). Lay out the real deliverables plainly: your first no-code agent, eight complete agents you can copy, the same agent rebuilt in a real framework, and the deploy + cost + paid-service layer most tutorials never reach. Promise every step on camera, nothing faked, and an honest limits lesson you will not skip. State the vendor-neutral frame once: the concepts work on any model; the demos use Claude and Arcade because that is the stack. This is long on purpose; the chapters let you jump.
- **Reuse:** cold-open "result first" beat from `046-arcade-build-agent/script.md` [0:00-0:15]; the "I built the heavy version, here is the easy one" framing from `038-build-first-ai-agent/script.md` cold open.

---

# L1 - WHO THIS IS FOR + WHAT AN AGENT ACTUALLY IS (0:04 - 0:10) ~6 min

**By the end you can:** define an agent as a model in a loop with tools and a goal, and tell it apart from a single prompt.

### 1.1 Who this is for and the one definition (0:04, 6 min)
Kill the intimidation first. Who this is for: you use AI chat, you keep hearing "agent," you do not want a computer science degree to start. The definition that anchors the whole course: an agent is a model running in a loop, with a goal and tools, deciding its own next step until the goal is met. Contrast it hard with a single prompt: a prompt answers once and stops; an agent has a job, takes an action, reads the result, and decides what to do next. Use the three-part graphic (goal / tool / plain English) as the visual, then add the fourth idea that makes it an agent: the loop. Earned authority once: Tyler built the production version at big companies, and none of it is required to start.
- **Reuse:** direct from `038/script.md` [0:20-1:30] (the three-part graphic and the "chatbot talks back, an agent has a job" reframe). Add the explicit "model in a loop" line, which is new and is the spine of this standalone course.

---

# L2 - WHEN YOU SHOULD AND SHOULD NOT BUILD AN AGENT (0:10 - 0:15) ~5 min

**By the end you can:** decide honestly whether a task deserves an agent, a plain prompt, or a plain script.

### 2.1 The build-or-skip decision (0:10, 5 min)
The lesson most agent content skips. Build an agent when the task is multi-step, needs to reach into real tools or data, and changes each time so a fixed script cannot cover it (triage my inbox, research this topic, brief me on my day). Do NOT build an agent when a single prompt already answers it (rewrite this paragraph), or when the steps never change and a plain script or automation is cheaper and more reliable (rename these files by a fixed rule). The honest cost frame: an agent is more moving parts, more tokens, and more ways to be wrong, so it has to earn the complexity. Rule of thumb on screen: same steps every time, use a script; judgment needed every time, use an agent; one answer needed, use a prompt.
- **Task (PROJECT 1):** write down one task you do weekly and label it script, prompt, or agent using the rule of thumb. You will build the agent version later.
- **Reuse:** new, but rhymes with the "Cowork vs Code vs Chat, when to use which" decision-rule beat in the mega-course `2026-08-04-claude-mega-course-outline.md` (2.8). Frame it as decision discipline, which is on-brand honesty.

---

# L3 - THE AGENT LOOP IN DETAIL (0:15 - 0:22) ~7 min

**By the end you can:** describe the loop step by step and explain how planning changes what an agent does.

### 3.1 Plan, act, observe, decide (0:15, 7 min)
Slow the loop down and make it concrete, still visual, not a lecture. Walk the four beats on a diagram, then narrate them over a real run later: PLAN (the agent reads the goal and sketches the steps it thinks it needs), ACT (it picks one tool and calls it), OBSERVE (it reads the result, including errors), DECIDE (goal met, or take another step). Show why the loop is the whole point: a prompt does one pass; an agent re-plans when a step fails. Teach planning explicitly: some agents plan the whole thing up front, some plan one step at a time, and most good ones do a light plan then adjust as they observe. Honest note: more loop steps means more tokens and more chances to drift, so a tight goal and few tools keep the loop short. This lesson is the mental model every build later leans on.
- **Task:** on paper, write the plan-act-observe-decide loop for your weekly task from L2. What tool does step one call? What does it observe? When does it stop?
- **Reuse:** new footage; sets up the narration you will reuse over the live runs in L8 and L9. Rhymes with the "nudge is the loop, not a failure" beat from `038/script.md`.

---

# L4 - TOOLS, MCP, AND THE AUTH PROBLEM (0:22 - 0:30) ~8 min

**By the end you can:** give an agent real tools over MCP and explain why auth is the actual hard part, with Arcade as the fix.

### 4.1 Tools + MCP + why auth is the wall (0:22, 8 min)
An agent is only as capable as its tools, and the wall everyone hits is not the tools, it is the permission to use them: OAuth, tokens, scopes. Explain MCP in one line (a standard way to plug an agent into external tools and data instead of copy-pasting). Then show the fix on camera: Arcade is an MCP runtime that does per-user OAuth for you, thousands of prebuilt tools (Gmail, Calendar, Slack, GitHub), so you authorize once per tool and it manages the tokens. Build a Gateway (a bundle of tools behind one URL), then connect it to Claude Code in one line: `claude mcp add arcade --transport http "<GATEWAY_URL>"`, verify with `claude mcp list`, trigger the OAuth authorize once. Say the honest part: the authorize popup is the good kind of friction, it means your token is not hardcoded and every action is logged. Vendor-neutral note: any MCP tool works here; Arcade just removes the auth plumbing. Note free vs paid tiers honestly.
- **Task (PROJECT 2):** build a two-tool Gateway (Gmail + Calendar), connect it to Claude Code, and clear the OAuth authorize.
- **Reuse:** direct from `046/script.md` [0:15-2:30] (the "tools + auth, auth is the hard part" framing, the Arcade one-liner, the OAuth-is-good-friction beat) and `2026-08-02-arcade-mcp-course-outline.md` Modules 1-2 (Gateway build + connect). Disclosure if sponsored.

---

# L5 - TOOL DESIGN: GIVING AN AGENT GOOD TOOLS (0:30 - 0:35) ~5 min

**By the end you can:** tell a good tool from a bad one and understand why most agent failures are really tool failures.

### 5.1 The tools make or break the agent (0:30, 5 min)
Most "the agent is dumb" moments are actually bad tools. Teach the traits of a tool an agent can use well, vendor-neutral: a clear name that says what it does, a tight and obvious set of inputs (fewer, well-named parameters beat many fuzzy ones), a description written for the model like you would brief a new hire, and honest errors (a tool that returns "no results found" teaches the agent; a tool that returns an empty success lies to it). Contrast a vague tool (`do_stuff(query)`) with a clear one (`search_unread_email(since, from_sender)`). Show it on the Arcade tools already connected: point out how prebuilt tools are named and scoped, and why that is half the reason they just work. Honest note: when you build your own tool later, this is the difference between an agent that recovers and one that spins.
- **Task:** look at the tools in your Gateway and write a one-line "brief" for one of them, as if onboarding a new assistant. Note anything ambiguous.
- **Reuse:** new footage; leans on Tyler's software-engineer credibility (he has designed real integrations). Rhymes with the "clear instructions like a new assistant" beat from `038/script.md`.

---

# L6 - MEMORY: SHORT-TERM VS LONG-TERM (0:35 - 0:41) ~6 min

**By the end you can:** explain the two kinds of agent memory and give an agent long-term memory it reads every run.

### 6.1 What the agent remembers, and for how long (0:35, 6 min)
Two kinds, kept plain. SHORT-TERM memory is the current run: the context window, what it has seen and done this session; it disappears when the run ends. LONG-TERM memory is what survives across runs: an instructions/memory file the agent reads every time, plus the corrections you have taught it, so tomorrow's morning brief does not start from zero. Show the pattern live: a plain-English memory file (who you are, your voice, standing rules like "skip newsletters," things you corrected last time) that the agent loads at the top of every run. Say the honest limits: long context is not free (more tokens, and the model can lose the thread in a very long run), so keep the memory file tight and specific, not a dumping ground. Tie it back: this is the same instructions-file pattern that made the L8 agent work, now named and used on purpose.
- **Task (PROJECT 3):** write a short memory file for your future morning-brief agent: your name, your reply voice, and two standing rules.
- **Reuse:** new footage; the memory idea maps directly to the CLAUDE.md-as-instructions pattern used across Tyler's Cowork/Code material (`023`, `040`). Reinforces the "instructions, not code" beat from `038`.

---

# L7 - SELF-VERIFICATION AND EVALS: HOW TO TEST AN AGENT (0:41 - 0:49) ~8 min

**By the end you can:** make an agent check its own work and write simple evals so you catch failures before a user does.

### 7.1 Make it check itself, then test it like software (0:41, 8 min)
The lesson that separates a demo from something you would rely on. Two layers. First, self-verification: tell the agent to check its own output against the sources or the goal before it declares done, and to flag what it is unsure about ("before you finish, check every claim against a source and list anything you could not verify"). Show it live on the research agent and watch it self-correct. Second, evals, kept beginner-friendly: an eval is just a saved test case with a known-good answer. Write three by hand (a normal case, an edge case, a "should refuse" case), run the agent against them, and check the output yourself. Explain why this matters more for agents than for prompts: an agent takes actions, so a silent wrong step is worse than a wrong sentence. Honest framing: you are not building a lab, you are building a habit of testing the same handful of cases every time you change the agent. This is how you catch drift before it reaches your inbox or a client's.
- **Task (PROJECT 4):** add a self-check line to your research agent, then write 3 evals (normal, edge, should-refuse) and run them.
- **Reuse:** new footage; extends the "nudge" rhythm from `038` into deliberate testing. The self-check beat was L5 in v1, now expanded with evals. This lesson is the backbone of the "agents fail" honesty later.

---

# L8 - AGENT 1: BUILD YOUR FIRST AGENT, NO CODE (0:49 - 0:56) ~7 min

**By the end you can:** build and run a real agent from one plain-English instructions file and one tool.

### 8.1 The research-brief agent, live (0:49, 7 min)
Build ONE real agent on camera, no frameworks, no code: a research agent (topic in, real web research, one-page sourced brief out). Make a folder, write ONE plain-English instructions file (who it is, what to do, and the non-negotiable line "if you are not sure, say so, do not make things up"), turn on the one tool it needs (web search), run it on a real relatable topic, then nudge it (it gets you 80-90 percent, you steer the rest). Land the teaching beats: you wrote instructions, not code; one tool on is the difference between a chatbot and an agent; the nudge is the normal rhythm, not a failure. Narrate the plan-act-observe-decide loop from L3 as it runs, so the concept becomes visible.
- **Task (PROJECT 5):** build and run the research-brief agent, then nudge it once to prove the loop.
- **Reuse:** direct from `038/script.md` [1:30-8:00], the full live build, including the "notice I wrote instructions like a new assistant on day one" beat and the honest nudge. Copy-pack for this agent already exists. Trimmed from 11 min in v1 because L3/L5/L6/L7 now carry the concepts this build used to teach inline.

---

# L9 - AGENT 2: THE MORNING-BRIEF AGENT, END TO END (0:56 - 1:07) ~11 min

**By the end you can:** ship a real agent that reads your Calendar and Gmail, summarizes your day, flags what needs a reply, and drafts those replies without sending.

### 9.1 The morning-brief agent, start to finish (0:56, 11 min)
The flagship build, with a visible timer so the segment doubles as a short. Using the Gateway from L4 (Gmail + Calendar) and the memory file from L6, write the agent as one plain-English prompt: read today's calendar and give a time-ordered rundown; read unread Gmail from the last 24 hours; tell me which actually need a reply and why (skip newsletters, receipts, notifications); draft a short reply in my voice for each and save it as a Gmail draft, never send; show me the summary and reply list first, and ask if unsure. Run it live on the real inbox and calendar, narrate the loop (it calls Calendar, then Gmail, then decides what matters), open the real drafts, read one aloud. The core honesty beat of the whole course: drafts before sends, always, you hit send yourself. If the live run flags a wrong email or writes a stiff draft, keep it and narrate the fix.
- **Task (PROJECT 6):** build and run the morning-brief agent; confirm drafts land in Gmail and nothing is sent.
- **Reuse:** direct from `046/script.md` [2:30-8:00], this is exactly that agent and prompt. Shoot once, cut the timed short from it. Keep the "drafts, do not send, ask if unsure" line verbatim.

---

# L10 - AGENT 3: INBOX TRIAGE (1:07 - 1:12) ~5 min

**By the end you can:** build a focused agent that sorts unread mail into what needs you versus noise, and drafts the replies.

### 10.1 Inbox triage + draft, start to finish (1:07, 5 min)
Same shape, narrower job than the morning brief: no calendar, just the inbox, done well. Write the agent: read unread from the last day, sort into "needs a reply from me" versus "noise" (newsletters, receipts, notifications, FYIs), for each that needs you say why in one line, then draft a reply in my voice and save it as a draft. Run it live, show the sorted list, open two drafts. Point out the design choice out loud: one tool (Gmail), one job, which makes it reliable and cheap to run daily. Honest beat: it will mis-sort sometimes; the sorted list is there so you catch that in five seconds before any draft matters.
- **Task (PROJECT 7):** build the inbox-triage agent and run it on your real unread; check the sort before the drafts.
- **Reuse:** the "same three parts, change the goal and the tool" beat from `038/script.md` [8:00-9:15]; inbox-triage example from `2026-08-02-arcade-mcp-course-outline.md` (walkthrough 2) and `2026-08-02-arcade-mcp-claude-code.md` demo ideas.

---

# L11 - AGENT 4: RESEARCH ASSISTANT THAT SAVES AN ARTIFACT (1:12 - 1:17) ~5 min

**By the end you can:** level up the L8 research agent so it produces a saved artifact you keep, not just chat output.

### 11.1 Research assistant, leveled up (1:12, 5 min)
Take the research-brief agent from L8 and add one thing that makes it real work: a save step. Instead of printing the brief into the chat, the agent writes it to a file or a Google Doc (via the Drive/Docs tool in the Gateway), named and dated, with sources listed. Run it live, open the saved doc. Teach the small but important idea: an artifact the agent produces and stores is the difference between "I asked it a question" and "it did a job and left me something." Keep the self-verification line from L7 in the prompt so the saved brief flags anything unverified. Honest beat: a saved wrong answer is still a wrong answer, which is exactly why the verify step rides along.
- **Task (PROJECT 8):** add a save-to-doc step to your research agent so every run leaves a dated, sourced artifact.
- **Reuse:** builds directly on PROJECT 5 (L8) and the self-check from L7; the "produce an artifact you keep" beat is the leveled-up research assistant from v1's L7 list, now its own build. Web search + Drive/Docs tool via Arcade.

---

# L12 - AGENT 5: REPO TRIAGE TO A CLICKUP TASK (1:17 - 1:23) ~6 min

**By the end you can:** build an agent that reads open GitHub issues/PRs and files the most important one as a real task.

### 12.1 Repo triage that ends in a task (1:17, 6 min)
An agent that ends in an action in a second system, which is where agents start to feel like leverage. Write it: read the open issues and PRs in a repo, summarize them, pick the one that matters most and say why, then create a task for it in ClickUp with a clear title and a short description. Run it live, show the summary, show the created task. Note the tool reality honestly: GitHub is in Arcade's catalog; if ClickUp is not, use Tyler's existing ClickUp MCP connector alongside Arcade in Claude Code, and the demo still works. Teach the pattern: read from one tool, decide, write to another; that read-decide-write shape is most useful agents. Honest beat: the agent's "most important" is a judgment call, so the summary is shown first and you can override which one it files.
- **Task (PROJECT 9):** build the repo-triage agent and have it file the top issue as a ClickUp task; review before it creates.
- **Reuse:** the repo-to-task example from `2026-08-02-arcade-mcp-course-outline.md` (walkthrough 3, incl. the documented ClickUp-MCP fallback) and `2026-08-02-arcade-mcp-claude-code.md` demo ideas. Same shape as L10, new tools.

---

# L13 - AGENT 6: CONTENT-REPURPOSING AGENT (1:23 - 1:29) ~6 min

**By the end you can:** build an agent that turns one piece of content into platform-ready drafts, in your voice, saved not posted.

### 13.1 One input, many drafts (1:23, 6 min)
A creator/operator agent that mirrors real work: take a source (a transcript, a doc, a published video) and produce drafts for other platforms (an X post, a LinkedIn post, three short-form hooks), each in your voice, using the memory file from L6 so the voice is consistent. The agent reads the source (file/Drive tool), drafts each piece, and saves them to a doc or folder; it does NOT post. Run it live on a real transcript, open the drafts, read one. Teach the honesty beat hard here because it is tempting to automate posting: drafts before publish, you approve and post yourself, because your name is on it. Note the voice-consistency win from long-term memory, and the failure mode: without a tight voice file it drifts into generic AI copy, which you would catch on review.
- **Task (PROJECT 10):** build the repurposing agent on one real piece of content; generate drafts for two platforms, saved not posted.
- **Reuse:** new footage, but leans on Tyler's existing `/repurpose` and `/social-copy` skill logic (source in, platform drafts out, voice-consistent, never auto-post). The "drafts before publish" beat matches the channel's standing rule. Voice file from L6.

---

# L14 - AGENT 7: CUSTOMER-SUPPORT / FAQ AGENT (1:29 - 1:34) ~5 min

**By the end you can:** build a support agent that answers from YOUR docs and refuses to guess when the answer is not there.

### 14.1 The support agent that says "I do not know" (1:29, 5 min)
The agent most small businesses actually want, built honestly. Give it a source of truth (a FAQ doc, a help folder, product docs via the Drive/Docs tool), and one rule that matters more than any other: answer only from these documents, and if the answer is not there, say so and hand off to a human, do not invent an answer. Run it live: ask it a question the docs cover (good answer with a citation), then a question they do not cover (watch it refuse and escalate instead of guessing). Draft the reply, do not auto-send to the customer. Teach why this is the whole game for support: a confident wrong answer to a customer is worse than no answer, so grounding plus refusal plus a draft-first handoff is the safe shape. This is where the evals from L7 pay off: your "should refuse" test case is a real support scenario.
- **Task (PROJECT 11):** build the FAQ agent over your own docs; prove it answers in-scope and refuses out-of-scope.
- **Reuse:** new footage; reuses the "answer only from the source, refuse otherwise" grounding rule and the draft-first handoff. Ties directly to L7's should-refuse eval and L5's honest-errors idea. Good candidate for the paid-service lesson (L20).

---

# L15 - AGENT 8: SCHEDULED MONITORING AGENT (1:34 - 1:39) ~5 min

**By the end you can:** build an agent that watches something on a schedule and only pings you when something actually changed.

### 15.1 The agent that watches so you do not have to (1:34, 5 min)
A monitoring agent: pick something worth watching (a competitor's new uploads, a keyword in the news, a channel's stats, a folder for new files) and have the agent check it, compare against what it saw last time, and report ONLY when something meaningful changed, otherwise stay quiet. Build it manually first and run it once live. The "compare against last time" part is long-term memory from L6 in action (it stores what it saw so it can diff). Teach the discipline that makes monitors useful instead of noise: define "meaningful change" tightly, or you train yourself to ignore it. Honest beat: this one is built to run unattended, which raises the stakes, so it only reports and drafts, it does not act on its own. This build sets up the scheduling lesson (L19), where you actually put it on a timer.
- **Task (PROJECT 12):** build the monitoring agent and run it twice manually to prove the "only ping on real change" behavior.
- **Reuse:** the "runs while I am not here" monitors from `040/script.md` [6:30-9:30] as a real example; the diff-against-memory idea from L6. Sets up L19.

---

# L16 - FRAMEWORKS WITH HANDS-ON (1:39 - 1:47) ~8 min

**By the end you can:** rebuild one of your agents in a real framework and know which to reach for and why.

### 16.1 Pydantic AI, LangGraph, the Claude Agent SDK, and Arcade (1:39, 8 min)
Move from no-code to code without losing the thread: the concepts are identical, a framework just gives you structure, types, and control. Keep it vendor-neutral on ideas, concrete on a few. Show the same simple agent (the research-brief) sketched in each so the shape stays recognizable:
- **Pydantic AI:** define the agent, its tools as typed Python functions, and a structured output, and let it run the loop. Good when you want typed inputs/outputs and to stay close to plain Python.
- **LangGraph:** model the agent as a graph of steps with explicit state and branches. Good when the flow is complex, has loops and conditions you want to see, or you need fine control over the path.
- **Claude Agent SDK:** the first-party way to build a Claude agent in code, with the loop, tools, and permissions handled for you. Good when you are building on Claude specifically and want the batteries included. (Read the `claude-api` reference before writing any Claude-specific code or naming models.)
- **Arcade:** not a competing framework, it is the tools + auth layer that plugs into any of them, so your typed agent still gets per-user OAuth and the prebuilt catalog. This is why the earlier lessons carry over.
Hands-on: take ONE of your working agents and rebuild the core in Pydantic AI (or the Claude Agent SDK) on camera, keeping the same instructions and the same one tool, so the viewer sees "same agent, now in code." Honest framing: frameworks add power and add moving parts; start no-code, move to a framework when you need types, tests, version control, or to hand it to another engineer.
- **Task (PROJECT 13):** rebuild one of your agents in Pydantic AI or the Claude Agent SDK, same instructions, same tool; run it once.
- **Reuse:** new footage. Load `claude-api` skill before writing any Claude Agent SDK code. Keep the research-brief instructions identical to L8 so the "same agent" point is visual. Disclosure carries from L4 if Arcade portion is sponsored.

---

# L17 - MULTI-AGENT AND ORCHESTRATION (1:47 - 1:54) ~7 min

**By the end you can:** decide when multiple agents actually help and when one agent is simpler and better.

### 17.1 When more agents help, and when they hurt (1:47, 7 min)
The honest take on the shiniest topic in the space. What multi-agent means: instead of one agent doing everything, an orchestrator hands parts of a job to specialized agents (a researcher, a writer, a checker) and combines the results. When it genuinely helps: the job has clearly separate skills or sources, the parts can run in parallel, or one agent's context would get too crowded doing all of it. When it hurts, and this is the part most videos skip: more agents means more tokens, more coordination bugs, more places to fail, and slower runs; two agents passing bad context to each other is worse than one focused agent. Show a simple, real orchestration (a research agent produces a brief, a writer agent turns it into a draft, a checker agent verifies claims) and then say plainly that for most tasks in this course, one well-scoped agent beats a swarm. Rule of thumb on screen: reach for multiple agents when a single agent is failing because the job is genuinely several jobs, not because more agents sounds impressive.
- **Task:** take one of your agents and write down whether splitting it into two agents would help or just add cost; justify the call.
- **Reuse:** new footage; leans on Tyler's software-engineer instinct for "simplest thing that works." Uses the research-then-write-then-check chain from L11/L13 as the concrete example so no new agents are needed.

---

# L18 - WHERE AGENTS FAIL AND HOW TO KEEP THEM SAFE (1:54 - 2:01) ~7 min

**By the end you can:** name how agents fail, tell real failure stories, and put real guardrails on one.

### 18.1 The trust lesson, do not skip (1:54, 7 min)
The beat that earns the whole course. Tell real, specific failure stories (kept honest, no drama): the research agent that cited a source that did not say what it claimed and how the L7 self-check caught it; the triage agent that buried a real email in "noise" and why the sorted-list-first design saved it; the kind of runaway loop where an agent keeps calling a tool because it never gets the result it expects, quietly burning tokens. Name the failure modes plainly: weak sources, missed nuance, confident wrong answers, doing the wrong thing quickly at scale, and looping without progress. Then the guardrails, concretely:
- **Approval:** drafts before sends, and a human check on anything irreversible or public.
- **Reversibility:** prefer actions you can undo; keep the agent narrow (one job, few tools) until it earns more.
- **Logging + auth:** per-user OAuth so tokens are never hardcoded, every action logged so you can see what it did.
- **Limits:** cap the loop and the scope so a stuck agent stops instead of spinning; a runaway loop is a real failure mode, not a hypothetical.
State plainly what you never let an agent do unattended: send, pay, publish, or delete without a human in the loop.
- **Reuse:** direct from `038/script.md` [9:15-10:30] (honest limitations, "leverage not magic") and the safety rules from `046/script.md` [8:00-9:00] (drafts before sends, per-user OAuth, start narrow). The real failure stories tie back to L7, L10, L11. Cost gets its own full treatment in L19.

---

# L19 - DEPLOY, SCHEDULE, MONITOR, CONTROL COST (2:01 - 2:08) ~7 min

**By the end you can:** put an agent on a schedule, watch it run, and treat cost as a first-class concern from day one.

### 19.1 From "I ran it once" to "it runs without me, and I can afford it" (2:01, 7 min)
Take the morning-brief or monitoring agent from manual to automatic, then make it observable and affordable. Three parts.
- **Schedule:** options stated vendor-neutrally: a scheduled cloud routine (cron/event trigger, runs even when your machine is off), a desktop scheduled task, or a plain local cron job. The discipline is the same regardless: prove it manually first, schedule it in plain language, confirm it still has access to the tools it needs, let the first real run fire, then read the output before you trust it. Honest caveat: whether a job runs fully in the background or needs an app open depends on your setup and the current rollout, so test it before you depend on it.
- **Monitor:** you cannot trust what you cannot see. Keep a log of each run (what it did, what it drafted, what it skipped) and glance at it; the scheduled monitoring agent from L15 is itself a monitoring pattern you can point at your other agents.
- **Cost, as a first-class concern:** agents loop and call tools, which costs tokens and can call paid APIs. Make cost visible: know roughly what one run costs, cap the scope and the loop, set a spend/usage alert if your setup supports it, choose a smaller/cheaper model where the job allows, and remember a runaway loop is a cost failure as much as a correctness one. Rule on screen: a scheduled agent you are not watching the cost of is a bill waiting to happen.
- **Task (PROJECT 14):** schedule the morning-brief (or monitoring) agent, verify the first real fire, add a run log, and note the per-run cost with one cost guardrail.
- **Reuse:** the scheduled-task discipline ("prove it manually, then schedule, then verify the first run") from `023/script.md` Module 8 via mega-course 3.7; the "runs while I am not here" monitors from `040/script.md` [6:30-9:30]. Cost as first-class is the major expansion over v1's schedule lesson; the `claude-api` skill is the reference for model pricing/choice.

---

# L20 - RUNNING AN AGENT AS A PAID SERVICE (2:08 - 2:15) ~7 min

**By the end you can:** understand what it takes to run an agent for someone else: scoping, pricing, delivering, and maintaining it.

### 20.1 From your agent to a client's agent (2:08, 7 min)
The step most tutorials never reach, walked as a real workflow, not a business-guru pitch. Someone will pay for the morning-brief, triage, or FAQ agent because they will not build it themselves. Four parts:
- **Scoping:** write down exactly what the agent will and will not do, which tools it touches, and what "done" looks like, before you build. A tight scope is what keeps a client agent reliable and keeps you out of trouble. This is L2's decision discipline applied to someone else's task.
- **Pricing:** price with the cost of an error in mind and your own token/API cost covered, not just your time. Keep it a concept lesson: no revenue claims, no hype, no money amounts in titles. The honest frame is that you are pricing a reliable, supervised assistant, not an autonomous employee.
- **Delivering:** multi-user auth is what makes this possible without holding anyone's password. Per-user OAuth means each client authorizes their own accounts, tokens stay theirs, you never hardcode credentials; this is exactly why the Arcade/auth layer from L4 matters for real work. Drafts before sends is non-negotiable for a client; get explicit sign-off on what the agent may touch; keep every action logged so there is an audit trail if they ask "what did it do."
- **Maintaining:** you now own the failure modes from L18 and the cost from L19. Re-run your evals (L7) whenever a tool or a model changes, watch the run log, and expect to tune the voice/memory file over time. Honest positioning: you are selling something supervised that does the boring first 80 percent; undersell and overdeliver. Tyler's software-engineer credibility is the wedge: you understand the auth, reliability, and cost layer that separates a demo from something you can charge for.
- **Task (PROJECT 15):** pick one of your agents, write a one-page scope (does / does not / tools / done), and note how you would price and maintain it.
- **Reuse:** expanded from v1's L10. Governance/audit-trail framing from `046/script.md` [8:00-9:00] and `2026-08-02-arcade-mcp-course-outline.md` Module 6 (per-user OAuth, tokens never hardcoded, every action logged), reframed from "safe for you" to "safe enough to charge for." Scoping/pricing/maintaining structure is new. The FAQ agent (L14) is the best concrete example of a saleable agent.

---

# OUTRO (2:15 - 2:20) ~5 min

### Recap + what to build next (2:15, 5 min)
Zoom out: you learned what an agent actually is (a model in a loop with tools and a goal), when to build one and when not to, the loop in detail, how to give an agent good tools and memory, and how to test it with self-checks and evals. Then you built eight agents start to finish, rebuilt one in a real framework, learned when multiple agents help and when they hurt, put real guardrails on them, deployed one on a schedule with cost under control, and saw what running one for a client takes. That is a working skill, not a feature tour. Reinforce the one definition one last time. One clear action: pick ONE annoying task you do every week and build the smallest agent that does it, this week, drafts-only. Point to the copy-paste agent pack, the instructions files, and the community/newsletter (free.tylerai.dev/youtube). Comment prompt: what is the first thing you will hand to an agent.
- **Reuse:** outro + CTA structure from `038/script.md` [10:30-12:15] and `046/script.md` CTA; keep the actual ask under ~90 seconds.

---

# The hands-on projects (15 across the course)

1. **Label your weekly task** (L2) - script, prompt, or agent, using the rule of thumb.
2. **Two-tool Arcade Gateway, connected** (L4) - build a Gmail + Calendar Gateway, connect it to Claude Code, clear the OAuth authorize.
3. **Write a memory file** (L6) - name, reply voice, and two standing rules for your future morning-brief agent.
4. **Self-verification + 3 evals** (L7) - add a self-check line, then write and run normal / edge / should-refuse test cases.
5. **Research-brief agent, no code** (L8) - one instructions file plus web search: topic in, sourced one-pager out, nudged once.
6. **Morning-brief agent, end to end** (L9) - Calendar + Gmail summary, reply triage, drafts saved in Gmail, nothing sent.
7. **Inbox-triage agent** (L10) - sort unread into needs-you vs noise, draft replies, check the sort first.
8. **Research assistant that saves an artifact** (L11) - add a save-to-doc step so every run leaves a dated, sourced brief.
9. **Repo triage to a ClickUp task** (L12) - summarize open issues/PRs and file the top one as a task, reviewed first.
10. **Content-repurposing agent** (L13) - one source in, platform drafts out in your voice, saved not posted.
11. **Customer-support / FAQ agent** (L14) - answers only from your docs, refuses and hands off when out of scope.
12. **Scheduled monitoring agent** (L15) - watch something, diff against last time, only ping on a real change.
13. **Rebuild an agent in a framework** (L16) - same instructions, same tool, now in Pydantic AI or the Claude Agent SDK.
14. **Deploy with cost control** (L19) - schedule an agent, verify the first fire, add a run log, note per-run cost and one guardrail.
15. **Scope + price a client agent** (L20) - one-page does/does-not/tools/done, plus how you would price and maintain it.

---

# Reusable-footage map (so Tyler does not re-shoot everything)

| Lesson | Reuse from |
|---|---|
| Intro cold open | 046 [0:00-0:15] (result first); 038 cold open (built the heavy version) |
| L1 what an agent is | 038 [0:20-1:30] (three-part graphic + reframe) |
| L2 when to build | new; rhymes with mega-course 2.8 decision rule |
| L3 the loop in detail | new; sets up narration reused over L8/L9 runs |
| L4 tools/MCP/auth | 046 [0:15-2:30]; arcade-mcp-course-outline Mod 1-2 |
| L5 tool design | new; leans on Tyler's integration experience |
| L6 memory | new; CLAUDE.md-as-instructions pattern from 023, 040 |
| L7 self-verify + evals | new; extends the 038 nudge into deliberate testing |
| L8 first agent, no code | 038 [1:30-8:00] full live build (+ existing copy-pack) |
| L9 morning brief e2e | 046 [2:30-8:00] full (timed short cut from it) |
| L10 inbox triage | 038 [8:00-9:15]; arcade-mcp-course-outline walkthrough 2 |
| L11 research assistant + artifact | builds on L8 + L7; Drive/Docs tool via Arcade |
| L12 repo triage to ClickUp | arcade-mcp-course-outline walkthrough 3 (+ ClickUp-MCP fallback); arcade-mcp-claude-code demo ideas |
| L13 content-repurposing | new; leans on /repurpose + /social-copy logic, never auto-post |
| L14 support / FAQ | new; grounding + refusal + draft handoff; ties to L7 should-refuse eval |
| L15 scheduled monitoring | 040 [6:30-9:30] monitors; diff-against-memory from L6 |
| L16 frameworks | new; load claude-api skill for Claude Agent SDK; keep L8 instructions identical |
| L17 multi-agent | new; uses the L11/L13 research-write-check chain as the example |
| L18 fail + safety | 038 [9:15-10:30]; 046 [8:00-9:00]; real stories tie to L7/L10/L11 |
| L19 deploy/schedule/monitor/cost | 023 Mod 8 discipline (via mega-course 3.7); 040 [6:30-9:30]; cost is the new expansion (claude-api for pricing) |
| L20 paid service | 046 [8:00-9:00] + arcade-mcp Mod 6 governance; scoping/pricing/maintaining is new |
| Outro/CTA | 038 [10:30-12:15]; 046 CTA |

# Sources
- `research/youtube/2026-08-04-claude-mega-course-outline.md` (Part 3 expanded into this standalone course)
- `research/youtube/2026-08-02-arcade-mcp-claude-code.md` (Arcade tools + auth, demo ideas)
- `research/youtube/2026-08-02-arcade-mcp-course-outline.md` (Gateway build, connect, one-gateway spine, governance)
- Packages: `youtube/videos/038-build-first-ai-agent` (what-is-an-agent, first agent, honest limits), `youtube/videos/046-arcade-build-agent` (tools + auth, morning-brief agent, safety rules)
- Framework references: Pydantic AI, LangGraph, Claude Agent SDK (load the `claude-api` skill before any Claude-specific code or model naming), Arcade (tools + auth layer)
