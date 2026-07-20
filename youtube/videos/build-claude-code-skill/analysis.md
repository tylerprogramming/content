# Analysis — Build a Claude Code Skill from Scratch

## Source Video Analysis

**Reference:** "How to build Claude Skills Better than 99% of People" — Ben AI
**URL:** https://youtube.com/watch?v=X3uum6W2xEI
**Views:** 161,622 | **Duration:** 18:36 | **Uploaded:** 2026-02-24

**Secondary Reference:** "5 Claude Code skills I use every single day" — Matt Pocock
**URL:** https://youtube.com/watch?v=EJyuu6zlQCg
**Views:** 146,127 | **Duration:** 16:42 | **Uploaded:** 2026-03-16

### Structure Breakdown (Ben AI)

| Timestamp | Section | Purpose |
|-----------|---------|---------|
| 0:00–3:00 | Why skills matter | Skills vs custom GPTs, n8n, Codex — "sits in the middle" |
| 3:00–5:30 | What a skill is | SKILL.md + reference files + scripts + assets |
| 5:30–6:20 | Progressive disclosure | How agents load skills without overloading context |
| 6:20–7:30 | Skills vs plugins | Plugins = bundled skills + commands + connectors |
| 7:30–9:00 | Three layers of skills | General, marketplace, company-specific |
| 9:00–11:45 | How to build — planning | Step back, define process, gather reference files |
| 11:45–14:30 | Building framework | Name, goal, context/MCPs, step-by-step, rules, output |
| 14:30–17:00 | Live demo | Infographic skill — QA boxes, variations, self-learning |
| 17:00–18:00 | Sharing + plugins | Zip file, GitHub, plugin marketplace |
| 18:00–18:36 | CTA | AI Accelerator |

### What Works Well
- Strong "why" before the "how" — builds urgency before showing the product
- Framework is clear: name → goal → context → process → rules → output
- Progressive disclosure concept is genuinely insightful and underexplained elsewhere
- Infographic demo shows clear before/after (bad first version vs polished final)
- Self-learning concept (save approved outputs as examples) is smart and unique
- QA box / human-in-loop design angle is interesting (UX for AI)

### Weaknesses / Gaps (Our Opportunities)
- **Uses Claude Cowork UI, not Claude Code CLI** — most viewers use the terminal, not Cowork
- **No actual file creation shown** — you never see a SKILL.md being written from scratch
- **No front matter explanation** — name, description, allowed-tools, user-invocable are never shown
- **Abstract demo** — the infographic skill is hard to replicate; no one else has that API setup
- **Heavy on theory** — 9+ minutes before any building starts
- **No iteration loop shown** — says "iterate" but doesn't show the cycle clearly
- **No GitHub/sharing workflow** — mentioned briefly, no demo

### Our Differentiation
- **Live file creation** — open terminal, write SKILL.md from scratch, test it
- **Show the front matter** — the metadata that makes skills actually trigger correctly
- **Build something universally useful** — hook writer = applicable to any founder doing content
- **Show the iteration** — write, test, see problem, fix one thing, test again
- **Reference files explained hands-on** — not abstract, actually create examples.md
- **Less theory, more building** — 30 seconds of why, 12 minutes of how

---

## Web Research

### Official SKILL.md Structure (2026)
```yaml
---
name: skill-name          # lowercase, hyphens, required
description: What it does + trigger phrases (this controls auto-invocation)
argument-hint: [optional hint for args]
allowed-tools: Read, Write, Bash, WebSearch  # limit what Claude can use
user-invocable: true      # can user invoke with /skill-name?
---
```

**Key insights:**
- `description` field = how Claude decides when to trigger skill automatically
- `allowed-tools` = security + focus (don't give bash access to a writing skill)
- Progressive disclosure: only metadata loaded at startup, SKILL.md loaded on trigger, reference files loaded when instructed
- Skills are stored at `~/.claude/skills/<skill-name>/SKILL.md`

### Skill Building Best Practices (Community)
- Keep SKILL.md focused on PROCESS — move extra context to reference files
- Add examples of good outputs — biggest single quality improvement
- Use rules section to handle edge cases (things that went wrong in testing)
- Build self-improving skills: instruct Claude to save approved outputs as examples
- Iterate continuously — skills are never "finished"
- Two ways to build: (1) do task manually → ask Claude to save as skill, (2) instruct skill from scratch

### Market/Community Context
- Anthropic/skills GitHub repo: **87,000+ stars** as of March 2026
- Skills marketplaces emerging: SkillsMP, Smithery, claude-skills.cc
- Predictions: skills will become monetizable, SaaS will launch branded plugins
- awesome-claude-code: curated community skills library (growing fast)

### Competitive Landscape (from yt-search "claude code skills")
| Views | Duration | Title |
|-------|----------|-------|
| 562K | 2:54 | What are skills? (Official Anthropic) |
| 203K | 16:15 | Claude Code Skills Just Got Even Better |
| 161K | 18:36 | How to build Claude Skills Better than 99% |
| 146K | 16:42 | 5 Claude Code skills I use every single day |
| 131K | 16:42 | Claude Skills: Build Your First AI Marketing Team |

**Gap:** Nobody shows building a skill from scratch in the terminal with actual file creation. All existing videos either use the Cowork UI or show pre-built skills.

### Matt Pocock's Key Insights (secondary reference)
- Skills encode process so AI has "a strict path it can walk down every single time"
- His best skills: /grill-me (3 sentences — tiny but powerful), /write-a-prd, /tdd
- Demonstrates that simple skills (3 sentences) can be just as powerful as complex ones
- Frame: "You have a fleet of engineers with no memory — process is everything"

---

## Sources

- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)
- [Skill Authoring Best Practices — Anthropic](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [How to Build a Production-Ready Claude Code Skill — Towards Data Science](https://towardsdatascience.com/how-to-build-a-production-ready-claude-code-skill/)
- [Building Skills for Claude — Innobu](https://www.innobu.com/en/articles/building-skills-for-claude-complete-guide)
- [A Mental Model for Claude Code: Skills, Subagents, and Plugins](https://levelup.gitconnected.com/a-mental-model-for-claude-code-skills-subagents-and-plugins-3dea9924bf05)
- [Claude Code Skills vs MCP vs Plugins](https://www.morphllm.com/claude-code-skills-mcp-plugins)
- [awesome-claude-code GitHub](https://github.com/hesreallyhim/awesome-claude-code)
- [Claude Skills Explained — Lenny's Newsletter](https://www.lennysnewsletter.com/p/claude-skills-explained)
- [Claude Skills Tutorial — AI Productivity Coach](https://aiproductivitycoach.com/claude-skills-tutorial/)
