# Channel refresh plan: @tylerreedai

Audit 2026-09-20. Read from the API (channel, 23 playlists, 8 home sections, last 25 uploads)
and the public page. Nothing executed. Priority order, rough effort, and what I can do vs
what only you can do.

## What the audit found

**The channel says 2024. The uploads say 2026.** Every surface a new visitor sees was set in
the AutoGen / CrewAI era and has not moved since:

| Surface | Current state | Age |
|---|---|---|
| Banner | Pixel-art characters labelled AI AGENTS, CREWAI, AI AUTOMATION, AI SERVICES, COURSES | 2024 |
| Trailer (non-subscribers) | "How To Use AI Agents To Do ALL Your Work - Full CrewAI Course" (119,708 views) | Nov 2024 |
| Description | "discussions about Autogen and AI", a Skool link with a `-5174` slug, a stray `HIGGS-0QGWS` code | 2024 |
| Channel keywords | `ai "ai agents" autogen "crew ai" "lm studio" ollama python` | 2024 |
| Home layout | 8 sections: Newcomers CrewAI playlist, Courses For YOU, AI Made This, Popular uploads, plus 4 broken `channelsectiontypeundefined` rows | 2024 |
| Newcomers playlist (12) | 100% AutoGen / CrewAI, every video dated 2024-07-26 | 2024 |
| Courses For YOU (11) | Newest is Firecrawl (Jul 2025); nothing from the Claude Code era | 2025 |

Meanwhile the last 25 uploads are 24 Claude Code / agent-harness videos and one DeepSeek.
The Claude Code playlist (21 videos) exists but is not on the home page. Hermes just landed
in a one-video playlist called "Agent Harness" (id `PLfcS7kMXNRKA`, note the odd short id).

**Playlist sprawl:** 23 playlists. Two named `n8n` (3 and 28). Five with one or two videos
(Agent Harness, Huggingface, AI Apps, Podcast, ChatGPT). Six are pre-AI Java content
(SOLID, Interview Coding, Java Quickies, Sorting, Data Structures) that dilute the channel
identity for a "Claude Code / AI agents" visitor.

**Links:** the header link is `skool.com/the-ai-agent-5174/about`. Video descriptions link
three different Skool URLs (`the-ai-agent-5174`, `the-ai-agent`, `the-ai-agency-5370`) plus a
Calendly strategy call and a `master-crewai-course` repo. A visitor cannot tell which is
current. GitHub link is `tylerprogramming/ai` (fine).

## The plan, in order

### 1. Home page and trailer (you, 30 min, biggest impact)

The home page is the landing page. Right now it lands a Claude Code viewer on a CrewAI
course and a "Newcomers" row from 2024.

- **Trailer:** set to Hermes 057 once it has 48 hours of data, or to "How To Build an AI
  Agent in 5 Steps (Claude Code)" now. Both say what the channel is in 2026. The CrewAI
  trailer has 119K views because it is 22 months old, not because it converts today.
- **Home sections, new order** (YouTube Studio → Customization → Layout):
  1. Video spotlight: latest upload (auto)
  2. Playlist: **Start Here** (new, see 3)
  3. Playlist: **Claude Code** (exists, 21)
  4. Playlist: **Agent Harness** (rename to **AI Agents That Run Themselves** or keep, but it
     needs 3+ videos: add Hermes 057, DeepSeek 056, "Build an AI Agent in 5 Steps", and 058
     when it lands)
  5. Playlist: **Courses** (rename from "Courses For YOU", prune to 2025+)
  6. Popular uploads
  7. Delete the 4 `channelsectiontypeundefined` rows (dead sections; they render as nothing
     but they are in the layout)
  Drop "Newcomers" and "AI Made This" from the home page. They stay as playlists.

I can do all of this via the API (channelSections + playlists) except the trailer, which is
Studio-only. Say go and I write the layout.

### 2. Banner (you + me, 1 to 2 hours)

The pixel-art banner is well made and the style is yours; the labels are the problem. Two
options:

- **A. Relabel the existing art.** Same characters, new tags: CLAUDE CODE, AI AGENTS, HERMES,
  AUTOMATION, COURSES. Cheapest, keeps continuity. Needs the source file (Figma / PSD?).
- **B. New banner in the same pixel style** with the 2026 stack drawn in: a terminal, the
  Hermes bots roster, a phone with a Slack card. I can brief it with the kie image skills or
  write the prompt for your designer; the safe zone is 1546x423 inside a 2560x1440 canvas.

Either way the banner should carry one line of text a visitor can act on: "New video every
week" or "Free community below". The current banner has no CTA.

Recommend A now, B when the Hermes/agents lane is proven with views.

### 3. Start Here playlist (me, 20 min)

Replace the 2024 "Newcomers" as the front door. 6 to 8 videos, all 2026, in watch order:

1. How To Build an AI Agent in 5 Steps (Claude Code)
2. Set Up Hermes Agent in 30 Minutes (057)
3. Full Claude Code + MCP Tutorial for Non-Technical Beginners
4. Build ANYTHING with Claude Skills (in 30 Minutes)
5. Claude Cowork Full Course
6. DeepSeek Harness (056)
7. I Automated My Entire Content Workflow with Claude Code

Title: **Start Here: Claude Code and AI Agents (2026)**. The old Newcomers playlist gets
renamed **Newcomers 2024 (AutoGen and CrewAI)** and stays public for search traffic; the
brain says legacy search is passive income, not something to delete.

### 4. Playlist cleanup (me, 30 min)

- Merge the two `n8n` playlists (3 → 28, delete the 3).
- Delete or fold the singletons: Huggingface (1), AI Apps (1), Podcast (1), ChatGPT (2) → fold
  into an **Archive: 2024 tools** playlist or delete. Your call; I would delete.
- Rename "Courses For YOU" → **Full Courses**; add Hermes 057, Cowork course, DeepSeek; keep
  the 2024 ones at the bottom.
- Rename "AI Services (55)": it is a grab bag. Either **Everything 2024** or leave it and
  keep it off the home page.
- Leave the six Java/CS playlists alone but confirm they are not on the home page (they are
  not).
- "31 Day Challenge AutoGen" (31): keep, off home.

### 5. Description, keywords, links (me, 15 min, you approve the copy)

Description draft (front-loaded, no emoji wall, no stray code):

> I'm Tyler, a software engineer (8 years at IBM and Chase, now AI engineering at Pfizer).
> This channel is Claude Code and AI agents that actually run for you: setup guides, real
> builds on my own workflows, and the honest limits. New video every week.
>
> Free community with every command and setup note from the videos: [ONE Skool link]
>
> GitHub for the code: github.com/tylerprogramming/ai

Channel keywords → `claude code, ai agents, hermes agent, ai automation, agent harness,
local ai, ollama, software engineer`. Drop autogen, crew ai, lm studio.

Links (header shows the first one; keep it to 5): Skool (one URL, decide which), GitHub,
LinkedIn, X, Instagram. Drop Calendly unless you still take strategy calls. Remove the
`HIGGS-0QGWS` line (looks like a verification code that was never cleaned up).

**Decision needed from you:** which Skool URL is canonical. Three are live in descriptions.

### 6. Old video descriptions (optional, later)

The last 25 uploads each carry a different Skool link and some still point at the CrewAI
repo. A one-time pass with the `yt-upload` skill can rewrite the links block on every 2026
video to the canonical one. I would not touch 2024 videos.

## What I need from you before executing

1. Canonical Skool URL (one of the three)
2. Banner: relabel (A) or new (B), and where the source file is if A
3. Trailer: Hermes 057 or "5 Steps" now
4. Delete the singleton playlists, or archive them
5. Keep the Calendly link or drop it

Everything in sections 1 (except trailer), 3, 4, 5 is API-writable and reversible; I would
snapshot the current playlists and sections to JSON first so any of it can be put back.
