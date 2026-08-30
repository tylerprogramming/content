# Plugins: install them, show them off

Verified 2026-08-30 against the repo and against **your actual profile** at
`~/.dsh/profiles/web/`. Not yet run live, so dry-run before the real take.

## The ladder (this is the spine of the whole video)

Do these in order and the video escalates on its own:

1. **See them** - 86 plugin rows are already running
2. **Turn one off** - even the UI is a plugin
3. **Install one** - and install a plugin that installs plugins
4. **Build one** - Creator mode (existing 6:45 section)
5. **The one that runs Claude Code** - the hero (existing 8:30 section)

Use → disable → install → build → orchestrate. Each rung is a bigger claim than the last.

---

## Your actual setup (read before filming)

`~/.dsh/profiles/web/package.json` composes the tree from two bundles:
```json
"bundles": ["@deepseek-ai/dsh-base", "@deepseek-ai/dsh-web-app"]
```
The web-app bundle alone declares **86 plugin rows**. `cordis.yml` is intentionally empty
(`[]`) - do not edit it. **`cordis.patch.yml` is your file**, and right now it is also `[]`.
It is a top-level YAML array of patch entries applied after every bundle layer.

> "There are eighty-six plugins running right now in the default setup. Not eighty-six
> features. Eighty-six plugins, and I can turn any of them off."

---

## Rung 1 - See them (30s)

**Settings > Plugins.** Two sub-tabs:
- **Plugin config** - expandable settings cards for the configurable ones. On screen you get
  **Terminal** ("limit every command the agent runs"), **Agent Loop** ("how the agent dispatches
  tool calls"), **Subagent** ("the agent's permission to choose models for subagents"), and
  **Web Search**.
- **Plugin list** - the full installed inventory.

Point at the **Subagent** card while you are here. It plants the hero beat 4 minutes early.

**There is no install button in this tab.** Configuring is UI, installing is CLI. Say that,
it is the honest bit and it sets up rung 3.

---

## Rung 2 - Turn one off (60s, the "even the UI is a plugin" beat)

Edit `~/.dsh/profiles/web/cordis.patch.yml`:

```yaml
- id: ui-sidebar
  disabled: true
```

Restart the profile. **The sidebar is gone.** Not hidden by a preference - the plugin that
draws it never loaded.

> "That is not a settings toggle. The code that renders the sidebar did not load. In Claude
> Code there is no equivalent of this, because there is nothing to unplug."

Then put it back (delete the two lines) so the rest of the video has a sidebar.

**Real ids you can disable, from your bundle** - pick whichever demos best:

| id | What disappears |
|---|---|
| `ui-sidebar` | the whole left sidebar (**best shot**) |
| `ui-theme` | theme switching |
| `ui-trajectory` | the Trajectory tab (fun: turn off the feature you just praised) |
| `ui-model-selection` | the model picker |
| `ui-settings-models` | the Models settings page |
| `tool-web` | the agent's web access |
| `tool-todo` | the todo tool |
| `ui-workspace` | the workspace browser |

Others present: `tool-bash`, `tool-fs`, `tool-fs-search`, `tool-skill`, `tool-jobs`,
`plan-mode`, `compaction-basic`, `agent-presets`, `locale`, `session-stats`,
`skill-filesystem`, `system-prompt`, `ui-approval`, `ui-chat`, `ui-layout`, `ui-permission`,
`ui-settings-plugins`, `webserver`, `workspace`.

> `ui-trajectory` is the spiciest choice: "watch, I'll delete the best feature in the product."

---

## Rung 3 - Install one (90s, the meta move)

### How installing actually works
```
dsh plugin --profile web add <npm-package>
dsh plugin --profile web remove <npm-package>
```
`dsh plugin` **forwards its remaining arguments to pnpm inside the profile directory** - that
is why there is a `pnpm-workspace.yaml` sitting in `~/.dsh/profiles/web/`. A plugin is just an
npm package added to that workspace. **Restart the profile after any add or remove.**

> You have no pnpm on PATH, but dsh runs it from inside the profile. **Confirm this in the dry
> run** - it is the one assumption here I could not test.

### The install to do on camera
```
dsh plugin --profile web add dsh-plugin-install
```
`dsh-plugin-install` (v0.3.9) puts a plugin installer **inside the Settings page** - install any
dsh plugin by npm spec, from the UI.

> "I just used the command line to install a plugin whose entire job is to let me stop using the
> command line."

That is the beat. Then install the next one from the UI to prove it.

### The ecosystem stat (this is the real story)
The repo is **17 days old** and there is already a third-party plugin ecosystem on npm with its
own marketplaces. Verified live today:

| Package | What it does |
|---|---|
| `dsh-plugin-install` | install any plugin by npm spec from Settings (**start here**) |
| `dsh-find-plugin` | the **agent** searches the GitHub `dsh-plugin` topic and finds its own plugins |
| `dsh-plugin-marketplace` | browses `github.com/topics/dsh-plugin` inside the settings page |
| `dsh-plugin-studio` / `dsh-plugin-console` | official + community catalogs, enable/disable panels |
| `dsh-plugin-mgr` | manage installed plugins from Settings: list, enable, disable |
| `dsh-plugin-uisfx` | per-scenario UI sound effects (**audible on camera**, good for a laugh) |
| `dsh-plugin-appshot` | macOS/Windows context screenshots |
| `dsh-plugin-observatory` | plugin compatibility audit |

> "Seventeen days. There are already four competing plugin marketplaces. Nobody had to ask
> DeepSeek for permission to build any of these."

`dsh-find-plugin` is the strongest second install if you want one: the agent finds its own
plugins, which is a nice ramp into Creator mode building its own.

---

## Rung 4 and 5

Creator mode (6:45) and the Claude Code subagent (8:30) are already scripted. The ladder above
just means by the time you get there, the audience already believes plugins are real, because
they watched you unplug the sidebar and install a marketplace.

---

## Pacing warning

This is a genuinely rich segment and it will eat time. **Budget 3 minutes total for rungs 1-3**
and protect the hero beat. If you are running long, cut in this order:
1. cut the second install (`dsh-find-plugin`)
2. cut the Plugin config tab tour, keep the Plugin list
3. keep `ui-sidebar` disable no matter what - it is the single most convincing 30 seconds in
   the video

## Dry-run checklist
- [ ] `dsh plugin --profile web add dsh-plugin-install` works **without pnpm on PATH**
- [ ] Profile restart brings the installer into Settings
- [ ] `- id: ui-sidebar / disabled: true` in `cordis.patch.yml` actually removes the sidebar
- [ ] Sidebar comes back when you remove those lines
- [ ] Settings > Plugins renders both sub-tabs
