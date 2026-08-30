# 051 - Scrape ANY Website With This AI Agent (2026) - Full Script

Target length: 11-13 min. Voice: Tyler (humble, "so" openers, short sentences, hedges, no hype, no em dashes). Face never sits bare >5-7s; every claim gets a synced visual within ~1-2s. Webcam PIP stays up on every screen-share.

Uses hook OPTION A verbatim for 0:00-0:41 (see hooks.md). Script below picks up the shape from the cold open and carries it through the full build.

---

## 0:00 - 0:41 | COLD OPEN (see hooks.md, Option A)
[SHOW: empty sheet filling itself, face at 0:08, chips, credibility at 0:27, roadmap card + open loop at 0:35, hard cut to terminal.]
[NOTE: do not re-record the intro here, it lives in first-2-min-opening.md second-by-second.]

---

## 0:41 - 1:40 | SECTION 1 - What we're actually building (the map)

[SHOW: simple 3-node diagram builds element by element: WEBSITE -> AGENT (Claude Code) -> SPREADSHEET + BRIEF.]

"So before we touch anything, let me show you the whole thing on one screen. It's three pieces.

[SHOW: node 1 highlights.]
"One, a website. Any list-shaped page you keep checking by hand. Today I'm using a remote jobs board, but this is the same for product prices, event listings, a directory, whatever.

[SHOW: node 2 highlights, Claude Code logo.]
"Two, the agent. That's Claude Code. It's the brain. I just talk to it in plain English.

[SHOW: node 3 highlights, sheet + brief icons.]
"Three, the output. A clean spreadsheet, and then a short brief that tells me what in the sheet actually matters.

[SHOW: Firecrawl logo drops onto the arrow between node 1 and node 2.]
"There's one more tool sitting in the middle, and it's the piece that changed since a couple years ago. It's called Firecrawl. Think of it as the agent's eyes. Claude tells it 'go read this page,' and Firecrawl does the annoying part. It renders the JavaScript, it deals with the sites that try to block bots, and it hands back clean text instead of a mess of HTML.

[SHOW: chip: "old way: write selectors" gets a red strike; chip "new way: ask in English" appears.]
"And that's the big shift. The old way, you'd write code to find the exact spot on the page where the price lived, and it broke every time the site changed. We're not doing that. We just describe what we want."

---

## 1:40 - 3:30 | SECTION 2 - Setup (the five minutes)

[SHOW: screen-share, terminal. Webcam PIP bottom-right stays up the whole section.]

"Okay, setup. This is the only install-y part, and it's about five minutes. I'll go slow.

[SHOW: type `npx -y firecrawl-mcp` in terminal, highlight command.]
"First I add Firecrawl to Claude Code as an MCP server. If MCP is a new word, don't worry about it. It just means I'm plugging a tool into the agent so it can use it. One command.

[SHOW: Firecrawl signup page, free tier badge "500 credits, no card".]
"Then I need an API key. I go to Firecrawl, sign up, grab the key. The free tier gives you 500 page credits to start and it doesn't ask for a card, so you can follow along for free.

[SHOW: `/firecrawl:setup`, paste key, success message.]
"Back in Claude Code I run the setup, paste the key in once, and that's it. Now the agent can see the web.

[SHOW: NOTE card: "That's the whole setup."]
"That's genuinely the whole setup. From here it's just talking.

[NOTE: keep this section tight. The setup is not the value, the build is. Do not linger.]

[SHOW: quick aside card: "Later: Apify + Playwright" with two small icons.]
"Quick note for later, not now. If you ever hit a site that needs you to log in, or something like LinkedIn or Google Maps that's really locked down, there are two other tools you'd reach for, Apify and Playwright. I'll mention where they fit at the end. For ninety percent of pages, Firecrawl on its own is all you need. So let's use it."

---

## 3:30 - 5:40 | SECTION 3 - First scrape (get SOMETHING back)

[SHOW: browser, the live jobs board. Push-in / scroll over the listings.]

"Here's the page. It's a remote jobs board. A bunch of listings, company, title, sometimes a salary, a link to apply. Normally if I wanted this in a spreadsheet I'd sit here and copy each one. Let's not.

[SHOW: Claude Code, type the prompt.]
"I go to Claude Code and I just say it plainly: 'Scrape this page and show me what's on it.' And I paste the URL.

[SHOW: Firecrawl runs, returns clean markdown of the listings. Highlight-sweep the clean text.]
"Watch what comes back. It's not raw HTML. Firecrawl already stripped the ads, the nav, the footer, all the junk, and handed back clean readable text of just the listings. This is the part that used to take real work.

[SHOW: NOTE card: "clean text, not HTML".]
"So already, with one sentence, I have the content of the page in a form the agent can actually reason about.

[SHOW: talking head, brief.]
"But a wall of text isn't a spreadsheet yet. Right now it's everything on the page. I don't want everything. I want specific fields, in order, every time. So that's the next step, and it's the one trick that makes all of this clean."

---

## 5:40 - 7:50 | SECTION 4 - The schema trick (clean, structured data)

[SHOW: kinetic build of a tiny JSON schema, fields appearing one at a time: title, company, location, salary_range, tags, apply_url.]

"This is the part I want you to steal. Instead of asking for 'the page,' I tell the agent the exact shape I want back. It's called a schema, and it's smaller than it sounds.

[SHOW: each field highlights as he says it.]
"I say: for every listing, give me a title, a company, a location, a salary range, the tags, and the apply link. Six fields. That's the schema.

[SHOW: Claude Code prompt: "Use Firecrawl extract with this schema across the whole page. Return one row per listing."]
"Then I tell Claude to use Firecrawl's extract on the whole page with that shape. And here's the nice part, I don't tell it where those fields are on the page. I don't say 'the price is in the third column.' It figures that out. It reads the page like a person would and fills in the boxes.

[SHOW: JSON results stream in, one clean object per listing. Push-in.]
"And look, now every listing is a clean little record. Same six fields, every row, even though some listings formatted their salary differently or hid it in a different spot. That's the thing that used to be so painful, and now it just handles it.

[SHOW: chip: "missing field -> null, not broken".]
"When a listing doesn't have a salary, it just leaves that one blank instead of falling over. So the whole run doesn't break because one row was weird.

[SHOW: NOTE card: "This schema is the reusable part."]
"So the schema is the real move here. Once you can describe the fields you want, you can point this at almost anything. Swap the six job fields for product name, price, rating, and link, and you're scraping a store instead. Same exact trick."

---

## 7:50 - 9:30 | SECTION 5 - Into a spreadsheet (the payoff, again)

[SHOW: Claude Code prompt: "Write these to a CSV / Google Sheet, one row per listing, header row."]

"Now the easy part. I just tell Claude to write these rows to a spreadsheet.

[SHOW: file appears, rows fill in visibly. This is the callback to the cold open. Push-in.]
"And there it is. Same shot from the very beginning of the video. An empty file, and now it's a full clean spreadsheet, one row per job, sorted columns, ready to filter. I didn't touch a cell.

[SHOW: open the sheet, scroll, filter by salary. Webcam PIP stays up.]
"I can sort it by salary. I can filter to just the remote ones. It's just data now, it's mine, I can do whatever I want with it.

[SHOW: talking head, brief.]
"And if I stopped right here, honestly, this would already beat an hour of copy-pasting. But this is the exact place most tutorials end. A file. And a file is still work. I still have to read all of it. So let's do the part that actually saves the time."

---

## 9:30 - 11:00 | SECTION 6 - Make it useful (data becomes an answer)

[SHOW: Claude Code prompt: "Read the sheet. Rank the top 10 roles for a senior backend engineer who wants remote and pays well. One line why for each."]

"Here's the step that turns this from a scraper into something I actually use. The data is already in front of the agent. So I just ask it a question about the data.

[SHOW: Claude reads the sheet, returns a ranked top-10 list with a one-line reason each. Highlight-sweep the reasons.]
"I say, out of all these, give me the top ten worth applying to for what I care about, and tell me why in one line each. And it reads its own spreadsheet and hands me a shortlist.

[SHOW: NOTE card: "Data -> answer, not data -> file".]
"That's the whole difference. The old video, and most videos, get you to a file. This gets you to an answer. I went from a website to a ranked shortlist, with reasons, without reading a single listing myself.

[SHOW: talking head.]
"And you can point that last question at anything. If it's prices, ask which competitor undercut you this week. If it's listings, ask which three are new since yesterday. The scrape is the boring middle. The question at the end is where it pays off."

---

## 11:00 - 12:00 | SECTION 7 - Make it repeatable (close the open loop)

[SHOW: Claude Code, saving the whole flow as a reusable skill / slash command. A markdown file appears.]

"Last thing, and this closes the loop I opened at the start. Right now I typed a few sentences. I don't want to retype them next week.

[SHOW: the flow saved as a `/scrape` command, one line to re-run.]
"So I have Claude save the whole thing as a reusable command. Now tomorrow, it's one line. 'Run the scrape.' Same schema, same sheet, same shortlist, fresh data.

[SHOW: chip: "and you can schedule it".]
"And because it's one command, you can put it on a schedule and just get the shortlist in the morning without opening anything. I'm not going to set that up here, but that's the door it opens.

[SHOW: aside card: "When Firecrawl isn't enough: Apify (LinkedIn/Maps/Amazon) / Playwright (login + forms)".]
"And that Apify and Playwright note from earlier, here's where they land. If a page needs you to log in, or fill something out, Playwright drives the actual browser for you. If you want really structured data off a big platform like LinkedIn or Maps, Apify has ready-made scrapers for those. Same agent, you just hand it a different tool. But start with Firecrawl. It'll cover almost everything you actually run into."

---

## 12:00 - 12:40 | CLOSE + CTA

[SHOW: talking head. Recap chips flash: 1 setup, 2 schema, 3 sheet, 4 the question.]

"So that's it. Four steps. Plug in Firecrawl, describe the fields you want, write them to a sheet, then ask the agent a real question about the data. That last one is the part to remember.

[SHOW: soft CTA card, folded in, then snap back.]
"If you build one of these, I'd genuinely like to see what page you pointed it at. Tell me in the comments, I read them. And everything I set up here, the schema, the command, I'll drop the templates for the community, link's below.

[SHOW: end card, one related video.]
"Pick one page you check every single week and just point it at that one. Start there. That's the whole thing. I'll see you in the next one."

[HARD CUT. No long outro.]

---

## Production checklist (from teardown)
- [ ] Face delayed to ~0:08 over the filling-sheet b-roll.
- [ ] Credibility (IBM/Chase/Pfizer) delayed to ~0:27-0:35, framed as "I'd still rather have the agent do it," never "you don't need to be a developer."
- [ ] Roadmap card by 0:35, open loop = "the last step almost nobody does" + "make it repeatable," closed in Section 7.
- [ ] Cold-open shot (empty sheet fills) is called back verbatim at 7:50.
- [ ] Webcam PIP up on every screen-share (Sections 2-7).
- [ ] Every number/claim gets a synced visual within ~1-2s; no bare talking head >5-7s.
- [ ] Setup section stays tight (it is not the value).
- [ ] Real on-screen receipts: real page, real clean-text return, real filling sheet, real ranked list.
