# Northwind Financial - Senior Backend Engineer (Technical Round)

Date: 2026-06-09
Attendees: Tyler Reed (candidate), Priscilla Hahn (Engineering Manager, Payments), Devon Castellano (Staff Engineer)

## Summary

This was the second-round technical interview for the Senior Backend Engineer role on the Payments Platform team at Northwind Financial, a mid-size fintech doing card issuing and money movement. Priscilla opened with about ten minutes on the team's mission and where the role sits. The team owns the core ledger and the settlement pipeline, and they are actively rebuilding a chunk of it off an aging monolith. Stack is Java 21, Spring Boot, Postgres as the system of record, Kafka for events, and they run on AWS with a lot of ECS. They were upfront that there is real on-call here because it is money movement.

The bulk of the hour was a system design exercise led by Devon. The prompt was to design a payments ledger that guarantees no double-charges under retries and network partitions. We went deep on idempotency keys, how to scope them per merchant and per request, and where to store them so a retry hits the same row. I walked through a Postgres approach using a unique constraint on the idempotency key plus an outbox table for downstream events, and we debated exactly-once versus effectively-once. Devon pushed on what happens when the client retries with the same key but a different request body, and we talked through hash-of-payload validation and returning a 409.

Comp came up briefly at the end. Priscilla quoted a base band of roughly 195k to 220k plus a 15 percent target bonus and an equity refresher. She said the senior band tops out a bit higher for someone who lands the staff-track conversation later. Overall a strong, substantive conversation. They move fast and the people seemed sharp and direct.

## My notes

- Devon clearly the strongest technical interviewer so far, liked him
- ledger design - they really care about the retry / partition story, that was the whole crux
- idempotency key scoped per merchant + per request, unique constraint does the heavy lifting
- outbox pattern for Kafka events so the write + the publish are atomic in one txn
- they asked: same key, different body -> 409, store payload hash to detect
- reconciliation job nightly, they admitted it is painful today
- Priscilla mentioned the monolith migration is the real reason they are hiring
- on-call is 1 week in 6, money movement so it is serious
- comp 195-220 base, 15% bonus, equity refresh - room above for staff track
- vibe: fast, direct, no fluff, I like the team

## Action items / Next steps

- Priscilla to schedule final onsite loop (4 rounds, likely next week)
- Send Devon the link to the outbox-pattern writeup I mentioned
- Prep for final: deeper on Kafka exactly-once and Postgres isolation levels
- Ask recruiter for the full comp breakdown in writing before onsite
- Decide my target number before the offer conversation
