# Helix Health - Staff Software Engineer, AI Platform

Date: 2026-06-12
Attendees: Tyler Reed (candidate), Naomi Okonkwo (Director of AI Platform), Raj Venkataraman (Principal Engineer), Casey Lindgren (Senior ML Engineer)

## Summary

Panel-style interview for the Staff Software Engineer role on the AI Platform team at Helix Health, a health-tech company building clinical documentation and patient-summary tooling. Naomi framed the role as half deep technical and half technical leadership. The platform team builds the shared infrastructure that product teams use to ship LLM features, so think internal RAG services, an evaluation harness, prompt and model versioning, and guardrails. Because it is healthcare there is a heavy compliance overlay - PHI handling, audit logging, and a hard requirement that nothing sensitive leaves their VPC.

Raj ran the architecture portion. We designed a RAG pipeline for clinician-facing summaries over patient records. We talked chunking strategies for clinical notes, hybrid retrieval with BM25 plus embeddings, and a reranker. He pushed hard on evaluation - how do you actually know the summaries are accurate and not hallucinating, which in a clinical setting is the entire ballgame. I walked through a layered eval approach: golden datasets with clinician-labeled answers, automated faithfulness and groundedness checks using an LLM judge, regression gates in CI, and human-in-the-loop review for a sampled percentage in production. Casey dug into how I would catch silent regressions when a model version changes underneath you.

The leadership round with Naomi was lighter on code and more about how I would set technical direction across three product teams, handle a disagreement with a principal, and mentor mid-level engineers. I leaned on examples from my current Fortune 500 role and the cross-team enablement work I do. Comp was not discussed in detail, Naomi said that is the recruiter's next conversation, but she hinted the staff band is competitive and includes meaningful equity.

## My notes

- Helix is healthcare so PHI / compliance is non-negotiable, everything stays in VPC
- Raj is the bar-raiser, very sharp on eval, that is clearly their pain
- RAG design - clinical notes chunking is hard, sections matter, used hybrid + reranker
- evaluation was the whole interview really - golden sets, LLM-as-judge for groundedness, CI gates
- silent regression on model swap -> Casey's question, answered with versioned eval suite + canary
- they have an internal eval harness already but want it productized for other teams
- leadership round - influence across 3 teams, mentoring, handling principal disagreement
- this is a true staff role, scope is platform-wide enablement, more my speed than IC-only
- comp deferred to recruiter, Naomi hinted competitive staff band + equity
- liked the mission, clinical accuracy is a meaningful problem

## Action items / Next steps

- Recruiter (Naomi to loop in) for comp + level confirmation
- Naomi to send the take-home-style design doc prompt for the final round
- Follow up with Raj - send my notes on groundedness eval metrics I mentioned
- Prep final round: be ready to write an actual eval-harness design doc
- Research Helix's recent funding and how stable the team funding is
