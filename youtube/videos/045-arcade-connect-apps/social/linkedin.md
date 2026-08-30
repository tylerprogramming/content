# LinkedIn - 2026-08-19 - BUILD mode
**Topic:** 045 Arcade Connect Apps - giving Claude Code real access to Gmail, Calendar, Drive, Docs, Slack and ClickUp
**Scorecard:** 9/10 (video URL is a placeholder until 045 is live)
**Image brief:** "Give Claude Code Real Access" banner over a left-to-right pipeline diagram: Claude Code → arcade.dev gateway → Gmail / Calendar / Drive / Docs / Slack / ClickUp
**Supersedes:** `linkedin-v1-insight-197imp.md` (the insight-mode version, posted 2026-08-17, 197 impressions, 0 comments)

---

I have been wiring Claude Code into real apps for months now, and the part almost nobody warns you about is not the connecting. It is the auth.

Anything Google related makes you reconnect every seven days unless you are a full production app. So you build something that genuinely helps, you walk away, and a week later your agent has quietly stopped working and never told you.

In my latest video I walk through how I actually solve that now, using arcade.dev as the MCP runtime that holds the per-user OAuth for you. In 9 steps you go from a terminal that can only talk, to an agent taking real actions in your real accounts:

✅ Reads a live thread straight out of your Gmail inbox
✅ Writes the summary up as an actual Google Doc
✅ Files that Doc into a named Google Drive folder
✅ Posts the same summary into a Slack channel
✅ Checks your Google Calendar so it knows what your day looks like
✅ Creates ClickUp tasks without you ever touching an API token

Video: [PASTE 045 URL]

🎥 Video Preview, here is what we build together:

👉 Step 1: Create your first MCP gateway on arcade.dev
👉 Step 2: Pick only the tools you need, starting with three Gmail tools
👉 Step 3: Choose who is allowed to connect to it
👉 Step 4: Paste one command to add the gateway to Claude Code
👉 Step 5: Authorize once, then run the first real test
👉 Step 6: Rebuild it as a multi-tool gateway, 65 tools across five apps
👉 Step 7: Turn off the servers you do not want Claude reaching for
👉 Step 8: Run the five-step prompt, Gmail to Google Doc to Drive folder to Slack
👉 Step 9: Add ClickUp to a live gateway, and hit the mistake everybody makes

There is no server to build, no tokens to hardcode and no scopes to fight. You pick your tools, paste one command, authorize once, and it keeps running. You can add your whole team to it without anyone handling a token.

I left my own mistake in the cut on purpose, because it catches everyone: if you add a tool after the gateway already exists, you have to re-authenticate before Claude can use it.

If you have a five-step thing you do by hand every week, this is the setup that can take it.

👇 Tell me the one workflow in your week you would point this at first.

---

## Image brief

**Format:** single landscape image, LinkedIn feed native (1200x627 or 1200x1200).

**Top strip:** branded banner, high contrast, short. `GIVE CLAUDE CODE REAL ACCESS`. Match the "Build AI Agents" banner treatment from the 31,875-impression post: bold black type on a saturated block.

**Body:** left-to-right architecture diagram of the actual pipeline.

```
   Claude Code  ──▶  arcade.dev gateway  ──┬──▶  Gmail
   (terminal)        (holds per-user       ├──▶  Google Calendar
                      OAuth, 65 tools)     ├──▶  Google Drive
                                           ├──▶  Google Docs
                                           ├──▶  Slack
                                           └──▶  ClickUp
```

**Node labels must use real product wordmarks/logos** for Gmail, Google Calendar, Google Drive, Google Docs, Slack, ClickUp and arcade.dev. Recognizable logos are part of why this format travels.

**Optional callout badge** on the gateway node: `one command · authorize once`.

**Why an architecture diagram and not a thumbnail:** this is the frame people screenshot and repost. Reposts are what carried the 31,875 post out of the follower graph (12 reposts, only 2 comments). A talking-head thumbnail does not do that job.

## Notes

- **Scorecard 9/10.** Fails check 5 (video link in body) only because 045 is not uploaded yet per `youtube/notes/status.md`. Paste the URL before posting. Do not move it to the first comment.
- **Named tools: 8** (arcade.dev, Claude Code, Gmail, Google Calendar, Google Drive, Google Docs, Slack, ClickUp) against a floor of 5.
- **Credibility line** is the seven-day Google re-auth failure, kept from the v1 post. It was the strongest thing in that draft and it survives here.
- **Skool CTA deliberately omitted.** Objective is authority first, Skool second, roughly 1 post in 3. The v1 version already carried the Skool link, so this one closes on the build ask instead.
- **Direct comparison available:** v1 (insight mode, same topic, same week) did 197 impressions. If this format is the driver rather than topic timing, this should clear it by a wide margin. This is the first real test of the open question logged in `BRAIN/linkedin/brain.md`. Report the 7-day number back and the brain gets updated.
