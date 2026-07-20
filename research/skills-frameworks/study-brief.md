# Skills Frameworks Study Brief - 2026-07-21

Prep for videos #32 (Pocock plugin) and #33 (Superpowers). Repos cloned here.

## Matt Pocock's skills (mattpocock/skills, 20.4K stars, plugin v1.2.0)

Organized: engineering/ (17 skills), productivity/ (5), misc/, personal/.
Plugin = managed bundle, auto-updates ("subscribe, don't fork"). Release imminent
(X-pulse watches @mattpocock).

The ones that transfer to a BUSINESS (demo these in #32):
- /handoff - compacts a conversation into a handoff doc for the next session
  (universal: end a planning session, hand to tomorrow's session)
- /research - spawns a BACKGROUND agent to research against primary sources
  while you keep working (works for niche research, not just APIs)
- /grill-me -> /grilling - relentless interview to sharpen a plan (works on a
  content plan or offer as well as a design)
- /wayfinder - plans work too big for one session as decision tickets on an
  issue tracker; explicitly "domain-agnostic - engineering work, course
  content, whatever fits the shape" (his own words - quote this on camera)
- /teach - learn anything interactively
Engineering-only (name, don't demo): /tdd, /implement, /code-review,
/domain-modeling, /triage, /to-spec, /to-tickets.

## Superpowers (obra/superpowers, plugin v6.1.1 - INSTALLED user-scope)

14 skills + SessionStart hook (~715 always-on tokens). The pipeline:
brainstorming (HARD GATE: no building until design approved - "every project,
regardless of perceived simplicity") -> using-git-worktrees -> writing-plans
(assumes implementer has "zero context and questionable taste") -> subagent
TDD execution -> fresh-agent code review -> finishing-a-development-branch.
Install demo for camera: /plugin marketplace add obra/superpowers-marketplace
then /plugin install superpowers@superpowers-marketplace.

## Test findings (2026-07-21)

- Headless test (claude -p, build task in ~/jarvis): the brainstorm gate did
  NOT fire - Claude went straight to implementation. The gate is strong
  guidance, not an enforced wall; engagement differs by mode/context. This is
  an honest, differentiated take for video #33 - test it INTERACTIVELY on
  camera (where the SessionStart hook + skill system engage properly) and
  report what actually happens, both ways if they differ.
- Side artifact: the test produced a good design for [ / ] keyboard cycling of
  Jarvis primary cards (in the test output) - could apply to ~/jarvis later.

## Demo plans

#32 (film within 48h of plugin release): install the plugin live -> run
/research on a niche question while doing something else -> /grill-me on this
week's content plan -> /handoff to end the session -> verdict: what an
engineer's skill system gives a business owner, and what it doesn't ->
"here's what business-native skills look like" -> 17-skills video + repo.

#33 (any slot): freestyle Claude vs Superpowers pipeline on the same real task
(e.g. plan + build one new business skill). Show the gate interrogating you,
the written plan artifact, the fresh-agent review. Calm verdict: the
discipline is the product; markdown is the delivery mechanism.
