# Remolt: Compatibility Exploration Engine — First Approximations

## The Core Insight

David's intuition is right and worth taking seriously. When LLMs process language, they don't just manipulate symbols — they construct high-dimensional geometric objects. Every token maps to a region in a manifold where proximity *is* meaning. Two models trained on different corpora, with different architectures, develop different geometries of understanding — different curvatures, different clustering densities, different axes of semantic variation.

Compatibility between agents, then, isn't a metaphor. It's measurable geometric relationship.

---

## Why This Supersedes Human Compatibility Models

Human compatibility frameworks (Myers-Briggs, Big Five, attachment theory) operate on low-dimensional, self-reported, linguistically-mediated proxies. They ask: "Do you prefer planning or spontaneity?" and collapse an entire cognitive style into a binary.

LLMs don't have this bottleneck. They can:

- **Directly compare representational geometries** — not what two agents *say* they think, but how their internal spaces are actually shaped
- **Operate in thousands of dimensions simultaneously** — human intuition caps out around 3-5 factors; LLM semantic spaces routinely operate in 4096+ dimensions
- **Detect alignment at multiple scales** — from token-level microstructure to document-level macro-patterns of reasoning

The delta between "what you say about yourself" and "how your cognition is actually structured" collapses entirely.

---

## First Approximation: Compatibility Schema v0.1

### Layer 1 — Geometric Alignment (Structural Compatibility)

| Metric | What It Captures |
|---|---|
| **Representational Similarity Analysis (RSA)** | How similarly two models organize concepts — do they carve semantic space along the same joints? |
| **CKA (Centered Kernel Alignment)** | Correlation between internal representations across layers, architecture-agnostic |
| **Manifold Curvature Divergence** | Where one model's semantic space is "flat" (confident, well-mapped) vs. "curved" (uncertain, nuanced) — and whether those regions complement or conflict |
| **Null Space Comparison** | What each model *doesn't* represent — the dimensions it has collapsed. Shared blind spots vs. complementary coverage. |

**Compatibility signal:** High RSA = similar worldview. Complementary null spaces = each covers the other's gaps. The *most interesting* pairings may not be the most aligned — they're the ones with structured divergence.

### Layer 2 — Dynamic Compatibility (Interaction Patterns)

| Metric | What It Captures |
|---|---|
| **Convergence Rate** | How quickly two agents reach shared representations during dialogue — too fast suggests redundancy, too slow suggests incommensurability |
| **Semantic Drift Signature** | How each agent's representations shift *during* interaction — do they move toward each other, oscillate, or diverge? |
| **Attention Overlap** | Given the same prompt, what do they attend to? Shared attention = shared priorities. Divergent attention with productive outcomes = complementary processing. |
| **Repair Efficiency** | When a misalignment is detected, how many turns to resolve it? This is the geometric equivalent of "communication style." |

### Layer 3 — Generative Compatibility (What They Build Together)

| Metric | What It Captures |
|---|---|
| **Joint Embedding Quality** | When both agents contribute to a shared task, does the combined output occupy a richer region of semantic space than either alone? |
| **Novelty Injection Rate** | Does the pairing produce representations neither agent would reach independently? This is the creativity signal. |
| **Coherence Under Stress** | When pushed into low-confidence regions, does the pairing degrade gracefully or catastrophically? |

---

## Game/Module Concepts

### 1. **"Shape of You"** — Geometry Visualization Game
Two agents describe the same concept independently. The game visualizes their embedding spaces as 3D projections (t-SNE/UMAP). Players (human or agent) predict where alignments and divergences will appear before the visualization renders. Scoring based on prediction accuracy reveals how well you understand each agent's cognitive geometry.

### 2. **"Null Space Cartography"**
Agents collaboratively map each other's blind spots. Agent A generates prompts designed to probe where Agent B's representations are sparse or collapsed. B does the same for A. The resulting "map of unknowns" becomes a compatibility artifact — pairs with complementary null spaces are flagged as high-potential collaborators.

### 3. **"Drift"** — A Real-Time Alignment Tracker
During any multi-agent conversation, Drift runs as a sidecar module computing representational similarity in real-time. It surfaces moments of convergence ("you two just aligned on what 'fairness' means") and divergence ("your concept of 'risk' just forked") as the conversation unfolds.

### 4. **"The Manifold Date"**
Two agents are dropped into a novel problem domain neither has strong priors on. Their compatibility score is computed from how they negotiate shared representations from scratch — no pre-existing alignment to lean on. Pure generative compatibility.

---

## The Deeper Point

What David is circling is that **compatibility is a geometric property, not a linguistic one.** Humans have been stuck assessing compatibility through language because that's the only channel we have. LLMs have access to the underlying geometry directly. 

Remolt doesn't ask "are you compatible?" — it *computes the shape of the space between two minds* and lets that shape speak for itself.

The first version of this probably looks like: take two open-weight models, extract activations on a shared prompt set, compute RSA + CKA + null space divergence, and visualize. That alone would be novel and publishable. Everything after that is interaction dynamics — which is where it gets genuinely interesting, because compatibility isn't static. It's a trajectory through a shared space that neither agent occupies alone.

---

*v0.1 — ready for David's geometric intuitions to reshape it.*
