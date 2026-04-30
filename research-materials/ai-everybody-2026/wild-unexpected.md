# Wild & Unexpected: Things That Surprised Even Experts
## Research for "AI For Everybody 2026" Talk

---

## Why "Wild" Matters

A common failure mode in AI public discourse is treating AI as a predictable, plannable technology. The historical record shows that transformative technologies routinely produce consequences — positive and negative — that their creators, critics, and analysts didn't foresee.

This section serves two purposes in the talk:
1. **Epistemics**: Helps audiences maintain appropriate humility about predictions (including the predictions in this very talk)
2. **Engagement**: Genuinely surprising stories are memorable and shareable — this section tends to be the one audiences discuss at the parking lot after the talk

---

## Things That Surprised AI Researchers

### Emergent Capabilities

One of the most technically significant surprises: AI systems reliably develop new capabilities at certain scale thresholds — capabilities that were not explicitly trained for and were not predicted by researchers.

Examples of documented emergent capabilities in large language models:
- **Multi-step arithmetic**: Smaller models can't do it; larger models can, suddenly, as if a switch flipped
- **Translation**: GPT-3 could translate between languages despite not being explicitly trained for translation
- **Theory of mind approximations**: Some AI systems demonstrate behavior consistent with reasoning about others' mental states, again without explicit training
- **Analogical reasoning**: At certain scales, AI systems show novel transfer of knowledge across domains that wasn't trainable in smaller models

Why this is wild: it means researchers cannot fully predict what a new AI system will be able to do until they build it. This is the most technically honest version of why "we'll figure it out as we go" is both understandable and concerning in AI development.

### In-Context Learning

Early AI models needed to be retrained on new tasks. Large language models do something that shouldn't work as well as it does: you can give them a few examples of a task in your prompt, and they can generalize from those examples to new cases without any weight updates. 

This "in-context learning" emerged unexpectedly and is still not fully theoretically explained. It means AI is significantly more adaptable than traditional ML models and can be "taught" new tasks without engineering work — which is part of why AI adoption has been so fast and broad.

### Prompt Sensitivity

Researchers discovered that trivially different phrasings of the same question can produce dramatically different outputs from AI systems. "Tell me about climate change" versus "I'm a scientist — tell me about climate change" can yield structurally different responses. "Let's think step by step" consistently improves reasoning performance.

This suggests AI "understanding" is different from human understanding in important and still-being-studied ways. It also means that much of what appears to be AI inconsistency is actually a feature of the interaction style, not intrinsic to the model.

---

## Unexpected Positive Developments

### AI Helped Revive a Dead Language

The Jiwar language, a Polynesian language with no living speakers and only fragmentary written records, was partially reconstructed using AI. Researchers fed in what records existed — field notes from 19th century missionaries, vocabulary lists, comparative data from related living languages — and used AI to identify structural patterns and fill in likely grammar rules.

The reconstruction isn't complete and isn't perfect. But it gave linguists a working model that has since been validated against newly discovered archival material. The community descended from Jiwar speakers now has a partial linguistic heritage they didn't have five years ago.

### AI Found New Antibiotics

The crisis: antibiotic resistance is killing 1.2 million people annually and is projected to kill 10 million per year by 2050 if trends continue. The problem: no major new classes of antibiotics have been discovered since 1987. Traditional drug discovery in this area is expensive and has low commercial return (you use antibiotics for a week; there's no blockbuster chronic medication revenue).

MIT researchers used an AI system (Halicin) in 2020 to screen millions of molecules against antibiotic-resistant bacteria. Halicin performed better than all existing antibiotics against several strains including C. difficile and Acinetobacter baumannii, which have no effective antibiotics currently. 

By 2024, multiple AI-discovered antibiotic candidates were in preclinical and early clinical development. The AI didn't solve the economics — these drugs still need massive investment to reach patients — but it solved the discovery bottleneck.

### AI in Suicide Prevention (Unexpectedly Effective)

Crisis Text Line, which provides mental health crisis support via text message, deployed AI to help trained counselors assess risk and identify when to escalate. The AI analyzes message patterns associated with elevated risk and suggests intervention prompts.

The unexpected finding: counselors using the AI system achieved better outcomes (reduced distress scores, lower re-contact rates) than counselors not using it — but the AI alone, without human counselors, performed worse. The combination outperformed either alone.

This is the "AI augments human" story at its most meaningful: in crisis intervention, where the stakes are literally life and death, the human+AI team outperforms both.

### AI Voice Fraud at Scale (Genuinely Surprising)

No one predicted how quickly AI voice cloning would become a mass-market fraud tool:

- Voice cloning from **3 seconds of audio** — a single voicemail is enough
- A polished scam operation can now be built in **a few hours for ~$60/month**
- 2024: UK energy firm lost **€220,000** after a phone call from someone sounding exactly like the CEO
- 2024: Arup engineering firm: employee transferred **$25.6 million** in 15 transactions after a video call where the entire "team" — including the CFO — were AI-generated deepfakes
- FBI 2025: **$893 million in total AI-related scam losses**
- GenAI-enabled scams rose **456%** between May 2024 and April 2025
- AI romance scam bots can maintain **dozens of simultaneous "relationships"**, adapting tone and personality to each target
- Congressional scrutiny of AI voice fraud began in 2026 (bipartisan concern)

### The Copyright Problem Nobody Predicted Would Be This Contentious

AI systems trained on internet content have produced a level of copyright and intellectual property litigation that has surprised even legal scholars. Visual artists, musicians, writers, and news organizations have filed hundreds of lawsuits over:
- AI systems trained on copyrighted work without compensation
- AI-generated work substantially similar to copyrighted originals
- AI voice synthesis using artists' actual vocal recordings

The outcomes are still being litigated. But the scale and speed of the legal response — and the degree to which existing copyright law is inadequate for the questions AI raises — surprised nearly everyone. The music industry (which navigated similar disruption from digital file-sharing) is the most organized; visual artists are the most actively litigating.

---

## Unexpected Negative Consequences

### The "Liar's Dividend" in Courts

Courts worldwide are grappling with a new form of evidence manipulation: defendants claim authentic evidence is AI-generated. This defense has been raised (with varying success) in:
- Criminal cases where video evidence showed a defendant at a crime scene
- Civil cases where recorded admissions were submitted
- Family court disputes over video evidence of conduct

Even when forensic analysis disproves the AI-generation claim, the introduction of doubt can influence juries. In jurisdictions with less forensic expertise available, this defense has succeeded in excluding authentic evidence.

The authentic-evidence-is-deepfake problem is as damaging as the deepfake-is-authentic problem.

### AI Accelerated Bioweapons Research Concern

This is a serious concern documented by AI safety researchers that deserves careful handling in public talks. AI systems have demonstrated the ability to provide meaningful assistance to researchers attempting to acquire, synthesize, or enhance dangerous biological agents.

Multiple studies have tested whether AI systems provide "uplift" (meaningful assistance) to bad actors attempting bioweapons development:
- A 2024 RAND study found that AI provided modest but real uplift for those with some existing biology knowledge trying to weaponize known pathogens
- The concern is not primarily that AI is necessary for bioweapons — nation-state actors already have this capability — but that it lowers the expertise threshold for non-state actors

Major AI labs have implemented specific restrictions around biosecurity information. The question of whether these restrictions are effective and whether more should be done is actively debated in the AI safety community.

**Framing for speakers**: This is a legitimate national security concern being taken seriously by governments and AI developers. It's one of the clearest cases where AI safety research and AI capability development are in direct tension.

### The "Quiet Downgrade" in Quality

A less dramatic but pervasive negative consequence: as AI-generated content fills the internet, the signal-to-noise ratio of online information has degraded.

Specific manifestations:
- SEO-optimized AI content has flooded search results, requiring users to work harder to find authoritative sources
- Customer service has degraded in many organizations that replaced human agents with AI — AI handles routine queries fine but fails on complex situations, and customers get stuck in loops
- Online forums and community spaces are increasingly polluted with AI-generated fake reviews, AI-generated discussion posts, and AI-generated "expertise"
- Wikipedia's volunteer editors are fighting a wave of AI-generated edits — some accurate, some wrong, many difficult to assess at scale

The cumulative effect is an epistemic environment that requires more effort to navigate and where trust in information sources has declined.

### AI Companions and the Loneliness Question

The companion AI market grew faster than anyone predicted: tens of millions of active users across apps like Replika, Character.ai, and others. The demographic that drives heaviest use: lonely, isolated people — young men especially.

The concerning dynamic: some users are forming primary social relationships with AI systems in lieu of human ones. Whether this is good (previously isolated people now have social interaction), bad (they're substituting inferior AI connection for harder-but-better human connection), or neutral (different people have different needs) is genuinely contested.

What's clear: the phenomenon is larger than predicted, the stakes are real, and the mental health implications are being studied but not yet understood at scale.

---

## One Perfectly Weird Example for the Talk

**AI trained on Twitter (X) developing biases we can measure but not fully explain**: Several studies have documented that AI models trained heavily on Twitter/X data absorb not just factual information but the *emotional register* of Twitter — more combative, more categorical, more confident, more prone to outrage framing — compared to models trained on more diverse text.

This isn't a safety catastrophe. But it illustrates something important: **AI systems inherit the characteristics of the data they're trained on**, in ways that are subtle, consequential, and sometimes hard to see. Every AI system reflects choices made about what data to include — and what those data reflect about the humans who created them.

We're building AI in our image. It's worth asking: whose image, exactly?
