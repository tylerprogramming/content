# 052 - First 2 Minutes: second-by-second opening spec

Applies the Nate graphics kit (see 2026-08-16-nate-herk-first-2min-teardown.md).
Targets: face ~35% of first 2 min, a graphic on 70%+ of seconds, new visual every ~3s in
first 30s, roadmap card by 0:30, one open loop, and NO graphic-free screen-share (webcam PIP
lives on every screen frame).

VO is Hook A verbatim (see hooks.md), then rolls into script 0:44+.

## 0:00 - 0:41 (second-by-second)

| Sec | Face? | On screen | Graphic / overlay | VO line |
|---|---|---|---|---|
| 0:00 | No | Screen-record: messy ./inbox folder + terminal, agent starting | Kinetic caption builds "AI agent" | "So this is an AI agent running on my laptop." |
| 0:01 | No | Same, terminal reading file 1 | Chip: "on my laptop" | (cont.) |
| 0:02 | No | Terminal continues | Chips flip in: "No API key" | "No API key." |
| 0:03 | No | Terminal continues | Chip: "No subscription" | "No subscription." |
| 0:04 | No | Terminal continues | Chip: "Nothing to the cloud" + cloud icon struck red | "Nothing is going to the cloud." |
| 0:05 | No | Cut to macOS wifi menu, cursor hovers "Turn Wi-Fi Off" (NOT clicked) | Red glow around the menu; caption "watch this later" | "And in a minute I'm going to turn off the internet," |
| 0:06 | No | Hold on wifi menu | Push-in on the toggle | (cont.) |
| 0:07 | No | Hold on wifi menu | Open-loop tag pins to corner: "wifi off = ?" | "and it keeps working." |
| 0:08 | YES | FACE reveal, push-in | Lower-third: name only (no title yet) | "I know, everybody says 'local and private.'" |
| 0:09 | Yes | Talking head | Kinetic caption: "local and private" | (cont.) |
| 0:10 | Yes | Talking head | Caption: "barely runs" turns red | "Most of the time it barely runs." |
| 0:11 | No | Cut: b-roll of a model download bar / old messy tool-call log | Caption: "that changed this year" | "That changed this year." |
| 0:12 | Split | Talking head + PIP over the log | Highlight sweep on "use tools" | "The local models can actually use tools now." |
| 0:13 | Yes | Talking head | Beat / music stinger | (cont.) |
| 0:14 | No | Card scene | Card 1 builds: LOCAL | "So we're going to build one together." |
| 0:15 | No | Card scene | Card 2 builds: PRIVATE | (cont.) |
| 0:16 | No | Card scene | Card 3 builds: FREE | (cont.) |
| 0:17 | Split | PIP over the ./inbox folder | Arrow: folder -> agent | "It reads a folder of my files and cleans it up," |
| 0:18 | No | Folder -> summary animation | Caption: "stays on this machine" | (cont.) |
| 0:19 | No | Summary file writes | Lock icon lands | "and it never leaves this machine." |
| 0:20 | Yes | Talking head | - | (breath) |
| 0:21 | Yes | Talking head | Chip flies in: "Developer" | "Doesn't matter if you write code every day" |
| 0:22 | Yes | Talking head | Chip flies in: "Never touched Ollama" | "or you've never run a model locally." |
| 0:23 | No | Editor peek, ~40 lines scrolls | Counter: "~40 lines" | "The whole build is about forty lines." |
| 0:24 | Yes | Talking head | Push-in | (beat) |
| 0:25 | No | Mock YouTube UI: this video's thumbnail + Subscribe | Soft subscribe pulse | (visual only) |
| 0:26 | Yes | Talking head | - | (breath into roadmap) |
| 0:27 | No | Roadmap card frame in | "In this video" header | "So, three parts." |
| 0:28 | No | Roadmap card | Line 1: "1) The model" | "The model," |
| 0:29 | No | Roadmap card | Line 2: "2) How it gets tools" | "how it actually gets tools," |
| 0:30 | No | Roadmap card | Line 3: "3) The one setup mistake" (dimmed = open loop) | "and the one setup mistake" |
| 0:31 | No | Roadmap card, line 3 pulses | Open-loop tag: "mistake = ?" | "that makes people think local agents don't work." |
| 0:32 | Yes | Talking head | - | (beat) |
| 0:33 | No | Receipt: survey headline, employees pasting company data into chatbots | Yellow highlighter sweeps "sensitive company data" | "Quick reason this matters." |
| 0:34 | No | Same receipt, push-in | Highlight holds | "Most people are pasting work files straight into a chatbot right now." |
| 0:35 | Split | PIP over receipt | - | (cont.) |
| 0:36 | Yes | Talking head | Lower-third UPGRADES: "Software engineer, 8 yrs" | "I spent eight years as an engineer" |
| 0:37 | Yes | Talking head | Chips: IBM / Chase | "at places like IBM and Chase," |
| 0:38 | Yes | Talking head | Chip: Pfizer (now) | "now Pfizer," |
| 0:39 | Yes | Talking head | Red glow on the phrase | "and that is the thing you are not supposed to do." |
| 0:40 | No | Snap wipe toward the build | Transition | (beat) |
| 0:41 | No | Editor / terminal, build begins | Section card: "Part 1 - The Model" | (hard cut into 0:44 content) |

## 0:41 - 2:00 (beat-level, keep the density rule)
- 0:44-1:30 "what is an agent" 3-box diagram (Model/Tools/Loop) builds element-by-element,
  webcam PIP on. No bare talking head over ~5-7s; highlight the Model box on the "the catch
  was the model" line.
- 1:30-2:00 Part 1 begins: terminal `ollama pull qwen3`, download bar (motion without cuts),
  model chips (Qwen3 8B / 30B-A3B / gpt-oss 20B) fly in as named. PIP stays on.
- Every number/model name = a synced chip or caption within ~1-2s. Never spoken bare.

## Targets check
- Face-on-screen seconds in 0:00-0:41: ~18 of 42 (~43%). Trim a couple face beats to b-roll
  if the full-two-minute face share runs above ~40%; the diagram + terminal stretch from
  0:44-2:00 is mostly PIP, which pulls the 2-min average toward ~35%.
- Graphic/overlay present: every row above has one. Target 70%+ met (100% in the hook).
- New visual cadence: a change on essentially every second 0:00-0:31, comfortably beating
  "new visual every ~3s in first 30s."
- Roadmap card: lands 0:27-0:31. Met (by 0:30).
- Open loops: (1) wifi-off planted 0:05, (2) "the mistake" planted 0:30. Both deferred.
- Screen-share rule: webcam PIP specified on every screen/terminal/editor frame. No
  graphic-free screen-share.
