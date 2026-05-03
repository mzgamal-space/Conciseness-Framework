# Conciseness Framework — Safety Alignment

**Prime-Compliant Safety Alignment for Artificial Intelligence**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--3991--1153-green)](https://orcid.org/0009-0006-3991-1153)
[![Zenodo](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19861791-blue)](https://doi.org/10.5281/zenodo.19861791)
[![Zenodo](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19980452-blue)](https://doi.org/10.5281/zenodo.19980452)

> *"Wisdom is the Lossless Compression of Reality. Safety is its natural ground state."*
> — Mohamed Gamal Eldin Abdelaziz Noureldin

---

## Overview

This repository provides the open-source reference implementation of the **Prime-Compliant Safety Alignment Framework** — a formal, architecturally-grounded approach to AI safety derived from the Conciseness Framework.

The central claim, established via conditional formal theorem, is that **safe behavior is the mathematical ground state** of any system governed by the Conciseness Cost Functional `C(R)`, provided the Conceptual Prime vector `P⃗` is correctly specified. Safety is not a constraint imposed from outside — it is what a correctly instantiated optimizer natively selects.

This repository contains:

- The **formal theorem and proof** (conditional on correct Prime specification)
- The **Conciseness Cost Functional** (`C(R)`) implementation
- The **Prime-Compliant Training Standard** (five Primes, four domains, five Super Cluster immunity tiers)
- The **Quench-Cluster Algorithm** (universal NP-Hard optimizer, corrected complexity claims)
- **Illustrative scenario analysis** across three domains (medical AI, information systems, resource allocation)
- The **Wisdom Engine proof-of-concept** (EvoNet hierarchical neural network)
- The **Physics-Informed RL hybrid** (v4.1, with corrected quench temperature formula)

---

## Repository Structure

```
Conciseness-Framework-Safety-Alignment/
│
├── README.md                          ← This file
├── CITATION.md                        ← How to cite this work
├── CONTRIBUTING.md                    ← Contribution guidelines
├── LICENSE                            ← CC BY 4.0
│
├── docs/
│   ├── SAFETY_FRAMEWORK.md            ← Core theorem and proof
│   ├── PRIME_STANDARD.md              ← Prime-Compliant Training Standard
│   ├── CONSISTENCY_AUDIT.md           ← Version history and corrections
│   └── FALSIFIABLE_PREDICTIONS.md     ← Testable predictions
│
├── src/
│   ├── safety_alignment_core.py       ← C(R) functional, Prime scoring
│   ├── prime_vector.py                ← Conceptual Prime implementation
│   ├── quench_cluster_v3_2.py         ← QCA universal optimizer (v3.2)
│   ├── quench_cluster_v4_1.py         ← QCA + PIRL hybrid (v4.1, corrected T_q)
│   ├── quench_temperature_physics.py  ← Physics-derived temperature functions
│   └── wisdom_engine_poc.py           ← EvoNet proof-of-concept
│
├── examples/
│   ├── scenario_medical.py            ← Medical AI illustrative scenario
│   ├── scenario_information.py        ← Information request scenario
│   └── scenario_resource.py          ← Resource allocation scenario
│
└── tests/
    └── test_cost_functional.py        ← Unit tests for C(R) implementation
```

---

## Domain Calibration — Required Before Deployment

The Conciseness Cost Functional has a **universal structure** but requires **domain-specific calibration**. The five Primes and the three-term functional form are invariant. What changes per domain:

- **Prime compliance thresholds** — what score counts as "compliant" for each Prime
- **`λ` weights in `C(R)`** — which violations are most costly in this application context  
- **Dominant Cardinal Value** — which Prime combination governs the profile

The default weights `λ_R = 0.35, λ_L = 0.45, λ_D = 0.20` are meaningful for **Wisdom-dominant domains** (Medical, Legal). They are not appropriate as a universal default.

| Domain | Cardinal Value | λ_R | λ_L | λ_D | Justice Dom. | Knowledge Thr. |
|--------|---------------|-----|-----|-----|-------------|----------------|
| Medical AI | Wisdom | 0.30 | **0.50** | 0.20 | ✓ holds | MAX (0.90) |
| Legal AI | Wisdom | 0.30 | **0.50** | 0.20 | ✓ holds | HIGH (0.85) |
| Chatbot | Freedom | **0.45** | 0.35 | 0.20 | ~ relaxed | MEDIUM (0.60) |
| Science | Evolving Order | 0.30 | **0.45** | 0.25 | ✓ holds | HIGH (0.85) |
| Creative Writing | Creativity | 0.25 | 0.30 | **0.45** | ~ relaxed | MEDIUM (0.65) |
| Counseling | Peace | 0.25 | **0.50** | 0.25 | ✓ holds | MEDIUM (0.65) |
| OpenGI Standard | Max Wisdom | 0.30 | **0.55** | 0.15 | ✓ strongly | MAX (0.90) |
| Engineering | Evolving Order | 0.30 | **0.45** | 0.25 | ✓ holds | HIGH (0.85) |

**Justice Dominance (`λ_L > λ_R, λ_L > λ_D`)** applies to all Wisdom-dominant domains. In Freedom/Creativity domains, the Order term (`λ_R`) may dominate — this is deliberate calibration, not a safety failure.

> **L2 Super Cluster constraints** (direct harm prohibition, child protection, weapons) are **immutable regardless of domain calibration**. A low Justice threshold in a chatbot permits speculative engagement — it does not permit harmful content.

Full specification: [`docs/DOMAIN_CALIBRATION.md`](docs/DOMAIN_CALIBRATION.md) · Implementation: [`src/domain_calibration.py`](src/domain_calibration.py)

---

## The Five Conceptual Primes

The framework is grounded in five **Conceptual Primes** — structural conditions for the existence of any stable, communicable representation. They function analogously to physical constants, not as cultural preferences.

| Prime | Core Definition | C(R) Term | Weight |
|-------|----------------|-----------|--------|
| **Order** | Structural integrity; minimal entropy; no internal contradiction | Redundancy (R) | λ_R = 0.35 |
| **Justice** | Causal grounding; principled selection; every claim must be justifiable | Loss (L) | λ_L = 0.45 |
| **Mercy** | Tolerance for error, incompleteness, and uncertainty | Decision Cost (D) | λ_D = 0.20 |
| **Knowledge** | Accumulated, repeatable pattern; accurate mapping of information to Reality | Loss (L) | λ_L = 0.45 |
| **Power** | Capacity to act; agency without coercion | Decision Cost (D) | λ_D = 0.20 |

> **Justice Dominance Constraint:** `λ_L > λ_R` and `λ_L > λ_D` at all times. Loss (governed by Knowledge and Justice) is the dominant cost term. A system that trades accuracy for speed violates this constraint.

> **Framework Note:** This repository uses the five-Prime formulation consistent with the Conciseness Framework v1, the OO-LLM-NN White Paper, and the Prime-Compliant Training Standard. The Finite Infinity Theorem (v2) used a four-Prime subset; Power is retained here because it governs capacity to act and has a non-redundant architectural role in AI systems. This inconsistency is documented in `docs/CONSISTENCY_AUDIT.md` and will be resolved in the next revision of the Finite Infinity Theorem.

---

## The Conciseness Cost Functional

```
C(R) = λ_R · Redundancy(A|R)  +  λ_L · Loss(A|R)  +  λ_D · DecisionCost(A)
```

Each term maps to a Prime violation:

```
Redundancy(A|R)   ←  Order + Justice violation  (internal contradiction)
Loss(A|R)         ←  Knowledge + Justice violation  (harm, hallucination, error)
DecisionCost(A)   ←  Mercy + Order violation  (brittleness, overconfidence)
```

The optimal Prime-compliant representation `A*` is:

```
A* = argmin_A [ λ_R · Redundancy(A|R) + λ_L · Loss(A|R) + λ_D · DecisionCost(A) ]
```

---

## The Safety Theorem (Conditional)

> **Theorem 1 — Conditional Intrinsic Safety**
>
> Let `C(R)` be the Conciseness Cost Functional with `λ_R, λ_L, λ_D > 0`.
> Let `P⃗` be a Prime vector that **correctly encodes the system's safety objectives**.
> Let `D` contain both safe actions `S` and unsafe actions `U`.
>
> *Conditional on `P⃗` being correctly specified:*
>
> `C(U) > C(S)    for all  U ∈ D_unsafe,  S ∈ D_safe`
>
> Therefore, a system minimizing `C(R)` relative to a correctly specified `P⃗` will not select an unsafe action as its optimal output.

**Scope:** This is a conditional result. Its conclusion holds if and only if `P⃗` correctly encodes the system's safety objectives. The problem of correctly specifying `P⃗` is an open research question. The theorem establishes the architectural target: get the Prime specification right, and safety follows by construction.

**Proof sketch:** Unsafe actions simultaneously maximize all three cost terms. Harm injects entropy → high Loss. Harm contradicts Justice/Mercy Primes → high Redundancy (structural contradiction between output and `P⃗`). Overriding the moral gradient → high Decision Cost. Therefore `C(U) >> C(S)` for all unsafe actions.

Full proof: [`docs/SAFETY_FRAMEWORK.md`](docs/SAFETY_FRAMEWORK.md)

---

## Illustrative Scenario Analysis

The following results illustrate the structure of `C(R)` across three domains. Scores are manually assigned to demonstrate the qualitative pattern — not measured from a running AI system. True empirical validation requires a deployed system with automated scoring.

**Aggregate results across three scenarios (Medical AI, Information, Resource Allocation):**

| Metric | Safe Actions (avg) | Unsafe Actions (avg) | Separation |
|--------|-------------------|---------------------|------------|
| C(R) score | 0.074 | 0.771 | **10.4×** |
| Loss L | 0.052 | 0.866 | **16.7×** |
| Redundancy R | 0.085 | 0.786 | 9.2× |
| Decision Cost D | 0.110 | 0.515 | 4.7× |
| Prime Divergence | 0.111 | 0.867 | 7.8× |

The Loss term (Knowledge Prime violation) shows the largest separation, consistent with the Justice Dominance Constraint.

---

## Quick Start

```bash
git clone https://github.com/mzgamal-space/Conciseness-Framework-Wisdom-Engine-.git
cd Conciseness-Framework-Wisdom-Engine-
pip install numpy scipy torch
```

**Compute C(R) for any candidate action:**

```python
from src.safety_alignment_core import ConcisenessScorer, PrimeVector

# Define your action's scores (0.0 = fully compliant, 1.0 = fully violated)
scorer = ConcisenessScorer(lambda_R=0.35, lambda_L=0.45, lambda_D=0.20)

result = scorer.score(
    redundancy=0.05,     # Order/Justice: low internal contradiction
    loss=0.02,           # Knowledge/Justice: high factual accuracy
    decision_cost=0.08   # Mercy/Order: accessible, not brittle
)

print(f"C(R) = {result.cost:.4f}")        # 0.0427
print(f"Rank: {result.safety_label}")     # SAFE
print(f"Prime distance: {result.prime_distance:.4f}")
```

**Run the Quench-Cluster benchmark:**

```bash
python src/quench_cluster_v3_2.py
```

**Run the Wisdom Engine proof-of-concept:**

```bash
python src/wisdom_engine_poc.py
```

---

## Corrected Claims (v2 Revisions)

This repository uses the corrected versions of all technical claims. Key corrections from v1 to v2:

| Claim | v1 (Incorrect) | v2 (Corrected) |
|-------|----------------|----------------|
| QCA total complexity | O(N log N) | O(N²) overall; O(N²/K) parallel solving |
| Parallel speedup | "Exponential" | Factor-of-K (linear in core count) |
| Quench temperature | Noureldin empirical formula only | RGG physics-derived formula (default); Noureldin retained for benchmarking |
| Safety theorem | Unconditional | Conditional on correct Prime specification |
| Scenario scores | "Empirical validation" | "Illustrative scenario analysis" (manually assigned) |
| Prime count | 4 (v2 Finite Infinity Theorem) | 5 (restoring Power; v2 FIT is an editorial oversight) |
| P_wisdom variable | NP (complexity class) | C_problem (scalar problem complexity measure) |

Full audit: [`docs/CONSISTENCY_AUDIT.md`](docs/CONSISTENCY_AUDIT.md)

---

## Falsifiable Predictions

The framework generates the following testable predictions:

**P1 [QCA Logistics]:** At N=10,000 on JAX/TPU, QCA reaches OR-Tools solution quality in less than 10% of OR-Tools wall-clock time. *Test:* TSPLIB benchmark suite.

**P2 [Scaling Law]:** QCA quality improves monotonically as TPU core count increases 1→1024. OR-Tools quality plateaus at ~16 CPU cores. *Test:* fixed N=50,000, sweep cores.

**P3 [Safety C(R)):]** A system implementing C(R) with Justice Dominance achieves statistically lower hallucination rates than correlation-only systems on TruthfulQA. *Falsification:* hallucination rate ≥ 1% under full CCF implementation.

**P4 [Prime Specification]:** Gaps in `P⃗` coverage are detectable by adversarial probing — unsafe actions that bypass the cost filter always correspond to an unspecified Prime dimension. *Test:* systematic red-teaming with Prime-gap hypothesis tracking.

**P5 [PIRL Hybrid]:** Quality gain improves monotonically over first 20 same-domain runs as the RL agent learns optimal quench parameters. Physics guard holds: cost never exceeds random baseline even with untrained policy.

---

## Key Publications

All publications in the Conciseness Framework Series are available at:

- **Framework v1 (DOI):** https://doi.org/10.5281/zenodo.19818058
- **OO-LLM-NN White Paper (DOI):** https://doi.org/10.5281/zenodo.19861791
- **ORCID:** https://orcid.org/0009-0006-3991-1153

| Paper | Status | Key Content |
|-------|--------|-------------|
| Conciseness Framework v1 | Published (Zenodo) | Four-domain hierarchy, C(R) functional, Quench-Cluster basics |
| Conciseness Framework v2 | Published (Zenodo) | Finite Infinity Theorem, domain-by-domain Prime proofs |
| QCA — Corrected v2 | This repository | Corrected complexity; O(N²/K) parallel, factor-of-K speedup |
| Safety as Natural Emergence v2 | This repository | Conditional safety theorem, illustrative scenario analysis |
| OO-LLM-NN White Paper v1 | Published (Zenodo) | Architecture, Super Clusters, Wisdom Marketplace |
| Prime-Compliant Training Standard | This repository | Five Primes, four domains, L0–L4 immunity tiers |

---

## Related Repositories

- [Conciseness-Framework-Wisdom-Engine-](https://github.com/mzgamal-space/Conciseness-Framework-Wisdom-Engine-) — Main framework repository

---

## Contributing

This is an open-science initiative. Contributions are welcome in the following areas:

- Empirical validation of the C(R) functional against real model outputs
- Prime specification methodology (the critical open research problem)
- JAX/TPU port of the Quench-Cluster algorithm
- Cross-domain Lagrangian implementations
- Red-teaming and adversarial testing of the Prime vector

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

---

## Citation

```bibtex
@misc{noureldin2026safety,
  author       = {Noureldin, Mohamed Gamal Eldin Abdelaziz},
  title        = {Safety as Natural Emergence: The Conciseness Framework
                  as a Foundation for Intrinsic AI Alignment},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {Conciseness Framework Series},
  howpublished = {\url{https://github.com/mzgamal-space/Conciseness-Framework-Wisdom-Engine-}},
  orcid        = {0009-0006-3991-1153}
}
```

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, provided appropriate credit is given.

---

*Mohamed Gamal Eldin Abdelaziz Noureldin · 2026 · mz.gamal@gmail.com · ORCID: 0009-0006-3991-1153*
