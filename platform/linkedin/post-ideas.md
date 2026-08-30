# LinkedIn Post Ideas

Working queue. Built 2026-08-19 from the formats in `BRAIN/linkedin/creatives.md` and the rules in
`BRAIN/linkedin/brain.md`, applied to work Tyler has actually done.

Each idea names its **format**, **hook lane**, and **creative**. Formats and lanes come from the evidence files.
Nothing here uses a money amount, a controversy hook, or a client case study, per the rejected list.

Mark ideas `[USED yyyy-mm-dd, N impressions]` as they go out so this doubles as a test log.

---

## Tier 1: build posts (the 31,875 shape, ceiling is highest)

These need a video, a repo, or a working system to point at. One per video, minimum.

1. **Give Claude Code real access to your apps** (045). Stack: arcade.dev, Gmail, Calendar, Drive, Docs, Slack,
   ClickUp. 9 steps. Already drafted at `youtube/videos/045-arcade-connect-apps/social/linkedin.md`.
   *Creative:* pipeline architecture diagram.

2. **The morning-brief agent** (046). Calendar plus Gmail into a day summary with flagged replies and drafts,
   then the same job moved into a scheduled script so it runs without you.
   *Lane:* accomplishment. *Creative:* diagram plus a screenshot of a real brief it produced.

3. **Build an MCP server with no code** (048). Assemble a gateway, get a hosted URL, `claude mcp add`, use it.
   *Creative:* terminal screenshot at the moment it connects.

4. **Ship your own custom MCP server** (049). Write a tool, deploy it, auth and hosting handled.
   *Creative:* before/after diagram, local tool versus deployed endpoint.

5. **The content operation that runs out of one folder of text files.** Markdown packages, skills, no app.
   The folder framing is already the best-performing frame on Instagram (171), and the transfer test is why.
   *Lane:* contrast. *Creative:* a real screenshot of the repo tree.

6. **Every video on the channel, from research to upload, as one chain of slash commands.**
   `/yt-search` → `/transcribe` → `/yt-package` → `/yt-seo` → `/yt-chapters` → `/yt-shorts` → `/yt-upload`.
   *Creative:* the chain as a horizontal pipeline diagram.

7. **Replacing a paid tool with 200 lines and the official API.** The Blotato to `/yt-upload` move, and what
   you get back: real tags, real scheduling, custom thumbnails.
   *Lane:* mistake/threat. *Creative:* side-by-side screenshot.

8. **A skill is a folder with one file in it.** The anatomy of SKILL.md, frontmatter through workflow steps,
   using a real one from the repo end to end.
   *Creative:* the actual file, syntax highlighted.

---

## Tier 2: breakdown posts (the untested format with the best odds)

Explain how something respected actually works. Architecture over personality. See `creatives.md`.

9. **How Claude Code's skill system is actually structured**, and why a markdown file beats a prompt library.
10. **What MCP actually does under the hood**, in the five minutes nobody spends on it.
11. **Why per-user OAuth is the real wall for agents**, not tool-calling. The 7-day Google re-auth failure is
    the concrete anchor, and it is already the strongest line Tyler has written this year.
12. **How the Claude Agent SDK differs from a plain tool-use loop**, and when the extra machinery earns its keep.
13. **Breaking down a Fortune 500 AI deployment pattern** at a level a marketer cannot reach. Tyler is an AI
    engineer at Pfizer with 8 years at IBM and JPMorgan Chase. Nothing confidential, just the shape of how real
    enterprise AI work differs from what the timeline shows.

*Creative for all of these:* a diagram he draws, or a screenshot of the real thing running. Not a stock photo.

---

## Tier 3: tactical first-person posts (the 10,000-impression shape)

Hook, credibility stat, the belief you dropped, four or five tactical lines, the principle, no CTA, one photo.

14. **How I record and ship a video in a day** without an editor, and the four things that made it possible.
    *Creative:* real photo of the filming setup.
15. **Everything I stopped doing manually this year**, as a list. Transcription, chapters, thumbnails, SEO,
    social copy, uploads.
    *Creative:* handwritten list, photographed. Untried format, near-zero effort.
16. **What running a whole-life tracker taught me about building agents**: the logging surface matters more than
    the model.
17. **The automation I built and then deleted**, and why the maintenance cost beat the time saved.
    *Lane:* mistake/threat. Honest, and nobody posts these.

---

## Tier 4: insight posts (filler, caps around 551)

Confession or correction only. Never process narration. PAS when stuck.

18. **"I never learned the video editor."** Already did 213. The lane works. Run the sibling: *I never learned
    the design tool either*, about the thumbnail pipeline.
19. **"Most people automate the wrong thing first."** The 55-impression version failed because it stayed
    general. Rewrite it with one specific job, real timings, and the actual output.
20. **The part of agent work nobody films**: the reconnect, the silent failure, the run that dies at 3am and
    tells no one.

---

## Standing rules for everything in this file

- Close on a **comment or DM ask**, never a click. Link goes in the body as reference, Skool link lives in the
  profile slot.
- **Every post gets a visual.**
- Skool CTA on roughly **1 post in 3**, not every post.
- No em dashes, no hashtags, no bold, no money amounts, no hype words.
- Reply to every comment personally, same day. That is the reach multiplier, and it is currently at zero.
