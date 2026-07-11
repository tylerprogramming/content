# Follow Along: Let the ElevenLabs Flows Agent Build a Video From One Sentence

> The exact prompt, answers, and settings from the video. Copy it move for move.
> Flows in ElevenCreative is currently in alpha, so a button may move, but the steps are the same.
>
> **Try it free:** https://try.elevenlabs.io/8n9sgoi23fkk (code: [CODE])
> **My example Flow (shown in the video):** https://elevenlabs.io/app/flows/rLP9x4JJoyjN2F5frt3P (set sharing to "Link only" so it opens for you)
> **Turn this into the public Google Doc lead magnet + pinned comment.**

## The 3 names (so you don't mix them up)
- **ElevenCreative** = the platform
- **Flows** = the node canvas
- **Flows Agent** = the AI that builds the Flow for you (this video). NOT "ElevenAgents" (a different product).

## Step 1: Open the agent
ElevenCreative -> Flows -> New Flow -> open the **Flows Agent** chat panel on the right.

## Step 2: The prompt I typed (copy this shape)
> "Make me a 15 second product video for a ceramic coffee mug, warm and cozy tone, with a voiceover and background music."

## Step 3: Answer its clarifying questions
It asks BEFORE it spends (length, tone, voice, structure). My answers:
- Length: 15 seconds
- Tone: warm
- Voice: friendly female voice
- Structure: hero shot, then a couple of detail shots

Then watch it build on its own: it adds an image node, a video node, a Text to Speech node (Eleven v3), a music node, and wires them all into a Composition node. It selects the models, creates the nodes, connects them, and runs them.

## Step 4: Iterate by talking (non-destructive)
Just type the change, it re-runs only that branch:
- "Use a warmer voice for the voiceover." -> redoes the voice + downstream only
- "Use Veo for the video instead." -> swaps the video model, re-runs that branch
Your images do NOT regenerate if they didn't change. **But every re-run is a new generation = new credits. Not free.**

## Step 5: Set Assist mode BEFORE you go crazy iterating (the important one)
Agent panel -> Assist mode. Three settings:
1. **Approve each** - it asks before every generation. Safe. Start here.
2. **Auto-run** - no confirmation, it just goes. Fast, but you handed it the keys.
3. **Auto under threshold** ⭐ (recommended) - runs cheap steps automatically, only stops to ask when a single action costs more than the limit you set. Speed + a guardrail on big spends.

## Step 6: The async superpower
Give it something big ("build 3 variations with different opening shots"). It runs **async, on ElevenLabs' side** - so you can **close the tab**, walk away, and come back to a finished Flow. You are not babysitting a progress bar.

## Models available
50+ image and video models (Veo 3, Sora 2, Kling, Seedance, Flux, Nano Banana) + the full audio stack (Eleven v3 TTS, voice cloning, lip-sync, sound effects, music). The agent picks a sensible default; you can override by asking.

## The honest rules (say these, they build trust)
- It's in **alpha** - things move.
- **Not free** - chat is billed on tokens, generations use credits, iterating costs each time. Set a threshold.
- Be **specific** in the first prompt = fewer re-runs = less money.
- The **API is coming soon**, not live - don't wait on it.
