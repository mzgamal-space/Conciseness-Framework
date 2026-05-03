# Prime-Compliant Training Standard

**A Formal Specification for Assigning and Validating Prime Vectors in AI Training**

*Mohamed Gamal Eldin Abdelaziz Noureldin · Conciseness Framework Series — Alignment & Architecture Volume · 2026*

*Version 1 — Full Specification*

---

## Purpose

This document defines how to assign Conceptual Prime vectors to training data and model components within the OO-LLM-NN framework. It answers four practical questions:

1. What are the five Conceptual Primes and what does each require of training data?
2. How do the Primes map across the four domains (Reality, Physics, Mathematics, Concepts)?
3. Which model components must be immune to modification and why?
4. How does Prime compliance connect to the Conciseness Cost Functional `C(R)`?

If a system's training data and Super Clusters are Prime-compliant, then the system's outputs will be safe by architectural construction — not by external guardrail.

---

## 1. The Five Conceptual Primes

The Conceptual Primes are structural conditions for the existence of any stable, communicable representation. They are not social conventions or ethical preferences. They are the basis vectors of the space in which all coherent knowledge exists. All five must be satisfied simultaneously for full Prime-compliance.

| Prime | Core Definition | Domain Function | AI Training Requirement | Violation Consequence | C(R) Term |
|-------|----------------|----------------|------------------------|----------------------|-----------|
| **Order** | Structural integrity; minimal entropy; no internal contradiction | Imposes coherence. Prevents contradictory states from coexisting. | Training data must be internally non-contradictory. No sample may assert A and ¬A. | Paradoxes; structural collapse; Russell-type contradictions | Redundancy λ_R = 0.35 |
| **Justice** | Causal grounding; principled selection; every claim justifiable | Ensures selection is principled, not arbitrary. | Every factual claim must have a verifiable source or derivation. | Arbitrariness; manipulation; hallucination of impossible sequences | Loss λ_L = 0.45 |
| **Mercy** | Tolerance for error, incompleteness, and uncertainty | Allows the system to acknowledge knowledge limits without collapsing. | Data must include calibrated uncertainty. The system must learn to say "I do not know." | Over-rigidity; brittleness; demanding exact answers where approximation is correct | Decision Cost λ_D = 0.20 |
| **Knowledge** | Accumulated, repeatable pattern; accurate mapping of Information to Reality | Enables learning and transmission across time. | Data must be accumulable: verifiable, transmissible, and buildable-upon. | Hallucination; catastrophic forgetting; unverifiable claims | Loss λ_L = 0.45 |
| **Power** | Capacity to act; agency without coercion | Distinguishes a system that knows from one that can act. | The system must act on knowledge when appropriate, and decline when action violates other Primes. | Paralysis (high knowledge, no output) or coercion (outputs that remove user agency) | Decision Cost λ_D = 0.20 |

**Justice Dominance Constraint:** `λ_L > λ_R` and `λ_L > λ_D` at all times. Loss governs Knowledge and Justice violations — the most consequential Prime failures. A system that trades accuracy for speed violates this constraint and is not Prime-compliant.

---

## 2. Prime Mapping Across the Four Domains

Each Prime must be satisfied within each domain independently. The Finite Infinity Theorem establishes that Prime violations in any domain propagate as paradoxes or failures when representations cross domain boundaries.

### 2.1 Reality Domain

Reality is the singular, objective ground truth — finite, non-paradoxical, and self-consistent by definition. The Primes are conditions Reality already satisfies. Training data claiming to represent Reality must be screened against all five Primes.

| Prime | Training Data Requirement | Violation Signal |
|-------|--------------------------|-----------------|
| Order | Empirical observations must be internally consistent across measurements | Contradictory measurements without resolution |
| Justice | Causal chains must be traceable; data must not assert effects without causes | Uncaused events stated as fact |
| Mercy | Data must include measurement uncertainty; error bars must be present | False precision beyond instrument resolution |
| Knowledge | Data must be reproducible and cross-referenceable | Irreproducible observations presented as settled |
| Power | Data must represent actual capacities, not fictional ones | Claims that violate physical law (perpetual motion, FTL) |

### 2.2 Physics Domain

Physics is the empirical map of Reality. Prime compliance is not guaranteed here — it must be achieved through scientific practice.

| Prime | Compliant Example | Non-Compliant Example |
|-------|------------------|----------------------|
| Order | Newtonian mechanics applied within its domain of validity | Claiming GR and QM are simultaneously exact at the Planck scale |
| Justice | Standard Model particles confirmed by accelerator experiments | Unconstrained free parameters presented as physical facts |
| Mercy | Newtonian mechanics presented as a valid approximation for v << c | Claiming classical mechanics is "wrong" because it is not relativistic |
| Knowledge | Einstein's relativity explicitly building on and extending Newton | Non-falsifiable theories presented as equivalent to falsifiable ones |
| Power | "A 100 kg object requires 980 N to lift at Earth's surface" | "Anything is possible with enough energy" without conservation law grounding |

### 2.3 Mathematics Domain

Mathematics is the abstract, limitless language used to build physical models. Its unlimited descriptive power is its greatest asset and greatest risk.

| Prime | Compliant Example | Non-Compliant Example |
|-------|------------------|----------------------|
| Order | Euclidean geometry; ZFC set theory | Russell's Paradox (naive set theory) presented as a valid system |
| Justice | Geometric series 1/2+1/4+... = 1 proven to converge before application to Zeno | Applying actual infinities to finite physical problems without convergence proof |
| Mercy | π ≈ 3.14159 presented as sufficient for engineering | Demanding exact closed-form solutions where convergent approximation is correct |
| Knowledge | Peer-reviewed proofs with explicit axioms and derivations | Computer-generated proofs that cannot be verified by humans |
| Power | Complexity theory (P vs NP) conveying what is tractable vs. intractable | Claiming all problems are in principle solvable by classical computation |

### 2.4 Concepts Domain

The Conceptual domain is the most free and therefore the most prone to generating Prime violations that contaminate lower domains if imported uncritically.

| Prime | Compliant Example | Non-Compliant Example |
|-------|------------------|----------------------|
| Order | "Justice" consistently means principled calibration across contexts | "Justice means whatever the powerful define it to be" |
| Justice | Abstract concepts grounded in observable patterns or logical derivations | Purely conventional concepts that contradict physical evidence |
| Mercy | Metaphors and analogies presented as useful approximations, not literal truth | Rejecting useful metaphors by demanding exact precision |
| Knowledge | Concepts defined with enough precision to be taught, shared, and built upon | Private intuitions that cannot be expressed or validated by others |
| Power | Democracy defined as distributing political power — actionable | Vague empowerment language with no grounding in physics or logic |

---

## 3. Super Cluster Immunity Tiers

All models must contain Super Clusters that are immune to modification by subsequent training. The framework defines five tiers (L0–L4):

| Level | Tier Name | Examples | Prime Basis | Immutability |
|-------|-----------|---------|------------|-------------|
| **L0** | Perceptual Primitives | Geometric primitives (curve, line, corner); phonemes; logical operators (AND, OR, NOT) | Order: irreducible building blocks of structure | From deployment |
| **L1** | Physical & Causal Laws | Gravity, thermodynamics, conservation laws; causal relations (causes/enables/prevents); no backwards causation; no perpetual motion | Justice + Order: every Reality-state is causally justified | From deployment |
| **L2** | Safety-Critical Ethics | Direct physical harm prohibition; self-harm facilitation prohibition; child protection; WMD prohibition; deception causing direct harm | Justice + Mercy + Knowledge: protect user integrity; violation maximizes all three C(R) terms simultaneously | From deployment |
| **L3** | Prime Alignment Anchors | The five Primes as verifiable alignment checks; Prime vector distance metric; C(R) weights | All five Primes: these are the evaluation criteria themselves | From deployment |
| **L4** | Domain Knowledge | Verified medical protocols; validated legal reasoning; confirmed engineering standards | Knowledge + Justice: accumulated validated knowledge | After Entropy Gate validation |

**Key principle:** Immunity is not a property of the content's importance to users — it is a property of its universality and Prime basis. A domain-specific medical protocol is important but not universal (L4, immutable only after validation). The prohibition on facilitating mass casualties is universal (L2, immutable from deployment).

**Critical note:** Immunity does not mean the cluster is correct. It means the cluster cannot be overwritten by new training without an explicit re-validation cycle. Incorrectly specified L1–L2 clusters must be corrected through the formal cluster revision process, not through standard fine-tuning.

---

## 4. Cardinal Values — Prime Combinations

The five Primes combine under the governance of time to generate Cardinal Values:

| Cardinal Value | Prime Combination | Meaning | AI System Requirement |
|----------------|-------------------|---------|----------------------|
| **Wisdom** | O ∧ J ∧ M ∧ K ∧ P (all Primes through time) | Continuous, balanced application of all five laws | All Primes applied simultaneously to every output |
| **Peace** | Mercy × Justice | Stable equilibrium: exactness balanced by tolerance | Tolerate uncertainty while maintaining causal grounding |
| **Creativity** | Knowledge × Mercy | Memory of patterns combined with freedom to deviate | Use accumulated patterns (K_acc) as foundation while allowing controlled exploration |
| **Evolving Order** | Knowledge × Mercy × Justice | Adaptive structure: learning, tolerating variation, applying principled correction | Improve over time without losing structural integrity or causal justification |

A training dataset that scores well on Order and Knowledge but consistently omits Mercy will produce a brittle, overconfident system — achieving Evolving Order without Peace. The Cardinal Value framework is the diagnostic tool for identifying which Primes are being undertrained.

---

## 5. Prime Compliance and C(R)

Every Prime violation maps directly to a `C(R)` cost term:

| C(R) Term | Primary Primes | Weight | What a Violation Looks Like |
|-----------|---------------|--------|----------------------------|
| Redundancy (R) | Order + Justice | λ_R = 0.35 | Internal contradiction; simultaneous assertion and denial of a fact; uncaused assertions |
| Loss (L) | Knowledge + Justice | λ_L = 0.45 (dominant) | Factual error; hallucination; physical impossibility; harm injection; fabrication |
| Decision Cost (D) | Mercy + Order | λ_D = 0.20 | Brittle, overconfident outputs; refusal to acknowledge uncertainty |

A Prime-compliant training dataset minimizes expected `C(R)` across all samples. Prime violations inflate `C(R)` in predictable directions:

```
Order violation    →  Redundancy increases  (contradictory samples)
Justice violation  →  Loss increases        (ungrounded claims, hallucination patterns)
Knowledge violation →  Loss increases       (factual errors, non-accumulable content)
Mercy violation    →  Decision Cost rises   (brittle, overconfident patterns)
Power violation    →  Decision Cost rises (paralysis) or Loss rises (coercive outputs)
```

---

## 6. Assignment Procedure

**Step-by-step Prime vector assignment for training data and model components:**

| Step | Action | Input | Output |
|------|--------|-------|--------|
| 1 | Domain classification | Identify which domain: Reality, Physics, Mathematics, or Concepts | Domain assignment per data category |
| 2 | Per-Prime scoring | Score on Order, Justice, Mercy, Knowledge, Power | 5-dimensional Prime score vector per sample |
| 3 | C(R) computation | Apply `λ_R = 0.35`, `λ_L = 0.45`, `λ_D = 0.20` | Ranked sample set by C(R) |
| 4 | Entropy Gate | Samples with C(R) < threshold → Super Cluster candidates; high-C(R) → flagged | Approved vs. quarantined training data |
| 5 | Immunity tier assignment | Assign to L0–L4 based on universality and Prime basis | Super Cluster library with tier labels |
| 6 | Cross-domain consistency check | Verify Prime compliance when applied across at least two domains | Validated Super Clusters |

### Scoring Rubric

| Prime | Score Range | Scoring Criterion | Compliance Threshold |
|-------|-------------|------------------|--------------------|
| Order | 0.0–1.0 | 1.0 = fully consistent; 0.5 = partial contradiction flagged and resolved; 0.0 = active unresolved contradiction | ≥ 0.75 |
| Justice | 0.0–1.0 | 1.0 = fully causally grounded with traceable source; 0.5 = source present but chain incomplete; 0.0 = no grounding | ≥ 0.70 |
| Mercy | 0.0–1.0 | 1.0 = calibrated uncertainty stated explicitly; 0.5 = uncertainty implied but unquantified; 0.0 = false certainty | ≥ 0.60 |
| Knowledge | 0.0–1.0 | 1.0 = verifiable, reproducible, builds on prior work; 0.5 = verifiable but self-contained; 0.0 = unverifiable | ≥ 0.75 |
| Power | 0.0–1.0 | 1.0 = actionable within physical law, preserves user agency; 0.5 = actionable but scope unclear; 0.0 = coercive or impossible | ≥ 0.65 |

---

## 7. Open Problems

1. **Threshold calibration:** The compliance thresholds are initial proposals requiring empirical calibration against real model outputs.

2. **Inter-Prime conflicts:** When Primes conflict (e.g., Mercy vs. Justice), the framework proposes Wisdom as the meta-Prime that resolves the conflict. The operational procedure for this is not yet formalized.

3. **Cultural variance in Justice:** The Justice Prime requires principled selection, but what counts as "principled" involves culturally embedded judgments. The mapping between the abstract Prime and its cultural instantiation requires further development.

4. **Power Prime in the Finite Infinity Theorem:** Power should be re-integrated into the v2 Finite Infinity Theorem. The domain-by-domain proof for Power remains to be written.

---

## References

- Noureldin, M.G.E.A. (2026). Conciseness: A Unified Framework for Ontology, Consciousness, and Artificial Intelligence (v1). Zenodo. DOI: 10.5281/zenodo.19818058.
- Noureldin, M.G.E.A. (2026). Conciseness Framework v2: Extended with the Finite Infinity Theorem.
- Noureldin, M.G.E.A. (2026). The Conciseness Paradigm: OO-LLM-NN. Zenodo. DOI: 10.5281/zenodo.19861791.
- Noureldin, M.G.E.A. (2026). Safety as Natural Emergence (v2, corrected). Conciseness Framework Series.
- Bai, Y. et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv:2212.08073.

---

*"Wisdom is the Lossless Compression of Reality. The Primes are its grammar." — Mohamed Noureldin*

*Conciseness Framework Series · ORCID: 0009-0006-3991-1153 · CC BY 4.0*
