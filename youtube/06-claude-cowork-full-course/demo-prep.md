# Demo Prep - What to Stage Before You Film

The course only lands if the demos are real and visibly finish on screen. Stage everything below BEFORE you record. I have already scaffolded the safe local sample files in `demo-assets/` - the rest are your real accounts.

Legend: 🟢 = I built it for you in `demo-assets/`  |  🟡 = you prep it (real account, ~5 min)  |  🔴 = swap in real material before filming

---

## Module 1: Setup
- 🟡 A clean empty `Cowork` folder in Documents to point at on camera.
- 🟡 Have the desktop app NOT yet pointed at a folder so the "choose your folder" step is real.
- First task on camera: create `welcome.md`. No prep needed.

## Module 2: File Management and Documents
- 🟢 **Organize demo:** `demo-assets/messy-client-folder/` - already filled with a realistic messy client onboarding pile (contract, two invoices, intake form, proposal, notes, w9 placeholder, bad filenames). Copy it into your Cowork folder before filming. Note: the invoices say "[redacted on camera]" and the w9 is a placeholder so you never show real financials.
- 🟢🔴 **Document demo:** `demo-assets/competitor-research/` - text stand-ins for 3 competitors. For the best on-screen look, swap these for REAL screenshots of competitor channels/pricing pages (see the `_README` note in that folder). Either works, real screenshots look better.

## Module 3: The Memory System
- 🟡 Start with NO `CLAUDE.md` so the "have it interview you" step is live and real.
- 🟡 Have a 5-question answer set in your head: who you are (SWE + AI channel/community), audience (business owners not devs), format preference (markdown, recommendation on top), one rule (no dollar amounts in titles).
- 🟡 For the "it already knows my voice" proof: use an account that has real prior usage so the draft genuinely sounds like you. If filming on a fresh profile, be honest and say "after a few weeks of feedback it gets here" and show a saved example.

## Module 4: Research and Analysis
- 🟢 **Weekly report demo:** `demo-assets/analytics/youtube-analytics-last7days.csv` + `youtube-analytics-prior-week.csv` - already built with realistic numbers including your real recent video titles. Cowork builds a week-over-week report with recommendations from these.
- 🔴 Optional upgrade: drop in a real YouTube Studio screenshot or a CSV export from your channel for full authenticity.
- 🟢 **Gap analysis demo:** reuse `demo-assets/competitor-research/` (or real transcripts) for the "find the gaps" spreadsheet.

## Module 5: Connectors - THE ONE THAT NEEDS REAL PREP
You cannot fake connectors, they hit live accounts. Decide and set up before you film.

- 🟡 **Gmail (do this one):** connect your real Gmail. Tip for a clean, safe demo: use a secondary inbox, or a label/filter view, so you are not exposing private threads on camera. Or do the demo, then blur sensitive subject lines in the edit. Have the connector ALREADY approved before the take so you only show the triage, not the OAuth wait. Then re-show the "add connector" flow separately so the steps are on camera without the dead time.
  - Prompt ready: "Go through my Gmail from the last 48 hours. Sort into needs reply, FYI, newsletter, can delete. Draft replies in my voice. Save a triage report to my folder."
- 🟡 **Google Drive (do this one):** make a Drive folder called `Scripts` and drop 5-10 of your real video scripts in it (you already have these). Powers the "two sources together" demo.
  - Prompt ready: "Read my last 10 scripts from my Drive folder Scripts, cross reference with the analytics report in my Cowork folder, and tell me which topics I write most, which perform, and 5 I should cover. Save locally."
- 🟡🔴 **Notion (optional - swap if you do not use it):** if you keep a content calendar in Notion, use it. If not, the script already says swap to a Google Sheet. Pick one before filming so you are not deciding live.

## Module 6: Claude in Chrome
- 🟡 Be logged into the dashboard you will demo (YouTube Studio is the natural one) in Chrome before the take.
- 🔴 **Verify on camera** what is actually live in YOUR app version - the feature name and availability have shifted during rollout. Show what is real; do not promise a button the viewer may not have.
  - Prompt ready: "Open my YouTube Studio, go to analytics for the last 28 days, and pull views, watch time, and top 5 videos into a report in my Cowork folder."

## Module 7: Skills and Plugins
- 🟡 Have run the weekly-report task a couple times already so "save this as a skill" is believable. The analytics CSVs from Module 4 make this easy - run that report twice before filming, then capture it as a skill on camera.
- 🟡 Open the plugins/extensions area once beforehand so you know what is there and can speak to it accurately.

## Module 8: Scheduled Tasks - THE CAPSTONE, prep carefully
This is the most-shared section, so the examples have to be real and finished.

- 🟡 **Show existing outputs:** have 1-2 REAL prior outputs ready to display (a past morning triage report, a past Monday analytics report). These prove the tasks actually run. If you do not have history yet, run a task manually a few times this week so you have genuine output files to show.
- 🟡 **Build one live:** the Monday analytics report is the cleanest one to create on camera, because it uses the safe sample CSVs, not private email.
  - Task ready: "Every Monday at 8am, pull my latest analytics, compare to last week, and save a performance report with 3 recommendations to my Cowork folder."
- 🔴 **Honesty flag (must do on camera):** confirm whether the task runs with the app closed or needs it open, in YOUR setup, and say it plainly. Do not claim it runs "in the cloud while you sleep" unless you have verified it. Protects your verifiability brand.

## Module 9: Cowork + Claude Code
- 🟡 Have your Claude Code terminal open with your real skills list visible (you have ~25+). Blur or skip anything with keys/tokens.
- 🟡 A simple flow diagram (you talking through it, or a graphic for the editor): Monday scheduled task -> review -> Code skills for production -> graduate repeated tasks into Code.

## Module 10: First Week + Prompt Pack
- No prep. The 5 starter prompts are in the script. Optional: put them in a free PDF / Skool resource and mention it.

---

## On-screen safety (every module)
- Never show API keys, tokens, passwords, or `.env` contents. Blur or close those windows.
- Blur or redact real revenue numbers and client PII. The sample files already use placeholders for this.
- For Gmail, use a secondary inbox or blur sensitive subject lines in the edit.

## Fastest path to "ready to film"
1. Copy `demo-assets/messy-client-folder` and `demo-assets/analytics` into your live Cowork folder.
2. Connect Gmail + make the Drive `Scripts` folder (10 min).
3. Run the weekly-report task 2-3 times this week so you have skill + scheduled-task history to show.
4. (Optional) swap the competitor `.txt` stand-ins for real screenshots.
Do those four and every demo in the course is real and stage-ready.
