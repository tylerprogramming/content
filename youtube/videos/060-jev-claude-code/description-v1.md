# Description, video 060

Jev is TypeSafe AI's new decision model: $0.042 per million input tokens, output free, 70 to 500 ms per call (TypeSafe's published numbers). It does not write text. You send it a state and typed questions (Choice, Score, Noul) and it returns a pick with a probability and a confidence. In this video I take a real LLM-as-judge loop from my agentic prompts repo, replace the judge with one Jev Score question, and put the two runs side by side: latency, tokens, cost. Then I put Jev inside Claude Code as a PreToolUse hook that checks every Bash command with one Noul before it runs.

The honest section covers what the other Jev videos skip: which numbers are TypeSafe's and which are independent (Vercel, Bryo AI, Theo's 100-email run), the documented failure list for jev-1.13 including the 0.72 + 0.47 = 1.19 example from their own docs, the unpublished RLCD training method, and where Jev does not belong next to Claude Code.

Code: [UPDATE: repo link to jev_judge.py and hooks/jev_gate.py]
Free community: [UPDATE: Skool link]

Chapters
00:00 - The same decision, twice
00:45 - What Jev is in 60 seconds
01:45 - The before: an LLM as the judge
02:45 - The after: one Jev question
04:00 - Choice, Score, Noul and the confidence threshold
06:00 - A Jev gate on Claude Code's Bash tool
08:00 - Honest limits: 1.19, vendor numbers, no paper
09:30 - Where it fits next to Claude Code
10:30 - Recap
[UPDATE: timestamps after the edit]

Sources
TypeSafe launch post: https://typesafe.ai/blog/introducing-system-one-models-and-jev
Docs: https://docs.typesafe.ai
Failure modes for jev-1.13: https://docs.typesafe.ai/model-jaggedness/jev-1.13
Claude Code hooks: https://code.claude.com/docs/en/hooks
TechCrunch (Vercel, Bryo AI quotes): https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/
OpenRouter Jev docs: https://openrouter.ai/docs/guides/community/jev
Latent Space interview with Diogo Almeida: https://youtube.com/watch?v=cFx9Z3ZXca0
