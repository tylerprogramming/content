# 052 - Script: 100% Local AI Agents in 2026 (Free, Private, No API Keys)

Remake of the 25k-view CrewAI/Ollama local-agents video. Target ~9-11 min.
Voice: short spoken sentences, "so" openers, humble, honest limits, delayed credibility,
no em dashes, no hype words. Uses HOOK A verbatim for the open.

Legend: [SHOW: on-screen] / [NOTE: production/direction]

---

## 0:00 - 0:44  COLD OPEN (use Hook A word-for-word)
[NOTE: face hidden until 0:08. New visual every ~3s. Cards build LOCAL/PRIVATE/FREE by 0:14,
roadmap card by 0:28, credibility at ~0:38, hard cut at 0:44. See hooks.md Hook A.]

Plant the open loop out loud: "in a minute I'm going to turn off the internet, and it keeps
working." Do NOT pay it off yet.

---

## 0:44 - 1:30  THE FRAME: what "local agent" actually means
[SHOW: simple diagram builds, three boxes: Model / Tools / Loop. Webcam PIP on.]

"So real quick, what is an agent, without the buzzwords.

An agent is three things. A model that can think. Some tools it's allowed to use. And a
loop that lets it keep going until the job's done.

[SHOW: highlight the Model box.]

The catch has always been the model. If you run a model on your own laptop, can it actually
call tools? For a long time, kind of not really. They'd chat fine, but the tool calling was
messy.

[SHOW: caption: 'that changed in 2026'.]

That's the part that's different now. So let me show you the exact pieces, and then we build."

---

## 1:30 - 2:45  PART 1 - THE MODEL (Ollama + Qwen3)
[SHOW: terminal. `ollama pull qwen3`. Progress bar. Webcam PIP.]

"So the model runs through Ollama. If you've never used it, Ollama just lets you run models
on your own machine. It's free.

[SHOW: type `ollama pull qwen3`, it downloads.]

We're going to use Qwen3. In 2026 this is kind of the go-to for local agents, because it's
actually good at calling tools. The 8B version fits on a normal laptop, around 8 gigs.

[SHOW: chips: Qwen3 8B (laptop) / Qwen3 30B-A3B (more RAM) / gpt-oss 20B.]

If you've got more memory, the 30B one that only activates a few billion params at a time is
the sweet spot. gpt-oss also works. But 8B is plenty for what we're doing.

[SHOW: `ollama run qwen3` then a quick prompt, it replies.]

And that's it. No account, no key, no bill. The model is on your machine now.

[NOTE: honest-limit beat per voice.] It's not GPT. It's not going to write your novel. But
for private file work on your own laptop, it's more than enough. It gets you most of the way
and you nudge it."

---

## 2:45 - 4:15  PART 2 - HOW IT GETS TOOLS (MCP, the 2026 way)
[SHOW: diagram. Old way vs new way. Old: tangled custom wires per tool. New: one MCP box.]

"Okay, part two, and this is the piece that's really changed since the old version of this
video.

[SHOW: caption: 'the old way'.]

Back then you wired up every tool by hand, in the framework, for that one model. It worked,
but it was a lot of glue.

[SHOW: caption: 'MCP', logo-ish card.]

Now there's a standard for it called MCP, the Model Context Protocol. It's open. The idea is
simple. You define a tool once as a little server, and any model can discover it and use it.
No custom wiring per model.

[SHOW: card: 'filesystem MCP server' with read/write icons.]

For our agent we just need one tool: the file system. So the agent can read the folder and
write a summary back. There's already an MCP server for that, we don't write it.

[SHOW: quick `pip install` of the MCP client + point at the filesystem server config.]

So we point our agent at that server, and now it can touch files. That's the whole tool
layer. One server."

[NOTE: keep it honest.] "You don't have to use MCP. You can hand the model plain Python
functions too. But MCP means the tool works with any model later, so I'd start here."

---

## 4:15 - 6:15  PART 3 - BUILD THE AGENT (~40 lines, live)
[SHOW: editor. Build the file top to bottom. Webcam PIP. Kinetic captions on the 3 key lines.]

"So now we connect the three pieces. Model, tool, loop. This is the whole agent, about forty
lines, and I'll go slow.

[SHOW: line group 1 - connect to Ollama, pick qwen3.]
"First we point at Ollama and pick our model. Local, no key.

[SHOW: line group 2 - start the filesystem MCP server, list its tools.]
"Then we start the file system tool and ask it what it can do. It comes back with read and
write. The model now knows those exist.

[SHOW: line group 3 - the loop: send prompt + tools, model asks to call a tool, we run it,
feed the result back, repeat.]
"And here's the loop, the actual agent part. We send the model the job and the list of tools.
The model says 'call read on this folder.' We run it. We hand back what it read. It thinks,
then it says 'now call write with this summary.' We run that. Done.

[SHOW: kinetic caption: 'think -> call tool -> read result -> repeat'.]

That back and forth is the whole thing. That loop is what makes it an agent instead of a
chatbot.

[SHOW: the prompt we give it, plain English: 'Read every file in ./inbox, pull out the
action items and key dates, write a clean summary to summary.md'.]

And the job is just plain English. Read my folder, pull the important stuff, write me a clean
summary."

---

## 6:15 - 7:45  RUN IT + THE PROOF (pay off the open loop)
[SHOW: the messy ./inbox folder first: a few notes, a receipt, a meeting dump. Then run.]

"Alright, let's run it. Here's the folder. It's a mess. Some notes, a receipt, a meeting
dump, the kind of stuff you'd never paste into ChatGPT.

[SHOW: run the script. Terminal streams: reading file 1... reading file 2... writing summary.]

Watch it work. It's reading each file. Now it's deciding what matters. Now it's writing.

[SHOW: 6:45 - the wifi/airplane menu. Cursor clicks 'Turn Wi-Fi Off'. Menu bar icon changes.]

And remember what I said at the start. Watch this.

[NOTE: THE payoff beat. Hold on the wifi-off click. Let it breathe.]

I'm turning off the internet. Completely. And it just keeps going.

[SHOW: terminal keeps streaming, finishes, writes summary.md.]

Nothing broke. Because nothing was ever leaving this laptop. No API to reach. That's what
local actually means.

[SHOW: open summary.md, clean action items + dates. Push-in.]

And there's the output. Clean list, action items, the dates it found. From a folder that was
a mess a second ago."

[NOTE: honest limit again.] "Is it perfect? No. It missed one thing, I'd read it over. It's
80 percent there and you tidy the rest. But it's private, it's free, and it did the boring
part."

---

## 7:45 - 8:45  MAKE IT YOURS + WHERE IT BREAKS
[SHOW: chips of other folders you could point it at: receipts, code, client docs, notes.]

"So now the fun part. It's the same agent, you just change the folder and the instruction.

[SHOW: chips.] Point it at your receipts. Your client files. A codebase you can't send to a
cloud API. Your own notes. Same forty lines.

[SHOW: the 'one setup mistake' card - callback to the roadmap open loop.]

And the one thing people get wrong, the thing that makes them say local agents don't work.
They grab a tiny model with no tool support, or they skip the tool list, so the model never
knows the tools exist. It just talks. Use a model built for tools, like Qwen3, and actually
pass it the tools. That's it. That's the mistake.

[NOTE: this closes the roadmap open loop planted at 0:28.]

If you want to go bigger later, you can put a framework like LangGraph on top for multi-step
stuff. But you don't need it to start. This is already a real agent."

---

## 8:45 - 9:30  CLOSE + CTA (folded in, then out)
[SHOW: recap card: LOCAL (no cloud) / PRIVATE (offline) / FREE (no key). Face.]

"So that's a 100 percent local agent. Runs on your laptop, works with the internet off, and
it never costs you a token.

[NOTE: CTA folded in, no dead air.] I dropped the full code and the exact model and MCP setup
in my free Skool, link's below, so you can copy it and run it in about ten minutes.

[SHOW: soft end card.]

So pick a folder you'd never send to the cloud, and point this at it. Tell me in the comments
what folder you'd start with, I read every one.

That's it. I'll see you in the next one."

[NOTE: no long outro. Snap to end card.]

---

## Production checklist (from the teardown)
- [ ] Intro killed, first sentence is the payoff.
- [ ] Face hidden to ~0:08 over screen-record.
- [ ] LOCAL/PRIVATE/FREE cards by 0:14; roadmap card by 0:28.
- [ ] Open loop = wifi-off, planted 0:05, paid off 6:45, NOT before.
- [ ] Second open loop = "the one setup mistake", planted 0:28, closed 8:00.
- [ ] Credibility (IBM/Chase/Pfizer) delayed to ~0:38, framed as why-I-care, never "expert".
- [ ] Webcam PIP on every screen-share so the face never disappears.
- [ ] No bare static talking head longer than ~5-7s.
- [ ] Every claim/number gets a synced visual within ~1-2s; the paste-data stat shown as a
      real receipt with a highlighter sweep.
- [ ] Honest-limit beats kept (voice): "not GPT", "80 percent there, you tidy the rest".
