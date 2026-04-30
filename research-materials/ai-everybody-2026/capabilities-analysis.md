# AI Capabilities Analysis: What's Real in April 2026
## Research for "AI For Everybody 2026" Talk

---

## The Honest Map: What AI Can Do, What It Can't, What's In Between

The single biggest source of public confusion about AI is the gap between the marketing narrative and the operational reality. Both the hype and the dismissiveness miss the truth. This document provides a calibrated assessment.

---

## What AI Can Do Reliably (High Confidence)

### Text and Language

**Writing assistance** — AI can draft, revise, summarize, translate, and adapt text at professional quality for most standard tasks. Business emails, reports, documentation, marketing copy, first drafts of speeches, legal boilerplate, grant applications. Not all writing — creative voice, original argument, and context-sensitive judgment still require humans — but the bulk of text-production work can be significantly accelerated.

**Translation** — Fluency across 100+ languages at professional quality for most common language pairs. Specialized and technical translation still benefits from human review. Real-time spoken translation has crossed the "good enough" threshold for most conversations.

**Summarization and extraction** — Given a long document (contract, scientific paper, earnings report, meeting transcript), AI can reliably extract key information, identify main arguments, and produce structured summaries. This is one of the highest-value, lowest-risk applications.

**Question answering from documents** — When given source material to work from (rather than asked to produce knowledge from memory), AI accuracy increases substantially. "What does this contract say about termination clauses?" is far safer than "Tell me about termination clauses in employment law."

### Code and Technical Tasks

**Code generation** — AI can write functional code in most major languages for most standard tasks. Experienced developers using AI tools report 2-5x productivity gains on implementation tasks. This doesn't eliminate the need to understand code — it eliminates some of the *typing* and *scaffolding* — but you still need to know if what it produced is correct.

**Code explanation and debugging** — AI excels at explaining what code does and identifying common bugs. These tasks are often the most time-consuming for developers; AI assistance here is highly reliable.

**Data analysis** — Given structured data and clear questions, AI can write the analysis code, interpret results, identify anomalies, and generate visualizations. Spreadsheets, SQL databases, Python notebooks — all accessible to non-coders via AI.

### Reasoning and Analysis (with caveats)

**Structured analysis** — Breaking down a problem into components, applying frameworks, identifying pros and cons. Solid for well-defined problem types. Weaker for genuinely novel situations with no clear precedent.

**Mathematical reasoning** — Dramatically improved since 2023, especially for models with "thinking" capabilities. Top AI systems score at PhD level on competition mathematics. But: they can still fail on novel problems in unexpected ways. Verify mathematical outputs for anything consequential.

**Research synthesis** — Given access to source documents, AI can synthesize information across multiple sources effectively. It's a powerful research assistant. It's not a replacement for expert judgment on what the synthesis means.

---

## What AI Cannot Do Reliably (Important Caveats)

### The Hallucination Problem

This is the most important limitation for lay audiences to understand. AI language models can and do generate plausible-sounding but factually incorrect information — confidently. Not sometimes. Routinely.

The technical reason: AI doesn't "look up" facts. It generates the most statistically probable next word given the context. When it doesn't know something, it doesn't say "I don't know" — it generates something that sounds like an answer.

Practical implication: **Never use AI output as a sole source for factual claims that matter.** Medical information, legal specifics, financial numbers, historical facts, quotes attributed to real people — all require verification. The AI will sound certain even when it's wrong.

How to mitigate: Ask AI to provide sources, then verify the sources exist and say what the AI claims they say. Many don't. Ask AI to do tasks where the output can be verified (write code you can run, draft text you can review, analyze data you have).

### Novel Reasoning

AI is excellent at pattern-matching on situations it has "seen" (in training data). It struggles with genuinely novel problems that require first-principles reasoning in unfamiliar territory. This is why AI passed the bar exam (lots of legal text in training data) but still struggles with truly original scientific hypotheses or unprecedented legal cases.

### Physical World Interaction

As of April 2026, AI's physical world capabilities remain limited. Robotic AI can perform specific physical tasks in controlled environments (warehouses, labs) but generalized physical AI — a robot that can navigate your kitchen and make breakfast — is not commercially deployed at scale.

### Long-Horizon Autonomous Action

Agentic AI can complete multi-step tasks, but reliability degrades with complexity and duration. A 10-step automated workflow works much better than a 100-step one. The more consequential the task (affecting real money, real relationships, real data), the more human oversight remains essential. Current agentic systems are best thought of as "supervised automations" rather than truly autonomous agents.

### Understanding, Intention, and Values

AI language models do not understand in the way humans understand. They process patterns. This distinction matters for:
- **Tasks requiring genuine empathy** — AI can produce empathetic-sounding responses; whether that constitutes real empathy is philosophically contested and practically important in healthcare, therapy, and grief support contexts
- **Tasks requiring values judgment** — AI can apply rules about values. It cannot hold values. This matters in ethical dilemmas, nuanced fairness decisions, and anywhere the right answer isn't in the training data

---

## The Hardest-to-Explain Middle Ground

### "Brilliant Intern" Model

The most useful analogy for lay audiences: **AI is like having access to a brilliant intern who sometimes makes things up confidently.**

They can do enormous amounts of work, very quickly. They have knowledge spanning every domain you can think of. They are tireless and never resentful. 

But they need supervision. They will occasionally produce confident nonsense. They don't know what they don't know. And for anything truly consequential, you still want an experienced person to review their work.

### Context Dependency

AI performance varies dramatically by:
- **How well you ask the question** — Vague prompts get vague answers; specific, well-structured prompts get dramatically better results. This is the "prompt engineering" skill, and while it's real, it's also evolving fast as models get better at inferring intent.
- **Whether you have source material** — AI with documents outperforms AI from memory by a wide margin
- **Domain** — AI performs at near-expert level in areas heavily represented in training data (medicine, law, software, finance, science) and worse in niche domains with less published material

### The Improvement Trajectory

Perhaps most important for public understanding: the capabilities described as limitations today were not limitations just 18 months ago. The direction of travel is clear. The speed is debated. But planning as if today's limitations are permanent would be a mistake — and planning as if tomorrow's capabilities are here today would be an equal mistake.

---

## Current Hallucination Statistics (2026 Benchmark Data)

From a 2026 benchmark across 37 AI models:
- Hallucination rates range from **15% to 52%** depending on the model and task
- In **medical case summaries**: hallucinations reach **64.1%** without mitigation prompts
- In **legal queries**: hallucinations occur **69–88%** of the time on specific questions
- A 2025 mathematical proof confirmed hallucinations **cannot be fully eliminated** under current LLM architectures
- Models were **34% more likely** to use highly confident language ("definitely," "certainly") when generating incorrect information than correct information

**Key insight for audiences**: The paradox of AI confidence — the system sounds most certain precisely when it's most wrong.

---

## AI Coding Tools: Current State (April 2026)

- **GitHub Copilot**: 4.7 million paid subscribers (Jan 2026, up ~75% YoY); 90% of Fortune 100 companies; 29% of developers use it at work
- **Cursor**: Crossed $2 billion annualized revenue (early 2026); 18% market share within 18 months of launch
- **Claude Code**: 57% developer awareness (vs. 31% in April-June 2025); 18% using at work
- **Market size**: AI coding tools market reached $7.37 billion in 2025
- **Productivity**: Developers complete tasks **55% faster** with GitHub Copilot (study of 4,800 developers); average **3.6 hours saved per week**
- **Goldman Sachs**: Piloting AI coding agents alongside 12,000 developers; claims equivalent of 20% efficiency gain
- **Nubank**: Used Devin for large-scale refactoring → 8x engineering efficiency, 20x cost savings (January 2026)

---

## Agentic AI: Real Deployments vs. Demos (April 2026)

- Agentic AI market: $7.6 billion in 2025 → projected $10.8 billion in 2026
- **Enterprise adoption gap**: 79% of enterprises say they've adopted AI agents; only **11% run them in production**
- Most reliable use: supervised, bounded tasks (code review, data extraction, document processing)
- Devin 2.0: Price dropped from $500/month to $20/month + $2.25 per Agent Compute Unit
- Gartner prediction: 75% of software developers will use AI coding agents by 2028 (up from <10% in 2023)
- Multi-agent systems (specialized agents coordinating) are the dominant 2026 architectural trend

---

## A Calibration Exercise for Audiences

Ask your audience to imagine a scale:
- 1 = AI is useless for this
- 5 = AI needs significant supervision but adds real value
- 10 = AI handles this as well as or better than a skilled human

Typical ratings by task:
- Summarizing a long document: **8-9**
- Translating a business email: **8-9**
- Writing first draft of a report: **7-8**
- Debugging code I wrote: **7-8**
- Answering a legal question: **5-6** (needs expert verification)
- Diagnosing a medical symptom: **4-5** (useful starting point, not diagnosis)
- Making a nuanced ethical decision: **3-4**
- Understanding why my teenager is acting out: **2**

This framework lets audiences think concretely about where AI fits in their own lives without either dismissing it or over-trusting it.
