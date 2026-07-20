# Analysis: Claude Code Skills That Run My Business

**Working slug:** `claude-code-skills-run-my-business`
**Reference video:** [Nate Herk - "I asked Claude Code to make me as much money as possible"](https://youtube.com/watch?v=iTY8Q449YNQ) (147,608 views, 28:12, uploaded 2026-06-25)
**Our angle:** Real skills that actually run a real content business - the honest counter to the staged demo.
**Target audience:** Creators and solopreneurs who are NOT developers.

---

## Source Video Analysis

### Structure breakdown

| Time | Segment | Purpose |
|------|---------|---------|
| 0:00 - 0:35 | Hook: "3x more money in 30 days" + "4 upgrades" | Bold claim + promise |
| 0:35 - 1:50 | Problem framing: Claude is tuned to feel productive, not make money | Set up the stakes |
| 1:50 - 7:50 | Upgrade 1: `/roast` skill (council of personas kills/reshapes your idea) | Named problem (sycophancy) + Elephant study + live demo |
| 7:50 - 16:45 | Upgrade 2: verification loop (Playwright, screenshot, stress-test forms) | NYU/Copilot study + live landing-page build |
| 16:45 - 21:15 | Upgrade 3: context management (`/context`, `/clear`, `/session-handoff`) | Context Rot study + status line demo |
| 21:15 - 25:35 | Upgrade 4: parallel subagents + `/goal` command | Anthropic multi-agent result + 6-file go-to-market build |
| 25:35 - 28:12 | Recap + free Skool CTA | Payoff + funnel |

### What works well
- **Every claim is backed by a named research study.** Sycophancy ("Elephant"), code vulnerabilities (NYU/Copilot 40%), context rot (18-model study), multi-agent (Anthropic 90%+). Reads as authority, not opinion.
- **One continuous build narrative.** He builds one fake product ("Cadence," a $9/mo YouTube-transcript-to-LinkedIn tool) start to finish, so every upgrade lands on something concrete instead of disconnected tips.
- **His own custom skills are the hook.** `/roast`, `/session-handoff`, `/goal` feel exclusive and give people a reason to join the Skool community to get them.
- **Problem -> study -> fix -> live proof** is a clean, repeatable beat structure.
- Strong, woven CTA to the free Skool community at every upgrade.

### Weaknesses / gaps (our opportunities)
1. **The product is fake and staged.** "Cadence" never ships, never gets a customer, never earns a real dollar. The title promises money; the video delivers a hypothetical. A real, already-running business is the obvious counter.
2. **Only 3 custom skills, all generic.** Idea-validation, handoff, goal-loop. Nobody with a genuine library of production skills shows their actual stack.
3. **Aimed at aspiring builders, not operators.** It's a "here's how you could" video. There's no coverage of a non-developer creator who already runs a live content business on Claude Code.
4. **28 minutes and demo-heavy.** A tighter, proof-first cut wins on retention.

### Target audience of the source
Aspiring AI builders / solopreneurs who want to make money with Claude Code but are early. Assumes light familiarity with Claude Code (knows what a terminal is), but explains subagents and skills from scratch.

---

## Our Differentiation

**Nate showed a staged demo. We show the real thing running.**

- His skills were built for the video. Ours (27+ and counting) already run a live content business day to day.
- We keep his winning *beat structure* (problem -> proof -> real demo) but every demo is a skill that's genuinely in production.
- We do NOT build a fake SaaS. The proof is the system that already exists: the content pipeline, the cron jobs firing on their own, the Skool automation.
- Audience shift: from "aspiring builder" to "creator/solopreneur who isn't a developer." Widest lane, least competed, matches the channel north star.

**On-screen demo anchors (chosen):**
1. **Content pipeline** - `/yt-search` -> `/transcribe` -> `/yt-package` -> `/social-copy`. Research to published, the most visual and relatable flow.
2. **Automation on autopilot** - `/yt-replier` + `/tiktok-replier` cron jobs and `/email` drips. The "it's running right now without me" proof.
3. **Skool + community ops** - `/skool` posting, member sync, classroom modules. Real business automation nobody else demos.

---

## Web Research

### What a Claude Code skill actually is (2026)
- A skill is a small folder with a single `SKILL.md` inside: YAML frontmatter (name + one-line description telling Claude *when* to use it) plus markdown instructions Claude follows when invoked.
- Claude Code's older "commands" (`.claude/commands/*.md`) and "skills" (`.claude/skills/*/SKILL.md`) have been **merged** - both now create the same `/slash-command` interface.
- Frontmatter options that matter: `disable-model-invocation: true` (only you can trigger it - good for side-effect skills like posting/sending), and `allowed-tools` (tools the skill can use without per-use approval).
- Takeaway for the video: the format is genuinely simple. That's the whole point - a non-developer can write one. Lead with that reassurance.

### Subagents, `/goal`, context (2026)
- **Subagents** each run in their own isolated context window with their own tools/permissions and return only a summary to the main session - which is exactly why they protect the main context from bloat.
- **`/goal`** shipped May 2026. Devs are reporting multi-hour autonomous runs (one 9-hour session: 45 commits, 41 subagent invocations, 4 chained goals). Set a goal when the finish line is objective.
- **Context management**: `/context` visualizes what's eating the window; `/compact` now runs immediately by loading a continuous session summary into a fresh context.
- These are hot but under-explained. Worth a quick, plain-English aside even in a creator-focused video.

### Market / landscape
- Claude Code hit **~$2.5B annualized run-rate by Feb 2026**; the average developer using it spends **~20 hrs/week** in it. Weekly active users doubled Jan 1 -> Feb 12, 2026.
- The official plugins marketplace had **101 plugins** (33 Anthropic + 68 partner) as of March 2026. The Agent Skills repo sits at **150K+ GitHub stars**.
- The "make money with Claude" YouTube lane is **saturated with aspirational/fake demos** (dozens of "How I'd start a $10K/mo one-person business" videos). A real operator showing a live system is the clear gap.
- There's already a Medium essay titled *"I Am Not a Developer. I Still Run My Whole Content Business on Claude"* - demand for the non-dev-operator angle exists, but almost nobody is covering it in video.

### Content gap = our video
No one who **actually runs a real content business** on Claude Code is showing their **real** skill stack to a **non-developer** audience. That's the whole video.

---

## Sources
- [Extend Claude with skills - Claude Code Docs](https://code.claude.com/docs/en/skills)
- [Create custom subagents - Claude Code Docs](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents - alexop.dev](https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/)
- [Claude Code Skills: A Practical Guide for 2026 - DEV Community](https://dev.to/muhammad_moeed/claude-code-skills-a-practical-guide-for-2026-3f6p)
- [Claude Code Sub-Agents Explained: Context, Cost, and Parallel Execution - MindStudio](https://www.mindstudio.ai/blog/claude-code-sub-agents-explained)
- [Long-Running Coding Agents: The 2026 Guide - O-mega.ai](https://o-mega.ai/articles/long-running-coding-agents-the-2026-guide)
- [I Am Not a Developer. I Still Run My Whole Content Business on Claude - Medium](https://dkspeaks.medium.com/i-am-not-a-developer-i-still-run-my-whole-content-business-on-claude-8341587102ef)
- [How to Automate Content Repurposing With Claude Code Skills - MindStudio](https://www.mindstudio.ai/blog/automate-content-repurposing-claude-code-skills)
- [claude-plugins-official - Claude Code Marketplace](https://www.claudepluginhub.com/marketplaces/anthropics-claude-plugins-official)
- [Claude Code Usage Statistics 2026 - SerpSculpt](https://serpsculpt.com/claude-code-usage-statistics/)
- [Claude Revenue and Usage Statistics (2026) - Business of Apps](https://www.businessofapps.com/data/claude-statistics/)
- [The Complete Guide to Building Skills for Claude - Anthropic](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

**Reference video URL:** https://youtube.com/watch?v=iTY8Q449YNQ
