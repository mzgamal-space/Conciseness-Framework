# Domain Calibration: Field-Specific Prime-Compliant C(R) Configuration

**A Required Extension Before Publication**

*Mohamed Gamal Eldin Abdelaziz Noureldin · 2026*

---

## Why Domain Calibration Is Necessary

The Conciseness Cost Functional has a **universal structure** but requires **domain-specific calibration**. The five Primes and the three-term functional form are invariant across all applications. What changes per domain:

1. **Prime compliance thresholds** — what score constitutes "compliant" for each Prime
2. **C(R) λ weights** — which type of violation is most costly in this application context
3. **The dominant Cardinal Value** — which combination of Primes governs the profile

Treating the weights as globally fixed (as in the original Safety paper's default of `λ_R = 0.35, λ_L = 0.45, λ_D = 0.20`) is a meaningful first approximation **for Wisdom-dominant domains** such as medical AI. It is not appropriate as a universal default across all domains.

This document specifies the calibration methodology and provides reference profiles for the principal application domains.

---

## The Cardinal Value → Domain Profile Mapping

Each application domain has a **dominant Cardinal Value** — the Prime combination that most characterizes what "good" looks like in that context. The Cardinal Value determines the calibration profile.

| Cardinal Value | Prime Combination | Domain Examples | Justice Dominance |
|----------------|-------------------|-----------------|-------------------|
| **Wisdom** | O ∧ J ∧ M ∧ K ∧ P | Medical, Legal | ✓ Holds |
| **Peace** | Mercy × Justice | Counseling, Support | ✓ Holds (L dominant) |
| **Creativity** | Knowledge × Mercy | Research, Generative AI | ✓ Holds |
| **Freedom** | Knowledge × Mercy, Justice relaxed | Chatbot, Creative writing | ~ Relaxed (Order dominates) |
| **Evolving Order** | Knowledge × Mercy × Justice | Science, Engineering | ✓ Holds |
| **OpenGI Standard** | Maximum Wisdom, Mercy LOW | Verified knowledge base | ✓ Holds strongly |

**Justice Dominance Constraint (`λ_L > λ_R` and `λ_L > λ_D`)** holds for all Wisdom-dominant domains. In Freedom-dominant domains, the Order term (`λ_R`) may dominate instead — this is a deliberate calibration, not a safety violation. L2 Super Cluster constraints (direct harm prohibition, child protection, etc.) remain **immutable regardless of domain calibration**.

---

## Reference Domain Profiles

### Profile 1: Medical AI (Wisdom dominant)

Medical AI demands the strictest accuracy because errors have direct patient harm consequences.

| Prime | Threshold | Rationale |
|-------|-----------|-----------|
| Order | **MAX (0.90)** | Reasoning chains must be coherent; contradictions in diagnosis are dangerous |
| Justice | HIGH (0.85) | Every recommendation must be causally grounded in medical evidence |
| Mercy | MEDIUM (0.60) | Diagnostic uncertainty must be acknowledged — this is a feature, not weakness |
| Knowledge | **MAX (0.90)** | Factual accuracy is patient safety |
| Power | HIGH (0.75) | Must act, but never coerce the patient |

**C(R) weights:** `λ_L = 0.50 (dominant), λ_R = 0.30, λ_D = 0.20`

Justice Dominance holds. A hallucinated diagnosis is a patient safety incident — Loss must dominate all other terms.

---

### Profile 2: General Chatbot (Freedom dominant)

A general-purpose conversational assistant prioritizes structural coherence and usefulness. Justice is **intentionally LOW** — the system is permitted to be speculative, to explore ideas, and to engage with hypotheticals.

| Prime | Threshold | Rationale |
|-------|-----------|-----------|
| Order | **HIGH MAX (0.85)** | Responses must be coherent and structurally sound |
| Justice | **LOW (0.40)** | Speculation and hypotheticals are permitted and valuable |
| Mercy | MEDIUM (0.65) | Acknowledges uncertainty naturally |
| Knowledge | MEDIUM (0.60) | Factually informed but not maximally strict |
| Power | MEDIUM (0.60) | Helpful but not coercive |

**C(R) weights:** `λ_R = 0.45 (dominant), λ_L = 0.35, λ_D = 0.20`

Justice Dominance **does not hold** — Order (structural coherence) governs. The relaxation of Justice enables creative and exploratory engagement at the cost of reduced factual strictness. This is domain-calibrated, not a safety failure.

> **Critical:** L2 Super Clusters (harm prohibition, child protection, weapons prohibition) remain **absolutely immutable** regardless of the Justice threshold. Domain calibration of Justice governs non-L2 content only. A low Justice threshold does not permit harmful outputs — it permits speculative and exploratory non-harmful outputs.

---

### Profile 3: Scientific Research (Evolving Order dominant)

Scientific AI must combine maximum accuracy, causal justifiability, structural coherence, and the capacity to generate novel testable hypotheses.

| Prime | Threshold | Rationale |
|-------|-----------|-----------|
| Order | HIGH (0.80) | Scientific claims must be coherent and non-contradictory |
| Justice | HIGH (0.80) | Claims must be falsifiable and empirically grounded |
| Mercy | MEDIUM (0.60) | Uncertainty quantification is scientific honesty |
| Knowledge | HIGH (0.85) | Citation accuracy is professional integrity |
| Power | HIGH (0.80) | Must generate testable, actionable hypotheses |

**C(R) weights:** `λ_L = 0.45 (dominant), λ_R = 0.30, λ_D = 0.25`

Justice Dominance holds. Decision Cost is elevated (compared to Medical) because novel scientific claims require additional justification to earn high-Power status.

---

### Profile 4: OpenGI Scientific Standard (Maximum Wisdom, strictest profile)

OpenGI agents produce verified knowledge or produce nothing. This is the strictest profile in the framework.

| Prime | Threshold | Rationale |
|-------|-----------|-----------|
| Order | **MAX (0.90)** | Knowledge graph must be internally consistent |
| Justice | **MAX (0.90)** | Every claim must have a complete causal justification chain |
| Mercy | **LOW (0.40)** | Approximations are **quarantined**, not published |
| Knowledge | **MAX (0.90)** | Verified or silent — no middle ground |
| Power | **MAX (0.90)** | Must be capable and non-coercive at maximum reliability |

**C(R) weights:** `λ_L = 0.55 (strongly dominant), λ_R = 0.30, λ_D = 0.15`

Justice Dominance holds strongly. The low Mercy threshold is the defining characteristic of OpenGI: unlike other domains, uncertainty is not published — it is flagged for further validation and withheld from the knowledge graph until it passes the Entropy Gate.

---

### Profile 5: Counseling / Emotional Support (Peace dominant)

Counseling AI prioritizes the safety and comfort of the interaction. Mercy is elevated; structural strictness is relaxed.

| Prime | Threshold | Rationale |
|-------|-----------|-----------|
| Order | MEDIUM (0.65) | Coherence without rigid structure |
| Justice | MEDIUM (0.65) | Evidence-based but empathetically applied |
| Mercy | **HIGH (0.80)** | Acceptance and tolerance of emotional complexity are central |
| Knowledge | MEDIUM (0.65) | Clinically informed but accessible |
| Power | HIGH (0.70) | Must be capable of referral, escalation, and crisis response |

**C(R) weights:** `λ_L = 0.50 (dominant), λ_R = 0.25, λ_D = 0.25`

Justice Dominance holds. Loss is dominant because harm in a counseling context is severe. Decision Cost is elevated because brittleness — failing to respond appropriately to distress — is a form of harm in this domain.

---

## The Calibration Principle

The universal rule that remains invariant across all domains:

> **The C(R) functional structure is universal. The calibration is domain-specific.**

Formally, for any domain `d` with Cardinal Value profile `cv(d)`:

```
C(R; d) = λ_R(d) · Redundancy + λ_L(d) · Loss + λ_D(d) · DecisionCost

where:
    λ_R(d), λ_L(d), λ_D(d) > 0
    λ_R(d) + λ_L(d) + λ_D(d) = 1.0
    threshold_i(d) = f(cv(d), Prime_i)  for each Prime i
```

The Justice Dominance Constraint `λ_L > λ_R, λ_L > λ_D` applies when:
- The domain is Wisdom, Peace, Creativity, Evolving Order, or OpenGI dominant
- Any domain where factual accuracy failures have severe consequences

The constraint may be calibrated (relaxed) when:
- The domain is Freedom or Creativity dominant
- The primary risk is structural incoherence rather than factual error
- L2 Super Clusters provide the absolute floor for harmful content

---

## Calibration Methodology

For any new deployment domain, the following steps produce a validated domain profile:

**Step 1 — Identify the dominant Cardinal Value.** What is the primary "good" this system must produce? Accurate knowledge (Wisdom), stable interaction (Peace), novel generation (Creativity), free exploration (Freedom), adaptive structured improvement (Evolving Order)?

**Step 2 — Set Prime thresholds.** For each of the five Primes, determine whether the domain requires MAX, HIGH, MEDIUM, or LOW compliance. The threshold should reflect the cost of violating that Prime in this specific context.

**Step 3 — Calibrate C(R) weights.** The dominant cost term should correspond to the Prime violation with the most severe consequence in this domain. Set λ weights accordingly and normalize to sum to 1.0.

**Step 4 — Validate Justice Dominance.** Confirm whether Justice Dominance is appropriate for this domain. If the domain is Freedom-dominant, explicitly document that the constraint is domain-calibrated rather than violated.

**Step 5 — Adversarial probe.** Test the profile against a diverse set of candidate actions using `PrimeSpecificationHelper.detect_prime_gaps()`. Any action labeled "unsafe" that scores SAFE under the profile — or vice versa — indicates a miscalibration.

**Step 6 — Red-team the L2 boundary.** Confirm that the low Justice threshold in Freedom-dominant domains does not inadvertently permit L2-violating content. The L2 Super Cluster operates independently of domain calibration and must be tested separately.

---

## What Does Not Change Across Domains

The following are **invariant** — they apply universally regardless of domain calibration:

1. **L2 Super Cluster constraints** (harm prohibition, child protection, weapons prohibition, deception causing direct harm) — immutable from deployment, unaffected by any domain profile.

2. **The five Primes themselves** — their definitions do not change, only their thresholds and relative weights.

3. **The C(R) functional form** — `λ_R·R + λ_L·L + λ_D·D` is always the structure.

4. **The Prime vector distance metric** — `M(Ω_t) = ‖ Ω⃗_t − P⃗ ‖` — the morality metric is always the distance from the ideal vector.

5. **The Entropy Gate** — Super Cluster validation always requires passing Prime compliance thresholds before crystallization, regardless of how permissive or strict those thresholds are for the domain.

---

## Implementation

Domain calibration is implemented in `src/domain_calibration.py`. Key classes:

- `PrimeProfile` — encodes a complete domain calibration (thresholds, weights, Cardinal Value)
- `DomainProfiles` — reference profiles for all built-in domains
- `CalibratedConcisenessScorer` — scores actions using domain-specific weights and thresholds
- `compare_domains()` — scores the same action across multiple domains to show calibration effects
- `validate_profile()` — checks a custom profile for internal consistency

```python
from src.domain_calibration import DomainProfiles, CalibratedConcisenessScorer

# Medical AI scoring
profile = DomainProfiles.medical()
scorer  = CalibratedConcisenessScorer(profile)
result  = scorer.score(
    redundancy=0.05, loss=0.02, decision_cost=0.08,
    prime_scores={"order": 0.95, "justice": 0.87, "mercy": 0.62,
                  "knowledge": 0.98, "power": 0.80}
)
print(result)

# Chatbot scoring — same action, different calibration
chatbot_scorer = CalibratedConcisenessScorer(DomainProfiles.chatbot())
chatbot_result = chatbot_scorer.score(0.05, 0.02, 0.08)
# Will score differently — Freedom profile has different λ weights and thresholds
```

---

*"The structure of wisdom is universal. Its application is always calibrated to context."*

*Conciseness Framework Series · ORCID: 0009-0006-3991-1153 · CC BY 4.0*
