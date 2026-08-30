# SHOT LIST — step by step, with sub-steps

Screens: **A** camera · **B** terminal · **C** dsh UI (`127.0.0.1:3080`, workspace `content`) ·
**D** external browser · **E** editor · **F** motion graphic (post)

---

## 0. PRE-ROLL (do all of this before recording)

**0.1 Fix the two blockers**
- Quit the Ollama desktop app from the menu bar
- `OLLAMA_CONTEXT_LENGTH=64000 ollama serve` in a terminal you leave running
- `npm i -g @deepseek-ai/dsh`
- `dsh --version` to confirm it resolves

**0.2 Make a restore point**
- `cp -R ~/.dsh ~/.dsh.known-good`
- Confirm clean: patch layer is `[]`, no deps, bundles are base + web-app

**0.3 Capture assets you cannot get later**
- 4-6 competitor thumbnails ("The End of Claude Code?" etc.)
- The repo page framed on the 204k star count
- The `dsh-plugin` GitHub topic, scrolled so reactive-resume / PicGo / NocoBase are visible in the star ranking
- The awesome-list category table (2,710 across 23)
- Whatever crash evidence you still have (see 9.4)

**0.4 Set the stage**
- Do Not Disturb on, all notifications off
- Close every unrelated app and tab
- Browser window 1 = dsh UI only. Browser window 2 = external tabs only
- Pre-open external tabs: repo, deepseek.com/harness, openrouter.ai, `dataelement/dsh-desktop`
- Bump the dsh UI font size
- **Scan the `content` file tree and your terminal scrollback for anything private** (Pfizer work, keys, client names)
- Start a new dsh session so the sidebar is clean

---

## 1. HOOK — 0:25

- **1.1** [A] Cold open, no greeting: "Half of YouTube is telling you DeepSeek Harness is the end of Claude Code."
- **1.2** [D] Cut to the thumbnail montage, fast, 3-4 seconds total
- **1.3** [A] "It's not. But it is the most interesting thing to happen to coding agents this year..."
- **1.4** [D] Cut to the repo, star count on screen, as you say "over two hundred thousand"
- **1.5** [A] Land the three payloads: open source / any model including free local / runs Claude Code
- **1.6** Hard cut out. No intro card, no "in this video"

## 2. WHAT A HARNESS IS — 1:00

- **2.1** [A] "Quick thing first, because the word is doing a lot of work and nobody explains it."
- **2.2** [A] The model does nothing list: can't read a file, run a command, remember a minute ago, decide to stop
- **2.3** [F] Leave 8 seconds of clean read for the MODEL box graphic, text in one side out the other
- **2.4** [A] Name the harness parts in order: the loop, the tools, context in and out, permissions, the interface
- **2.5** [F] Leave room for rings building around the box as you name each one
- **2.6** [A] **"The model is the engine. The harness is the rest of the car."** Hold on your face. Say it once, never again.
- **2.7** [A] "And you already use one. Claude Code is a harness. Codex is a harness. Cursor is a harness."
- **2.8** [F] Leave room for three logos over one shared model box
- **2.9** [A] "The catch is you can't open any of them. You get the finished car."
- **2.10** [C] **First reveal of the dsh UI.** "This one, every part is a piece you can pull out."
- **2.11** [C] "That's what everything is a plugin means. Eighty six of them running by default."
- **2.12** [A/C] "Alright. Let's run it." Straight into the terminal, no transition

## 3. INSTALL — 1:00

- **3.1** [B] Clear the terminal, type `npx @deepseek-ai/dsh web` live
- **3.2** [B] Let it print the URL, say "that's the whole install"
- **3.3** [C] Click through to the UI at `127.0.0.1:3080`
- **3.4** [A] Say the fresh-install line without showing it: "on a fresh install it asks for a DeepSeek key and there's a Configure later button. You never need one."
- **3.5** [A] The desktop-app caveat: community wrappers, not official
- **3.6** [D] 5 seconds on `dataelement/dsh-desktop`, 3.3k stars. **Do not install it**
- **3.7** [C] Back to the UI

## 4. MODELS — 2:00

- **4.1** [A] Set the frame: a provider it ships is one key, one it's never heard of is three fields
- **4.2** [C] Settings > Models, show your existing `openrouter` row
- **4.3** [C] Click Add provider, open the dropdown, **scroll all 39 slowly**. The length is the argument
- **4.4** [D] Cut to openrouter.ai while you explain it: one account, one key, hundreds of models, it routes and takes a cut
- **4.5** [C] Show the model picker with `deepseek/deepseek-v4-flash`. "DeepSeek's own model, through OpenRouter, inside DeepSeek's harness"
- **4.6** [A] Optional 10s: the free tier exists, 17 tool-capable free models, heavily rate limited, so you're on the cheap route
- **4.7** [B] Show `ollama serve` running. "This is my machine, no key"
- **4.8** [C] Settings > Models > **Add custom provider** (call out that it's a different button)
- **4.9** [C] Fill it: leave key blank, name `Ollama`, URL `http://127.0.0.1:11434/v1`, protocol `openai-completions`
- **4.10** [C] Click **Fetch available models**. Let this land, it's the money click
- **4.11** [C] Keep `qwen3.8:27b-q8_0`, delete the rest, set capacity to **64000**, Save
- **4.12** [C] Composer model dropdown, switch cloud to local. "No restart, it re-reads per request"
- **4.13** [C] Click **Open config file**, show the YAML both forms wrote
- **4.14** [A] "The secret isn't in there. It's a separate credential store. You can commit this."

## 5. TRAJECTORY — 1:30

- **5.1** [C] New session in the `content` workspace
- **5.2** [C] Type the task, send it
- **5.3** [C] Let it run, speed-ramp the wait in post
- **5.4** [C] Click the **Trajectory** tab
- **5.5** [C] Pan the step timeline so the shape is visible
- **5.6** [C] Click into one tool call and expand it
- **5.7** [C] Point at each part: system prompt, your prompt, context loaded, thinking, the call, payload, result, timing
- **5.8** [C] Show the session export / download
- **5.9** [A] "This is the opposite of Claude Code, where the thinking is hidden"

## 6. YOUR SKILLS ALREADY WORK — 1:00

- **6.1** [B] `ls ~/content/.agents/skills` — 25 skills you wrote for Claude Code
- **6.2** [A] "These are mine. I wrote them for Claude Code, months ago, for a completely different tool."
- **6.3** [C] In a live session, ask it to list its skills
- **6.4** [C] Scroll the result to **26 skills**, stop on `house-style` at #8
- **6.5** [C] Point out hyperframes, motion-graphics, talking-head-recut
- **6.6** [A] "I didn't port anything. It reads the same `.agents/skills` convention Claude Code does."
- **6.7** [A] The why: "That's what an open harness buys you that a sealed one can't."

## 7. YOUR OWN MODE — 1:30

- **7.1** [C] Open the mode dropdown
- **7.2** [C] Read the four shipped ones: Standard, **PTC**, Minimal, Creator
- **7.3** [C] Scroll to **Tyler** sitting fifth, hover so the description is readable
- **7.4** [B] `ls ~/.dsh/.agent-presets/tyler/` — `preset.yml` and `agent.cordis.yml`
- **7.5** [E] Open `agent.cordis.yml`, scroll the plugin rows so the shape is visible
- **7.6** [E] Stop on the persona row, show your house style in it
- **7.7** [C] Select Tyler, start a session, header confirms **Tyler**
- **7.8** [A] "That's my agent, in the same picker as DeepSeek's own four. There's no difference between theirs and mine."
- **7.9** [A] Honesty note: authoring is copy-only, you duplicate a shipped preset and edit on disk. No create-from-scratch
- **7.10** [C] Optional: mention Creator mode is the mode for building these, which is how you got here

## 8. HERO — IT RUNS CLAUDE CODE — 1:30

- **8.1** [F] Diagram: dsh in the middle, arrow to Claude Code, result coming back
- **8.2** [A] "This is the part I made the video for, and almost nobody is showing it"
- **8.3** [B] `dsh plugin --profile web add @deepseek-ai/dsh-subagent-claude-code`
- **8.4** [E] Open `cordis.patch.yml`, flip `tool-subagent` on
- **8.5** [E] **Set `permissionMode: acceptEdits`.** Say why: the default denies and the task silently does nothing
- **8.6** [B] Restart the profile
- **8.7** [C] New session, delegate a real task to Claude Code
- **8.8** [C] Show the sidebar subagent activity while it runs
- **8.9** [C] Result folds back into the session, agent keeps reasoning on it
- **8.10** [C] Open **Trajectory**, show the delegation call, its payload and the returned answer
- **8.11** [B] `git status` or `ls` the new files. Physical proof the child did the work
- **8.12** [A] "This isn't Harness versus Claude Code. Harness becomes an orchestration layer above it."

## 9. THE HONEST PLUGIN REALITY — 1:00

- **9.1** [A] Open to camera. Your face carries this one
- **9.2** [D/F] The category table: 2,710 plugins, 23 categories. Biggest is UI at 441. The one that matters is Models and Providers at 110
- **9.3** [D] The `dsh-plugin` topic star ranking with reactive-resume, PicGo, NocoBase visible. "These aren't plugins. They tagged the topic for reach."
- **9.4** [A] The age: three weeks old, one sidebar plugin shipped 19 versions in 17 days
- **9.5** [F] Card: no security review · runs with your permissions · reads your files · **98 plugins in a Security category, many of them scanners for other plugins**
- **9.6** [A] "And it broke my install." Two plugin managers, same routes, wouldn't boot, 479MB purge, leftover state under unrelated names
- **9.7** [A] Land it: "Everything is a plugin is the best thing about this and the most dangerous thing about it, and three weeks in, both are true."

> **9.4 note:** if your crash scrollback is gone after the purge, tell this to camera with the
> numbers and lean on the screenshots. Do not stage a fake crash.

## 10. VERDICT + OUTRO — 1:00

- **10.1** [A] "Is this replacing Claude Code today? No. It's a preview, it's rough in places."
- **10.2** [A] The turn: see everything, any model including free local, your existing skills work unchanged, your own modes, and it drives Claude Code
- **10.3** [F] Recap card: open source / any model + local / your skills already work / your own agent mode / runs Claude Code
- **10.4** [A] CTA: the config and commands are in the free community, one destination only
- **10.5** [A] Sequel ask: "Tell me in the comments if you want the one where a design app drives this, which drives Claude Code. Three layers, one task."
- **10.6** [F] End card

---

## Screen hygiene during the take
- One browser window for **C**, a second for **D**, so cuts stay clean
- Never refresh the browser during an OAuth flow or a running delegation
- If something is janky, narrate it. That is the whole differentiator
- `~/.dsh.known-good` is your restore point if beat 8 breaks the boot
