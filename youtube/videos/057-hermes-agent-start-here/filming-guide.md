**⚠️ UPDATED 2026-08-31 (v3):** the script now runs ~13 min, not ~10. Two changes: a new **"what this actually is, and why you'd run one"** segment at 1:00-2:30 (it was cut in v2, it is back and it is what makes the rest land), and **memory promoted to the hero beat** at 4:00-6:15 with the editable markdown file as the money shot. Timings below may still read v2 - trust `script.md`.

# Filming Guide — Set Up Hermes Agent in 10 Minutes

The do-this / click-that version. Follow it top to bottom while recording. Target ~10 min finished.

This is the **Hermes** setup/explainer video - its own thing. Do NOT frame it as "Build Your First AI Agent in 5 Steps" (that is the format of video 050). Keep it clearly the Hermes video: hook + montage, then the 3 features (memory / skills / schedule), then local + where it fits.

## Pre-recording setup
- [ ] **Fresh machine state.** Uninstall or move your existing `~/.hermes` folder aside so the install + first-run looks clean on camera (`mv ~/.hermes ~/.hermes.bak`). Restore after.
- [ ] Have a **second, already-configured Hermes** ready (real memory, a couple skills, a cron job, a Discord/Telegram gateway) to cut to for the "remembers last week" and "daily brief arrives" moments - do not try to create weeks of history live. Tina does exactly this.
- [ ] **Host that second Hermes on an always-on box** - ideally a cheap VPS you can SSH into on camera (or a Mac mini left on). This makes the "runs while the laptop is closed" claim real and gives you the VPS shot for Feature 3. Have the SSH session / provider dashboard ready in a tab.
- [ ] **Wire the real workflows on that VPS Hermes so the cutaways are genuine, not staged.** Tyler is wiring the **YouTube Data API** (comments + analytics); `yt-dlp` also works read-only as a fallback. Have these running before you film:
  1. Morning brief to Telegram: channel views + top video (YouTube Analytics/Data API, or yt-dlp view counts).
  2. Summarize new YouTube comments each morning + draft replies to Discord (API to read; the LLM drafts).
  3. **Competitor watch** (the LIVE cron demo): ping Telegram when a named channel uploads (API or `yt-dlp --flat-playlist`, diff against last seen).
  4. **/next-video** skill: reads your last ~20 uploads + 2-3 competitors' recent top videos, returns 5 scored ideas (the Feature 2 build).
  5. **/skool-post** skill: drafts a Skool post from a new video (show it in the skills list as "another one I made").
  6. **github-tests cron** (the developer beat): nightly, pull your repos, run the tests, ping Telegram only on failure. Needs a `GITHUB_TOKEN` set via `hermes config set` and the repos reachable on the VPS.
  If any one is not wired in time, cut that clip rather than faking it - honesty is the brand.

**Posting boundary (state it plainly in the video):** Hermes only READS and DRAFTS here - it never posts. Publishing/scheduling goes through **Blotato**. Reading comments/analytics uses the YouTube Data API (or yt-dlp); actually posting a reply would need OAuth, and we deliberately keep that in Blotato.
- [ ] Terminal font bumped up, clean prompt, window sized for 16:9.
- [ ] Desktop app downloaded but NOT yet opened (film the first open).
- [ ] A model key ready (Nous Portal or Anthropic/OpenAI) so first-run "say hi" works instantly.
- [ ] Ollama installed with one small model already pulled (e.g. a Qwen or Llama) so the local demo is fast.
- [ ] Browser tabs pre-opened: github.com/NousResearch/hermes-agent, hermes-agent.nousresearch.com, ollama.com.
- [ ] Discord or Telegram open on your phone (or a phone frame on screen) for the gateway shot.

## Timing cheat sheet
| Section | Target | Running |
|---|---:|---:|
| Hook | 0:30 | 0:30 |
| What it does (montage - FILM LAST) | 0:30 | 1:00 |
| Install + model | 1:30 | 2:30 |
| Feature 1: memory | 1:30 | 4:00 |
| Feature 2: skills (+ show the SKILL.md file) | 1:45 | 5:45 |
| Feature 3: cron + credentials + hosting (+ show the job) | 2:45 | 8:30 |
| Local + free | 1:00 | 9:30 |
| Fits with Claude Code + CTA | 1:00 | 10:30 |

**Note:** now ~10:30. Still fine (the 10-35 min band is neutral), but if you want it under 10, trim the montage to 2 results or tighten the Local segment. Feature 3 is the densest section - consider letting it breathe and cutting elsewhere.

## Record order (important)
Do NOT film top to bottom. Film in two passes:

1. **Main take (record live, in order):** Install → Feature 1 → Feature 2 → Feature 3 → Local → Fits/CTA. This is the substance and it is where the camera actually rolls first. Record the hook voiceover too, but keep it loose - you can retime it after you see the montage.
2. **Montage + cutaways (film LAST, from your mature Hermes on the VPS):** the three "look what it does" results - overnight brief on the phone, "what were we building last week" recall, one-prompt app build - plus any b-roll (the .hermes folder, the skill file being written, the VPS terminal). Assemble the 0:30-1:00 montage in the edit.

Why: the montage needs a lived-in agent with real history, real skills, a real cron job, and a real gateway. You cannot fake weeks of memory during a clean install take, so capture those results separately and cut them into the cold open.

---

## Step 1 — Hook (to 0:30)
Talk to camera or over the screen. Show your working Hermes + the desktop app side by side.
> "If you already use Claude Code, you are going to get this one fast. Hermes is the other half. Free, open source, runs on your own server, remembers everything, writes its own skills, keeps going while your laptop is closed. Before I set it up, look at what that actually gets you."
Land the three-part promise, then hard cut to the montage. Under 30 seconds, no intro.

## Step 2 — Montage: "look what it does" (to 1:00) — FILM LAST
[NOTE] This is a b-roll montage cut in during the edit, captured AFTER the main take from your mature Hermes on the VPS. Three fast, real results, tight voiceover:
- [SHOW] a morning brief in Telegram on your phone, ~7am - channel views + top video → "7am, already on my phone. My numbers and my top video, pulled while I slept."
- [SHOW] a Discord channel / terminal showing new YouTube comments summarized with draft replies → "Overnight it read my new comments, summarized them, drafted the replies. I just approve."
- [SHOW] a phone ping "Heads up: [competitor] just posted" → "The second a competitor I watch posted, it pinged me."
- [SHOW] quick VPS terminal shot → "No laptop babysitting. Runs on a five dollar server all day."
Close: "Here is the whole setup in ten minutes." Keep it under 30 seconds, energy up. The montage IS the sell.

## Step 3 — Install (to 2:30) — LIVE RECORDING STARTS HERE
Show BOTH paths quickly, let viewer pick.

Terminal:
```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```
> "One command. Paste it, walk through the onboarding."

Desktop: download for your OS, open it (film the first open), clean chat UI.

Then the model choice:
> "It drives on anything. Best driver is a frontier model through Nous Portal, but you do not have to pay per token - I will point it at a free local model in a minute. For now, connect what you have and say hi."
[SHOW] type `hi`, get a reply.

**Dead-air filler while it installs:** "Same install whether this is your laptop or a five dollar VPS - that matters later when we make it run twenty four seven."

## Step 4 — Feature 1: Memory (to 4:00)
[SHOW] Type:
```
Here is a bit about me, please remember this: I'm a software engineer building AI content. Prefer concise answers.
```
Point out "running memory."
[SHOW] Finder → the `.hermes` folder → open `memory/user.md` in a text editor. Plain markdown.
> "You can literally read what your agent knows about you."
[CUT to the pre-built Hermes] New session:
```
Remind me what we talked about earlier this week.
```
It runs session search, pulls it back.
> "That is the thing Claude Code cannot do out of the box."

## Step 5 — Feature 2: Skills (to 5:45)
[SHOW] skills/tools panel, scroll pre-built skills.
Give it a real task worth turning into a skill - the "what's working" idea finder:
```
Look at my last 20 YouTube uploads and the recent top videos from these three channels: [competitor 1], [competitor 2], [competitor 3]. Find the patterns in what is getting views, then give me 5 new video ideas I could film, each scored 1 to 10 with a one line reason.
```
Then:
```
Make this into a skill for finding my next video.
```
**Now SHOW the mechanism (this is the teaching beat).** Open the file it just wrote:
```
~/.hermes/skills/next-video/SKILL.md
```
[SHOW] the SKILL.md open in a text editor - point at the description + the step-by-step "how to use."
> "That is the whole skill. A plain markdown file in a skills folder. It wrote it itself with a built-in skill tool. You never touched a config."
[SHOW] call it:
```
/next-video
```
> "I did the same move to make a skill that drafts my Skool post from a new video, and a couple others. That is the learning loop - do this with everything you repeat."
[NOTE] Pre-build the `/skool-post` skill too so it appears in the skills list as "another one I made." The /next-video skill needs read access to your uploads + the competitor channels (YouTube Data API or yt-dlp).

[NOTE] Mechanism facts to keep accurate: skills live at `~/.hermes/skills/<name>/SKILL.md` (can have scripts/ references/ templates/ subfolders); the agent authors them via its `skill_manage` tool; `/learn` is the fast path to make one without doing the task first. Same open standard as Claude Code skills.

## Step 6 — Feature 3: Cron + credentials + hosting (to 8:30)
[SHOW] create a scheduled task in plain English (this is the LIVE demo - competitor watch):
```
Every hour, check these channels for new uploads: [competitor 1], [competitor 2]. The moment one posts, send me the title and link on Telegram.
```
**Now SHOW what it created (teaching beat).** List the jobs, open the new one:
```
hermes cron list
```
[SHOW] the job - point at the three parts: schedule, prompt, delivery target.
> "A cron job is just three things: a schedule, a prompt, and where to deliver it. Every hour, this prompt, delivered to Telegram."
Show it can be made by hand too:
```
hermes cron create "0 * * * *" "<self-contained prompt>" --name "competitor-watch" --deliver telegram
```
Say the two things people get wrong:
> "Every run is a fresh session with no memory of last time, so the prompt has to stand on its own. And Hermes validates the job before it runs - the model key, the skills it needs, and that it can reach your Telegram - so it fails now, not silently."
Trigger a test on camera so the payoff is live, not just claimed:
```
hermes cron run "competitor-watch"
```
[SHOW] a ping arriving on Telegram - "[competitor] just posted: <title> <link>".

**Safe-credential beat (mirror Nate's GitHub move).** Any job that touches a service needs a key, and it never goes in the chat:
```
hermes config set GITHUB_TOKEN <paste your token>
```
> "You never paste keys in the chat. One command drops it into the .env instead. Same move for any service, YouTube included."
Then the developer cron (leans your SWE authority):
> "As a software engineer, the one I lean on most is a GitHub cron - every night it pulls my repos, runs the tests, and pings me on Telegram only if something broke. Alongside that, one summarizes my new YouTube comments and drafts replies in Discord, one sends my channel numbers each morning. It only reads and drafts, it never posts - publishing goes through Blotato."

[NOTE] Mechanism facts to keep accurate: scheduler runs as a background process (`hermes cron start`), the gateway ticks it every 60s, jobs run in fresh isolated sessions, a lock at `~/.hermes/cron/.tick.lock` prevents double-runs, output saved to `~/.hermes/cron/output/` and delivered to the gateway target. Then do the honest hosting beat below.

**Hosting honesty beat (still in this section):**

Then be honest about hosting (this is the part people get wrong):
> "One honest thing. Hermes runs as a background process, so it only works while the machine it lives on is awake. Close your laptop lid and it sleeps. So you do not run this on your laptop. You put it on a host that is always on."
[SHOW] SSH into the cheap VPS (or the provider dashboard) with Hermes running there.
> "A five dollar VPS, on twenty four seven by design. Install Hermes there once, and your laptop is just a remote. Overnight it briefs you, checks your systems, drafts replies, laptop closed the whole time. That is the piece Claude Code does not try to do."

## Step 7 — Local + free (to 9:30) — show BOTH terminal and desktop
Ollama is already installed. Show the flow both ways.

**1. Pull a tool-capable model** (chat-only models can't run agents):
```
ollama pull qwen3
```
(Docs example is `gemma4:31b` but it's heavy - use a lighter tool-capable model like `qwen3` for a smooth on-camera demo; pick a size your machine can run.)

**2. The gotcha everyone misses - set the context window** (Ollama doesn't report one; agents need >=64k):
```
OLLAMA_CONTEXT_LENGTH=64000 ollama serve
```

**3a. Connect - fast path** (one command, from Ollama's launch integrations):
```
ollama launch hermes --model qwen3.8
```
- `qwen3.8` = the Qwen3 8B model (small, fast - good first local run). Ollama offers the same `ollama launch <app> --model ...` for Claude Code, OpenCode, OpenClaw too; it just wires each tool to your local model + endpoint.
- **Separate terminal?** Not for launch itself - the Ollama app runs the server in the background, and `ollama launch hermes ...` becomes your Hermes session in that one terminal. You only need a 2nd terminal if you set context the manual way (`OLLAMA_CONTEXT_LENGTH=64000 ollama serve` occupies its own terminal). Cleaner: set it persistently first so one terminal is enough:
```
launchctl setenv OLLAMA_CONTEXT_LENGTH 64000   # then quit + reopen the Ollama app
ollama launch hermes --model qwen3.8
```

**3b. Connect - manual path** (terminal):
```
hermes model
```
> Choose **custom endpoint**, enter `http://127.0.0.1:11434/v1`, leave the API key **blank**, confirm the detected model.
(Slow inference? add `HERMES_API_TIMEOUT=1800` to `~/.hermes/.env`.)

**3c. Connect - desktop app** (so viewers can use the app too):
[SHOW] Settings > Models > **Edit models** > **Add provider** > custom / OpenAI-compatible > base URL `http://127.0.0.1:11434/v1` > leave key blank > select your model.
(Menu labels mirror the terminal config; exact wording may shift by version - this is the flow Tina uses in her walkthrough.)

**4. Prove it uses tools, not just chats:**
```
hermes chat -q "List the files here, read README.md, and tell me the project name."
```
> "Model on your machine, memory on your machine, nothing leaves. Private and free."

[NOTE] Keep port 11434 off the public internet. Bigger models = better tool use but need real RAM/VRAM (often well over 8GB).

## Step 8 — Fits with Claude Code + CTA (to 10:30)
[SHOW] split - Claude Code in a repo / Hermes running a scheduled task.
> "This is not Hermes versus Claude Code. I run both. Claude Code is my specialist. Hermes is my always-on generalist."
Tease the next two videos (how I use it daily / 100% private local). One CTA to the community for the setup notes + commands.

---

## On-camera tips
- If a command errors on camera, keep it - narrate the fix. "It remembers" and "it fixes itself" are the brand; a real recovery sells it.
- Energy: calm and precise beats hype (Tyler's voice). Let the cron/gateway "aha" breathe.
- Capture clean b-roll of: the `.hermes` folder, the skill file being written, the Discord brief landing. Those are the three screenshot moments.
- Do not imply you are not a developer - lean into the engineer POV ("here is how I think about it as a software engineer").

## Files to have open / ready
- A throwaway business idea to evaluate (so Feature 2 is instant).
- Your pre-built Hermes with visible memory + at least one prior session about a named topic to "remember."
- A phone frame with Discord/Telegram for the brief.
