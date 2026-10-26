## AI Video Production Script: Reverse Engineering a Skill (From Output $\rightarrow$ Workflow)

**Topic:** How to Reverse Engineer a Skill (From Output to Workflow)
**Target Skill:** Reverse Engineering Workflow Logic
**Tone:** Highly technical, Authority, Process-Driven. No hype, no vague concepts.
**Goal:** To teach a precise, 4-step, repeatable methodology for transforming a single "perfect" AI output—a single genius response—and systematically reversing-engineering its underlying logic into a reusable, structured skill (e.g., a Claude Code command or custom CLI tool).
**Target Audience:** Advanced AI Developers, Prompt Engineers, Automation Specialists.

---

## 💾 FILE PATH: ~/content/research/youtube/creator-breakdowns/video_003-reverse-engineer-skill-production-plan.md

### **Act I: The Problem (The Fluke) [Approx. 1:30]**
*   **Visual Hook:** Display a complex, beautifully structured AI output (The "Winner").
*   **Narrative Core:** This output *looks* perfect, but that level of quality is **non-deterministic**. It was a fluke—a perfect intersection of prompt, context, and timing. You cannot budget on it.
*   **The Thesis:** The failure of prompting is that it aims for an *output*. The mastery is in building a *system* that guarantees the output. We must build the skill.
*   **Key Concept:** Transition from Prompting (Giving instructions) $\\rightarrow$ Skill Engineering (Encoding rules).

### **Act II: The 4-Step Methodology (The System) [Core Lesson - 6:00]**
*   **Visual:** A clear, animated workflow diagram is essential here.

**STEP 1: Analyze the Output (The Annotation Pass)**
*   **Method:** Take the Winner output and break it down by sentence or element.
*   **Question:** For every piece of text, ask: *"What specific, preceding instruction or constraint MUST have been applied for this element to exist or achieve this format?"*
*   **Output:** A list of **Implicit Rules**. (Example: *Rule 1: Must include a 2-sentence summary*. *Rule 2: Must use exactly 3 bullet points per section.*)

**STEP 2: Identify the Structural Patterns (Pattern Extraction)**
*   **Method:** Systematically group the implicit rules into defined system constraints.
*   **The Triad:** Every skilled output adheres to three patterns:
    1.  **Structural Flow:** (e.g., Hook $\\rightarrow$ Proof $\\rightarrow$ CTA).
    2.  **Constraint Set:** (e.g., Tone: Formal. Word Count: 500 $\\pm$ 50. Required elements: Title, Lead, Sub-header).
    3.  **Mechanic:** (e.g., Use the AIDA model; always assume the user is skeptical).

**STEP 3: Encode the Logic (Writing the Skill/Meta-Prompt)**
*   **Action:** Translate the rules into an explicit command format (show `CLAUDE.md` or `Claude Code` structure).
*   **Coding Best Practice:** Use placeholders (`$ARGUMENTS`) for variable inputs. The skill must define its *own* internal workflow steps.
*   **The Result:** The output is no longer free text; it is a structured prompt template that forces adherence to the Rules/Constraints.

**STEP 4: Test the Skill (The Iron Test)**
*   **Crucial:** A skill is unreliable until it passes three tests:
    1.  **Typical Case:** Baseline verification.
    2.  **Edge Case:** Extreme short/long/vague input. (Does it break cleanly?)
    3.  **Failure-Prone Case:** Repeat the exact input that originally generated the "Winner" output to confirm the adherence is structural, not coincidental.

### **Act III: Advanced Application (The System Level) [Conclusion - 3:30]**
*   **Advanced Example (The Proof Point):** Transition to the Android/API deconstruction skill. Show that "Skill" isn't just text formatting—it's *systems* (calling external APIs, analyzing binary structure).
*   **Concept Elevation:** The highest level of AI engineering isn't asking for text; it's enabling a subprocess that requires state management (calling a shell command, reading a file, making an API call).
*   **Call to Action:** Your goal is no longer to write prompts; it is to become a system architect who designs the *logic gate* for the AI.

## 🛠️ IMPLEMENTATION NOTES FOR FILMING:
*   **[VISUAL]**: Use a split-screen: Left side shows the raw, free-flowing "Winner" output. Right side shows the highly structured, constrained "Skill" output.
*   **[SHOW]**: When demonstrating Step 3, physically show the variable definitions and the `{#if rule}}...{/{#if}}` logic, symbolizing enforced structure.
*   **[FOCUS POP]**: Emphasize that **Structure follows Style**. The skill defines the pipes and valves; the style is the water flowing through them.
