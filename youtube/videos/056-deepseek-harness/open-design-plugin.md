# OpenDesign + DeepSeek Harness (github.com/nexu-io/open-design)

Verified 2026-08-30 against the repo and against your machine. **Read the first section before
you plan a shot around this** - the direction is the opposite of what it looks like.

## What it actually is

It is **not** a plugin you install inside DeepSeek Harness. You cannot
`dsh plugin --profile web add` it. It is a **standalone local-first desktop app** (92,786 stars,
v0.21.0) that drives coding-agent CLIs as its backends - Claude Code, Codex, Cursor, OpenCode
and about 20 others. **DeepSeek Harness is one of the agent runtimes it drives.**

```
OpenDesign (desktop app)  ->  DeepSeek Harness  ->  Claude Code
```

So the arrow points the other way from what you assumed. Which is actually the best possible
thing for this video, because it is the same story one level up:

> "Harness can drive Claude Code. And this thing drives Harness. That is what an open harness
> gets you - it is a component other people build on top of. You cannot do that with a sealed box."

That is a stronger close than the one currently scripted. It turns the subagent hero beat from
a party trick into a pattern.

(The repo title calls it a "DeepSeek Harness Design Plugin" - that is marketing, not packaging.
There is also a curated `deepseek-harness-genui` design skill on their landing site, which is a
separate, smaller thing. Do not conflate them on camera.)

---

## Your machine, checked just now

| Prereq | State |
|---|---|
| OpenDesign app | **not installed** |
| `od` command | **collides with `/usr/bin/od`** (see below) |
| `dsh` on PATH | **missing** - you have been running via `npx`. The runtime def is `bin: 'dsh'`, so this is a hard blocker |
| Node | v26.5.0 (source build wants `~24` - so **do not build from source**) |
| pnpm | none (source build wants 10.33.2) |
| Arch | arm64 |

---

## Exact steps

### 1. Get `dsh` on your PATH (required, and you do not have it)
OpenDesign's runtime definition looks for a binary literally named `dsh`. `npx` does not
satisfy that.
```
npm i -g @deepseek-ai/dsh
dsh --version
```

### 2. Install OpenDesign - use the DMG, not the source build
Download **`open-design-0.21.0-mac-arm64.dmg`** from
`github.com/nexu-io/open-design/releases`.

Zero config: no Node, no pnpm, no clone. **Do not follow QUICKSTART.md** - that is the
from-source path, it pins Node `~24` and pnpm `10.33.2`, and you are on Node 26. It will fail
on `engines` and cost you a take.

### 3. Know the `od` trap before it bites you
Verified on your machine: `which -a od` returns **`/usr/bin/od`**, the macOS built-in octal-dump
utility. It shadows OpenDesign's `od`. The repo calls this out explicitly.

Options:
- Open **Settings > MCP server** in the desktop app and copy the snippet - it uses absolute
  paths and never relies on bare `od`.
- Or call OpenDesign's binary by its absolute path.
- Do **not** just run `od ...` and expect it to work. It will silently be the wrong program.

> This is a genuinely good 15-second on-camera moment if you want one: "watch, this command
> exists on every Mac already and it is not the one I want."

### 4. Wire Harness in
```
od agent setup deepseek-harness
```
This installs the connector components OpenDesign ships and verifies them. If a profile exists
but is incompatible, **the same command repairs it**.

**Important and good news:** it creates its own profile at
**`~/.dsh/profiles/open-design/`** - confirmed in the runtime source. It does **not** touch
`~/.dsh/profiles/web/`, so everything you set up for the rest of the video (OpenRouter,
v4-flash, your patch layer) stays untouched. You currently have `web` only.

There is a `--json` form (`od agent setup deepseek-harness --json`) if you want clean output
on screen instead of a spinner.

### 5. Give it a model
Their own release notes say: add a DeepSeek API key on the **Models** page, or expose
**`DEEPSEEK_API_KEY`** to the daemon.

**Open question, resolve this in the dry run:** you do not have a DeepSeek key - you are on
OpenRouter. OpenDesign reads the dsh profile's model catalog (it parses provider/model pairs
out of the profile), so an OpenRouter route configured in the `open-design` profile *should*
show up. But their docs only document the DeepSeek-key path. **Test this before you commit a
shot to it.** Worst case, grab a DeepSeek key from platform.deepseek.com; it is cheap and it
removes the variable.

### 6. Use it
Pick **DeepSeek Harness** as the agent like any other, then choose the model and reasoning
effort directly in the composer. Then give it a design brief and let it produce real files
(HTML/PDF/PPTX/MP4 export is the pitch).

---

## My honest recommendation on whether this belongs in THIS video

**Probably not as a full segment.** You are already at 11-13 minutes with five sections plus
the hero beat, and this is an entire second product with its own install, its own binary
collision, and an unresolved model-key question. Dropping it in mid-video will blow the runtime
and dilute the subagent beat, which is your actual differentiator.

Two better options:

**Option 1 (recommended) - a 60 second closing beat, no install on camera.**
Have OpenDesign already installed and wired before you roll. At the verdict section, cut to it
for one shot: "and here is what that openness actually buys you - this is a completely separate
design app, ninety thousand stars, and it drives Harness as its backend." One design generation,
speed-ramped. Then the recap card. It upgrades your close and costs you a minute.

**Option 2 - it is the sequel.**
You already planned to ask in the CTA whether people want a real-project build orchestrating
Claude Code. This is a cleaner sequel hook: OpenDesign -> Harness -> Claude Code, three layers,
one task. That is a whole video and a better one than cramming it here.

Either way the line to say out loud is the same: **the arrow points both directions now.**

---

## Dry-run checklist
- [ ] `npm i -g @deepseek-ai/dsh` then `dsh --version` resolves
- [ ] DMG installs, app opens, auto-detects your CLIs
- [ ] Confirm the `od` collision and find the absolute-path invocation that works
- [ ] `od agent setup deepseek-harness` succeeds and creates `~/.dsh/profiles/open-design/`
- [ ] Confirm `~/.dsh/profiles/web/` is UNTOUCHED afterward
- [ ] **Resolve the model question:** does your OpenRouter route work, or do you need a DeepSeek key?
- [ ] One design generation completes end to end
