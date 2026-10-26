# REA (morluto/rea) - creator breakdown, 5 reference videos

Repo: https://github.com/morluto/rea - 193,733 stars, 47,239 forks (gh api, 2026-10-13). Created 2026-04-14, last push 2026-10-13.
Install: `npx rea-agents setup` (registers MCP server + "reverse-engineer-anything" skill in Claude Code, Codex, Cursor, Gemini CLI). Needs Node 22.19+/24.11+/26+.
What it is: an MCP + CLI that wraps Ghidra / Hopper / IDA, JADX, Chrome DevTools, etc. Returns pseudocode, assembly, call paths, module maps, network activity, each with evidence + unknowns. Static JS/Electron and .NET analysis need no native engine.

Transcripts: `~/content/transcripts/transcript_<id>.txt` (mlx-whisper, 2026-10-13).

| Video | Channel | Views | Length | Transcript |
|---|---|---|---|---|
| I Tested The Viral Github Repo To Reverse Engineer Anything | Nick Saraev | 841,336 | 10:47 | dAzs_rU6080 |
| The Fastest-Rising Repo on GitHub Is a Little Scary REA | Rob Shocks | 449,913 | 9:10 | OMobTlfjb8s |
| How To Use REA To Clone Any Software In Minutes | Eric Tech | 202,497 | 9:03 | FnB9tHKBJXQ |
| AI Is Making Every App Open Source | Better Stack | 95,519 | 4:53 | jtfpCGsbSJU |
| How to Reverse Engineer Anything in Claude Code | MG | 28,495 | 15:39 | nL9MmtrdcC8 |

yt-search 30-day run (`~/content/research/2026-10-13-reverse-engineer-anything.md`): 20 long-form, 0 Shorts. Its title filter missed Rob Shocks and Eric Tech. Not in that report's top 15 above #1: Escola de Aplicativos 95,508; lustoykov 39,904; Jack Roberts "I Tested the Viral Reverse Engineering Repo" 31,649 (16:46, untranscribed, closest format to Nick).

Not transcribed, worth a look: Sirio "Dear Higgsfield, I reverse engineered you in 12 hours" (433,955), AI Search "The AI unlock has begun" (935,856, may be broader).

## Nick Saraev (dAzs_rU6080) - the take-down angle

| # | Beat | Time | What he does on screen |
|---|---|---|---|
| 1 | Hype roundup | 0:00-1:08 | Reads tweets: Berman "software is done", Replit CEO "all software will soon be open source", "God help us all" |
| 2 | How it works | 1:08-2:08 | Diagram: you -> agent -> REA MCP -> Ghidra (2019) / Hopper (2011) / IDA (90s) + Chrome DevTools -> pseudocode, proof, unknowns -> agent loops |
| 3 | Install | 2:08-2:44 | Prompt: "hey, go download Reverse Engineer Anything, REA, and let me know when you're done." Runs in Orca terminal manager |
| 4 | Race demo | 2:44-4:44 | Pane 1: "use REA to rebuild the preview app on my Mac". Pane 2: "without using REA, rebuild the Mac preview app, the photo viewer one, and then serve me the result." |
| 5 | Result | 4:44-5:27 | Vanilla Opus finishes first. REA version takes ~3-4 min longer, near-identical, drawing faster, rotate, save |
| 6 | Take-down | 5:27-7:28 | "Nothing is super new." Tools are old (NSA Ghidra). "Haven't seen very good demos." Mocks GitHub star-chart intros |
| 7 | Business take | 7:28-9:13 | Wrapper apps get swallowed by models, value ladder moved, IP risk if you resell clones |
| 8 | Thesis | 9:13-10:47 | "You don't need REA." Vanilla agents get there in ~2/3 the time; Claude Code will absorb this in 1-2 months |

Rhythm: hype quotes -> explain -> live A/B race -> contrarian verdict -> business implication. He wins on the contrarian take, not the demo. His demo is shallow (Preview.app, judged by eye, no evidence shown, no numbers).

## The other four, one line each

| Creator | Demo target | Method | Verdict they land on |
|---|---|---|---|
| Rob Shocks | His own "vault" binary, stripped symbols, 242 functions named `fun_<addr>` | REA + Ghidra finds `check_unlock_code`, writes a key generator, gets in with `AGNT-1001` | Code was never the moat. Sandbox it, keep approvals on, prompt injection risk |
| Eric Tech | Wispr Flow (installed app) | Prompt: find Whisper Flow in desktop folder, use REA to inspect, use official site as background, build small working version | Clone works (hotkey, multilingual, local). Brand is the moat. No evidence shown |
| MG | His own compiled iOS app (WellView AI), Today tab only | A/B: with REA vs "never ever use REA". Without: 40 min, ~$12, wrong order, missing features. With: 1h12m, ~$40, functionally much closer, UI still off | REA wins functionality, vanilla wins look. Combine REA + screenshots |
| Jack Roberts (8rBiTpcoTrM, 31,649, 16:46) | Calendly, Typeform, Trello | Never runs REA. Claims REA is "420,000 lines of TypeScript, 789 pulled into the skill" and vanilla is faster (unverified). Pastes a screenshot + Notion prompt into Base44 (sponsor), one-shots each app, then adds features with follow-up prompts | Gets ~80% of each app. Build-vs-buy depends on complexity and your time. Don't copy code, images, logos |
| Better Stack | Space Cadet Pinball .exe from Internet Archive | Skipped REA install. Vanilla Opus 5.5, 15 subagents, 2h25m, 31,000 lines Rust, 174 tests, ~$140 API equiv | Software is de facto open source if it can be verified |

## What the field has covered (saturated)

- Hype tweets + star chart intro (Nick mocks it, everyone else does it)
- "Wraps Ghidra/Hopper/IDA, not a decompiler, you get pseudocode not source" (all 5)
- Legal + sandbox warning (Rob, MG)
- "Code isn't the moat, brand/data is" (Rob, Eric, Nick)
- With vs without REA race (Nick, MG)
- Title says REA, demo skips REA entirely (Better Stack, Jack Roberts): 2 of 6 videos never ran it

## Gaps (our openings)

1. **Nobody shows the evidence.** REA's selling point is findings with evidence + unknowns. Every video judges the clone by eyeballing UI. Nobody opens the actual JSON / evidence output.
2. **Nick's claim is untested with numbers.** He says vanilla is faster and good enough; MG's data says REA costs ~3.3x more but gets functionality right. Nobody measured on the same target with tokens, time, and a pass/fail checklist.
3. **Nobody used the no-Ghidra path.** `analyze-javascript-application` on an Electron app needs no native engine. Cheapest, fastest, most relevant to Claude Code users (half their desktop apps are Electron).
4. **Nobody did the security audit use.** "What is this app sending home?" Rob mentions it in one sentence, nobody demos it.
5. **Nobody used it from a non-Claude agent.** Hermes speaks MCP; no one showed REA outside Claude Code / Codex.
6. **Nobody turned the findings into a skill.** One-off clones; nobody saved the investigation as a reusable skill.

## Her beat / our beat / exact prompt

| Their beat | Our beat | Exact prompt (Tyler voice) |
|---|---|---|
| Hype quotes | Skip quotes. Open on Nick's claim "you don't need REA" and say we test it | (talking head) "Nick says you don't need this. I measured it." |
| Install by asking agent | Run setup ourselves, show the 5 proposed changes and backups | `npx rea-agents setup` *(to verify: not installed yet)* |
| Clone a 3rd-party app | Own app first: a build of one of Tyler's Electron/JS apps. Static JS path, no Ghidra | `npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json` *(to pick: which app ships as a build)* |
| Eyeball the clone | Open the evidence JSON on screen: modules, IPC, unknowns | "Show me the evidence for each claim and list what you could not prove." |
| A/B race | Same target, same model, both panes; log tokens, minutes, and a 10-item feature checklist | "Use REA to explain how <feature> works in <app>, show the evidence, and build it in ./clone-rea." / "Do not use REA or any reverse engineering MCP. Explain how <feature> works in <app> and build it in ./clone-vanilla." |
| "Code isn't the moat" | Audit: what does an Electron app on this Mac send home | "Use REA to list every network endpoint and IPC channel in <app>. Evidence only, no guesses." *(target to pick; own app safest)* |
| Outro | Save the investigation as a skill so it reruns | "Turn this investigation into a skill I can rerun on any Electron app." |

## Possible extras

- Run REA through Hermes MCP instead of Claude Code (Hermes is MCP-capable; verify registration).
- Native binary beat later: needs Ghidra (free) or Hopper demo. Neither is installed on this Mac (checked /Applications 2026-10-13).

## Machine state (2026-10-13)

- Node v26.5.0, npm 11.17.0: meets REA requirement.
- REA: not installed. No Hopper, Ghidra, IDA, JADX found.

## Why Nick (887K) beat Jack (35K)

Pulled 2026-10-13 19:17 UTC via yt-dlp.

| | Nick Saraev | Jack Roberts |
|---|---|---|
| Subs | 549,000 | 284,000 |
| Views | 887,537 | 34,777 |
| vs own median (last 19 uploads) | 12.2x (median 73K) | 0.77x (median 44K) |
| Uploaded | 2026-10-10 | 2026-10-12 (2 days later) |
| Avg views/hour since upload | 12,727 | 1,508 |
| Likes / view | 1.61% | 1.36% |
| Comments / view | 0.08% | 0.14% |
| Length | 10:46 | 16:46 |
| Ran REA on screen | Yes (A/B race vs vanilla) | No (Base44 sponsor demo) |

Subscriber count explains 1.9x. The gap is 25x, and Jack came in under his own median, so the cause is the video.

1. **Timing.** Nick posted Oct 10, while the repo was spiking. His thumbnail shows "11.5k stars"; the repo is at 193,733 now. Jack posted 2 days later into a crowded search page.
2. **Thumbnail names the thing.** Nick: "github/reverse-engineer" with a red underline, stars and installs counts, face looking up at it. It reads as the repo people saw on X. Jack: "Clone Apps" with Premiere, Photoshop, ChatGPT and Claude logos. That's his standard template and never says REA or GitHub.
3. **Title collision.** Jack's title, "I Tested the Viral Reverse Engineering Repo", is nearly Nick's, published second. A searcher sees both and clicks the one with more views.
4. **Promise kept.** Nick's title says he tested the repo and he did: REA vs no REA, same prompt, side by side. Jack's title says he tested the repo; he never runs it and the demo is a Base44 sponsor build of Calendly, Typeform and Trello.
5. **A take worth sharing.** Nick's "you don't need REA" contradicts the hype tweets he opens with. That gives people a reason to argue and share. Jack lands on "build vs buy depends", which nobody shares.
6. **Length.** 10:46 vs 16:46 for a news-wave topic.

Not verified: retention and CTR (need Studio access to their channels). Jack's higher comment rate suggests engaged viewers but a weak click.

Lesson for ours: we're 3+ days behind both. Speed is gone, so win on 2 to 5. Name REA in the thumbnail, run it on screen, and answer Nick's claim with numbers.
