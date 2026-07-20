# Aurora Cloud - Senior Backend Engineer (Full Loop)

Date: 2026-06-18
Attendees: Tyler Reed (candidate), Hannah Brightwater (Recruiter coordinator), Marcus Feld (Senior Engineer, coding), Imani Russell (Principal Engineer, system design), Theo Vasquez (Engineering Manager, behavioral)

## Summary

Full virtual onsite loop for the Senior Backend Engineer role at Aurora Cloud, a large cloud-infrastructure company. Four back-to-back rounds. Hannah coordinated and set expectations up front - the bar is high, they want distributed-systems depth, and the behavioral round carries real weight here. The team owns a multi-tenant control plane and they care a lot about reliability at scale.

The coding round with Marcus was to design and implement a rate limiter. We started with a simple token bucket in memory, then he steadily raised the stakes - make it thread-safe, then make it distributed across many nodes, then handle clock skew. I implemented the token bucket cleanly, talked through a sliding-window-log alternative and its memory tradeoffs, and we landed on a Redis-backed distributed approach using a Lua script for atomicity. He seemed satisfied, especially with the atomic-increment-plus-expire detail. The system design round with Imani was a large one - design a globally distributed metadata store with strong-ish consistency. We covered partitioning, replication, consensus (Raft), read versus write quorums, and the CAP tradeoffs they live with. Imani was tough but fair and clearly senior.

The behavioral round with Theo was the most leadership-heavy. He went deep on a time I drove a technical decision that was unpopular, a time I was wrong and had to course-correct, and how I handle being on-call during an incident. I leaned on real examples from my enterprise work. Comp came up at the end with Hannah - she said the senior band lands roughly 210k to 245k base, a 20 percent target bonus, and a sizable RSU grant vesting over four years, with refreshers. This was the strongest overall loop of the four and probably my top option on paper.

## My notes

- Aurora is the big-name one, bar is high, 4 rounds back to back, draining but good
- coding = rate limiter, escalated: in-mem token bucket -> thread-safe -> distributed -> clock skew
- nailed the Redis + Lua atomic approach, Marcus liked the increment+expire detail
- sliding window log alternative discussed, memory tradeoff
- Imani's design round = global metadata store, Raft, quorums, CAP - she was tough but fair
- Theo behavioral - unpopular decision, time I was wrong, on-call incident handling
- used real enterprise examples, felt strong
- comp: 210-245 base, 20% bonus, 4-yr RSU + refreshers - strongest on paper
- this is probably my #1 if the offer lands
- one ding: process is slow, decisions take a few weeks to come back

## Action items / Next steps

- Hannah to gather panel feedback and follow up within a week
- Send thank-you notes to Marcus, Imani, and Theo
- Prep references in case they ask (likely if offer is coming)
- Me: this is the benchmark - hold other offers against this comp + scope
- Confirm start-date flexibility given current role notice period
