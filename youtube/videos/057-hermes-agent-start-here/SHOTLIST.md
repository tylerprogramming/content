# SHOT LIST — 057 Hermes Agent. Step by step, with sub-steps.

Screens: **A** camera · **B** terminal (local) · **C** Hermes desktop app · **D** external browser ·
**E** editor / Finder (`.hermes` folder) · **F** motion graphic (post) · **G** phone (Telegram/Discord)

---

## ⚠️ READ THIS FIRST — you need TWO Hermes instances

The script installs Hermes **fresh** at 2:30, then at 4:00 asks it *"remind me what we discussed
about my content workflow earlier this week."* **A fresh install cannot answer that.** It has no
history. Same problem in beat 7: the cron and gateway proof only look real on an agent that has
been running.

So you are filming two agents and you have to be honest about the seam:

- **FRESH** — a clean install on your laptop. Carries beats 4 and the first half of 5.
- **MATURE** — your real Hermes on the always-on host, weeks of memory. Carries the montage,
  the session-search moment, cron, gateways, and the local-model test.

**Say the seam out loud** the first time you cut to it: *"This is mine, the one that has actually
been running for a few weeks, because I want to show you what this looks like once it knows you."*
That one sentence turns a continuity problem into a credibility beat. Do not try to hide it.

---

## 0. PRE-ROLL

**0.1 The mature agent must already exist and have real history**
- Hermes on the always-on host (Mac mini or the VPS), running for at least a couple of weeks
- Real memory in `.hermes/memory/*.md` you are willing to show on camera
- At least 3 working crons: morning brief, comment summary, competitor watch
- Telegram (or Discord) gateway connected and delivering
- **Read your own memory files before filming.** They are going on screen in the hero beat.

**0.2 The fresh machine**
- A clean box or user account with no `~/.hermes`
- If you rehearse, `mv ~/.hermes ~/.hermes.bak` before the real take
- API key ready to paste (Nous Portal or OpenRouter)

**0.3 Local model path (beat 8)**
- `ollama pull qwen3` (must be tool-capable)
- Quit the Ollama app, then `OLLAMA_CONTEXT_LENGTH=64000 ollama serve`
- Confirm it responds before you roll

**0.4 Capture for the montage (film LAST, see beat 2)**
- Phone screen: the 7am morning brief in Telegram
- The comment summary with drafted replies
- A competitor-posted push notification
- The always-on host terminal with the Hermes process running

**0.5 Stage**
- Do Not Disturb, notifications off, unrelated tabs closed
- Two browser windows: one for **C/app**, one for **D/external**
- Bump terminal and app font size
- **Scan `.hermes/memory/*.md` and your terminal scrollback for anything private**

---

## 1. HOOK — 0:00-0:30

- **1.1** [A] Cold open: "If you already use Claude Code, you are going to get this one fast. Hermes is the other half."
- **1.2** [B/C] Quick cut: Hermes in a terminal and the desktop app side by side
- **1.3** [A] The four claims: free and open source, runs on your machine, remembers everything, writes its own skills, keeps going with the laptop closed
- **1.4** [A] **The stakes line:** "Most people install this, poke at it for ten minutes, and never open it again. And it is almost always the same three things they skipped."
- **1.5** [A] "Get those three right and it stops being a toy and starts being staff."
- **1.6** [A] "Before I set it up, look at what that actually gets you." Hard cut to montage

> The three things = memory, a self-written skill, one cron on an always-on host. The outro pays this back word for word. Do not change the number.

## 2. MONTAGE — 0:30-1:00 · **FILM THIS LAST**

- **2.1** [G] Phone, ~7am: the morning brief in Telegram, channel views + top video
- **2.2** [C/G] The overnight comment summary with drafted replies listed
- **2.3** [G] A push notification: competitor just posted
- **2.4** [B] The always-on host terminal, Hermes process running
- **2.5** [A] "No laptop babysitting. It runs on a five dollar server all day."
- **2.6** Energy up, fast cuts, under 30 seconds. This montage IS the sell

## 3. WHAT THIS ACTUALLY IS — 1:00-2:30

- **3.1** [A] "Thirty seconds on what this thing is, because the category is new and the name does not tell you"
- **3.2** [A] "Not a chatbot, not a coding tool. It is a process that runs."
- **3.3** [F] Diagram: **CLAUDE CODE = a session you open** / **HERMES = a process that stays running**
- **3.4** [A] The Claude Code shape: open in a repo, it works, you close it, next time it does not know you. Not a flaw, that is the design
- **3.5** [F] Three items building as you name them: **remembers / runs when you are not there / reaches you anywhere**
- **3.6** [A] The honest why-both: Claude Code is for the code, this is for everything around it you currently do by hand
- **3.7** [A] Free, open source, Nous Research, your machine or a five dollar server
- **3.8** [A] Flag the one real cost now: it only works while its machine is awake. "We will deal with that later"

## 4. INSTALL + MODEL — 2:30-4:00 · **FRESH INSTANCE**

- **4.1** [D] `hermes-agent.nousresearch.com`
- **4.2** [B] Paste the install one-liner, let the onboarding run
- **4.3** [C] Show the desktop app as the alternative: same agent, nicer interface
- **4.4** [A] Dead-air filler while it installs: "same install whether this is your laptop or a five dollar VPS, and that VPS part matters in a few minutes"
- **4.5** [C] The model choice. Nous Portal / frontier model, paste the key
- **4.6** [A] Promise the free path: "at the very end I will show you how to run this on a model on your own machine"
- **4.7** [C] Type "hi", get a response. It is alive

## 5. MEMORY — THE HERO — 4:00-6:15 · **starts FRESH, cuts to MATURE**

- **5.1** [A] "If you only take one thing from this video, take this one"
- **5.2** [C] **FRESH:** type the about-me line, watch the status say *running memory*
- **5.3** [E] Open the `.hermes` folder in Finder
- **5.4** [E] Open `memory/user.md` in a text editor. **Scroll it slowly. This is the money shot**
- **5.5** [A] "That is a markdown file. On my machine. I can read exactly what my agent believes about me."
- **5.6** [E] Show the other core files: one about you, one about your setup, one about the agent
- **5.7** [E] **Edit a line live.** Delete something wrong, type something you want it to always know
- **5.8** [A] The contrast: "ChatGPT has memory, but you cannot open it. You cannot read the file. You cannot fix a line."
- **5.9** [F] Tier list building: **1 core files / 2 session history / 3 optional plugins**
- **5.10** [C] **CUT TO MATURE — say the seam out loud.** New session, ask "remind me what we discussed about my content workflow earlier this week"
- **5.11** [C] It runs a session search and answers with real detail
- **5.12** [A] "Brand new session. I did not paste anything in or re-explain who I am. It just knew."
- **5.13** [A] Tier three in one line: deeper user modeling, or point it at an Obsidian vault
- **5.14** [A] The compounding close: "A session tool is exactly as good on day two hundred as day one. This one is not."

## 6. SKILLS — 6:15-8:00

- **6.1** [A] "This is the one Claude Code users will feel at home with"
- **6.2** [C] Open the skills and tools panel, scroll the pre-built skills
- **6.3** [C] Give it the real task: last 20 uploads + 3 competitor channels, find patterns, 5 scored ideas
- **6.4** [C] Let it pull data and return the scored list. Speed-ramp the wait
- **6.5** [C] Then the move: "Make this into a skill for finding my next video"
- **6.6** [E] Open `~/.hermes/skills/next-video/SKILL.md`. Plain markdown, it wrote it itself
- **6.7** [C] Run `/next-video` to prove it persisted
- **6.8** [A] "It did the work once, wrote the how-to to disk, and kept it. Do this with everything you repeat."

## 7. CRON + ALWAYS-ON — 8:00-10:45 · **MATURE**

- **7.1** [C] Create the competitor-watch job in plain English
- **7.2** [B] `hermes cron list`, open the job it created
- **7.3** [A] "A cron job is three things: a schedule, a prompt, and where to deliver it"
- **7.4** [B] Show the by-hand version: `hermes cron create "0 * * * *" ... --deliver telegram`
- **7.5** [A] The two gotchas: every run starts a fresh session so the prompt must stand alone; Hermes pre-checks the model key, skills, and delivery before it ever runs
- **7.6** [B] `hermes cron run "competitor-watch"` to trigger it live
- **7.7** [G] **The ping lands on your phone.** Hold on it
- **7.8** [B] Credentials: `hermes config set GITHUB_TOKEN ...` — goes to `.env`, never the chat
- **7.9** [A] Your real crons: nightly repo tests pinging only on red, comment drafts, morning numbers. **Reads and drafts, never posts**
- **7.10** [A] **The honest limitation:** it is a background process, it only runs while its machine is awake. Close the lid and it sleeps
- **7.11** [B/D] SSH into the always-on host, or the VPS dashboard
- **7.12** [A] The aha: "Overnight it runs your briefing, drafts your replies, and it is waiting for you in the morning, laptop closed the whole time." **Let this breathe**

## 8. LOCAL AND FREE — 10:45-11:45

- **8.1** [B] `ollama pull qwen3`. Say why: it has to be tool-capable or the agent is useless
- **8.2** [B] The gotcha: `OLLAMA_CONTEXT_LENGTH=64000 ollama serve`. Ollama does not report a context window
- **8.3** [B] Fast path: `ollama launch hermes`
- **8.4** [B] Or by hand: `hermes model`, custom endpoint, `http://127.0.0.1:11434/v1`, blank key
- **8.5** [C] Same in the app: Settings > Models > Edit models > Add provider > custom endpoint
- **8.6** [C] **Test that it uses tools, not just chats:** "list the files here, read the README, tell me the project name"
- **8.7** [A] "Model on my machine, memory on my machine, nothing leaves"

## 9. WHERE IT FITS + OUTRO — 11:45-13:00

- **9.1** [A] "This is not Claude Code versus Hermes. I run both."
- **9.2** [F] Split: Claude Code in a repo / Hermes running a scheduled task
- **9.3** [A] Specialist vs generalist. You open one, the other never closes
- **9.4** [A] **Pay off the hook:** "If you set up just those three things, memory, a self-written skill, and one cron on a server that stays on, you already have something most people never get to"
- **9.5** [A] "Everything I showed you is running on mine right now. That is not a demo I built for the video."
- **9.6** [A] Sequel ask: the multi-agent version
- **9.7** [A] CTA: setup notes and commands in the free community, one destination
- **9.8** [F] End card

---

## Before it goes to the editor
- Confirm the FRESH/MATURE seam is stated out loud at 5.10, not silently cut
- Confirm no private content is legible in `memory/user.md`, the skills folder, or scrollback
- Confirm the phone ping at 7.7 actually landed on camera. If it did not, do not fake it
- Title still needs locking. See `titles.md`; "How to Run an AI Agent That Never Forgets (Hermes Setup)" got stronger now that memory is the hero
