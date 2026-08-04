# Course Outline (~30 min): Arcade MCP Across Claude Code, Cowork & the Web App

**Premise:** Build ONE Arcade Gateway (prebuilt MCP tools, auth handled), then plug the *same* gateway into Claude Code, Claude Cowork/Desktop, and claude.ai in the browser. Then do real "7-minute app" walkthroughs on each. Show that you connect it once and it works everywhere.

**The one-gateway spine (repeat this so it lands):**
- **Claude Code:** `claude mcp add arcade --transport http "<GATEWAY_URL>"`
- **Cowork / Desktop:** Settings → Customize → Connectors → Add custom connector → paste Gateway URL → authorize
- **Web (claude.ai):** same Connectors flow in the browser (Free = 1 connector; more on Pro/Max/Team)
- Custom connectors run from Anthropic's cloud, so the gateway must be a public URL (Arcade's is). Each tool authorizes via OAuth once.

---

## Module 0 — Cold open + why (0:00–2:30)
- Hook: "I connected Claude to my real Gmail, Calendar, and Slack — in the terminal, on my desktop, and in the browser — from one setup, in about 7 minutes."
- Why Arcade exists: connecting AI to your apps normally means fighting OAuth and tokens. Arcade is the runtime that handles auth. 7,500+ prebuilt tools.
- Your dev wedge: "I've built these integrations at Fortune 500s. The auth is the hard part. This removes it."
- What you'll have by the end: the same toolset working across all three Claude surfaces.

## Module 1 — Build the Arcade Gateway (2:30–7:00)
- Make an Arcade account → build a **Gateway** → pick tools (Gmail, Google Calendar, Slack, GitHub to start).
- Explain a Gateway = your chosen bundle of MCP tools behind one URL.
- Grab the Gateway URL. Note free vs paid tiers honestly.

## Module 2 — Connect all three surfaces (7:00–13:00)
- **Claude Code:** `claude mcp add arcade --transport http "<URL>"` → `claude mcp list` → run a tool → OAuth authorize popup. Done.
- **Cowork / Desktop:** Connectors → add custom connector → paste URL → authorize. Show the same tools appear.
- **Web (claude.ai):** Connectors → add custom connector → paste URL → authorize. Same tools, no install.
- Land the point: **one gateway, three surfaces, same tools.**

## Module 3 — Walkthrough 1: the 7-minute app in Claude Code (13:00–18:00)
- **Morning brief agent:** Gmail + Calendar → "What's my day, and which emails actually need a reply?" Put a **7-minute timer** on screen.
- Then take an action: "draft replies to the two that matter." Show it drafting (safe/draft first).
- Payoff: from nothing to a working agent in one sitting.

## Module 4 — Walkthrough 2: Cowork (the non-coder surface) (18:00–23:00)
- **Inbox triage + files:** in Cowork, "go through my unread, summarize what needs me, and draft replies" — plus a file task ("save the attachments to this folder").
- Point: Cowork is the desktop app for people who don't live in a terminal — same Arcade tools, friendlier surface.

## Module 5 — Walkthrough 3: the web app (anywhere, no setup) (23:00–27:00)
- **Quick action from the browser:** "summarize the open issues in my repo and post a standup to Slack" (GitHub + Slack), or a Calendar/meeting-prep task.
- Point: you're not at your machine — claude.ai + the same connector still does it.

## Module 6 — Which surface when + safety (27:00–30:00)
- **Code** = build/automate/dev, scriptable. **Cowork** = desktop, files + apps, non-coder power. **Web** = quick, anywhere, zero setup.
- Safety/governance: per-user OAuth, tokens never hardcoded, every action logged. This is why it's usable for real work, not a toy.
- CTA + the philosophy: stop building apps, assemble agents from tools. (Arcade link; disclosure if sponsored.)

---

## Example walkthroughs (pick/rotate; each is a "7-minute app")
1. **Morning brief** — Gmail + Calendar → day summary + reply triage. (Code)
2. **Inbox triage + draft** — reads unread, drafts in your voice, you approve. (Cowork)
3. **Repo → task** — GitHub → summarize issues, file the top one to ClickUp. (Web or Code)
   - Note: ClickUp is Tyler's task tool. If Arcade's catalog doesn't include ClickUp, use his existing ClickUp MCP connector in Claude Code alongside Arcade — the demo still works.
4. **Slack standup poster** — "post yesterday's wins to #standup." (Any)
5. **Meeting prep** — before a calendar event, pull the attendee's recent emails into a one-pager. (Code/Cowork)

## Notes
- Same honesty rules: no hype, show real runs, admit limits, keep everything in draft/safe first.
- Disclosure if this is a partner/sponsored piece (you worked with Arcade before).
- Long-form + the two short videos ("7 Minutes" title) can share footage — shoot the setup + walkthroughs once, cut the shorts from it.
- Open: confirm last year's Arcade video so this course builds on it.

## Sources
- Arcade: https://www.arcade.dev/  · Clients: https://docs.arcade.dev/en/get-started/mcp-clients
- Claude Code: https://docs.arcade.dev/en/get-started/mcp-clients/claude-code
- Claude custom connectors (remote MCP): https://support.claude.com/en/articles/11503834-build-custom-connectors-via-remote-mcp-servers
