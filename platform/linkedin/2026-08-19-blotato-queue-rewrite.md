# Blotato LinkedIn Queue: Audit + Rewrites

Pulled 2026-08-19. 9 LinkedIn posts scheduled, Aug 19 through Sep 7, all to account `4987` (Tyler Reed personal).
Audited against `BRAIN/linkedin/brain.md` + `creatives.md`.

**Nothing has been pushed to Blotato. These are drafts pending your go-ahead.**

---

## The audit

| # | ID | Fires (UTC) | Opener lane | Media | Named tools | Steps | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | `2834649` | **Aug 19 19:00 (today)** | vague/curiosity | none | 1 | none | rewrite |
| 2 | `2834660` | Aug 21 19:00 | correction ✅ | none | 1 | none | keep text, add image |
| 3 | `2834767` | Aug 24 19:00 | confession ✅ | none | ~4 | none | → BUILD post (video MVr2GrAjrgQ) |
| 4 | `2834771` | Aug 26 19:00 | correction ✅ | none | 1 | none | duplicate of #1, cut or repurpose |
| 5 | `2834776` | Aug 28 19:00 | confession ✅ | none | ~5 | none | duplicate of #3, cut |
| 6 | `2834658` | Aug 31 19:00 | **process narration ❌** | none | 2 | none | → BUILD post (video lfwt5tFfaSo) |
| 7 | `2834666` | Sep 2 19:00 | advice framing (weak) | none | 1 | none | duplicate of #6, cut |
| 8 | `2834675` | Sep 4 19:00 | correction ✅ | none | 1 | none | keep text, add image |
| 9 | `2834705` | Sep 7 19:00 | accomplishment ✅ | none | 2 | none | → BUILD post (video MLfyfNj1JrI) |

### Five findings

1. **Zero images on all nine.** Every one is `mediaUrls: []`. This breaks the top confirmed rule and the
   deck's only universal instruction. Uniform, and the single highest-leverage fix.
2. **No video link on any of them.** The Twitter and Pinterest versions of the same content carry the YouTube
   link. LinkedIn, which has the highest buying-power audience and where a link demonstrably did not suppress
   the 31,875 post, is the one platform not carrying it. That is backwards.
3. **Nine posts, four ideas.** Context-in-a-file (#1, #4), 23-concepts (#3, #5), skills-are-files (#6, #7, #8),
   the pipeline (#9). Each said twice inside two weeks.
4. **No named stacks, no step lists.** Every post is flowing prose. Zero ✅ outcome bullets, zero 👉 steps,
   and the tool count runs 1-2 against a build-post floor of 5.
5. **The Skool URL sits raw in the body of #2, #5, #8.** That is a click CTA competing with the question
   underneath it. It belongs in the profile link slot.

### What is already right

Every post closes on a real question the reader can answer from their own work. That is scorecard check 8b and
it is the one thing the queue does correctly. The confession and correction openers on #2, #3, #5, #8, #9 sit in
the lanes that produced 213, 366, and 551. **The writing is not the problem. The packaging is.**

### Timing note

All nine fire at 19:00 UTC, which is 3pm ET, the middle of the afternoon slump. The deck's slots are before 9am
or 4pm onwards. Shifting to 20:00-21:00 UTC would land in the after-work window. Deck-sourced and unconfirmed,
so low confidence, but it costs nothing.

---

# The rewrites

## A. Replaces #3 (`2834767`, Aug 24) — video MVr2GrAjrgQ

I have used Claude Code nearly every day for a year, and I still only use about six of its features.

There are 23 concepts in it. That is the number that makes people quit, because the first session is a black screen and a blinking cursor and no idea which six matter.

So in the new video I walk through all 23 live in the terminal, no slides, and show which three actually change how the tool feels. In 5 steps you go from a blinking cursor to finishing real work:

✅ Reads your whole project before it touches a single file
✅ Writes your rules once into CLAUDE.md and follows them every session after
✅ Proposes an approach in Plan Mode before it builds anything
✅ Checkpoints every edit so /rewind can undo any path you go down
✅ Pulls in outside tools through MCP servers when you actually need them

Video: https://www.youtube.com/watch?v=MVr2GrAjrgQ

🎥 Video Preview, here is the order I would learn them in:

👉 Step 1: Understand the context window, Claude's short term memory, and why answers quietly get worse as it fills
👉 Step 2: Run /init to generate your first CLAUDE.md, then edit it by hand
👉 Step 3: Use Plan Mode with Shift+Tab so it explores before it writes
👉 Step 4: Keep /compact and /clear in reach so you are managing context instead of fighting it
👉 Step 5: Learn /rewind before you need it, not after

The tool is not the hard part. Knowing what good looks like is the hard part, and Claude will build the wrong thing very quickly if you never say.

Never expect it to be a hundred percent right. Eighty or ninety, then you nudge it the rest of the way.

👇 Which of the 23 are you fuzzy on right now?

**Image:** screenshot of the terminal in Plan Mode with the proposed plan on screen. Real UI, not a graphic.

---

## B. Replaces #6 (`2834658`, Aug 31) — video lfwt5tFfaSo

**Note: the current opener is "I used to explain the same thing to Claude over and over." That is the exact
process-narration template that produced the account's three worst posts (40, 53, 55). It is the only opener in
the queue sitting in a lane the data says loses.**

People think building a Claude Code skill needs an SDK or a framework.

It is a folder with one file in it called SKILL.md. A name at the top, the tools it is allowed to use, then plain English instructions below. That is the whole thing.

In the new video I open three of mine on camera and then build a new one from scratch. In 6 steps you go from retyping the same paragraph every day to one command:

✅ Pulls a clean transcript out of any YouTube video with Whisper
✅ Asks your journal questions and saves a dated file without being told the format
✅ Writes a full video package, titles through filming guide, from one topic
✅ Runs the same way in every project once it lives in ~/.claude/skills
✅ Rewrites itself when you ask it to change something

Video: https://youtu.be/lfwt5tFfaSo

🎥 Video Preview, here is how you build one:

👉 Step 1: Do the task once with Claude, correcting it as you go, until the output is right
👉 Step 2: Say "make a skill out of this" and let it write down what you just did
👉 Step 3: Open the generated SKILL.md and read it, it is plain markdown
👉 Step 4: Set the frontmatter, the name, the description, and which tools it may use
👉 Step 5: Decide where it lives, the project folder for one repo or ~/.claude/skills for everywhere
👉 Step 6: Fix it in the file, not in the chat, the next time it gets something wrong

The bar is lower than people expect. If you can explain your process to someone new on your team, you can write one.

And the honest part: a skill does not make Claude smarter. It removes the retyping. The judgment is still yours every time.

👇 What is the one task you would turn into a skill first?

**Image:** the actual SKILL.md open in an editor, frontmatter visible. Proof screenshot, per `creatives.md`.

---

## C. Replaces #9 (`2834705`, Sep 7) — video MLfyfNj1JrI

I run the entire research and planning side of my YouTube channel out of a terminal.

Starting a video used to cost two or three hours before I wrote a word. Search the topic, click through a dozen videos, take notes, open a doc, outline from scratch. Half the time I skipped it and winged it.

In the new video I show the four Claude Code skills that replaced all of it. In 4 steps you go from a topic to a filmable package:

✅ Searches YouTube with yt-dlp and ranks what is actually working right now
✅ Pulls the full transcript of any competitor video with Whisper
✅ Writes the package, titles, hooks, script and filming guide, after doing its own web research
✅ Generates the thumbnail through the Kie.ai image API
✅ Saves every output as markdown in the folder where the video lives

Video: https://www.youtube.com/watch?v=MLfyfNj1JrI

🎥 Video Preview, here is the chain:

👉 Step 1: /yt-search pulls the newest videos on a topic, sorted by views, and writes a research report
👉 Step 2: /transcribe downloads and transcribes the top competitor video
👉 Step 3: Talk to Claude about how that video is structured and where the gaps are
👉 Step 4: /yt-package turns your topic and your angle into titles, hooks, a full script and a filming guide
👉 Step 5: /yt-thumbnail generates the cover

This video was planned by that same system. The script I read on camera came out of it, and so did the thumbnail you clicked to get here.

None of this is a product. They are markdown files. You can build the same thing for any workflow you repeat every week.

👇 If you built one skill for your own work, what would it take off your plate first?

**Image:** the pipeline as a left-to-right diagram, /yt-search → /transcribe → /yt-package → /yt-thumbnail,
with the real output filenames under each node.

---

## D. Replaces #1 (`2834649`, TODAY Aug 19) — video aOECs8oPZ2c — **PUSHED 2026-08-19**

> **Opener revised before pushing.** The original draft opened "Everyone is calling this stuff an AI employee,"
> which was almost word for word the Aug 21 post (`2834660`). Two Cowork posts with the same opener two days
> apart. Replaced with a continuity + authority line per build-post part 1.
>
> **Knock-on: `2834660` (Aug 21) is now redundant.** It covers the same video with the same honest-take angle.
> Cut it or replace it. Options: promote build post A (Beginner Blueprint) from Aug 24 into that slot, or write
> a breakdown post from the Tier 2 list in `post-ideas.md`.

I have been handing real work to Claude Cowork for a few weeks now, and the thing that decides whether it works for you is not the model. It is the folder you point it at.

Cowork is Claude with access to a folder on your computer. That is the honest description. It opens your files, reads them, builds new ones, and runs a task on a schedule without you.

In the new video I hand it real work on camera. In 5 steps you go from a chat box to something that actually finishes tasks:

✅ Opens a folder on your machine and treats it as its working memory
✅ Turns six phone photos of receipts into an expense spreadsheet
✅ Reads a CLAUDE.md in that folder before every task, so drafts come back sounding like you
✅ Triages Gmail and pulls reports off the web
✅ Runs the same job every Monday on a schedule, before you have had coffee

Video: https://www.youtube.com/watch?v=aOECs8oPZ2c

🎥 Video Preview, here is the setup:

👉 Step 1: Open Cowork in the Claude desktop app, not the website, this is where most people go wrong
👉 Step 2: Point it at one folder, that folder becomes its memory
👉 Step 3: Drop a CLAUDE.md in there with how you write and what good output looks like
👉 Step 4: Hand it something mechanical and checkable first, not something that needs judgment
👉 Step 5: Put the recurring version on a schedule once you trust the output

It is still a research preview. It gets things wrong, and sometimes it does the task sitting right next to the one you asked for.

So the line I use is simple. Anything I can check in ten seconds, it gets. Anything where being 85 percent right is worse than not doing it, I keep.

👇 What is the boring repeatable job in your week you would hand off first?

**Image:** screenshot of the receipts-to-spreadsheet output. Real artifact, highest-proof creative available.

---

# Proposed schedule

| Fires | ID | Action |
|---|---|---|
| Aug 19 | `2834649` | ✅ **LIVE (electric)** — build post + system diagram rendered in the electric palette. Text off `script.md` + real chapters. md5 verified. |
| Aug 21 | `2834660` | ✅ **LIVE (electric)** — 6-slide deck built with `/instagram-writer` (`THEME=electric`). Deck source `slides.json`, renders to `out/` incl. `carousel.pdf`. All 6 md5 verified. Caption CTA aligned to the deck's `Comment BLUEPRINT`. |
| Aug 24 | `2834767` | ⚠️ **now redundant**, the Aug 21 carousel covers the same video. Swap for a Tier 2 breakdown post. |
| Aug 26 | `2834771` | keep, best of the context-file versions, add image |
| Aug 28 | `2834776` | **delete**, duplicate of A |
| Aug 31 | `2834658` | replace with **B** (Skills build) |
| Sep 2 | `2834666` | **delete**, duplicate of B |
| Sep 4 | `2834675` | keep text, add image, drop the raw Skool URL |
| Sep 7 | `2834705` | replace with **C** (YouTube pipeline build) |

Result: 4 build posts alternating with 3 insight posts, each idea said once, every post carrying an image.

**Blocker on images:** Blotato needs a publicly reachable URL in `mediaUrls`. Screenshots have to be uploaded
first (`blotato_create_presigned_upload_url`). The text rewrites can go in now and images can follow.


---

## Rendering creatives (added 2026-08-19)

Images are rendered from HTML with headless Chrome, not generated by an AI image model. Exact label text every
time, which matters when a diagram carries eight product names. Reusable renderer:

```
python3 ~/.claude/skills/linkedin-writer/render.py spec.json outdir/
```

Shared stylesheet lives in that script. Build-post diagrams render at 1200x680 (landscape), carousel slides at
1200x1200 (square). Slide spec for the Aug 21 carousel is checked in next to its PNGs as `slides-spec.json`,
so it can be re-rendered or restyled without rewriting the copy.


---

## Creative system, as built (2026-08-19)

**House style**, sampled from the newest IG carousels (`platform/carousels/nine-workflows-editor-2-5`,
`my-mistakes-editor-5-5`, 2026-07-26): near-black ground `#141419`, coral accent `#E07355`, cream ink
`#F5F0EB`, mono for metadata and body, terminal cards with a green success line, coral rule across the top,
`tylerreedai` + counter header, `@tylerreedai` + `swipe →` footer.

Note the social-studio theme literally named `electric` is blue on near-white and is **not** this look. The
renderer hardcodes the sampled house palette rather than reading that theme file.

**Renderer:** `~/.claude/skills/linkedin-writer/render.py`, HTML to PNG via headless Chrome. Exact label text
every time, which AI image models cannot guarantee for diagrams carrying product names.

- Build-post diagram: 1200x760 landscape
- Carousel slides: 1080x1350, matching the IG carousels

**Diagram doctrine:** a build-post diagram shows the SYSTEM, not a chapter list. Three columns, what it reads
→ the thing that makes it work → what it makes, plus a band for when it runs. No timestamps.

**Known gap:** IG covers use a real darkened photo of Tyler at the desk under the coral highlight block. The
LinkedIn covers are currently flat dark because no photo was available. Compositing one in would close the last
visible difference.

**Gotcha:** this shell is zsh, whose arrays are 1-indexed. A bash-style `for i in 0 1 2 3 4 5` loop silently
drops the last item. It caused one failed slide upload. Use Python for upload and verification loops.


## Creative system, settled 2026-08-19

Carousels and PDFs render through `~/.claude/skills/instagram-writer/instagram_writer.py` from a
`slides.json` deck: `THEME=electric python3 instagram_writer.py <deck>/slides.json <deck>/out/`.
One command produces the slides **and** `carousel.pdf`.

Reference decks: `platform/instagram/arcade-mcp-gateway/`, `platform/instagram/first-claude-skill/`.
Spec: `~/.claude/skills/instagram-writer/SLIDES.md`.

Landscape build-post diagrams stay on `~/.claude/skills/linkedin-writer/render.py`, now retargeted
to the same electric theme file so the two renderers cannot drift.

Earlier attempts sampled the look from screenshots and got the palette wrong twice. Read the deck
JSON and the theme file, never a screenshot.


---

# Sweep completed 2026-08-19

| Fires | ID | Final state |
|---|---|---|
| Aug 19 | `2834649` | ✅ Cowork build post + electric system diagram |
| Aug 21 | `2834660` | ✅ 6-slide electric deck, `Comment BLUEPRINT` CTA |
| Aug 24 | `2834767` | ✅ **NEW** breakdown post: the 7-day OAuth wall + diagram |
| Aug 26 | `2834771` | ✅ **REPLACED** with the 009 Claude Design build post (`aiMZrj4zqo8`) + diagram. Old CLAUDE.md insight archived: it was the third CLAUDE.md beat in seven days. |
| Aug 28 | `2834776` | 🗑️ deleted, duplicate of Aug 21. Archived in `_archive-blotato-2026-08-19/` |
| Aug 31 | `2834658` | ✅ **NEW** skills build post (lfwt5tFfaSo) + diagram |
| Sep 2 | `2834666` | 🗑️ deleted, third skills-are-files post. Archived. |
| Sep 4 | `2834675` | ✅ **KEPT + FIXED** — raw Skool URL removed from the body (it competed with the question), diagram added. Best-written post in the queue. |
| Sep 7 | `2834705` | ✅ **NEW** pipeline build post (MLfyfNj1JrI) + diagram |
| Sep 9 | `2834711` | 🗑️ deleted, fourth skills-are-files post. Archived. |

All diagrams md5-verified against `platform/linkedin/diagrams/`. Specs in `diagrams/specs.json`.

**Every LinkedIn post in the queue now carries an image.**

## The BLUEPRINT deliverable

`platform/linkedin/lead-magnets/claude-code-blueprint/` - the guide, a CLAUDE.md template, and a
paste-ready DM. Needs a public URL dropped into `dm-reply.md` before Aug 21.


## Published video inventory (2026-08-19)

Definitive list, from `youtube_video_id.txt` in each package. The loose ids scattered through
`research/` are competitor videos, not ours - do not post from those.

| Package | Video | Used |
|---|---|---|
| 009-claude-design | `aiMZrj4zqo8` | Aug 26 |
| 012-skills-full-course | `9ZsZgnWrs_E` | free (overlaps the skills thread) |
| 023-claude-cowork-full-course | `aOECs8oPZ2c` | Aug 19 |
| 025-granola-claude-code | `nFen2thkbmg` | **free** |
| 026-ai-video-editor | `cdvi2ooarDc` | free (package warns it pivoted away from a build) |
| 028-nano-banana-vs-gpt-image | `h5VtHSXY8Hc` | **free** |
| 030-claude-cowork-explained | `7ND_buIAQfA` | free (overlaps Aug 19) |
| beginner blueprint | `MVr2GrAjrgQ` | Aug 21 |
| skills system | `lfwt5tFfaSo` | Aug 31 |
| youtube workflow | `MLfyfNj1JrI` | Sep 7 |

**045 arcade is NOT published.** Its package still carries `REPLACE_045_URL`. The Aug 24 auth-wall
breakdown sets it up; give arcade its own build post the day the URL exists.

Genuinely unused ground: Granola, image-model comparison. The queue is otherwise all Claude
Code, Cowork and skills.
