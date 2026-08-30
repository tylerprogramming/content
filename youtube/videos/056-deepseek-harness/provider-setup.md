# Provider setup: OpenRouter + Ollama (the 3:30-5:00 beat)

Source: the harness's own `packages/llm/llm-pi-ai/README.md` and the web app's UI
snapshots in `apps/web/tests/expected/models-settings/` at current main (2026-08-30).
Not yet run on this machine, so do ONE dry run before the real take.

## The mental model (say this on camera, it makes the whole beat make sense)

Models in Harness are not special. They are a plugin: `@deepseek-ai/dsh-llm-pi-ai`.
That plugin holds a dictionary of **provider routes**, and there are exactly two kinds:

| Kind | What it is | Examples | What you have to supply |
|---|---|---|---|
| **Catalog route** | The harness already ships the endpoint, the wire protocol, and the model list | `openrouter`, `anthropic`, `openai`, `groq`, `google`, 39 total | Just the API key |
| **Declared route** | The harness has never heard of it, so you describe it | **Ollama**, any self-hosted or private OpenAI-compatible box | Base URL, protocol, and the model list |

> "So a provider it knows about is one key. A provider it has never heard of is three
> fields. There is no plugin to write and no code to change. That is what they mean by
> everything is a plugin."

OpenRouter is a catalog route. **Ollama is not in the catalog** - I checked, the string
`ollama` does not appear anywhere in the repo. So Ollama goes in as a *custom* provider.
That difference IS the segment. Do not blur them together.

---

## Step 0 - cold start (2:00-3:30 beat)

```
npx @deepseek-ai/dsh web
```
UI opens at `127.0.0.1:3080`.

**First-run dialog:** "Add an API Key to get started" with a single DeepSeek API key box.
It has a **"Configure later"** button next to "Save and continue".

> **Click "Configure later".** This is a better beat than pasting a DeepSeek key. It proves
> the point immediately: "It asks for a DeepSeek key. I'm going to skip it. You never need
> one." Then you earn the whole free/local story instead of asserting it.

**Language check before you roll:** every UI snapshot in the repo is Chinese, and there is a
language preference row (`packages/client/locale/.../LanguageRow.tsx`) in **Settings > General**.
If it comes up in Chinese, switch it there first. Check this in the dry run, not on camera.

**Settings layout** (one dialog, four tabs, plus one button worth pointing at):
`General` / `Models` / `Plugins` / `Agent Presets`, and an **"Open config file"** button.
That button opens the YAML behind the UI. Use it once at the end of this segment.

---

## Step 1 - OpenRouter (the catalog route)

### BEFORE YOU ROLL - you have no OpenRouter key on this machine
Checked: no `OPENROUTER_API_KEY` in the environment, nothing in `.zshrc`/`.zprofile`. So:
1. Make the account at openrouter.ai.
2. **Put 10 dollars of credit on it.** Not optional, and not just for the paid model - see the
   free-model trap below.
3. Keys page -> create a key -> have it in your clipboard **before** you hit record.

### Two ways to authenticate, and OAuth is the better shot
OpenRouter is one of the few providers that ships **both** an OAuth login and an API key path,
and the harness offers OAuth first.

- **OAuth (recommended on camera):** a device-code flow. Harness says "Open this page to continue
  signing in", you get a code, you enter it on OpenRouter's verification page, done. No key ever
  appears on screen, so **no blurring in post and no risk of leaking a key on a paused frame.**
- **API key:** paste it into the API key box in the settings form.

> **TAKE-KILLER:** a sign-in only lives in the process that started it. **Do not refresh the
> browser mid-login** or the flow is abandoned and you start over. Also worth knowing: signing out
> only deletes the local record, it does not revoke anything at OpenRouter.

### The click path
**Settings > Models > "Add provider"**

1. Provider dropdown -> **`openrouter`**. The list has 39 shipped providers: amazon-bedrock,
   ant-ling, anthropic, azure-openai-responses, baseten, cerebras, cloudflare-ai-gateway,
   cloudflare-workers-ai, deepseek, fireworks, github-copilot, google, google-vertex, groq,
   huggingface, kimi-coding, minimax, mistral, moonshotai, nvidia, openai, openai-codex, opencode,
   openrouter, qwen-token-plan, together, vercel-ai-gateway, xai, xiaomi, zai... **Scroll it slowly.
   The length is the argument.**
2. Sign in with OAuth (or paste the key).
3. Save.

Done. No URL, no protocol, no model list - the harness already ships OpenRouter's catalog. That
contrast with the Ollama form two minutes later is the whole point of the segment.

### Which model to pick (this matters, pick it in advance)
Use **`deepseek/deepseek-v4-flash`**. Verified live on OpenRouter today:

| | in | out | context | tools |
|---|---|---|---|---|
| `deepseek/deepseek-v4-flash` | $0.08/M | $0.16/M | 1,048,576 | yes |

Why this one:
- **The narrative is perfect.** DeepSeek's own model, routed through OpenRouter, running inside
  DeepSeek's harness. Say that out loud, it lands.
- It is cheap enough that the entire video costs you pennies.
- Tool-capable with a million-token context, so the Flask build will not stall.

Other cheap tool-capable DeepSeek routes if you want a backup: `deepseek/deepseek-v4-flash-0731`
($0.07/$0.18), `deepseek/deepseek-v3.2` ($0.27/$0.40). Avoid `deepseek/deepseek-r1` (64k context,
$0.70/$2.50) - reasoning models are slow on camera.

### The free-model trap - mention it, do not demo on it
OpenRouter has **18 free models right now, 17 of them tool-capable** (`minimax/minimax-m3:free`,
`google/gemma-4-31b-it:free`, `nvidia/nemotron-3-super-120b-a12b:free`, and others). Tempting.
But the limits will wreck an agent demo:

- **20 requests per minute**, all users.
- **50 requests per day** if you have never purchased 10 dollars of credit. 1,000 per day once you have.

An agent loop building an app fires many calls in a burst. On a fresh account you will hit the wall
mid-demo. So: **buy the 10 dollars of credit** (it also lifts you to 1,000/day on the free models),
demo on `deepseek-v4-flash`, and just *mention* the free tier exists.

> Optional 10-second beat if you want it: open the model picker, scroll to the `:free` entries,
> and say "there is a free tier here too, it is rate limited, so I am using the cheap DeepSeek
> route instead." Honest, and it costs you nothing in pacing.

### Two details worth saying (engineer credibility, 15 seconds)
- **The key never enters the config file.** Config holds a credential *reference*; the secret goes
  to a separate credential store. So you can commit your harness config to a repo. Engineers care.
- Harness deliberately does **not** send OpenRouter's app-attribution headers, so your usage will
  not show up on OpenRouter's app leaderboards. Cut this if pacing is tight.

## Step 2 - Ollama (the declared route) - the free beat

**Before you roll** (this is the blocker from record-prep):
```
# quit the Ollama desktop app first, then:
OLLAMA_CONTEXT_LENGTH=64000 ollama serve
```
Default context is far too small for an agent loop. Leave this terminal running.

**Settings > Models > "Add custom provider"** (the SECOND button, not "Add provider")

Fill exactly these:

| Field | Value |
|---|---|
| API key | **leave blank** (say this out loud: "no key, this is my machine") |
| Display name | `Ollama` |
| API base URL | `http://127.0.0.1:11434/v1` |
| API protocol | `openai-completions` (the default; other options are `openai-responses`, `anthropic-messages`) |

Then the **Model catalog** section:
- Click **"Fetch available models"** - it interrogates the endpoint live and offers back what
  it found. This is the money click, let it land.
- Pick / keep **`qwen3.8:27b-q8_0`**. Delete the rest so the picker stays clean on camera.
- Hit the **capacity** control on that model and set the context window to **64000** to match
  what you started Ollama with. If you skip this it falls back to a 262,144 default and will
  overrun the server.

Save.

> "No key, no account, no per-token cost, and nothing leaves this machine. That is the free
> Claude Code thing people are talking about, and it is real."

**Honest beat, keep it:** you cannot plug in a ChatGPT or Claude subscription login. API keys,
OAuth for the providers that offer it, or local. That is the whole list.

---

## Step 3 - the payoff shot (10 seconds, ties the segment to the thesis)

Click **"Open config file"** and show the YAML the two forms just wrote:

```yaml
- name: '@deepseek-ai/dsh-llm-pi-ai'
  config:
    providers:
      openrouter:
        apiKeyEnv: OPENROUTER_API_KEY
      ollama:
        displayName: Ollama
        api: openai-completions
        baseURL: http://127.0.0.1:11434/v1
        models:
          - id: qwen3.8:27b-q8_0
            contextWindow: 64000
```

> "Every click I just did wrote those lines. The UI is a form over a config file, and the
> config file is the truth. You can put this in a repo."

Then switch models in the composer dropdown, cloud to local, mid-session.
**No restart needed** - config is re-read per request. Say that, it's a real detail people
will not expect from a preview.

---

## Gotchas that will bite you on camera

- **"Add provider" vs "Add custom provider" are different buttons.** Ollama needs the second one.
  Picking `openai` from the dropdown and pasting an Ollama URL is the wrong path.
- **A declared route requires a non-empty model list.** If you leave the catalog empty it is
  refused at save time, naming the route. Fetch or type at least one model.
- **Blank API key is legal and intended** for local. The placeholder says so. Don't type a fake key.
- If a model has no declared capacity it silently takes the **262,144** default and your local
  server will choke. Set capacity.
- Error codes you might hit live, so you can narrate instead of panic: `MISSING_CREDENTIAL`
  (key reference resolves to nothing), `INVALID_CREDENTIAL`, `UNKNOWN_MODEL` (model not in the
  route's list), `QUOTA` vs `RATE_LIMIT`.

## Dry-run checklist (do this off camera, then `rm -rf ~/.dsh`)
- [ ] `OLLAMA_CONTEXT_LENGTH=64000 ollama serve` running
- [ ] `npx @deepseek-ai/dsh web` boots, UI at 127.0.0.1:3080
- [ ] UI language is English (or switched in Settings > General)
- [ ] "Configure later" dismisses the first-run key dialog
- [ ] OpenRouter account created and **10 dollars of credit added**, key in clipboard
- [ ] OpenRouter added via OAuth (do NOT refresh the browser mid-login), `deepseek/deepseek-v4-flash` selected and responding
- [ ] Ollama added as CUSTOM provider, "Fetch available models" returns qwen3.8, it responds
- [ ] Model dropdown switches cloud -> local without a restart
- [ ] `rm -rf ~/.dsh` to restore the fresh first-run
