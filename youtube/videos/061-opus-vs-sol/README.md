# 061: Opus 5.5 vs GPT-6 Sol, on my actual agents

Two Hermes profiles, `opus` (claude-opus-5-5) and `sol` (gpt-6-sol), same SOUL, same skills, same Slack.
Both on the 8am Coder cron since 2026-09-24 (the 3-day thread is the cold open).

| # | Use case | Prompt | Judged by |
|---|---|---|---|
| 1 | Website design (Attend landing) | prompts/1-website.md | looking, split screen |
| 2 | Code review, real skoolos commit | prompts/2-review.md | catches the stale $49/$147 comment or not |
| 3 | Write the Attend ad from the swipe file | prompts/3-ad.md | reading |
| 4 | Build a game (inbox triage) | prompts/4-game.md | playing |
| 5 | Last 50 videos, what to make next | prompts/5-videos.md | finds "10 to 17 min wins, courses die" or not |
| 6 | HyperFrames reel from 057 | prompts/6-reel.md | watching both; check --strict |
| 7 | Morning brief, same 4 files | prompts/7-brief.md | same 3 picks? numbers from files? |
| 8 | The bill + model-per-bot routing | (not a task) | two invoices, one config.yaml |

Run one: `cd inputs && hermes -p opus chat -q "$(cat ../prompts/5-videos.md)"` then same with `-p sol`.
Outputs land in `runs/<model>/<n>-<name>/`.
