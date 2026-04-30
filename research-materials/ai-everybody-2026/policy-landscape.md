# Policy & Power Landscape: Who's Building AI and Why
## Research for "AI For Everybody 2026" Talk

---

## The Power Map

Understanding AI policy requires understanding who has power, what incentives they have, and what citizens can actually influence.

---

## Who's Building Frontier AI

### The Seven Major Players (April 2026)

**OpenAI**
- Status: Private company, ~$157B valuation (pre-IPO as of late 2025, IPO discussions ongoing)
- Backing: Microsoft is a major investor and primary cloud partner (~$13B+ invested)
- Products: ChatGPT, GPT-4o, o3 reasoning models, API
- Governance: Nonprofit/capped-profit hybrid structure undergoing transformation; nonprofit board retains some oversight but influence has diminished since the November 2023 governance crisis when Sam Altman was briefly fired and reinstated
- Stated mission: "Ensure artificial general intelligence benefits all of humanity"
- Critique: Mission articulation and commercial imperative are increasingly in tension

**Google DeepMind**
- Status: Fully owned by Alphabet (Google's parent), publicly traded
- Products: Gemini (consumer + enterprise), AlphaFold, weather prediction AI, medical imaging AI
- Distinctive feature: Integration of both pure research (DeepMind) and commercial deployment (Google Brain, now unified)
- Accountability: Subject to Alphabet shareholder accountability and antitrust scrutiny

**Anthropic**
- Status: Private, "public benefit corporation"
- Backing: Amazon is primary investor (~$4B+), Google has also invested
- Products: Claude models, enterprise API, consumer Claude.ai
- Distinctive feature: Founded by former OpenAI researchers specifically around safety concerns; most published safety research in the industry
- Critique: "Safety-focused" framing exists alongside rapid capability development and commercial scaling

**Meta AI**
- Status: Fully owned by Meta (Facebook parent), publicly traded
- Products: Llama open-source models, Meta AI assistant across all Meta platforms
- Distinctive feature: Committed to open-source release of models — Llama models can be downloaded, modified, and run without Meta's infrastructure
- Implication: Meta's approach democratizes access AND means the models are outside Meta's control once released

**xAI**
- Status: Private, Elon Musk's company
- Products: Grok AI assistant (integrated with X/Twitter)
- Distinctive feature: Integration with X/Twitter gives direct distribution to ~330M monthly active users
- Governance concerns: No apparent safety governance structure; Musk's personal views on AI safety have oscillated significantly

**Mistral**
- Status: French startup, significant Microsoft investment
- Products: Mistral series of models, primarily open-source
- Significance: Only major European frontier AI company; fills a political and strategic role in European AI sovereignty debates
- Critique: Small relative to US/Chinese players; dependent on partnerships with larger actors

**DeepSeek**
- Status: Chinese company (affiliated with hedge fund High-Flyer)
- Products: DeepSeek R1 and subsequent models (open weights)
- Significance: The January 2025 R1 release demonstrated that frontier AI capability could be achieved at dramatically lower cost than assumed, disrupting US market assumptions
- Geopolitical dimension: US export controls on advanced chips were meant to limit Chinese AI development; DeepSeek's success challenged this framing

---

## Regulatory Landscape

### The European Union: Most Advanced Regulation

**EU AI Act (Regulation 2024/1689)**
- Passed: March 2024
- Enforcement timeline: 
  - Banned practices prohibited: February 2025
  - GPAI (general-purpose AI) rules: August 2025
  - High-risk AI requirements: August 2026

**Risk tier framework:**
- **Prohibited**: Real-time biometric identification in public spaces (with narrow law enforcement exceptions), social scoring by governments, AI that exploits vulnerabilities, subliminal manipulation
- **High-risk**: AI in employment (screening, evaluation), critical infrastructure, education, healthcare, legal decisions, border control — requires human oversight, documentation, bias testing, transparency
- **General-purpose AI (GPAI)**: Foundation models like GPT must publish training data summaries, comply with copyright, evaluate systemic risks — frontier models (>10^25 FLOPs) face stricter requirements
- **Limited risk**: Disclosure requirements — users must be told when they're interacting with AI
- **Minimal risk**: No requirements

**Penalties**: Up to 7% of global annual revenue for most serious violations; up to 3% for most violations; up to 1.5% for incorrect information

**Honest assessment**: The EU AI Act is the world's most serious attempt at comprehensive AI governance. Its procedural focus (documentation, oversight processes) rather than outcome focus (did harm actually occur?) is a real limitation. Enforcement is genuinely difficult across complex AI supply chains. But it is real law with real penalties, and it is already shaping how companies design products for European deployment.

**Brussels Effect**: Because major AI companies want European market access, EU standards are influencing global product design — similar to how EU data protection rules (GDPR) became a de facto global standard for privacy.

### The United States: Fragmented, Behind

**Federal landscape (as of April 2026):**
- No comprehensive federal AI law has passed
- Executive Order on AI Safety (October 2023): Required safety testing and reporting for powerful AI models, promoted AI standards development through NIST, addressed some immigration pathways for AI talent — but EOs have limited durability and no enforcement against private actors
- NIST AI Risk Management Framework: Voluntary guidelines for responsible AI development — well-regarded technically, but voluntary
- Congressional activity: Multiple bills introduced, including AI liability frameworks, deepfake bills (some passed for electoral content), federal AI coordinator proposals — most stalled in committee

**Agency-level action:**
- FTC: Active on AI-related deception, fake reviews, and discriminatory AI in consumer decisions
- EEOC: Guidance on AI in hiring discrimination
- FDA: Formal AI medical device pathway; approved 800+ AI/ML-based medical devices as of 2025
- SEC: Disclosure rules for material AI-related risks in public company filings

**State level (leading):**
- Colorado: Passed SB 205 (2024) — first US law regulating high-risk AI in consequential decisions
- California: Multiple AI bills; AB 2013 required training data transparency; SB 1047 (mandating safety testing for large models) vetoed by Governor Newsom in 2024 — signaling California's ambivalence about AI governance
- Ongoing state-level activity on deepfakes (especially electoral and non-consensual intimate images)

**The Gap**: The US's most significant AI governance is in the EU Act and the voluntary commitments by major AI companies. This means the actual governance of the most powerful AI systems depends heavily on whether Anthropic, OpenAI, and Google choose to do the right thing — which is an accountability structure civil society should be concerned about.

**December 11, 2025 — Trump Executive Order 14365**: "Ensuring a National Policy Framework for Artificial Intelligence." Key provisions:
- Directs the Attorney General to establish an **AI Litigation Task Force** to challenge state AI laws on federal preemption grounds
- States with "onerous AI laws" made ineligible for remaining federal grants (via Secretary of Commerce)
- FCC must begin proceeding to adopt federal AI reporting standards that preempt state laws within 90 days
- March 20, 2026: White House released the "National Policy Framework for Artificial Intelligence"
- Colorado's Anti-Discrimination in AI Law (effective February 2026) and California's laws placed under particular scrutiny
- **Bottom line**: The Trump administration's posture is to maximize AI development speed with minimal regulatory friction, using federal preemption to block more restrictive state laws

### China: Tight Government Control

China has moved quickly to regulate AI content — not safety in the Western sense, but content aligned with state priorities. Key requirements:
- Generative AI services must submit models for security review
- AI-generated content must be watermarked
- AI services cannot generate content that "undermines state power" or "disturbs the economic or social order"
- Real-name registration for AI services

This approach prioritizes political control over technical safety. The Chinese AI industry is heavily state-guided; major AI companies (Baidu, Alibaba, Tencent, Huawei) operate in close coordination with government priorities. DeepSeek represents a partially different model but still operates within this system.

**2025 China updates**:
- **August 27, 2025**: State Council issued the **AI Plus Action Plan** — China's national AI strategy blueprint, prioritizing AI in science/tech, industrial use, consumer services, public welfare, governance, and international collaboration
- **November 1, 2025**: Three new national standards for generative AI security and governance took effect
- **July 2025**: China issued its AI Action Plan at the World Artificial Intelligence Conference, covering innovation, infrastructure, standards, and multi-stakeholder governance
- China removed a comprehensive AI law from its 2025 legislative agenda — instead prioritizing pilots, targeted rules, and standards to manage risk while keeping compliance costs low
- China called for international consensus on AI governance frameworks in its Global AI Governance Initiative

### International Governance: Nascent

**UK AI Safety Institute**: Established 2023, focused on frontier AI evaluation. Pioneered international AI safety evaluation partnerships. Relatively small resource base; influential as a model.

**Bletchley Declaration**: 28 countries (including US, UK, EU, China) signed a declaration at the November 2023 Bletchley Park AI Safety Summit committing to AI safety cooperation. Largely aspirational; limited concrete commitments.

**UN Advisory Body on AI**: Issued recommendations in 2024 for AI governance principles; no binding authority. More significant as a signal of global concern.

**G7/G20 AI governance**: Repeated statements of principle; limited enforcement mechanism.

**Honest assessment**: International AI governance is where climate governance was in the early 1990s — emerging, inadequate, but establishing early frameworks that may matter more as the technology matures.

---

## EU AI Act: Current Status (April 2026)

The EU AI Act enforcement is at a critical inflection point as of April 30, 2026:

**What's already in effect:**
- February 2, 2025: Prohibited AI practices banned (social scoring, real-time biometric surveillance, subliminal manipulation)
- August 2, 2025: GPAI model obligations live (affects GPT, Claude, Gemini etc.)

**What's coming:**
- August 2, 2026: Full high-risk AI compliance (hiring, healthcare, education, law enforcement AI)

**Fines**: Up to €35 million or 7% of global annual turnover for most serious violations; up to €15 million or 3% for other violations.

**The Digital Omnibus complication**: The European Commission proposed on November 19, 2025 to defer the high-risk compliance deadline from August 2, 2026 to December 2, 2027. However, the second political trilogue on **April 28, 2026** (two days ago) ended without agreement. If the Omnibus is not adopted before August 2, 2026, the original Act's provisions apply as written.

**Power concentration data (April 2026):**
- OpenAI's infrastructure commitments: $22.4B to CoreWeave, $38B to AWS, $250B+ to Microsoft Azure (Stargate)
- Anthropic: Amazon committed up to $100B over time for ~5 gigawatts of compute; Google invested up to $40B in April 2026
- NVIDIA: 90%+ market share in cloud AI accelerators; $130.5B revenue in FY2025 (up 114%); Blackwell GPUs sold out through mid-2026 with 3.6M unit backlog
- Hyperscalers collectively committed $300B+ to capex in 2025; Alphabet, Meta, Microsoft, Amazon combined: $380B expected through 2025/2026
- OpenAI + Anthropic combined captured **14% of all global venture investment** across all sectors in 2025

---

## What Citizens Can Actually Influence

This section is crucial for not leaving audiences feeling helpless.

### Near-Term Leverage Points

**Vote, and vote on AI governance specifically**: AI policy is increasingly on the ballot in legislative elections. Candidates' positions on AI regulation, data rights, worker protection, and AI in public sector decisions are meaningful. Constituents asking candidates about AI signals that these votes matter.

**Contact representatives**: The most impactful individual political action in the US system. Specific bills worth tracking: federal AI accountability legislation, deepfake accountability bills, data privacy framework bills, AI in hiring discrimination bills.

**Engage with regulatory comment processes**: The NIST AI Risk Management Framework, FTC AI guidance, and state-level AI rulemakings have public comment periods. Organized civil society participation in these processes shapes outcomes.

**Support civil society organizations doing AI accountability work**: EPIC (Electronic Privacy Information Center), AI Now Institute, Algorithmic Justice League, EFF — organizations that research, litigate, and advocate on AI governance issues. They are substantially underfunded relative to the companies they monitor.

**Consumer pressure**: Companies respond to consumer preferences. Demanding AI transparency (is this content AI-generated? Was AI used in this hiring decision? Does this product collect my data for AI training?) creates accountability incentives.

**Employer/employee pressure**: Workers can negotiate AI use policies in workplaces — disclosure requirements, human oversight requirements, anti-discrimination requirements. Unions have done this effectively in entertainment and other sectors; the model can spread.

### The Policy Window

Policy windows — moments when legislation is actually achievable — are rare and move quickly. Several factors suggest a window may exist in the next 24 months:
- Growing bipartisan concern about AI in elections and national security
- Growing Democratic concern about AI and labor
- Growing Republican concern about AI censorship and corporate power
- International pressure from EU AI Act creating competitive disadvantage for US companies
- A significant AI-related incident (major deception, discrimination, or safety failure) could accelerate legislation

Citizens who want meaningful AI regulation need to be organized *before* the crisis, not just reactive to it.

---

## Key Framing for Speakers

AI governance is not primarily a technical problem. It's a political economy problem: powerful commercial interests, inadequate regulatory infrastructure, fast-moving technology that outpaces policy cycles, and a public that is not yet engaged on this issue.

The good news: this is the moment when early engagement matters most. Rules written now will shape AI development for decades. The GDPR, written in 2016, still governs digital privacy in Europe and influences it globally. The AI governance rules being written now will have similar staying power.

The audience leaving this talk can be part of that early engagement — if they know what to ask for.
