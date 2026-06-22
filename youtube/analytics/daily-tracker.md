# Daily Video Performance Tracker

> Updated daily. Views/likes/comments pulled via YouTube API. CTR is Studio-only (screenshot). Retention/AVD/subs-gained need the Analytics API token (re-auth - see note at bottom).

## Claude Code Skills Masterclass (`9ZsZgnWrs_E`) — live 2026-06-21
| Date | Views | Likes | Comments | CTR | AVD / Retention | Subs | Notes |
|---|---|---|---|---|---|---|---|
| 06-21 (d1) | 178 | — | — | 2.8% | 3:06 / ~14% | +2 | Thumbnail A → B swap (CTR soft). 100% like ratio. |
| 06-22 (d2) | 196 | 8 | 1 | (screenshot) | (screenshot) | (screenshot) | +18 views/day — slowing, not breaking out. Thumbnail B live. |

## How the daily update works
- **I pull automatically (YouTube API, working):** views, likes, comments per video.
- **You provide (Studio screenshot):** CTR (always Studio-only) + retention curve. Just paste the Reach/Engagement screenshots like before.
- **Needs token re-auth to pull programmatically:** retention %, AVD, subs gained, traffic sources (Analytics API).

## ⚠️ Analytics API token expired (2026-06-22)
The analytics token (`~/.claude/analytics/yt_token.json`) expired. To let me pull retention/subs/traffic again, re-auth once in your terminal:
`! python3 ~/.claude/skills/analytics/yt_analytics.py --days 1` (opens a browser, approve, token re-caches)
Until then: I track views/likes daily via API, you drop a Studio screenshot for CTR/retention/subs.
