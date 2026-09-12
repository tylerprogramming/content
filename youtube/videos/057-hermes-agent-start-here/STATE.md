# Hermes setup — where we are (2026-09-12)

Working state for video 057 + the "personal agency" build. Everything below is verified on Tyler's Mac Studio today.

## Running

| Piece | State | Proof |
|---|---|---|
| Gateway | launchd `ai.hermes.gateway`, **multiplexed** (one process serves default + coder + researcher) | `gateway.log`: "Cron scheduler will tick 3 profile(s)" |
| Slack | one app (`@hermes`), Socket Mode, home channel `C0C0CD3JUTU`. Bot token copied into coder + researcher `.env` so all three can post | `coder send -t slack` landed |
| Crons | `Attend: today` 8am wkdays → Slack (ok 09-11); `YouTube: What's Next` 9pm → Slack (ok 09-11); **new** `coder: morning repo check` 8am wkdays → Slack, skill `code-review` | `hermes cron list` |
| Bots | `coder` (Coder, boxy/blue), `researcher` (Researcher, round/green). Bot Mode managed via `profile.yaml ui_meta.hermes-bots` | roster shows both; `message_agent` fires from Bot Chat |
| GitHub | `gh` as tylerprogramming, `repo` scope | coder reviewed skoolos `9ea0712` live |
| Local model | Ollama `qwen3.8:latest` at 127.0.0.1:11434, vision confirmed | vision_probe read drawn text back exactly |

## Profiles

```
~/.hermes/profiles/coder/       SOUL.md (PR reviewer), skills/code-review, memories seeded w/ Tyler stacks
~/.hermes/profiles/researcher/  SOUL.md (YT research), memories seeded w/ content-repo conventions
```
Descriptions set via `hermes profile describe <name> --text "..."` — these are what teammates see in the roster.

## What works on camera (verified)

1. **Desktop → Slack.** Coder: "review latest commit on skoolos, post verdict to Slack." Runs skill, posts. ✅
2. **Bot → bot.** From researcher's *Bot Chat* (must be that exact session title): "tell @coder …" → `message_agent` → proc id → async reply. ✅ sent; reply landing not yet eyeballed
3. **Cron fired live.** `coder cron run "coder: morning repo check"` → Slack. (not yet run once — do before filming)
4. **Slack → agent.** DM @hermes from phone; it answers, searches sessions. ✅ (was already true)

## What does NOT work (and why — say it on camera or avoid)

- `@researcher` / `@coder` typed in Slack → nobody. They are not Slack users. Needs one Slack app per profile (manifest at `~/.hermes/slack-manifest.json`, rename, install, paste `xoxb`/`xapp` into that profile's `.env`).
- `@hermes` in Slack cannot hand off to other bots. `message_agent` is injected **only** into the session titled `Bot Chat` (hard-coded gate in `tools/bot_mode_dm.py`). Gateway sessions have other titles. So: **desktop is where you talk to a bot, Slack is where bots talk to you.**
- Nous Portal has no paid credits → managed web/TTS/browser tools off. Local + gh + Slack are unaffected.

## Self-created skills (13) — what to show

Strong: `attend-skool-crm` (3 files, repo constants), `slack-brief-cards` (powers the live crons), `clickup-project-tracking`, `claude-to-hermes-skill-porting` (perfect for the CC-users angle), `local-llm-runtime-operations`.
Honest beat: `jarvis`, `jarvis-hud`, `jarvis-ops`, `jarvis-ops-hud` — four skills for one project. "It drifts; here is the curation step." One line, not a section.

## Tina's structure (29:40) vs ours

She: hardware → desktop install → 5 features → 7-min memory (4 tiers) → local models → **ends on Discord `@Hermes build a Pomodoro app` + parallel bots.**
Us: same spine, half the explainer, and the ending beats hers: Bots tab handoff → real PR on GitHub → Coder pings Slack. Three surfaces, one story.

## Next (in order)

1. Open desktop Bots tab, confirm both bots + avatars render.
2. `coder cron run "coder: morning repo check"` once; confirm Slack card shape.
3. Optional: second Slack app for Coder only (pays off the ending).
4. Rewrite 057 script to 30 min with these beats.

## Files

- Video package: `~/content/youtube/videos/057-hermes-agent-start-here/`
- Pokemon test render (parked, not for this video): `~/YouTube Agency/pokemon-tcg/video/001-intro-30s/out/001-intro-30s.mp4`
