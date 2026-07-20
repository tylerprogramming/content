# The Ad You'll Build On Camera (Flows Agent demo) - EMBER Coffee

> For the Flows Agent video: you type ONE prompt, the agent builds the node graph and runs it.
> Structure Tyler likes: a script in parts + several reference images fed into a single video node,
> so the product and look stay consistent and the video is built FROM your real assets.
> Product/script swappable. Flows is alpha - verify the node behavior live.

## The structure (FINAL) - upload 1 real product, generate 5 to match it
1. **You upload ONE real product image** (your actual coffee bag / can / cup).
2. The **Flows Agent generates 5 more images that MATCH the uploaded product's design** - same color palette, lighting, and mood, so they read as one brand campaign - but showing different subjects (beans, a coffee house, someone enjoying a cup, a pour, a warm scene). Your uploaded image is the STYLE reference for all 5.
3. All **6 images feed into one Video node** as references -> it generates the ad from them (product stays consistent, everything matches).
4. **Eleven v3 voiceover** reads the script (in parts), **Music node** underneath.
5. Everything into a **Composition node** -> one finished 30s ad.

So the graph is:
[Upload: real product] --(style ref)--> Agent generates 5 matching shots -> [Video node] -> \
plus [Text to Speech] and [Music] -> [Composition].

The money shot of the whole video: you upload your real product, and the Agent builds a whole matching ad campaign around it, then turns it into a video. The 5 generated shots are your idea/product driving the look, not hardcoded - just prompts.

(Accuracy note: whether one video node takes multiple references depends on the model the Agent picks - some, like Kling "elements", take several; others take one start frame plus style refs. Let the Agent choose; if a model only takes one, it uses your real product image as the key reference and the rest guide the look. Verify live - it's alpha.)

## The product: EMBER Coffee (swap freely)
A premium small-batch coffee brand. Cozy, warm, morning-ritual energy. Upload or generate the reference images below.

Alternates: cold brew can, a cafe, a skincare serum, a candle. Any product you can supply reference images for.

## The images
- **Shot 1 (UPLOAD)**: your REAL product photo - the EMBER coffee bag / can / cup. This is the style anchor.
- **Shots 2-6 (GENERATED to match shot 1's design)**: the Agent creates these, matched to the uploaded product's palette + lighting + mood:
  2. Coffee beans scattered on a warm wooden surface
  3. A cozy coffee house interior, warm morning light
  4. A person in a cozy sweater holding a mug, morning light
  5. A close-up pour into a ceramic mug, steam rising
  6. A warm windowsill scene at sunrise with a mug (end-card feel)

These are a GUIDE, not hardcoded - the Agent generates them from your product's look. Tweak any with a follow-up.

## The script, in parts (Eleven v3 voiceover, ~25-30s)
Part 1: "Some mornings you wake up. Others, you rise."
Part 2: "EMBER is slow roasted in small batches, for the cup that actually earns its place in your hands."
Part 3: "Rich. Warm. Unhurried."
Part 4: "EMBER. Mornings worth waking up for."

## Music direction
Gentle, warm, unhurried instrumental. Soft piano or acoustic, low and cozy, a small lift on the final line. No vocals.

## THE PROMPT you type into the Flows Agent (word for word)
> "I've uploaded my real product photo - a coffee bag for a small batch brand called EMBER. Use it as the style reference and generate 5 more images that MATCH its design, color palette, lighting, and mood, so they look like the same brand campaign, but showing different subjects: coffee beans on warm wood, a cozy coffee house interior, a person in a cozy sweater holding a mug in morning light, a close-up pour with steam rising, and a warm windowsill at sunrise. Keep all 5 consistent with my uploaded product's look. Then feed all 6 images into a video node as references and generate a 30 second cinematic ad from them, warm and unhurried, golden morning light. Add a warm voiceover with Eleven v3 reading exactly: 'Some mornings you wake up. Others, you rise. EMBER is slow roasted in small batches, for the cup that actually earns its place in your hands. Rich. Warm. Unhurried. EMBER. Mornings worth waking up for.' Add gentle warm instrumental music with a small lift at the end. Assemble everything into one 30 second ad in a Composition node."

The 5 generated shots are a GUIDE, not hardcoded - the Agent matches them to YOUR product's look. Tweak any with a follow-up ("make the coffee house shot cozier," "warmer light on the pour").

## Answer its clarifying questions (likely)
- Length: 30 seconds
- Tone: warm, cinematic, cozy
- Voice: warm, calm (your pick)
- Use the uploaded images as references, keep the product consistent: yes

## Iteration prompts (show non-destructive editing live)
- "Use warmer morning light in the video."
- "Use a calmer, lower voice for the voiceover."
- "Make the music softer under the first line."
- "Give me a Spanish version of the voiceover." (bridge to the Dubbing video)

## Honest beats to keep in (on brand + brief-compliant)
- Every generation costs credits; re-running re-charges. Set Assist mode to auto-under-threshold first.
- Alpha - a generation may fail and you re-run it. Leave that in, it is real.
- The agent picks sensible models; you can override by asking.
