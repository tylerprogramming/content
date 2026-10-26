## In this lesson
You'll install DeepSeek Harness, connect a model (cheap cloud or 100% free on your own computer), and have it hand long jobs to Claude Code on the subscription you already pay for.

## Good to know
- Time: 20 to 30 minutes
- Cost: free with a local model. About $10 of OpenRouter credit if you use the cloud route.
- Level: Intermediate (you'll use a terminal)
- It's a developer preview. Things change and break. It doesn't replace Claude Code today.

## What you need
- Node.js (free): https://nodejs.org
- One model, pick one:
  - OpenRouter account with about $10 of credit (paid, cheap): https://openrouter.ai
  - Ollama for free local models: https://ollama.com
- Claude Code with a Claude Pro or Max plan, only for the sub-agent part: https://claude.com/claude-code

**1. Install and open it (1:39)**
Open a terminal and run:

```
npx @deepseek-ai/dsh web
```

It opens in your browser at http://127.0.0.1:3080 . When it asks for a DeepSeek API key, click "Configure later". You don't need one.
Skip the desktop version. It's made by a third party, not DeepSeek.

**2. Connect a model with OpenRouter (3:12)**
- Get an API key at openrouter.ai and add about $10 of credit.
- In Harness: Settings > Models > Add provider > openrouter > paste the key (or sign in) > Apply.
- Pick a model in the chat box. I used deepseek/deepseek-v4-flash. It's cheap and handles tools.
OpenRouter's free models exist, but they're rate limited and an agent will hit the limit fast.

**3. Or run it 100% free on your computer with Ollama (4:31)**
- Install Ollama and download a model (I used Gemma 4).
- Start Ollama with a bigger context window so the agent doesn't run out of room:

```
OLLAMA_CONTEXT_LENGTH=64000 ollama serve
```

- In Harness: Settings > Models > Add custom provider (the second button, not "Add provider"). Fill in:
  - Display name: Ollama
  - API base URL: http://127.0.0.1:11434/v1
  - API protocol: openai-completions
  - API key: leave it blank (or type ollama)
- Click "Fetch available models", pick yours, and save. A green dot means it's connected.

**4. Watch everything the agent does with Trajectory (5:58)**
Start a new workspace and ask it to build something small, like "create a simple Flask to-do app". Open the Trajectory tab to see every step: your prompt, the context, the skill it picked, each tool call and the result.

**5. Let it build its own tools with Creator mode (8:25)**
Settings > General > Agent preset > Creator mode. Then ask for something like "add a plugin for a calculator overlay in the bottom right". Everything in Harness is a plugin (165 of them, even the sidebar), so you can switch pieces on and off.

**6. Hand long jobs to Claude Code (11:25)**
This uses your Claude subscription, not an API key. Claude Code has to be installed and logged in on the same computer.
Install the plugin, then restart Harness:

```
dsh plugin --profile web add @deepseek-ai/dsh-subagent-claude-code
dsh --profile web
```

Then turn the delegation tool on. The easiest way is to ask Harness: "enable the Claude Code sub-agent plugin". If you'd rather edit it yourself, it lives in ~/.dsh/profiles/web/cordis.patch.yml:

```
- id: tool-subagent
  disabled: false
  config:
    provider: claude-code
    toolName: subagent_claude_code
    backgroundMode: one-shot
    permissionMode: acceptEdits
```

Restart again, then try: "delegate a task to the Claude Code sub-agent to write a simple Fibonacci function". The hand-off shows up in Trajectory.

## Files and links
- DeepSeek Harness on GitHub: https://github.com/deepseek-ai/deepseek-harness
- Quick start: https://deepseek.com/harness/en/
- OpenRouter: https://openrouter.ai
- Ollama: https://ollama.com
- Composio's plugin list: https://composio.dev/content/best-deepseek-harness-plugins

## If it breaks
- Ollama model won't connect: you used "Add provider" instead of "Add custom provider". Ollama needs the custom one.
- Local model stalls mid-task: Ollama was started without the bigger context. Quit the Ollama app and run the OLLAMA_CONTEXT_LENGTH command above.
- Claude Code task comes back having done nothing: permissionMode is still the default, which blocks edits. Set it to acceptEdits.
- New plugin doesn't show up: restart Harness. Every plugin change needs a restart.
- It restarted its own server and broke (happened to me on camera): run npx @deepseek-ai/dsh web again.
- One plugin from the Composio list added a pile of skins and wrecked the UI for me. If a plugin makes a mess, disable it and restart.

## Next
Set Up Hermes Agent in 30 Minutes
