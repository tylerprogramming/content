# How this actually works (the mental model)

Written 2026-08-30 because the OpenDesign detour exposed a real ambiguity. Everything here is
verified against the repo and your own `~/.dsh/`.

## Three different things get called "a plugin". Only one of them installs into Harness.

| # | Thing | How it attaches | Example |
|---|---|---|---|
| 1 | **A dsh plugin** | an npm package in your profile's workspace, registered as a row in the plugin tree | `dsh-plugin-mgr`, `tool-bash`, `ui-sidebar` |
| 2 | **A skill** | markdown/instructions the agent loads at runtime, not a package in the tree | the Cordis plugin-dev skill Creator mode pulls in |
| 3 | **An app that drives dsh** | not attached at all - it runs `dsh` as a subprocess | **OpenDesign** |

You wanted #1. OpenDesign is #3. That is the whole confusion, and it is a reasonable one to
have had, because their repo title literally says "DeepSeek Harness Design Plugin."

## How #1 actually composes (this is the part worth understanding)

Your profile is `~/.dsh/profiles/web/`. Three layers, applied in order:

**Layer 1 - bundles.** `package.json` names them:
```json
"bundles": ["@deepseek-ai/dsh-base", "@deepseek-ai/dsh-web-app"]
```
These ship the defaults. The web-app bundle alone declares **86 plugin rows** - `tool-bash`,
`ui-sidebar`, `ui-trajectory`, `tool-subagent`, all of it. This is why the thing works out of
the box.

**Layer 2 - `cordis.patch.yml`.** Your override file. Currently `[]`. A top-level YAML array
where each entry targets a row **by id** and disables it, reconfigures it, or inserts a new one:
```yaml
- id: ui-sidebar
  disabled: true
```
`cordis.yml` sitting next to it is empty on purpose. Do not edit that one.

**Layer 3 - installed packages.** `dsh plugin --profile web add <pkg>` forwards its arguments
**to pnpm inside the profile directory** - which is why there is a `pnpm-workspace.yaml` in
`~/.dsh/profiles/web/`. A plugin is just an npm package in that workspace. Adding the package
makes it *available*; the patch layer is what actually *mounts* it.

So: **a plugin is an npm package that registers itself on a context seam** (`ctx.llm`,
`ctx.subagents`, `ctx.tools`, a UI slot), and the patch layer decides whether it loads.

That single sentence is the whole architecture, and it is what "everything is a plugin" means.
Your model provider is one (`llm-pi-ai`, the thing you configured for OpenRouter). Your bash
tool is one. The sidebar is one. The Claude Code subagent is one.

## Why OpenDesign could never have been #1

It is a desktop app with its own daemon and GUI. It scans your `PATH`, finds `dsh`, and runs it
as a child process in its own profile (`~/.dsh/profiles/open-design/`). Nothing about it mounts
into your plugin tree. The relationship is:

```
OpenDesign  ->  DeepSeek Harness  ->  Claude Code
   (app)          (harness)            (agent)
```

Same shape as your hero beat, one level up. That is why it is a good sequel and a bad mid-video
detour.

---

## The plugin to actually add on camera

**`dsh-plugin-mgr`** (v0.2.8, published 2026-08-30 - today). Vetted, it is the right pick.

```
dsh plugin --profile web add dsh-plugin-mgr
```
Then restart the profile.

It injects a **Plugin Manager tab into Settings > Plugins** with:
- every installed plugin as a card, with version, running status, and an **enable/disable toggle**
- expandable details: install source, repo link, description
- uninstall with confirmation
- update-available badges and one-click update
- search across names and descriptions
- a red "load failed" indicator with the error, if one breaks

Prereqs: Node `^22.19.0 || >=24.0.0`. You are on 26.5.0, fine. (pnpm only needed for source builds.)

**Why this one is the best demo:** it is a plugin whose entire job is showing off plugins. You
install it *with* the plugin system and it immediately renders the plugin system. And its
enable/disable toggle writes the patch layer for you - the exact file you just hand-edited.

### The one-two that makes the segment land

1. **Hand-edit** `cordis.patch.yml`, add `- id: ui-sidebar / disabled: true`, restart, sidebar
   gone. *Teaches the mechanism.* "That is not a setting. The code never loaded."
2. **Then install `dsh-plugin-mgr`** and show the same toggle as a switch in the UI. *Shows the
   ecosystem.* "Seventeen days old, and somebody already built the UI DeepSeek did not ship."

Mechanism first, then convenience. If you only show the UI toggle, it looks like a settings
page and the whole point evaporates.

### Backups if that one misbehaves
- `dsh-plugin-install` (0.3.9) - install any plugin by npm spec from Settings
- `dsh-find-plugin` (0.3.7) - the **agent** searches GitHub's `dsh-plugin` topic and finds its
  own plugins. Great ramp into Creator mode.
- `dsh-plugin-appshot` (0.4.1) - macOS context screenshot capture
- `dsh-plugin-uisfx` (0.1.1) - UI sound effects, audible on camera, good for a laugh

All verified live on npm today.

## Dry-run checklist
- [ ] `dsh plugin --profile web add dsh-plugin-mgr` succeeds (needs `dsh` on PATH or run via npx)
- [ ] Restart, Plugin Manager tab appears under Settings > Plugins
- [ ] It lists the 86 rows and the toggles work
- [ ] Hand-edited `ui-sidebar` disable still works, and the manager reflects it
