# Setup checklist — everything needed before filming/running

Grouped by area. ✅ = you likely already have it. 🔧 = set up before you film. Do the 🔧 items on the **VPS Hermes** (the mature one), not your laptop demo instance.

## 1. Hosting / machines
- 🔧 **An always-on host for the "mature" Hermes** - a VPS (Hostinger KVM 1 or 2 is plenty) or a Mac mini left on. This is what makes "runs while the laptop is closed" real and gives the Feature 3 VPS shot. (You've used Hostinger before - reuse it.)
- ✅ **Your laptop/desktop** for the live install take (clean state - `mv ~/.hermes ~/.hermes.bak` first, restore after).
- 🔧 SSH access / provider dashboard open in a tab for the on-camera VPS shot.

## 2. Hermes itself
- 🔧 **Terminal install** ready to run on camera: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- 🔧 **Desktop app** downloaded but NOT opened yet (film the first open).
- 🔧 **Mature Hermes on the VPS** already onboarded with real memory (user.md / memory.md), a few skills, and the crons below - so the cutaways aren't faked.

## 3. Model / provider
- 🔧 **A working driver** for the live demo: an Anthropic/OpenAI API key, Nous Portal sub, or OpenAI Codex (ChatGPT sub) - whatever you'll show. Connect it before recording so "say hi" works instantly.
- 🔧 **Ollama + a tool-capable model pulled** for the 100%-local segment: `ollama pull qwen3` (chat-only models can't run agents). Set the context window (Ollama won't): `OLLAMA_CONTEXT_LENGTH=64000 ollama serve`. Connect fast with `ollama launch hermes`, or manually via `hermes model` → custom endpoint `http://127.0.0.1:11434/v1` (blank key). Desktop path: Settings > Models > Edit models > Add provider > same URL.

## 4. Gateways (messaging)
- 🔧 **Telegram bot**: create via BotFather (`/newbot`), copy the bot token, and get your user ID (message user info bot). Used for the analytics brief + competitor-watch pings.
- 🔧 **Discord** connected (for the comment-summary delivery), or just use Telegram for everything if simpler.

## 5. Data access (read-only from Hermes)
- ✅ **YouTube Data API / OAuth** - you already have this wired for `/yt-replier`; reuse those credentials so Hermes can read comments + analytics. (yt-dlp is the no-API fallback.)
- ✅ **Skool access** - your existing `/skool` logic / access for the `/skool-post` skill.
- 🔧 **`yt-dlp` installed + updated on the VPS** as the fallback: `brew upgrade yt-dlp` / `pip install -U yt-dlp` (the old build 403s - we already hit this).
- ✅ **Blotato** for any posting/publishing. Hermes never posts - it reads and drafts only.

## 6. The workflows wired on the VPS Hermes (for the demos/cutaways)
- 🔧 **/next-video skill** (Feature 2 live build): reads last ~20 uploads + 2-3 competitors' recent top videos → 5 scored ideas.
- 🔧 **competitor-watch cron** (Feature 3 live build): hourly channel check → Telegram ping on new upload.
- 🔧 **comment-summary cron**: morning YouTube comments summarized + replies drafted → Discord.
- 🔧 **analytics-brief cron**: morning channel views + top video → Telegram.
- 🔧 **/skool-post skill**: drafts a Skool post from a new video (shown in the skills list as "another one I made").
- 🔧 **github-tests cron** (the developer beat): nightly - pull repos, run tests, ping Telegram only on failure. Needs a `GITHUB_TOKEN` (`hermes config set GITHUB_TOKEN ...`) and your repos reachable on the VPS.
- 🔧 **Safe-credential move on camera**: `hermes config set <KEY>` puts a secret in the `.env`, never the chat. Use GitHub as the example (mirrors Nate).
- ⚠️ **Cron prompts must be self-contained** - each run is a fresh session with no memory of last time.
- ⚠️ If any one isn't wired by film day, **cut that clip** rather than fake it. Keep at least two for the montage.

## 7. Recording kit
- 🔧 Screen recorder (Camtasia/OBS), bumped terminal font, clean prompt, 16:9 window.
- 🔧 **Phone frame / device** showing Telegram + Discord for the "it arrived on my phone" shots.
- 🔧 Browser tabs pre-opened: the Hermes site, GitHub repo, ollama.com, your VPS dashboard.
- 🔧 A **competitor channel list** (2-3) for the /next-video skill and the competitor-watch cron.
- 🔧 A throwaway skill/cron for close-ups if you don't want real `~/.hermes` paths/keys on screen.

## 8. CTA
- 🔧 **Free community link** (Skool) for the description + end CTA, with the setup notes + commands from this video dropped in the classroom.

---

## The short version (blockers to clear first)
1. Spin up / pick the always-on VPS and install Hermes there.
2. Reuse your `/yt-replier` YouTube API creds so Hermes can read comments + analytics.
3. Connect Telegram (BotFather) + Discord.
4. Wire the workflows (analytics, comments, competitor, /next-video, /skool-post, github-tests) and let them run once.
5. Ollama + a local model pulled for the free segment.
Everything else (Blotato, Skool access, laptop, recorder) you already have.
