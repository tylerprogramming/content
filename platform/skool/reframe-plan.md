# The AI Agency - Free Classroom Reframe Plan
Created: 2026-06-17 | Status: PROPOSAL (no live writes yet, awaiting Tyler approval)

Reframes the free classroom from a pile of tool-named courses into a single outcome-driven path with Claude Code + Cowork as the spine. Keeps the "AI for Business" positioning; changes the mechanism from n8n to Claude.

---

## THE PROBLEM (why reframe)

The free classroom has split-brain:
- **Locked positioning:** "AI for Business" - outcome-focused, business owners.
- **What's actually live:** the biggest courses are stale tool tech (n8n 49 modules, AI Agents/CrewAI 18 modules), while Claude - Tyler's actual brand, content gravity, Fortune 500 authority, and what every new video + the SaaS is about - is a thin 3-module afterthought.
- **Result:** a new free member sees a parking lot, not a path. No clear "start here → win → go deeper." The strongest asset (Claude) is buried; the headline is tech Tyler isn't even creating content about anymore.

Cowork has **zero presence** anywhere in the classroom, even though it's the next video and the most beginner-friendly Claude entry point.

---

## THE PRINCIPLE

1. **Keep the umbrella:** "AI for Business" stays. We are not contradicting the locked positioning or the Harut-reviewed messaging.
2. **Change the mechanism:** Claude Code + Cowork becomes the engine, not n8n. More defensible in 2026 - Cowork does what n8n does, no-code, and it's where market attention is.
3. **Path, not pile:** the free classroom becomes a 5-step journey a member walks in order, plus a deep "library" for the old material, plus utilities.
4. **Don't throw away work:** the n8n (49) + Agents (18) modules are demoted into a library, never deleted.

---

## BEFORE → AFTER (course map)

### LIVE NOW (8 courses)
| Course | Modules | Fate |
|--------|--------:|------|
| Start Here | 6 | KEEP (refresh) |
| Build Your First AI Automation | 9 | MERGE into Automation Library (or keep as beginner automation) |
| The n8n Beginner Course | 49 | DEMOTE → Automation Library |
| AI Agents + Automations | 18 | DEMOTE → Automation Library |
| Claude Code | 3 | RENAME + GROW → course #2 (the drip target) |
| Social Media AI | 2 | KEEP or fold into a content course |
| Monthly Live Builds | 2 | KEEP (utility) |
| Affiliate Links + Discount Codes | 1 | KEEP (utility) |

### AFTER (the reframed free path)
| # | Course name | Built from | Outcome promise | Modules |
|---|-------------|-----------|-----------------|--------:|
| 1 | **Start Here: Your AI Roadmap** | existing "Start Here" | "the path + the 14-Day Ship Challenge" | 6 |
| 2 | **Get AI to Do Your Work** *(Claude Code basics)* | rename "Claude Code" (3) + drip fundamentals #1-5 | first real win with Claude Code | 3 → ~8 |
| 3 | **Build Your Own AI Skills** | drip skills videos #6-7 + Skills Masterclass | make Claude do YOUR repeat work | 0 → ~4 |
| 4 | **Run Your Business Without Code** *(Cowork)* | NEW - Cowork Clearly Explained + workflow videos | the no-code payoff | 0 → ~3 |
| 5 | **Connect AI to Everything (MCP)** | drip MCP series #13-17 | go deeper / power user | 0 → ~5 |
| 6 | **The Automation Library** *(n8n + Agents)* | n8n (49) + AI Agents (18) + Build Your First (9) | "want the deep automation stuff? it's all here" | ~76 |
| - | Monthly Live Builds | keep | utility | 2 |
| - | Affiliate Links + Discount Codes | keep | utility | 1 |

New member now sees: **Start → Get AI to do your work → Build skills → Run your business on Cowork → Connect everything → (library for the deep divers).** A staircase, not a parking lot.

---

## FEED CATEGORY CLEANUP

Live labels: General discussion, Tech Support, Wins, AI Agents + Automations, **Category-1** (junk default).

- **Rename "Category-1" → "Claude"** (or "Builds") so the drip posts have a clean home and members can filter.
- Consider renaming "AI Agents + Automations" label → "Automations" (shorter, matches the library).
- Keep: General discussion, Tech Support, Wins.

---

## FUNNEL LOGIC (free → paid)

The free path should point straight at the paid offer. Current tiers (STATE.md): Free $0 / Starter $9 / Builder $27.

- Free path ends at "**Run Your Business Without Code (Cowork)**" + "Connect Everything (MCP)" - the member has now shipped something and tasted the power.
- Natural upsell: the paid tier = "done-for-you skills library + live help to build YOUR system" (Builder $27) and/or the SaaS product.
- **OPEN QUESTION (need from Tyler):** what exactly does the paid SaaS / Builder tier deliver, and to whom? Once known, lock course #4/#5 CTAs to ladder directly into it. Until then, CTAs point to the 14-Day Ship Challenge + Builder tier generically.

---

## EXECUTION STEPS (when approved - all via Skool API + Playwright, WAF)

1. **Verify live** - pull the real classroom tree + the 3 existing "Claude Code" module titles (avoid dupes).
2. **Rename** "Claude Code" course → "Get AI to Do Your Work" (keep id `92c3144920a3437880425ef5d14630ee`).
3. **Create** course "Run Your Business Without Code" (Cowork) - new set/course.
4. **Create** course "Build Your Own AI Skills".
5. **Create** course "Connect AI to Everything (MCP)".
6. **Create** course "The Automation Library"; move/group n8n + AI Agents + Build Your First under it (or rename one of them as the umbrella).
7. **Reorder** courses so the 5-step path sits on top, library + utilities below.
8. **Rename** feed label "Category-1" → "Claude".
9. Then run the **drip** (skool-drip-plan.md): each video → feed post + module in its course.

Note: course creation/rename/reorder via `api2.skool.com/courses` (PUT/POST) through Playwright browser context per reference_skool_classroom_api.md. Confirm before each write (standing rule).

---

## RISKS / CAUTIONS

- **Member whiplash:** some joined for n8n. Mitigate by keeping all n8n content live in the Library and posting a "we reorganized the classroom" note (Tyler did this before, 3/25).
- **Don't over-rename:** only the 2 high-value moves matter (Cowork home + clear start). Resist renaming everything to cute outcome titles at once.
- **Naming not final:** "Get AI to Do Your Work" etc. are proposals - lock once SaaS funnel target is known.

---

## RELATED
- `~/content/youtube/skool-drip-plan.md` - the every-other-day video drip that fills this structure
- `~/content/platform/skool/STATE.md` - positioning, tiers, sessions (April 2026)
- `~/.claude/projects/-Users-tylerreed/memory/reference_skool_classroom_api.md` - classroom API docs
