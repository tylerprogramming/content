# The AI Agency - Current State
Last updated: 2026-04-22

Top-level tracker for the Skool relaunch. Points to everything else.

---

## POSITIONING (locked)

- **Name:** The AI Agency
- **Mechanism:** The AI for Business Stack (not an "AIOS" — "Stack" is more honest + defensible)
- **Promise:** Ship one working AI automation in 14 days
- **Audience:** Business owners who want AI to make money or save time (not tool demos)

## TIERS (locked)

| Tier | Price | What's in it |
|---|---|---|
| Free | $0 | 7 courses, 100+ modules, skills library, 14-Day Ship Challenge, monthly Q&A, bi-weekly New Member Orientation |
| Starter | $9/mo | Prompt packs, replay vault, monthly build lab, 15-min onboarding call |
| Builder | $27/mo | Full skills library (updated monthly), weekly live workshops + Q&A, 45-min strategy audit |

**Risk reversal:** Complete the 14-Day Ship Challenge → first month of Builder free (manually comped).

## RECURRING SESSION CALENDAR (locked, May 2026 events created)

| When (ET) | Session | Tier |
|---|---|---|
| 1st Friday 1:00-2:00 PM | Community Q&A | All |
| 2nd + 4th Friday 12:30-1:00 PM | New Member Orientation | All |
| Every Wednesday 5:00-6:00 PM (4x/mo) | Builder Weekly (alt Workshop/Q&A) | Builder |
| 2nd Sunday 10:30-11:30 AM | Monthly Build Lab | Starter + Builder |
| 4th Sunday 10:30-11:30 AM | Monthly Q&A + AI Updates | Starter + Builder |

Tyler's monthly live load: ~8 hours.

**May event IDs:** `~/content/skool/may-events.json`

---

## THE 14-DAY SHIP CHALLENGE

The backbone path for every new free member. Detailed in `~/content/skool/launch-drafts-v2.md`.

**Completion = 3 things:**
1. Automation deployed in their business
2. 60-sec Loom showing it working
3. Post in the Builds category with Loom + one metric

**Completers get:**
- Named in weekly Builder Roundup
- Access to Shipped Builders private channel
- First month of Builder free (manually comped)

---

## DOCUMENT MAP

| File | Purpose |
|---|---|
| `~/content/skool/STATE.md` | This file - top-level tracker |
| `~/content/skool/launch-drafts-v2.md` | Pinned post + About page + VSL script (v2, Harut-edited). **USE THIS, NOT v1** |
| `~/content/skool/launch-drafts.md` | v1 drafts (kept for history, do not ship) |
| `~/content/skool/14-day-drip-and-roundup.md` | 4 email drips (Day 0/7/14/16) + weekly Builder Roundup post template |
| `~/content/skool/restructure-plan.md` | Original 7-day sprint plan (partially outdated - still has $27→$47 step we're NOT doing right now) |
| `~/content/skool/filming-schedule.md` | What to film for the new courses |
| `~/content/skool/5-features.md` | (existing) |
| `~/content/skool/may-events.json` | Skool calendar event IDs for May 2026 (created via API 4/20) |

---

## DONE ✅

- May 2026 calendar events created (9 events, all privacy defaulted to "All members" - need tier-gating)
- Tyler manually renamed the 5 events that had "Free" or "$" in titles
- 3 launch drafts v2 (pinned / About / VSL) with Harut critique applied
- 14-Day Ship Challenge structure written
- 4-email drip + Builder Roundup template drafted
- `skool_calendar.py` script built: list/create/update/delete + tier-gating support (privacy_type 0/1/2/3 all supported)
- `/harut` skill on tap for all future conversion-sensitive drafts

## NEXT (ordered) 📋

**Tyler does manually in Skool UI:**
1. Create **"Builds"** category (2 min)
2. Delete dead draft courses (Create Your First Crew Here, First CrewAI Agent)
3. Set up 3 membership questions (business type, AI goal, email)
4. Tier-gate the 6 paid May events (4 Wednesdays = Builder, 2 Sundays = Starter+)

**Tyler reviews:**
5. Read `launch-drafts-v2.md` and `14-day-drip-and-roundup.md`, approve or flag changes
6. Decide final name for weekly posts ("Builder Roundup" or something else)

**Claude does after Tyler approves:**
7. Post the new pinned post + About page copy (via `/skool` + manual for About)
8. Schedule 4-email drip via `/email` (Resend)
9. Create the 3 new free courses via API (AI for Your Business, 5-Minute Carousel, Free Skills Library)
10. Expand Claude Code course with Cowork modules 4-6
11. Update Start Here to point into the 14-Day Ship Challenge as Day 1
12. Rename n8n course + fold Build AI Automation modules in

**Tyler films (content window needed):**
13. About page VSL (3-4 min dirty Loom, 3 hook variations — script in `launch-drafts-v2.md`)
14. Welcome video for updated Start Here
15. Carousel app walkthrough
16. Claude Code + Cowork intro ("why this matters for your business")

**Launch target:** May 1 - first Community Q&A. All Front-of-house stuff (pinned, About, VSL, Builds category, drip) must be live by then.

---

## PRICING NOTES

- Keeping $27 for Builder for now (not raising to $47 until we have 3+ case studies)
- If May feels right and we have proof, test $27 → $47 in June or July
- Decide at the 30-day post-launch review
