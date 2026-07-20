# Analysis: Claude Code /btw Side Questions

## Source Video Analysis

**Source:** [/btw command video by competitor](https://youtu.be/ZbKNpn0woDY) (5:10)

### Structure Breakdown

| Timestamp | Duration | Segment | Purpose |
|-----------|----------|---------|---------|
| 0:00-0:09 | 9s | Hook — "most useful feature ever" | Hook (bold claim) |
| 0:09-0:50 | 41s | The problem — opening new threads wastes tokens | Pain point setup |
| 0:50-1:45 | 55s | /btw intro + basic use cases | Teaching |
| 1:45-2:46 | 61s | Benefits recap — cheaper, unified context | Reinforcement |
| 2:46-3:39 | 53s | How to use it — syntax and dismiss keys | Tutorial |
| 3:39-5:07 | 88s | Setup instructions (VS Code, terminal mode) | Tutorial |
| 5:07-5:10 | 3s | Quick CTA/sign-off | CTA |

### What Works Well
- Strong opening bold claim grabs attention
- Clear pain point — 10-20k token cost per new window is concrete and relatable
- Shows the side panel in action while main thread continues
- Good pacing, stays under 5 minutes

### Weaknesses / Gaps
- Only covers basic use cases (correcting instructions, asking about a skill)
- Never explains limitations (no tool access, single response only)
- Doesn't compare /btw to alternatives (new session, background agents, subagents)
- Focused on VS Code/AntiGravity setup — terminal users left out
- Claims "twice the tokens" savings but never shows real numbers
- No advanced use cases demonstrated
- Doesn't explain it's ephemeral (not saved to history)

### Target Audience
VS Code / AntiGravity users, intermediate Claude Code familiarity.

---

## Web Research

### What /btw Actually Is (Official Docs)

From [Claude Code Interactive Mode Docs](https://code.claude.com/docs/en/interactive-mode#side-questions-with-%2Fbtw):

- `/btw <question>` — ask a quick question without adding to conversation history
- **Full visibility** into the current conversation context
- **No tool access** — answers only from what is already in context (can't read files, run commands, or search)
- **Single response** — no follow-up turns
- **Ephemeral** — appears in a dismissible overlay, never enters conversation history
- **Low cost** — reuses the parent conversation's prompt cache
- **Works while Claude is working** — runs independently, does not interrupt the main turn
- **Also works when idle** — not just during active processing
- Dismiss with **Space**, **Enter**, or **Escape**

Key quote from docs: "/btw is the inverse of a subagent: it sees your full conversation but has no tools, while a subagent has full tools but starts with an empty context."

### Community Reception

- Overwhelmingly positive — developers say it fills a crucial gap in agentic workflows
- "Side conversations mean more productivity and less wasted time" — common sentiment
- Solves the stop-and-restart cycle for 10-30 minute tasks
- Some bugs reported on GitHub (issues #33168, #14804)

### Related Multitasking Features in Claude Code

| Feature | Context | Tools | Persistent | Cost |
|---------|---------|-------|------------|------|
| /btw | Full conversation | None | No (ephemeral) | Minimal (cached) |
| New session | Empty | Full | Yes | High (cold start) |
| Subagent | Empty | Full | Yes (in parent) | Medium |
| Background agent | Task-scoped | Full | Yes | Medium |
| Worktree | Isolated repo copy | Full | Yes | Medium |

### Existing YouTube Content

- One reference video (5:10, surface-level, VS Code focused)
- No deep-dive tutorials found on YouTube specifically for /btw
- Most coverage is blog posts and news articles
- Content gap: nobody has done a concise, clear "here's exactly what /btw does and doesn't do" video

### News & Articles

- [Blockchain News: Claude Code Adds /btw Side-Chain Chats](https://blockchain.news/ainews/claude-code-adds-btw-side-chain-chats-latest-productivity-boost-for-developers)
- [Daily.dev: Claude Code adds /btw command](https://app.daily.dev/posts/claude-code-adds-btw-command-for-side-conversations-while-the-agent-is-working-1p5qf8k4y)
- [BaristaLabs: Claude Code's /btw Command Fixes One of the Most Annoying Parts](https://www.baristalabs.io/blog/claude-code-btw-side-conversations-smb-2026)
- [wmedia.es: Ask Questions While Claude Code Is Working](https://wmedia.es/en/tips/claude-code-btw-side-question)
- [Voice LaPaas: Claude Code Adds /btw for Instant Side Queries](https://voice.lapaas.com/claude-code-adds-btw-for-instant-coding-side-queries/)

## Sources

- [Claude Code Interactive Mode Docs](https://code.claude.com/docs/en/interactive-mode#side-questions-with-%2Fbtw)
- [BaristaLabs Blog](https://www.baristalabs.io/blog/claude-code-btw-side-conversations-smb-2026)
- [wmedia.es /btw Guide](https://wmedia.es/en/tips/claude-code-btw-side-question)
- [GitHub Issue #33168](https://github.com/anthropics/claude-code/issues/33168)
- [GitHub Issue #14804](https://github.com/anthropics/claude-code/issues/14804)
- [Blockchain News](https://blockchain.news/ainews/claude-code-adds-btw-side-chain-chats-latest-productivity-boost-for-developers)
- [Daily.dev Post](https://app.daily.dev/posts/claude-code-adds-btw-command-for-side-conversations-while-the-agent-is-working-1p5qf8k4y)
- [Claude Code Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [Claude Code Async Workflows](https://claudefa.st/blog/guide/agents/async-workflows)
