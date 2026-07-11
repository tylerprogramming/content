# Follow Along: Build an AI Agent That Answers WhatsApp (ElevenAgents)

> The exact system prompt, knowledge base, and setup steps from the video. Copy it, swap in your own business, and connect it to your own WhatsApp number.
> ElevenAgents and the WhatsApp integration are evolving, so a button may move, but the steps are the same.
>
> **Get started with ElevenLabs:** https://try.elevenlabs.io/8n9sgoi23fkk (code: [CODE])
> **Turn this into the public Google Doc lead magnet + pin it as the top comment.**

## What you're building
One AI agent in ElevenAgents - with a personality, real business knowledge, and a voice - connected to a WhatsApp Business number so it answers customer texts and voice notes instantly. Same agent also works on a website or phone line. Build it once.

## What you need before you start
1. An ElevenLabs account with ElevenAgents (start here: https://try.elevenlabs.io/8n9sgoi23fkk).
2. A WhatsApp Business account managed in Meta's WhatsApp Manager (business.facebook.com). Meta has to authorize it, and that can take time, so start it EARLY.
3. (Only if you want outbound calls) a payment method added in WhatsApp Manager.

---

## Step 1: Create the agent
ElevenLabs dashboard -> Agents -> New agent. Name it after the business (example: "Maple Street Barbershop").

## Step 2: The system prompt (copy this shape)
Paste this into the system prompt field and edit for your business:

> You are the front desk assistant for Maple Street Barbershop. Be warm, friendly, and brief. Answer questions about our hours, services, and prices, and help customers book an appointment. Only use the information in your knowledge base. If you do not know something or it is not in your knowledge, say so honestly and offer to take a message instead of guessing. Never invent prices, times, or policies. Keep replies short and easy to read on a phone.

The point of the system prompt is boundaries: what it's allowed to say, and what to do when it doesn't know.

## Step 3: The knowledge base (RAG)
Agent -> Knowledge base -> upload a one-page document with your real facts, then enable it so the agent answers from it. Example content to adapt:

> Maple Street Barbershop - FAQ
> Hours: Mon-Fri 9am-7pm, Sat 9am-5pm, Sun 10am-4pm.
> Services and prices: Haircut $30. Fade $35. Beard trim $15. Haircut + beard $40. Kids cut (under 12) $22.
> Address: 128 Maple Street, [City]. Parking on the street and in the lot behind the shop.
> Booking: walk-ins welcome, appointments preferred on weekends. To book, share your name, the service, and a day/time and we'll confirm.
> Payment: card, cash, and tap-to-pay.

RAG just means the agent looks things up in your document before it answers, instead of guessing. Swap in your own hours and prices and you're done.

## Step 4: Pick a voice
Agent -> Voice -> choose a natural, friendly voice and preview it. This is what customers hear when they send a voice note or call. ElevenLabs has thousands of voices across many languages, so match the business.

## Step 5 (optional, next level): Tools
Tools let the agent take real actions (like creating a booking), not just talk. That's a bigger setup, so skip it for your first build. Prompt + knowledge + voice gets you most of the value.

## Step 6: Connect WhatsApp
1. ElevenLabs dashboard -> WhatsApp page -> **Import account**.
2. Complete Meta's authorization flow: select your WhatsApp Business account and grant permissions so ElevenLabs can send and receive messages on it. (Your exact screens may differ; Meta changes this. The shape is import + authorize.)
3. On the account settings page, **assign your agent** to the WhatsApp number. This is the step people forget - without an assigned agent, inbound messages are ignored.
4. Profile picture: WhatsApp Manager -> Phone numbers -> select your number -> **Profile** tab.
5. Voice calls (optional): WhatsApp Manager -> Phone numbers -> **Call settings** tab to enable calling. Outbound calls also require a payment method (WhatsApp Manager -> Overview -> Add payment method).

## Step 7: Test it
Message the WhatsApp number from your own phone like a customer would. Ask a real question ("how much is a haircut and are you open Sunday"). Then send a voice note - it transcribes the audio and answers. If the answer is wrong, fix your knowledge document, not your patience.

---

## What it can do (verified)
- Inbound: text messages, voice notes (auto-transcribed), images, documents, locations, contacts, and inbound voice calls.
- Outbound: text via approved templates, and voice calls (which require the customer's permission and a payment method).
- One agent, same knowledge, across WhatsApp + web + phone.

## The honest rules (say these, they build trust)
- **Setup is real.** You need a WhatsApp Business account and Meta authorization. Start it early.
- **Not free.** ElevenLabs usage has a cost, and Meta charges for certain outbound messages sent outside the window right after a customer messages you. Replying to people who just messaged you is the cheap path.
- **Garbage in, garbage out.** The agent is only as good as your system prompt and knowledge base. Spend your time on the FAQ document.
- **Set a max conversation duration** so chats don't hang open forever.

## Sources (product truth)
- ElevenAgents overview: https://elevenlabs.io/docs/eleven-agents/overview
- WhatsApp integration docs: https://elevenlabs.io/docs/eleven-agents/whatsapp
- WhatsApp support announcement: https://elevenlabs.io/blog/elevenlabs-agents-whatsapp-support
