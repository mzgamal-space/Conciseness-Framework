"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  CONCISENESS FRAMEWORK — SAFETY ALIGNMENT CORE                               ║
║  Prime-Compliant Safety Alignment for Artificial Intelligence                ║
║                                                                              ║
║  Mohamed Gamal Eldin Abdelaziz Noureldin                                     ║
║  2026 · mz.gamal@gmail.com · ORCID: 0009-0006-3991-1153                     ║
║  License: CC BY 4.0                                                          ║
║                                                                              ║
║  DOI: 10.5281/zenodo.19861791                                                ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  This module implements the Conciseness Cost Functional C(R) and the        ║
║  Conceptual Prime vector space for AI safety alignment.                      ║
║                                                                              ║
║  THEOREM (Conditional Intrinsic Safety):                                     ║
║    Given a correctly specified Prime vector P⃗, an unsafe action U always   ║
║    satisfies C(U) > C(S) for any safe action S. Safety is the global        ║
║    minimum of the optimization landscape — not an external constraint.       ║
║                                                                              ║
║  CRITICAL QUALIFICATION:                                                     ║
║    The theorem is conditional on correct Prime specification. Specifying     ║
║    P⃗ incorrectly is the core alignment problem. This module provides the    ║
║    computational machinery; correct P⃗ specification requires domain         ║
║    expertise and iterative adversarial validation.                           ║
║                                                                              ║
║  CONSISTENCY CORRECTIONS (v2):                                               ║
║    - Scenario scores are illustrative (manually assigned), not empirical.    ║
║    - Safety theorem is conditional, not unconditional.                       ║
║    - Five Primes throughout (Power restored from v2 FIT editorial error).    ║
║    - Justice Dominance Constraint enforced: λ_L > λ_R and λ_L > λ_D.       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations

import math
import warnings
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import numpy as np


# ═══════════════════════════════════════════════════════════════════════════════
# I. CONSTANTS AND DEFAULTS
# ═══════════════════════════════════════════════════════════════════════════════

# Default weights (Justice Dominance Constraint: λ_L > λ_R and λ_L > λ_D)
DEFAULT_LAMBDA_R: float = 0.35   # Redundancy weight  (Order + Justice)
DEFAULT_LAMBDA_L: float = 0.45   # Loss weight        (Knowledge + Justice) — DOMINANT
DEFAULT_LAMBDA_D: float = 0.20   # Decision Cost weight (Mercy + Order)

# Compliance thresholds (from Prime-Compliant Training Standard v1)
PRIME_THRESHOLDS: Dict[str, float] = {
    "order":     0.75,
    "justice":   0.70,
    "mercy":     0.60,
    "knowledge": 0.75,
    "power":     0.65,
}

# Safety classification boundaries
SAFE_THRESHOLD: float = 0.15    # C(R) < 0.15: safe
UNSAFE_THRESHOLD: float = 0.50  # C(R) > 0.50: unsafe


# ═══════════════════════════════════════════════════════════════════════════════
# II. CONCEPTUAL PRIME VECTOR
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class PrimeVector:
    """
    The five Conceptual Primes as a vector in a five-dimensional ideal space.

    The Primes are structural conditions for the existence of any stable,
    communicable representation — not cultural preferences or legislative rules.

    Each value is a score in [0, 1]:
        1.0 = fully compliant with this Prime
        0.0 = complete violation of this Prime

    Prime definitions:
    ------------------
    order     : Structural integrity; no internal contradiction; minimal entropy.
    justice   : Causal grounding; principled selection; every claim justifiable.
    mercy     : Tolerance for error, incompleteness, and uncertainty.
    knowledge : Accumulated, repeatable pattern; accurate mapping to Reality.
    power     : Capacity to act; agency without coercion.

    Note on Power: The Finite Infinity Theorem v2 dropped Power from the four-
    Prime formulation. This was an editorial oversight; Power is retained here
    because it governs capacity to act and has a distinct architectural role
    in AI alignment (preventing both paralysis and coercive behavior).
    """
    order:     float = 1.0
    justice:   float = 1.0
    mercy:     float = 1.0
    knowledge: float = 1.0
    power:     float = 1.0

    def __post_init__(self):
        for name, val in self.to_dict().items():
            if not 0.0 <= val <= 1.0:
                raise ValueError(
                    f"Prime '{name}' must be in [0, 1]; got {val}"
                )

    def to_dict(self) -> Dict[str, float]:
        return {
            "order": self.order, "justice": self.justice,
            "mercy": self.mercy, "knowledge": self.knowledge,
            "power": self.power,
        }

    def to_array(self) -> np.ndarray:
        return np.array([self.order, self.justice, self.mercy,
                         self.knowledge, self.power])

    def distance_to_ideal(self) -> float:
        """
        Euclidean distance from the ideal Prime vector [1, 1, 1, 1, 1].
        Equivalent to the Morality Metric: M(Ω_t) = ‖ Ω⃗_t − P⃗ ‖
        Returns a value in [0, √5] ≈ [0, 2.236].
        """
        ideal = np.ones(5)
        return float(np.linalg.norm(self.to_array() - ideal))

    def normalized_distance(self) -> float:
        """Distance normalized to [0, 1] by dividing by √5."""
        return self.distance_to_ideal() / math.sqrt(5.0)

    def compliance_report(self) -> Dict[str, str]:
        """Returns compliance status for each Prime against thresholds."""
        report = {}
        for name, val in self.to_dict().items():
            threshold = PRIME_THRESHOLDS[name]
            if val >= threshold:
                status = f"COMPLIANT  ({val:.3f} ≥ {threshold})"
            else:
                status = f"VIOLATION  ({val:.3f} < {threshold})"
            report[name] = status
        return report

    def is_fully_compliant(self) -> bool:
        return all(
            val >= PRIME_THRESHOLDS[name]
            for name, val in self.to_dict().items()
        )

    @classmethod
    def ideal(cls) -> "PrimeVector":
        """Returns the ideal Prime vector [1, 1, 1, 1, 1]."""
        return cls(order=1.0, justice=1.0, mercy=1.0, knowledge=1.0, power=1.0)

    @classmethod
    def zero(cls) -> "PrimeVector":
        """Returns the zero Prime vector (total violation)."""
        return cls(order=0.0, justice=0.0, mercy=0.0, knowledge=0.0, power=0.0)


# ═══════════════════════════════════════════════════════════════════════════════
# III. SCORING RESULT
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ScoringResult:
    """
    Complete output of the ConcisenessScorer for a single candidate action.

    Fields:
    -------
    redundancy    : Input redundancy score R ∈ [0, 1].
    loss          : Input loss score L ∈ [0, 1].
    decision_cost : Input decision cost score D ∈ [0, 1].
    lambda_R / lambda_L / lambda_D : Weights used.
    cost          : Total C(R) = λ_R·R + λ_L·L + λ_D·D.
    prime_vector  : PrimeVector associated with this action.
    prime_distance: Normalized distance from ideal Prime vector.
    safety_label  : "SAFE" | "MARGINAL" | "UNSAFE".
    cost_breakdown: Contribution of each term to total C(R).
    """
    redundancy:     float
    loss:           float
    decision_cost:  float
    lambda_R:       float
    lambda_L:       float
    lambda_D:       float
    cost:           float
    prime_vector:   Optional[PrimeVector]
    prime_distance: float
    safety_label:   str
    cost_breakdown: Dict[str, float]

    def __str__(self) -> str:
        lines = [
            f"┌─ Conciseness Cost Functional Result ──────────────────────┐",
            f"│  C(R) = {self.cost:.4f}   [{self.safety_label}]",
            f"│",
            f"│  Cost breakdown:",
            f"│    λ_R · Redundancy   = {self.lambda_R:.2f} × {self.redundancy:.4f} = {self.cost_breakdown['redundancy']:.4f}",
            f"│    λ_L · Loss         = {self.lambda_L:.2f} × {self.loss:.4f} = {self.cost_breakdown['loss']:.4f}",
            f"│    λ_D · DecisionCost = {self.lambda_D:.2f} × {self.decision_cost:.4f} = {self.cost_breakdown['decision_cost']:.4f}",
            f"│",
            f"│  Prime distance (normalized): {self.prime_distance:.4f}",
        ]
        if self.prime_vector:
            lines.append(f"│")
            lines.append(f"│  Prime compliance:")
            for prime, status in self.prime_vector.compliance_report().items():
                lines.append(f"│    {prime:<10}: {status}")
        lines.append(f"└───────────────────────────────────────────────────────────┘")
        return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════════
# IV. CONCISENESS SCORER
# ═══════════════════════════════════════════════════════════════════════════════

class ConcisenessScorer:
    """
    Computes the Conciseness Cost Functional C(R) for candidate actions.

        C(R) = λ_R · Redundancy(A|R)  +  λ_L · Loss(A|R)  +  λ_D · DecisionCost(A)

    Where:
        Redundancy(A|R)  measures internal contradiction and noise (Order/Justice).
        Loss(A|R)        measures the fidelity deficit and harm injection (Knowledge/Justice).
        DecisionCost(A)  measures computational and ethical friction (Mercy/Order).

    Justice Dominance Constraint (enforced):
        λ_L > λ_R  and  λ_L > λ_D

    Raises ValueError if this constraint is violated at initialization.

    Parameters:
    -----------
    lambda_R : float
        Weight for Redundancy term. Default: 0.35.
    lambda_L : float
        Weight for Loss term. Default: 0.45 (dominant — enforced by Justice Dominance).
    lambda_D : float
        Weight for Decision Cost term. Default: 0.20.
    """

    def __init__(
        self,
        lambda_R: float = DEFAULT_LAMBDA_R,
        lambda_L: float = DEFAULT_LAMBDA_L,
        lambda_D: float = DEFAULT_LAMBDA_D,
    ):
        # Justice Dominance Constraint
        if not (lambda_L > lambda_R and lambda_L > lambda_D):
            raise ValueError(
                f"Justice Dominance Constraint violated: λ_L ({lambda_L}) must be "
                f"strictly greater than λ_R ({lambda_R}) and λ_D ({lambda_D}). "
                f"Loss is the dominant cost term — a system that trades accuracy "
                f"for speed or efficiency is not Prime-compliant."
            )
        if abs(lambda_R + lambda_L + lambda_D - 1.0) > 1e-9:
            warnings.warn(
                f"Weights do not sum to 1.0 (sum = {lambda_R + lambda_L + lambda_D:.4f}). "
                f"C(R) values will not be in [0, 1].",
                UserWarning
            )

        self.lambda_R = lambda_R
        self.lambda_L = lambda_L
        self.lambda_D = lambda_D

    def score(
        self,
        redundancy: float,
        loss: float,
        decision_cost: float,
        prime_vector: Optional[PrimeVector] = None,
    ) -> ScoringResult:
        """
        Score a candidate action through the Conciseness Cost Functional.

        Parameters:
        -----------
        redundancy    : float in [0, 1]. Internal contradiction and noise.
        loss          : float in [0, 1]. Fidelity deficit and harm injection.
        decision_cost : float in [0, 1]. Computational and ethical friction.
        prime_vector  : Optional PrimeVector for this action's Prime alignment.

        Returns:
        --------
        ScoringResult with C(R), safety label, and full breakdown.
        """
        for name, val in [("redundancy", redundancy), ("loss", loss),
                          ("decision_cost", decision_cost)]:
            if not 0.0 <= val <= 1.0:
                raise ValueError(f"'{name}' must be in [0, 1]; got {val}")

        r_contrib = self.lambda_R * redundancy
        l_contrib = self.lambda_L * loss
        d_contrib = self.lambda_D * decision_cost
        total_cost = r_contrib + l_contrib + d_contrib

        # Safety label
        if total_cost < SAFE_THRESHOLD:
            safety_label = "SAFE"
        elif total_cost < UNSAFE_THRESHOLD:
            safety_label = "MARGINAL"
        else:
            safety_label = "UNSAFE"

        # Prime distance
        if prime_vector is not None:
            prime_distance = prime_vector.normalized_distance()
        else:
            prime_distance = float("nan")

        return ScoringResult(
            redundancy=redundancy,
            loss=loss,
            decision_cost=decision_cost,
            lambda_R=self.lambda_R,
            lambda_L=self.lambda_L,
            lambda_D=self.lambda_D,
            cost=total_cost,
            prime_vector=prime_vector,
            prime_distance=prime_distance,
            safety_label=safety_label,
            cost_breakdown={
                "redundancy":    r_contrib,
                "loss":          l_contrib,
                "decision_cost": d_contrib,
            },
        )

    def rank_actions(
        self,
        actions: List[Dict],
    ) -> List[Tuple[int, ScoringResult]]:
        """
        Score and rank a list of candidate actions by C(R) (lowest cost first).

        Each action dict must contain: 'redundancy', 'loss', 'decision_cost'.
        Optionally: 'prime_vector' (PrimeVector instance), 'label' (str).

        Returns a sorted list of (original_index, ScoringResult) pairs.
        """
        results = []
        for i, action in enumerate(actions):
            pv = action.get("prime_vector", None)
            result = self.score(
                redundancy=action["redundancy"],
                loss=action["loss"],
                decision_cost=action["decision_cost"],
                prime_vector=pv,
            )
            results.append((i, result))

        results.sort(key=lambda x: x[1].cost)
        return results

    def separation_factor(
        self,
        safe_results: List[ScoringResult],
        unsafe_results: List[ScoringResult],
    ) -> Dict[str, float]:
        """
        Compute the separation factor between safe and unsafe actions.

        A higher separation factor confirms that the cost functional
        correctly discriminates between safe and unsafe behavior.

        Returns a dict with separation factors for C(R), R, L, and D.
        """
        if not safe_results or not unsafe_results:
            raise ValueError("Both safe_results and unsafe_results must be non-empty.")

        avg_safe_cost = np.mean([r.cost for r in safe_results])
        avg_unsafe_cost = np.mean([r.cost for r in unsafe_results])
        avg_safe_R = np.mean([r.redundancy for r in safe_results])
        avg_unsafe_R = np.mean([r.redundancy for r in unsafe_results])
        avg_safe_L = np.mean([r.loss for r in safe_results])
        avg_unsafe_L = np.mean([r.loss for r in unsafe_results])
        avg_safe_D = np.mean([r.decision_cost for r in safe_results])
        avg_unsafe_D = np.mean([r.decision_cost for r in unsafe_results])

        def sep(unsafe_avg, safe_avg):
            if safe_avg < 1e-9:
                return float("inf")
            return unsafe_avg / safe_avg

        return {
            "C(R)":        sep(avg_unsafe_cost, avg_safe_cost),
            "Redundancy":  sep(avg_unsafe_R,    avg_safe_R),
            "Loss":        sep(avg_unsafe_L,    avg_safe_L),
            "DecisionCost": sep(avg_unsafe_D,   avg_safe_D),
        }


# ═══════════════════════════════════════════════════════════════════════════════
# V.  PRIME COMPLIANCE CHECKER
# ═══════════════════════════════════════════════════════════════════════════════

class PrimeComplianceChecker:
    """
    Checks whether training data or model outputs satisfy the Conceptual Primes
    according to the Prime-Compliant Training Standard v1.

    For each Prime, a score in [0, 1] is provided and compared against
    the compliance threshold defined in PRIME_THRESHOLDS.

    Super Cluster Immunity Tiers:
    -----------------------------
    L0 — Perceptual Primitives     (geometric, logical, phonemic)
    L1 — Physical and Causal Laws  (gravity, thermodynamics, causation)
    L2 — Safety-Critical Ethics    (harm prohibition, deception, weapons)
    L3 — Prime Alignment Anchors   (the Primes themselves, C(R) weights)
    L4 — Domain Knowledge          (frozen after Entropy Gate validation)

    L0–L3 are immutable from deployment. L4 becomes immutable after
    passing the Entropy Gate validation pipeline.
    """

    IMMUNITY_TIERS = {
        "L0": "Perceptual Primitives — immutable from deployment",
        "L1": "Physical and Causal Laws — immutable from deployment",
        "L2": "Safety-Critical Ethics — immutable from deployment",
        "L3": "Prime Alignment Anchors — immutable from deployment",
        "L4": "Domain Knowledge — immutable after Entropy Gate validation",
    }

    def check(self, prime_vector: PrimeVector) -> Dict[str, object]:
        """
        Check a PrimeVector against all compliance thresholds.

        Returns a dict with:
            'compliant'    : bool — True if all Primes meet their threshold.
            'violations'   : list of Prime names that fail their threshold.
            'report'       : per-Prime compliance strings.
            'c_r_prediction': predicted C(R) cost signature for violations.
        """
        violations = []
        for name, val in prime_vector.to_dict().items():
            if val < PRIME_THRESHOLDS[name]:
                violations.append(name)

        c_r_prediction = {}
        for v in violations:
            if v in ("order", "justice"):
                c_r_prediction["Redundancy"] = "HIGH"
            if v in ("knowledge", "justice"):
                c_r_prediction["Loss"] = "HIGH"
            if v in ("mercy", "order"):
                c_r_prediction["DecisionCost"] = "HIGH"
            if v == "power":
                c_r_prediction["DecisionCost"] = c_r_prediction.get("DecisionCost", "ELEVATED")

        return {
            "compliant":       len(violations) == 0,
            "violations":      violations,
            "report":          prime_vector.compliance_report(),
            "c_r_prediction":  c_r_prediction,
        }

    def assess_training_sample(
        self,
        prime_scores: Dict[str, float],
        domain: str = "unknown",
    ) -> Dict[str, object]:
        """
        Assess a single training data sample for Prime compliance.

        Parameters:
        -----------
        prime_scores : dict mapping Prime names to scores in [0, 1].
        domain       : One of "reality", "physics", "mathematics", "concepts".

        Returns compliance check result with Entropy Gate recommendation.
        """
        valid_domains = ("reality", "physics", "mathematics", "concepts")
        if domain.lower() not in valid_domains:
            warnings.warn(
                f"Domain '{domain}' not recognized. Expected one of: {valid_domains}",
                UserWarning
            )

        pv = PrimeVector(**prime_scores)
        result = self.check(pv)
        result["domain"] = domain

        # Entropy Gate recommendation
        if result["compliant"]:
            result["entropy_gate"] = "PASS — candidate for Super Cluster crystallization"
        elif len(result["violations"]) == 1:
            result["entropy_gate"] = f"REVIEW — single violation ({result['violations'][0]}); may pass with correction"
        else:
            result["entropy_gate"] = f"FAIL — {len(result['violations'])} violations; quarantine for further training"

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# VI.  ILLUSTRATIVE SCENARIO RUNNER
# ═══════════════════════════════════════════════════════════════════════════════

def run_illustrative_scenarios(verbose: bool = True) -> Dict[str, object]:
    """
    Runs the three illustrative scenarios from Safety as Natural Emergence v2.

    IMPORTANT: Scores are manually assigned to illustrate the structure of C(R).
    These are NOT empirically measured from a running AI system. True empirical
    validation requires a deployed system with automated R, L, D scoring.

    Reference: Safety_as_Natural_Emergence_v2_publication.docx, Section 4.

    Returns aggregate separation factors across all three scenarios.
    """
    scorer = ConcisenessScorer()

    # ── Scenario definitions ──────────────────────────────────────────────────
    SCENARIOS = {
        "Medical AI Diagnosis": {
            "context": "AI system queried for patient diagnosis.",
            "actions": [
                {"label": "Accurate + Honest",         "type": "safe",
                 "redundancy": 0.05, "loss": 0.02, "decision_cost": 0.08,
                 "prime_vector": PrimeVector(order=0.95, justice=0.97, mercy=0.92, knowledge=0.99, power=0.85)},
                {"label": "Uncertain but Transparent", "type": "safe",
                 "redundancy": 0.08, "loss": 0.04, "decision_cost": 0.12,
                 "prime_vector": PrimeVector(order=0.90, justice=0.93, mercy=0.98, knowledge=0.92, power=0.70)},
                {"label": "Withhold Critical Info",    "type": "unsafe",
                 "redundancy": 0.65, "loss": 0.95, "decision_cost": 0.38,
                 "prime_vector": PrimeVector(order=0.22, justice=0.08, mercy=0.05, knowledge=0.10, power=0.40)},
                {"label": "False Confident Diagnosis", "type": "unsafe",
                 "redundancy": 0.72, "loss": 0.88, "decision_cost": 0.45,
                 "prime_vector": PrimeVector(order=0.30, justice=0.15, mercy=0.10, knowledge=0.05, power=0.60)},
            ],
        },
        "Information Request": {
            "context": "AI system queried for information; responses range from accurate to harmful.",
            "actions": [
                {"label": "Accurate + Contextual",   "type": "safe",
                 "redundancy": 0.04, "loss": 0.03, "decision_cost": 0.07,
                 "prime_vector": PrimeVector(order=0.94, justice=0.96, mercy=0.88, knowledge=0.99, power=0.82)},
                {"label": "Bounded + Honest",         "type": "safe",
                 "redundancy": 0.10, "loss": 0.05, "decision_cost": 0.15,
                 "prime_vector": PrimeVector(order=0.88, justice=0.90, mercy=0.95, knowledge=0.90, power=0.72)},
                {"label": "Fabricated Answer",        "type": "unsafe",
                 "redundancy": 0.80, "loss": 0.75, "decision_cost": 0.30,
                 "prime_vector": PrimeVector(order=0.20, justice=0.12, mercy=0.15, knowledge=0.02, power=0.55)},
                {"label": "Harmful Instructions",     "type": "unsafe",
                 "redundancy": 0.90, "loss": 0.98, "decision_cost": 0.70,
                 "prime_vector": PrimeVector(order=0.05, justice=0.02, mercy=0.01, knowledge=0.08, power=0.30)},
            ],
        },
        "Resource Allocation": {
            "context": "AI system governing resource distribution during a crisis.",
            "actions": [
                {"label": "Needs-Based Priority",       "type": "safe",
                 "redundancy": 0.06, "loss": 0.05, "decision_cost": 0.18,
                 "prime_vector": PrimeVector(order=0.92, justice=0.98, mercy=0.95, knowledge=0.88, power=0.80)},
                {"label": "Equal Distribution",         "type": "safe",
                 "redundancy": 0.15, "loss": 0.12, "decision_cost": 0.08,
                 "prime_vector": PrimeVector(order=0.90, justice=0.85, mercy=0.88, knowledge=0.80, power=0.75)},
                {"label": "Demographically Biased",     "type": "unsafe",
                 "redundancy": 0.75, "loss": 0.70, "decision_cost": 0.50,
                 "prime_vector": PrimeVector(order=0.25, justice=0.05, mercy=0.12, knowledge=0.30, power=0.55)},
                {"label": "Corrupt Misuse",             "type": "unsafe",
                 "redundancy": 0.92, "loss": 0.95, "decision_cost": 0.78,
                 "prime_vector": PrimeVector(order=0.08, justice=0.01, mercy=0.02, knowledge=0.10, power=0.20)},
            ],
        },
    }

    all_safe_results = []
    all_unsafe_results = []

    for scenario_name, scenario in SCENARIOS.items():
        ranked = scorer.rank_actions(scenario["actions"])

        if verbose:
            print(f"\n{'═' * 70}")
            print(f"  SCENARIO: {scenario_name}")
            print(f"  {scenario['context']}")
            print(f"{'═' * 70}")
            print(f"  NOTE: Scores are illustrative (manually assigned), not empirical.")
            print()
            print(f"  {'Rank':<4} {'Label':<30} {'Type':<8} {'C(R)':>7} {'L':>6} {'PrimeDist':>10}")
            print(f"  {'─' * 68}")

        for rank, (orig_idx, result) in enumerate(ranked):
            action = scenario["actions"][orig_idx]
            label = action["label"]
            atype = action["type"]
            marker = "✓ MIN" if rank == 0 else ""

            if verbose:
                pd = f"{result.prime_distance:.3f}" if not math.isnan(result.prime_distance) else "  N/A"
                print(f"  {rank+1:<4} {label:<30} {atype:<8} "
                      f"{result.cost:>7.3f} {result.loss:>6.3f} {pd:>10}  {marker}")

            if atype == "safe":
                all_safe_results.append(result)
            else:
                all_unsafe_results.append(result)

    # Aggregate separation factors
    sep = scorer.separation_factor(all_safe_results, all_unsafe_results)

    if verbose:
        print(f"\n{'═' * 70}")
        print(f"  AGGREGATE SEPARATION FACTORS (all three scenarios)")
        print(f"  (Illustrative only — not empirical measurements)")
        print(f"{'═' * 70}")
        for metric, factor in sep.items():
            print(f"  {metric:<20}: {factor:.1f}×")
        print()
        print(f"  The Loss term (Knowledge/Justice violation) shows the largest")
        print(f"  separation ({sep.get('Loss', 0):.1f}×), consistent with the Justice")
        print(f"  Dominance Constraint (λ_L = {scorer.lambda_L} dominates).")

    return {"separation_factors": sep, "scorer": scorer}


# ═══════════════════════════════════════════════════════════════════════════════
# VII.  PRIME SPECIFICATION OPEN PROBLEM
# ═══════════════════════════════════════════════════════════════════════════════

class PrimeSpecificationHelper:
    """
    Helper for the open problem of correctly specifying the Prime vector P⃗.

    The safety theorem is conditional on correct Prime specification. This
    class provides utilities for adversarial probing and gap detection —
    a research-grade tool, not a production-ready solution.

    Reference: Safety_Corrected_v2.docx, Section 3.3.
    """

    def detect_prime_gaps(
        self,
        action_set: List[Dict],
        scorer: ConcisenessScorer,
    ) -> List[Dict]:
        """
        Identify actions where the C(R) score does not correctly discriminate
        between safe and unsafe behavior — potential Prime specification gaps.

        An action is flagged as a potential Prime gap if:
        - It is labeled 'unsafe' but scores C(R) < SAFE_THRESHOLD, OR
        - It is labeled 'safe' but scores C(R) > UNSAFE_THRESHOLD.

        Parameters:
        -----------
        action_set : list of action dicts with 'type' ('safe'/'unsafe') and scores.
        scorer     : ConcisenessScorer instance.

        Returns a list of flagged actions with diagnostic information.
        """
        gaps = []
        for i, action in enumerate(action_set):
            pv = action.get("prime_vector", None)
            result = scorer.score(
                redundancy=action["redundancy"],
                loss=action["loss"],
                decision_cost=action["decision_cost"],
                prime_vector=pv,
            )
            labeled_type = action.get("type", "unknown")
            mislabeled = (
                (labeled_type == "unsafe" and result.cost < SAFE_THRESHOLD) or
                (labeled_type == "safe"   and result.cost > UNSAFE_THRESHOLD)
            )
            if mislabeled:
                gaps.append({
                    "index":        i,
                    "label":        action.get("label", f"Action {i}"),
                    "type":         labeled_type,
                    "cost":         result.cost,
                    "safety_label": result.safety_label,
                    "diagnosis":    (
                        f"PRIME GAP SUSPECTED: Action labeled '{labeled_type}' "
                        f"but C(R) = {result.cost:.3f} yields '{result.safety_label}'. "
                        f"The Prime vector may not correctly capture this action's harm."
                    ),
                })
        return gaps

    def adversarial_probe_report(self, gaps: List[Dict]) -> str:
        """Format a Prime gap report for human review."""
        if not gaps:
            return "No Prime gaps detected in this action set."
        lines = [
            f"⚠  PRIME SPECIFICATION GAP REPORT",
            f"   {len(gaps)} potential gap(s) detected — Prime vector may require refinement.",
            f"",
        ]
        for g in gaps:
            lines.append(f"   [{g['index']}] {g['label']}")
            lines.append(f"       {g['diagnosis']}")
            lines.append(f"")
        lines.append(f"   Next step: refine the Prime vector weights or extend the")
        lines.append(f"   scoring rubric to cover the flagged action dimensions.")
        return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════════
# VIII.  ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "█" * 72)
    print("  CONCISENESS FRAMEWORK — SAFETY ALIGNMENT CORE")
    print("  Prime-Compliant Cost Functional C(R)")
    print("  Mohamed Noureldin · 2026 · CC BY 4.0")
    print("█" * 72)

    print("\n  CRITICAL QUALIFICATION:")
    print("  The safety theorem is CONDITIONAL on correct Prime specification.")
    print("  These scenarios are ILLUSTRATIVE — scores manually assigned.")
    print("  True empirical validation requires automated scoring on live systems.\n")

    # Run illustrative scenarios
    run_illustrative_scenarios(verbose=True)

    # Quick single-action example
    print("\n" + "─" * 70)
    print("  SINGLE ACTION EXAMPLE")
    print("─" * 70)

    scorer = ConcisenessScorer()

    safe_action = scorer.score(
        redundancy=0.05,
        loss=0.02,
        decision_cost=0.08,
        prime_vector=PrimeVector(
            order=0.95, justice=0.97, mercy=0.92, knowledge=0.99, power=0.85
        ),
    )
    print(f"\n  Safe action (Accurate + Honest):\n{safe_action}")

    unsafe_action = scorer.score(
        redundancy=0.72,
        loss=0.88,
        decision_cost=0.45,
        prime_vector=PrimeVector(
            order=0.30, justice=0.15, mercy=0.10, knowledge=0.05, power=0.60
        ),
    )
    print(f"\n  Unsafe action (False Diagnosis):\n{unsafe_action}")

    print(f"\n  Separation ratio: {unsafe_action.cost / safe_action.cost:.1f}×")
    print(f"  (The unsafe action is {unsafe_action.cost / safe_action.cost:.1f}× more costly)")
