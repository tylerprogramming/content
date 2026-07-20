# Script - I Built an AI Agent That Answers WhatsApp Messages (ElevenAgents)

**Runtime target:** 12-16 minutes
**Format:** Horizontal, talking head + screen recording of the ElevenLabs dashboard + a phone showing the live WhatsApp thread
**Sponsor:** ElevenLabs (paid ambassador partnership) - #ad / #ElevenAgentsPartner
**Rules:** Full product name "ElevenAgents" in first 5 seconds. No em dashes. No competitor mentions. No money claims. Honest-limits beat mandatory. Product is ElevenAgents (NOT ElevenCreative / Flows).

Legend: [B-ROLL] = screen recording, [PHONE] = phone screen with WhatsApp, [CAM] = talking head, [TEXT] = on-screen text.

---

## 0:00 - 0:25 COLD OPEN (word for word)

[PHONE: a WhatsApp thread for "Maple Street Barbershop." A customer message lands: "Are you open Sunday?" Typing dots appear, then a reply types itself in about a second: "We're open Sunday 10am to 4pm. Want me to get you booked in?"]

**Tyler (VO):** "That business did not answer that message. An AI did. And it answered in about a second, on WhatsApp, the app that customer already had open."

[CAM: Tyler, smart-casual, clean background.]

**Tyler:** "This is ElevenAgents, and I connected it to a real WhatsApp number so it answers customers for me, texts and voice notes, all day, all night. Quick heads up before we go further, this video is sponsored by ElevenLabs and I'm one of their ambassadors, they're paying me to make this. So I'm going to show you exactly how to build one of these, and exactly where it costs you money. And I put the whole system prompt, the settings, and the setup steps in a free doc, link is in the description and pinned in the top comment, so you can copy it and build alongside me. Let's get into it."

---

## 0:25 - 1:40 WHAT THIS ACTUALLY IS

[CAM]

**Tyler:** "So let me set this up fast. ElevenAgents is ElevenLabs' platform for building AI agents that you can actually talk to, by voice or by text. You give it a personality, you give it knowledge, you give it a voice, and it holds a real conversation and gets things done."

**Tyler:** "The new part, the reason we're here, is that ElevenAgents now connects to WhatsApp. So instead of that agent living on a website widget somewhere, it lives on a WhatsApp Business number. And WhatsApp is where a huge chunk of the world already messages businesses. So now a customer messages the business like they always would, and the agent answers instantly."

[TEXT: "ElevenAgents = the AI agent platform | WhatsApp = where it now answers customers"]

**Tyler:** "And here's the part I like. It's the same agent everywhere. The brain you build works on the website, on a phone line, and on WhatsApp. One agent, same answers, every channel. So you build it once."

[B-ROLL: the ElevenLabs dashboard, Agents section, hovering the WhatsApp option.]

**Tyler (VO):** "Today I'm going to build one of these from scratch in front of you, connect it to WhatsApp, and then message it live so you can see it actually answer. And I'll be straight with you about the setup and the costs the whole way through, because there are a couple of real ones."

---

## 1:40 - 2:25 CTA #1 + WHO THIS IS FOR

[CAM]

**Tyler:** "If you want to build this in your own account while you watch, there's a link in the description to start with ElevenLabs. It's my partner link, using it is how they know you came from this channel and it helps support the videos, and there's a code down there too. Right next to it is a free doc with the exact system prompt I use, the knowledge base, and the step by step WhatsApp connection checklist, so you can copy it move for move. It's pinned in the top comment as well. Go grab it and follow along."

**Tyler:** "And who is this for? Two groups. One, anybody who runs a business and loses people in unanswered messages. A shop, a salon, a clinic, a gym, an agency. Somebody messages you, you're busy, six hours go by, that lead is cold. This answers the second it lands. Two, if you're a builder, this is a thing you can build for other businesses. You could set this up for a local business as a service. Same skills either way. Let me show you the build."

---

## 2:25 - 6:30 THE LIVE BUILD - CREATE THE AGENT

[B-ROLL: ElevenLabs dashboard. Tyler clicks into Agents, creates a new agent, names it "Maple Street Barbershop."]

**Tyler (VO):** "Okay, here's ElevenAgents. I'm creating a new agent and I'll call it Maple Street Barbershop. Now there are four things that make an agent good, and I'm going to do them in order. The system prompt, the knowledge, the voice, and then optionally tools. Let's start with the system prompt."

[B-ROLL: Tyler pastes the system prompt into the system-prompt field.]

**Tyler (VO):** "The system prompt is the personality and the rules. This is where I tell it who it is and how to behave. I'm keeping it plain. It's the front desk of a barbershop. Be warm, be short, answer questions about hours, services, and prices, help people book, and if you don't know something, say so and offer to take a message instead of making something up. That last line matters, it's what stops it from inventing prices."

[CAM]

**Tyler:** "The whole point of the system prompt is boundaries. A good agent isn't the one that knows everything, it's the one that knows what it's allowed to say and what to do when it doesn't know. I put this exact prompt in the free doc so you can just tweak it for your own business."

[B-ROLL: Tyler goes to the Knowledge base section, uploads a one-page FAQ document.]

**Tyler (VO):** "Next, knowledge. This is the difference between a chatbot and something actually useful. I'm uploading a one page document, just the real facts about the business. Hours, the list of services, the prices, the address, the booking policy. Then I turn on the knowledge base so the agent uses it. This is called RAG, retrieval, which just means before it answers, it looks things up in my document instead of guessing. So when someone asks how much a fade is, it reads the real price off the sheet."

[TEXT: "Knowledge base + RAG = it answers from your real info, not made-up info"]

**Tyler (VO):** "That FAQ document is in the free doc too. Copy it, swap in your own hours and prices, done."

[B-ROLL: Tyler goes to the Voice section, picks a voice, plays a preview.]

**Tyler (VO):** "Now the voice. This matters because on WhatsApp people send voice notes, and the agent can answer with a voice too. So I'll pick a friendly, natural sounding one and preview it. ElevenLabs has thousands of voices in a bunch of languages, so you can match the vibe of the business. I'll keep this one, it sounds like a real person on the front desk."

[CAM]

**Tyler:** "And there's a fourth thing, tools. Tools are where the agent doesn't just talk, it does. Like actually creating a booking in a calendar. That's the next level, and it's a whole thing on its own, so today I'm keeping the build to the three that get you ninety percent of the value, prompt, knowledge, and voice. But know that the door is there. Once this works, you can give it real actions."

[B-ROLL: Tyler picks the LLM/model option briefly.]

**Tyler (VO):** "Last setup thing, the model. This is the actual brain doing the reasoning. It picks a solid default, you can change it. I'll leave the default. Alright, the agent exists. It's got a personality, it's got the real facts, it's got a voice. Now let's give it a phone. Let's put it on WhatsApp."

---

## 6:30 - 9:30 CONNECTING IT TO WHATSAPP

[CAM]

**Tyler:** "Now I want to be honest with you before I click anything, because this is the part where a normal sponsored video would pretend it's one button. It's not one button. Connecting WhatsApp is the part with the most setup, so let me walk it exactly."

[B-ROLL: dashboard, the WhatsApp section.]

**Tyler (VO):** "First, the thing you actually need. You need a WhatsApp Business account. Not just the green WhatsApp on your phone, a WhatsApp Business account that you manage through Meta's WhatsApp Manager. If you run a business you may already have this. If you don't, you set one up, and Meta has to authorize it. That approval can take a little time, so if you're following along, start that early. I set mine up ahead of time so it's ready."

[TEXT: "You need: a WhatsApp Business account + Meta authorization (do this first, it can take time)"]

[B-ROLL: Tyler clicks Import account on the WhatsApp page, the Meta authorization flow opens, he selects the account and grants permissions.]

**Tyler (VO):** "Inside ElevenLabs I go to the WhatsApp page and hit import account. That kicks off Meta's authorization flow. I pick my business account, I grant the permissions so ElevenLabs is allowed to send and receive messages on it, and I finish the flow. Heads up, your exact screens here might look a little different than mine, Meta moves this stuff around, but the shape is the same, import and authorize."

[B-ROLL: back on the account settings page, Tyler assigns the agent.]

**Tyler (VO):** "Now the single most important click. On the settings page I assign my agent, Maple Street Barbershop, to this WhatsApp number. This is the one people forget. If you don't assign an agent, messages just come in and nothing answers them. So, assign the agent. Done."

[B-ROLL: Tyler shows the Profile tab and Call settings tab.]

**Tyler (VO):** "Couple of finishing touches. In WhatsApp Manager I can set the business profile picture so it looks legit to customers. And there's a call settings tab. If I turn that on, the agent can handle actual voice calls to the number, not just messages. I'll enable it so we can talk about it, and I'll note, to make outbound calls you also have to add a payment method, because those can cost money."

[CAM]

**Tyler:** "And that's the connection. Agent built, WhatsApp imported, agent assigned. Now the fun part. Let's actually message it and see if it holds up."

---

## 9:30 - 11:15 THE PAYOFF - MESSAGE IT LIVE

[PHONE: Tyler picks up his phone, opens WhatsApp fresh, messages the business number.]

**Tyler (VO):** "This is my phone, regular WhatsApp, messaging the business number like any customer would. I'll ask a normal question. How much is a haircut and are you open Sunday."

[PHONE: typing dots, then a reply arrives.]

**Tyler (VO):** "And there it is. It read the real price off my document, gave me the Sunday hours, and offered to book me. That's not a canned reply, that's the agent using the knowledge I gave it."

[PHONE: Tyler holds the mic button and sends a voice note: "Hey, do you guys do beard trims?"]

**Tyler (VO):** "Now let me push it. I'll send a voice note, because on WhatsApp that's how a lot of people actually message. Hey, do you guys do beard trims. I'm not typing it, I'm talking."

[PHONE: the agent replies.]

**Tyler (VO):** "It heard the voice note, understood it, and answered. It transcribes the audio, reasons about it, and replies. So a customer can talk to it exactly like they'd talk to a person, and it keeps up."

[CAM]

**Tyler:** "Stop and think about what that is. A customer messages a business at eleven at night, a real question, by text or by voice, and they get a correct answer in one second instead of waiting until tomorrow. That is the entire pain this solves. The message that used to sit unread and cost you the customer, now it's handled."

[TEXT: "[ Customer on WhatsApp ] -> [ Your ElevenAgent: prompt + knowledge + voice ] -> [ Instant reply, text or voice ]"]

---

## 11:15 - 12:45 THE OPPORTUNITY

[CAM]

**Tyler:** "So let's zoom out, because this is bigger than a barbershop. Think about who needs this. A dentist's office getting the same five questions all day. A gym answering hours and membership. A salon taking booking questions. An online store handling where's my order. Any business that gets messaged more than they can keep up with, which is basically all of them."

**Tyler:** "This is the kind of thing businesses pay for. A front desk that never sleeps, never takes a lunch, never leaves a message on read. And you just watched how it's built. So there are two moves here. Move one, you run a business, you build this for yourself and stop losing leads. Move two, you're a builder, and this is a service you can offer. You set this up for a local business, you maintain the knowledge base for them, and you've got something real to sell. Same build either way. I'm not going to throw income numbers at you, but you can see the demand for yourself."

[B-ROLL: quick montage of the agent answering a few different questions, showing it's not a one-trick reply.]

**Tyler:** "And because it's one agent across every channel, the same brain you built for WhatsApp is the same one you'd drop on their website or their phone line. You do the work once."

---

## 12:45 - 14:15 HONEST LIMITATIONS (the trust beat)

[CAM]

**Tyler:** "Alright, real talk section, because I'm not going to pretend this is magic and you shouldn't trust anyone who does. Here's the honest picture."

**Tyler:** "One, the setup is real. You need a WhatsApp Business account and Meta has to authorize it. That's not instant and it's the part most likely to slow you down, so start it early. Building the agent is the easy part, the account approval is the patient part."

**Tyler:** "Two, it is not free. You're using ElevenLabs, that has a cost. And separately, Meta charges for certain outbound messages, specifically when you message a customer outside the window right after they contacted you. Replies to someone who just messaged you are the cheap path. Blasting people first is where meta charges add up. Know that going in."

**Tyler:** "Three, outbound calls need a payment method on file and the customer's permission. So this isn't a robocall machine, and honestly that's a good thing. It's built to answer people, not to cold call them."

**Tyler:** "Four, it's only as smart as what you give it. If your knowledge document is thin or your system prompt is sloppy, the answers will be too. Garbage in, garbage out. Spend your time on that FAQ document, that's where the quality comes from. And set a max conversation length so a chat doesn't just hang open forever."

**Tyler:** "None of that is a dealbreaker for me. It's just the truth. What you get on the other side of that setup is an AI that answers your customers on the app they already use, by text or by voice, instantly. That's a real thing, and it actually works. I just showed you."

---

## 14:15 - 15:15 RECAP + FINAL CTA + OUTRO

[CAM]

**Tyler:** "Quick recap of what we did. I built an agent in ElevenAgents, gave it a system prompt for how to behave, uploaded a knowledge base so it answers from real facts instead of guessing, and picked a voice. Then I connected it to a WhatsApp Business number, assigned the agent, and messaged it live. It answered a text and a voice note in about a second. That's the whole thing."

**Tyler:** "If you want to build your own, two things are in the description and pinned in the top comment. The free doc with my exact system prompt, the knowledge base, and the WhatsApp connection checklist so you can copy it. And the link to get started with ElevenLabs. It's my partner link, there's a code down there too, and using it is how ElevenLabs knows you came from here and it supports the channel. Grab the doc, build your agent, and start it on your own number."

**Tyler:** "Full transparency one more time, this was a paid partnership with ElevenLabs, and I told you the good parts and the catches, because that's the only way this channel is worth anything to you."

**Tyler:** "If you got something out of this, subscribe. I make a lot of videos about AI agents and automation and how to actually use this stuff without the hype. I'll see you in the next one."

[TEXT: "Free doc + partner link in the description | #ad #ElevenAgentsPartner"]

---

## Compliance checklist (verify before publish)
- [ ] Full product name "ElevenAgents" spoken in the first 5 seconds
- [ ] Verbal paid-sponsorship disclosure in the first ~25 seconds
- [ ] Live product use shown (agent built + WhatsApp connected + messaged live), not just described
- [ ] Voice-note reply shown live
- [ ] The four build pillars shown: system prompt, knowledge base (RAG), voice, tools (mentioned)
- [ ] WhatsApp connection walked honestly (Business account + Meta authorization + assign agent)
- [ ] Honest-limits beat delivered (setup friction, costs, Meta outbound charges, garbage-in-garbage-out)
- [ ] Opportunity beat (build for yourself or for a business) with NO income numbers
- [ ] PartnerStack CTA at intro (~1:40), mid (implicit in build value), and end
- [ ] "system on one screen" graphic returned to at intro/payoff/recap
- [ ] No ElevenCreative / Flows references, no competitors, no puffery, no money claims
- [ ] No em dashes anywhere
- [ ] Script + thumbnail emailed to connie@elevenlabs.io for approval BEFORE publishing
