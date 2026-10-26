## In this lesson
You'll upload one product photo, paste one prompt, and let the Flows Agent in ElevenCreative build the whole ad pipeline: images, video clips, voiceover, music and the final edit.
Then you'll change it by talking to the agent, and swap in a new product to reuse the same flow.

## Good to know
- Time: I built the coffee ad live during the recording. Plan on an hour for your first one so you can iterate.
- Cost: Paid. The Starter plan gives 30,000 credits a month, the Creator plan 121,000. My ad came to about 32,000 credits, so you really need Creator for this. The agent chat is billed on tokens and every generation uses credits, so each re-run costs you.
- Level: Beginner. No code. You talk to the agent and it builds the nodes.
- Flows is in alpha, so the screens may look a little different when you try it.
- It's not really one prompt. My Pepsi ad had a long conversation behind it. Expect to iterate.
- This is a paid partnership. I'm an ElevenLabs ambassador.
- Partner link: the ElevenLabs link below is my partner link. I get paid if you sign up through it.

## What you need
- An ElevenLabs account, Creator plan recommended (paid). My partner link: https://try.elevenlabs.io/8n9sgoi23fkk
- Plans and credits: https://elevenlabs.io/pricing
- One photo of your product, saved on your computer (a bag, can, bottle, whatever you sell)

**1. Open Flows in ElevenCreative (0:33)**
ElevenLabs has three areas: ElevenCreative, ElevenAgents and the API. Go to ElevenCreative, then Flows. Open one of the example flows first, like the luxury perfume ad, to see how image, video, voiceover and composition nodes connect.

**2. Set the agent permissions before you spend (15:38)**
At the bottom of the agent chat there are three modes:
- Auto run: it runs everything with no confirmation.
- Confirm edits: you approve each step.
- Auto under threshold: it runs anything under a credit limit and asks about the rest. This is the one they recommend. Mine was set to 300, so a 178 credit GPT Image 2 node just ran.

**3. Start a new flow and paste the prompt (4:29)**
Click Create new flow. You can build nodes by hand from the bottom bar, but I let the agent do it. Paste this into the agent chat (swap EMBER and the scenes for your product):

> I've uploaded my real product photo - a coffee bag for a small batch brand called EMBER. Use it as the style reference and generate 5 more images that MATCH its design, color palette, lighting, and mood, so they look like the same brand campaign, but showing different subjects: coffee beans on warm wood, a cozy coffee house interior, a person in a cozy sweater holding a mug in morning light, a close-up pour with steam rising, and a warm windowsill at sunrise. Keep all 5 consistent with my uploaded product's look. Then feed all 6 images into a video node as references and generate a 30 second cinematic ad from them, warm and unhurried, golden morning light. Add a warm voiceover with Eleven v3 reading exactly: 'Some mornings you wake up. Others, you rise. EMBER is slow roasted in small batches, for the cup that actually earns its place in your hands. Rich. Warm. Unhurried. EMBER. Mornings worth waking up for.' Add gentle warm instrumental music with a small lift at the end. Assemble everything into one 30 second ad in a Composition node.

Then upload your product photo into the flow. I used a Tom Hanks coffee bag from a Google search. Make the brand name in the prompt match your photo. I didn't, and that's why my ad says Ember.

**4. Pick a voice and let it build the nodes (6:25)**
The agent offers a few voices to preview. I picked Frank. It lays out its plan (five campaign images, a 30 second ad, voiceover, music, composition) and then creates the nodes. Each node shows its model and credit cost. You can change the model, aspect ratio and resolution. I chose GPT Image 2 because it costs less than Nano Banana. Count the image nodes. Mine made three, so I typed:

> I only see three image generation nodes. I thought we were doing five.

**5. Animate the clips (8:59)**
The agent turns each image into a video clip. You can pick the video model and filter by realistic or upscaling. Most models only do set lengths, like 4, 6 and 8 seconds for Veo 3.1 Fast, or 2 second clips from a Runway model. Messy canvas? Select all the nodes, right click, and choose Tidy up.

**6. Watch the composition (10:44)**
Everything lands in the Composition node: one video track, plus audio tracks for voiceover and music. Download it and watch it.

**7. Change it by talking (11:40)**
My first cut never showed the word Ember on screen. So I typed:

> For the first and last video, we should have Ember cinematically onto the video as well as text.

It regenerated those two images with two options each, then re-animated them. Check it didn't leave the old nodes behind. I had to ask it to remove the original two. Then rerun the Composition node (13:25) and download again. Rerunning the composition costs no credits.

**8. Swap in a new product (14:47)**
Replace the photo at the top of the flow and click Run from here. If it's a different kind of product, ask the agent to update the image, video and music prompts first, or your energy drink ad will sound like a cozy coffee shop:

> This is my new product. We need the prompts updated for this product now.

## Files and links
- ElevenLabs (my partner link): https://try.elevenlabs.io/8n9sgoi23fkk
- ElevenCreative: https://elevenlabs.io/creative
- Flows (sign in first): https://elevenlabs.io/app/flows
- Pricing and credits: https://elevenlabs.io/pricing

## If it breaks
- Fewer image nodes than it promised: tell it how many you see and how many you expected. It adds the rest.
- Your edit doesn't show up in the final ad: rerun the Composition node. It only picks up updated clips when you run it again. It's free.
- Old nodes still wired in after a change: ask the agent to remove the originals.
- You can't make a clip an exact length: video models have fixed durations. Pick a model whose lengths fit your script.
- Seedance says it's not available: it isn't offered in the US. Pick another video model.
- The cost estimate looks huge: mine said $450, which was not correct. Go by the credit number. Mine was about 32,000.
- The ad mentions the wrong brand: your prompt and your photo don't match. Ask the agent to redo the prompts based on your uploaded image.

## Next
Build an AI agent in 5 steps with Claude Code
