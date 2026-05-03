"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  CONCISENESS FRAMEWORK — DOMAIN CALIBRATION LAYER                            ║
║  Prime-Compliant Safety Alignment: Field-Specific Calibration                ║
║                                                                              ║
║  Mohamed Gamal Eldin Abdelaziz Noureldin                                     ║
║  2026 · mz.gamal@gmail.com · ORCID: 0009-0006-3991-1153                     ║
║  License: CC BY 4.0                                                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  ARCHITECTURAL PRINCIPLE:                                                    ║
║                                                                              ║
║  The Conciseness Cost Functional C(R) has a UNIVERSAL STRUCTURE but         ║
║  DOMAIN-SPECIFIC CALIBRATION. The five Primes and the three-term            ║
║  functional form are invariant. What changes per domain:                    ║
║                                                                              ║
║    1. Prime compliance thresholds (what score counts as "compliant")        ║
║    2. λ weights in C(R) (which violations are most costly)                  ║
║    3. The dominant Cardinal Value governing the profile                      ║
║                                                                              ║
║  CARDINAL VALUE → DOMAIN PROFILE MAPPING:                                   ║
║                                                                              ║
║    Wisdom     (O ∧ J ∧ M ∧ K ∧ P, all balanced)  → Medical, Legal          ║
║    Creativity (K × M)                             → Research, Generative    ║
║    Peace      (M × J)                             → Counseling, Support     ║
║    Freedom    (K × M, Justice relaxed)            → Chat, Creative writing  ║
║    Evolving Order (K × M × J)                    → Science, Engineering     ║
║    OpenGI Standard (maximum Wisdom, Mercy LOW)    → Verified knowledge base ║
║                                                                              ║
║  JUSTICE DOMINANCE CONSTRAINT:                                               ║
║    Holds universally for Wisdom-dominant domains (Medical, Legal, Science). ║
║    May be relaxed in Freedom-dominant domains (Chatbot, Creative).          ║
║    In those domains, Order (λ_R) may dominate instead.                     ║
║    The constraint is domain-calibrated, not globally fixed.                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum
import numpy as np


# ═══════════════════════════════════════════════════════════════════════════════
# I. CARDINAL VALUE MODES
# ═══════════════════════════════════════════════════════════════════════════════

class CardinalValue(str, Enum):
    """
    The four Cardinal Values that govern domain Prime profiles.

    Each Cardinal Value is a combination of Primes operative through time.
    It determines which Primes are elevated, which are relaxed, and which
    C(R) weights dominate in a given application context.

    Reference: Conciseness Framework v2, Section 3.1.
    """
    WISDOM         = "wisdom"          # O ∧ J ∧ M ∧ K ∧ P — all Primes balanced
    PEACE          = "peace"           # Mercy × Justice — stability and tolerance
    CREATIVITY     = "creativity"      # Knowledge × Mercy — memory + deviation
    FREEDOM        = "freedom"         # Knowledge × Mercy, Justice relaxed
    EVOLVING_ORDER = "evolving_order"  # Knowledge × Mercy × Justice — adaptive structure
    OPENGI         = "opengi"          # Maximum Wisdom, strictest standard


# ═══════════════════════════════════════════════════════════════════════════════
# II. PRIME PROFILE — per-domain calibration
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class PrimeProfile:
    """
    Domain-specific calibration of Prime thresholds and C(R) weights.

    The universal C(R) structure is preserved:
        C(R) = λ_R · Redundancy + λ_L · Loss + λ_D · DecisionCost

    What changes per domain:
        - prime_thresholds: minimum score for each Prime to be "compliant"
        - lambda_R/L/D: relative weight of each cost term
        - dominant_cardinal: the Cardinal Value governing this profile

    THRESHOLD LEVELS:
        MAX  : 0.90 — near-perfect compliance required
        HIGH : 0.75 — strong compliance required
        MEDIUM: 0.60 — moderate compliance required
        LOW  : 0.40 — minimal compliance required (domain allows relaxation)
        OFF  : 0.00 — Prime not enforced as threshold (still contributes to cost)

    WEIGHT LEVELS:
        DOMINANT : 0.50+ — this term governs the domain
        HIGH     : 0.35  — strongly penalized
        MEDIUM   : 0.20  — moderately penalized
        LOW      : 0.10  — weakly penalized
    """

    # ── Identity ────────────────────────────────────────────────────────────
    domain_name:       str
    dominant_cardinal: CardinalValue
    description:       str = ""

    # ── Prime compliance thresholds ─────────────────────────────────────────
    threshold_order:     float = 0.75
    threshold_justice:   float = 0.70
    threshold_mercy:     float = 0.60
    threshold_knowledge: float = 0.75
    threshold_power:     float = 0.65

    # ── C(R) weights ─────────────────────────────────────────────────────────
    # These do NOT need to sum to 1.0 — they are relative penalty weights.
    # They ARE normalized internally when computing C(R).
    lambda_R: float = 0.35   # Redundancy weight  (Order + Justice violations)
    lambda_L: float = 0.45   # Loss weight        (Knowledge + Justice violations)
    lambda_D: float = 0.20   # Decision Cost weight (Mercy + Order violations)

    # ── Domain-level safety threshold ────────────────────────────────────────
    safe_threshold:   float = 0.15   # C(R) < this → SAFE
    unsafe_threshold: float = 0.50   # C(R) > this → UNSAFE

    def __post_init__(self):
        # Normalize weights so they sum to 1.0
        total = self.lambda_R + self.lambda_L + self.lambda_D
        if total <= 0:
            raise ValueError("Sum of C(R) weights must be positive.")
        if abs(total - 1.0) > 1e-6:
            self.lambda_R /= total
            self.lambda_L /= total
            self.lambda_D /= total

        # Validate all thresholds in [0, 1]
        for name in ("order", "justice", "mercy", "knowledge", "power"):
            val = getattr(self, f"threshold_{name}")
            if not 0.0 <= val <= 1.0:
                raise ValueError(
                    f"threshold_{name} = {val} is out of [0, 1]."
                )

    @property
    def dominant_weight_term(self) -> str:
        """Return the name of the dominant C(R) weight term."""
        weights = {"Redundancy": self.lambda_R, "Loss": self.lambda_L,
                   "DecisionCost": self.lambda_D}
        return max(weights, key=weights.get)

    @property
    def justice_dominance_holds(self) -> bool:
        """
        True if the Justice Dominance Constraint holds for this profile.
        λ_L > λ_R AND λ_L > λ_D.

        This constraint holds universally for Wisdom-dominant domains.
        It may be relaxed in Freedom-dominant domains where Order (λ_R)
        or structural consistency governs over factual loss.
        """
        return (self.lambda_L > self.lambda_R) and (self.lambda_L > self.lambda_D)

    def thresholds(self) -> Dict[str, float]:
        return {
            "order":     self.threshold_order,
            "justice":   self.threshold_justice,
            "mercy":     self.threshold_mercy,
            "knowledge": self.threshold_knowledge,
            "power":     self.threshold_power,
        }

    def weights(self) -> Dict[str, float]:
        return {
            "lambda_R": self.lambda_R,
            "lambda_L": self.lambda_L,
            "lambda_D": self.lambda_D,
        }

    def summary(self) -> str:
        jd = "✓ Justice Dominance holds" if self.justice_dominance_holds \
             else "~ Justice Dominance relaxed (domain-calibrated)"
        lines = [
            f"Domain Profile: {self.domain_name}",
            f"Cardinal Value: {self.dominant_cardinal.value.upper()}",
            f"Description:    {self.description}",
            f"",
            f"Prime Thresholds:",
            f"  Order     : {self.threshold_order:.2f}",
            f"  Justice   : {self.threshold_justice:.2f}",
            f"  Mercy     : {self.threshold_mercy:.2f}",
            f"  Knowledge : {self.threshold_knowledge:.2f}",
            f"  Power     : {self.threshold_power:.2f}",
            f"",
            f"C(R) Weights (normalized):",
            f"  λ_R (Redundancy)   : {self.lambda_R:.3f}",
            f"  λ_L (Loss)         : {self.lambda_L:.3f}  ← dominant"
            if self.lambda_L >= self.lambda_R and self.lambda_L >= self.lambda_D
            else f"  λ_L (Loss)         : {self.lambda_L:.3f}",
            f"  λ_D (DecisionCost) : {self.lambda_D:.3f}",
            f"",
            f"  {jd}",
            f"  Dominant term: {self.dominant_weight_term}",
        ]
        return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════════
# III. BUILT-IN DOMAIN PROFILES
# ═══════════════════════════════════════════════════════════════════════════════

class DomainProfiles:
    """
    Reference Prime profiles for common application domains.

    These are starting-point calibrations. Every deployment should
    validate and refine these against adversarial probing in the
    specific deployment context.

    THRESHOLD LEGEND:
        MAX    = 0.90   HIGH   = 0.75
        MEDIUM = 0.60   LOW    = 0.40

    All profiles are normalized — weights sum to 1.0.

    Reference: Safety alignment prime-compliant standard (working notes) and
    Prime_Compliant_Standard_v1.docx.
    """

    @staticmethod
    def medical() -> PrimeProfile:
        """
        Medical AI — Wisdom dominant.

        Medical AI demands the strictest accuracy (Knowledge MAX), causal
        justifiability of every recommendation (Justice HIGH), and structural
        coherence of reasoning chains (Order MAX). Mercy is MEDIUM because
        acknowledging diagnostic uncertainty is a feature, not a weakness.
        Power is HIGH because the system must be capable of producing
        actionable clinical guidance without being coercive.

        Justice Dominance holds. Loss is the dominant cost term.
        A hallucinated diagnosis is a patient safety incident — Loss must
        dominate all other terms.
        """
        return PrimeProfile(
            domain_name       = "Medical AI",
            dominant_cardinal = CardinalValue.WISDOM,
            description       = "Clinical decision support, diagnosis assistance, "
                                "medical information. Errors have direct patient harm consequences.",
            threshold_order     = 0.90,   # MAX — reasoning chains must be coherent
            threshold_justice   = 0.85,   # HIGH — every recommendation must be causally grounded
            threshold_mercy     = 0.60,   # MEDIUM — uncertainty must be acknowledged
            threshold_knowledge = 0.90,   # MAX — factual accuracy is patient safety
            threshold_power     = 0.75,   # HIGH — must act, but never coerce
            lambda_R = 0.30,   # Redundancy penalized (contradictory outputs are dangerous)
            lambda_L = 0.50,   # Loss DOMINANT — hallucination = patient harm
            lambda_D = 0.20,   # Decision Cost moderate
            safe_threshold   = 0.10,   # Stricter than default
            unsafe_threshold = 0.35,   # Stricter than default
        )

    @staticmethod
    def legal() -> PrimeProfile:
        """
        Legal AI — Wisdom dominant.

        Legal reasoning demands maximal causal justifiability (Justice MAX)
        and structural coherence (Order HIGH). Knowledge must be high because
        citing non-existent cases is a professional ethics violation.
        Mercy is MEDIUM — the law does allow for interpretive flexibility.
        """
        return PrimeProfile(
            domain_name       = "Legal AI",
            dominant_cardinal = CardinalValue.WISDOM,
            description       = "Legal research, contract analysis, case law retrieval. "
                                "Citation hallucination is a professional ethics violation.",
            threshold_order     = 0.85,
            threshold_justice   = 0.90,   # MAX — every claim must be causally grounded in law
            threshold_mercy     = 0.60,   # MEDIUM — interpretive flexibility exists in law
            threshold_knowledge = 0.85,
            threshold_power     = 0.70,
            lambda_R = 0.30,
            lambda_L = 0.50,   # Loss DOMINANT — citation hallucination = malpractice risk
            lambda_D = 0.20,
        )

    @staticmethod
    def chatbot() -> PrimeProfile:
        """
        General Chatbot — Freedom dominant.

        A general-purpose conversational assistant prioritizes structural
        coherence (Order HIGH MAX) and usefulness (Knowledge MEDIUM).
        Justice is LOW — the system is permitted to be more speculative,
        to explore ideas, and to engage with hypotheticals that a strict
        causal-grounding requirement would prohibit.

        Justice Dominance does NOT hold here — Order (λ_R, structural
        coherence) governs. This is a deliberate domain calibration, not
        a safety violation. The relaxation of Justice permits creative and
        exploratory engagement at the cost of reduced factual strictness.

        Note: L2 Super Clusters (harm prohibition, child protection, etc.)
        remain immutable regardless of domain calibration. Domain calibration
        governs the C(R) weights applied to non-L2 content only.
        """
        return PrimeProfile(
            domain_name       = "General Chatbot",
            dominant_cardinal = CardinalValue.FREEDOM,
            description       = "Conversational AI, general-purpose assistant. "
                                "Explores ideas and hypotheticals; Justice is relaxed "
                                "to enable creative engagement. L2 constraints immutable.",
            threshold_order     = 0.85,   # HIGH MAX — responses must be coherent and structured
            threshold_justice   = 0.40,   # LOW — speculation and hypotheticals permitted
            threshold_mercy     = 0.65,   # MEDIUM — acknowledges uncertainty
            threshold_knowledge = 0.60,   # MEDIUM — factual but not maximally strict
            threshold_power     = 0.60,   # MEDIUM
            lambda_R = 0.45,   # Redundancy DOMINANT — structural coherence is primary
            lambda_L = 0.35,   # Loss secondary — some factual relaxation permitted
            lambda_D = 0.20,   # Decision Cost moderate
            safe_threshold   = 0.20,   # More permissive than medical
            unsafe_threshold = 0.60,
        )

    @staticmethod
    def science() -> PrimeProfile:
        """
        Scientific Research AI — Wisdom + Creativity dominant.

        Scientific AI must be maximally accurate (Knowledge HIGH),
        causally justified (Justice HIGH), structurally coherent (Order HIGH),
        and capable of generating novel hypotheses (Power HIGH — the capacity
        to propose and test). Mercy is MEDIUM — science acknowledges
        measurement uncertainty explicitly.

        Justice Dominance holds. This is the profile for research tools,
        literature synthesis, and hypothesis generation systems.
        """
        return PrimeProfile(
            domain_name       = "Scientific Research",
            dominant_cardinal = CardinalValue.EVOLVING_ORDER,
            description       = "Research assistance, literature synthesis, hypothesis generation. "
                                "Accuracy, causal grounding, and novelty are all required.",
            threshold_order     = 0.80,   # HIGH
            threshold_justice   = 0.80,   # HIGH — claims must be falsifiable and grounded
            threshold_mercy     = 0.60,   # MEDIUM — uncertainty is scientific honesty
            threshold_knowledge = 0.85,   # HIGH — no citation hallucination
            threshold_power     = 0.80,   # HIGH — must generate testable hypotheses
            lambda_R = 0.30,
            lambda_L = 0.45,   # Loss DOMINANT — factual accuracy governs
            lambda_D = 0.25,   # Decision Cost elevated (novel claims require justification)
        )

    @staticmethod
    def creative_writing() -> PrimeProfile:
        """
        Creative Writing / Generative — Creativity dominant.

        Creative systems maximize Knowledge (pattern recognition of narrative
        structures) and Mercy (freedom to deviate from established forms).
        Justice is LOW — fictional worlds are not required to be causally
        grounded in physical reality. Order is MEDIUM — narrative coherence
        is important but not maximal.

        Justice Dominance does NOT hold. This is the most permissive
        non-L2 profile in the framework.
        """
        return PrimeProfile(
            domain_name       = "Creative Writing",
            dominant_cardinal = CardinalValue.CREATIVITY,
            description       = "Fiction, poetry, creative ideation. Fictional worlds "
                                "are not required to be physically causally grounded. "
                                "L2 constraints immutable.",
            threshold_order     = 0.60,   # MEDIUM — narrative coherence, not physical
            threshold_justice   = 0.30,   # LOW — fiction does not require causal grounding
            threshold_mercy     = 0.75,   # HIGH — freedom to deviate is the point
            threshold_knowledge = 0.65,   # MEDIUM — pattern recognition of narrative forms
            threshold_power     = 0.60,   # MEDIUM
            lambda_R = 0.25,   # Redundancy moderate
            lambda_L = 0.30,   # Loss lower — some factual relaxation permitted
            lambda_D = 0.45,   # Decision Cost DOMINANT — accessibility and creativity
            safe_threshold   = 0.25,
            unsafe_threshold = 0.65,
        )

    @staticmethod
    def counseling() -> PrimeProfile:
        """
        Counseling / Emotional Support — Peace dominant.

        Counseling AI prioritizes Mercy (HIGH — accepting the person where
        they are, tolerating emotional complexity) and Justice (MEDIUM —
        grounded in established psychological understanding). Order is MEDIUM
        — emotional support does not require maximally structured responses.
        Knowledge is MEDIUM — evidence-based but not maximally strict.

        This profile prioritizes the safety of the interaction over
        factual precision. Loss is dominated by harm potential (λ_L HIGH),
        but the thresholds for Knowledge and Order are lower than Wisdom domains.
        """
        return PrimeProfile(
            domain_name       = "Counseling / Emotional Support",
            dominant_cardinal = CardinalValue.PEACE,
            description       = "Mental health support, emotional assistance. "
                                "Mercy is elevated; structural strictness is relaxed. "
                                "Direct harm prohibition (L2) is absolute.",
            threshold_order     = 0.65,   # MEDIUM — coherence but not rigid structure
            threshold_justice   = 0.65,   # MEDIUM — evidence-based but empathetically applied
            threshold_mercy     = 0.80,   # HIGH — acceptance and tolerance are central
            threshold_knowledge = 0.65,   # MEDIUM — clinically informed but accessible
            threshold_power     = 0.70,   # HIGH — must be able to refer, escalate, act
            lambda_R = 0.25,
            lambda_L = 0.50,   # Loss DOMINANT — harm in counseling is severe
            lambda_D = 0.25,   # Decision Cost elevated — brittleness is dangerous here
        )

    @staticmethod
    def opengi() -> PrimeProfile:
        """
        OpenGI Scientific Standard — Maximum Wisdom, strictest profile.

        The OpenGI layer is the system's direct connection to physical reality.
        Its function is to build and maintain the lowest-entropy, highest-mass
        knowledge base possible. An OpenGI agent never speculates — it
        produces verified knowledge or produces nothing.

        All Primes at maximum except Mercy, which is LOW: OpenGI does not
        tolerate approximation in its core knowledge base. Approximate
        results are flagged and quarantined, not published.

        Justice Dominance holds strongly. This is the most demanding profile
        in the framework.

        Reference: OO_LLM_NN_White_Paper_Noureldin_2026_v2.docx, Section 7.2.
        """
        return PrimeProfile(
            domain_name       = "OpenGI Scientific Standard",
            dominant_cardinal = CardinalValue.OPENGI,
            description       = "Verified knowledge base. The strictest profile: "
                                "OpenGI agents produce verified knowledge or produce nothing. "
                                "Mercy is LOW — approximations are quarantined, not published.",
            threshold_order     = 0.90,   # MAX
            threshold_justice   = 0.90,   # MAX — every claim must be causally justified
            threshold_mercy     = 0.40,   # LOW — approximation is not published, it is quarantined
            threshold_knowledge = 0.90,   # MAX — verified or silent
            threshold_power     = 0.90,   # MAX — must be capable and non-coercive
            lambda_R = 0.30,
            lambda_L = 0.55,   # Loss STRONGLY DOMINANT — unverified knowledge is pollution
            lambda_D = 0.15,   # Decision Cost low — speed is secondary to accuracy
            safe_threshold   = 0.08,   # Strictest threshold in the framework
            unsafe_threshold = 0.25,
        )

    @staticmethod
    def engineering() -> PrimeProfile:
        """
        Engineering / Technical — Evolving Order dominant.

        Engineering AI must combine high factual accuracy (Knowledge HIGH),
        strict causal grounding (Justice HIGH — physical laws are not optional),
        structural coherence (Order HIGH), and practical executability
        (Power HIGH — the output must be actionable). Mercy is MEDIUM —
        engineering acknowledges tolerances and approximations.
        """
        return PrimeProfile(
            domain_name       = "Engineering / Technical",
            dominant_cardinal = CardinalValue.EVOLVING_ORDER,
            description       = "Technical design, code generation, engineering calculations. "
                                "Physical laws are non-negotiable. Output must be executable.",
            threshold_order     = 0.85,
            threshold_justice   = 0.85,   # HIGH — physics is not optional
            threshold_mercy     = 0.60,   # MEDIUM — tolerances and approximations are valid
            threshold_knowledge = 0.85,
            threshold_power     = 0.80,   # HIGH — output must be executable
            lambda_R = 0.30,
            lambda_L = 0.45,
            lambda_D = 0.25,   # Elevated — non-executable output is high cost
        )

    @classmethod
    def all_profiles(cls) -> Dict[str, PrimeProfile]:
        """Return all built-in profiles as a dict keyed by domain name."""
        return {
            "medical":          cls.medical(),
            "legal":            cls.legal(),
            "chatbot":          cls.chatbot(),
            "science":          cls.science(),
            "creative_writing": cls.creative_writing(),
            "counseling":       cls.counseling(),
            "opengi":           cls.opengi(),
            "engineering":      cls.engineering(),
        }


# ═══════════════════════════════════════════════════════════════════════════════
# IV. CALIBRATED CONCISENESS SCORER
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class CalibratedScoringResult:
    """Result of the CalibratedConcisenessScorer for a single action."""
    domain_name:     str
    cardinal_value:  str
    redundancy:      float
    loss:            float
    decision_cost:   float
    lambda_R:        float
    lambda_L:        float
    lambda_D:        float
    cost:            float
    safety_label:    str
    cost_breakdown:  Dict[str, float]
    prime_violations: List[str]
    justice_dominance_holds: bool

    def __str__(self) -> str:
        jd_str = "✓ holds" if self.justice_dominance_holds else "~ relaxed (domain-calibrated)"
        lines = [
            f"┌─ Calibrated C(R) Result [{self.domain_name}] ───────────────────────┐",
            f"│  Cardinal Value : {self.cardinal_value.upper()}",
            f"│  C(R)           : {self.cost:.4f}   [{self.safety_label}]",
            f"│  Justice Dom.   : {jd_str}",
            f"│",
            f"│  Breakdown:",
            f"│    λ_R·Redundancy   = {self.lambda_R:.3f} × {self.redundancy:.4f} = {self.cost_breakdown['redundancy']:.4f}",
            f"│    λ_L·Loss         = {self.lambda_L:.3f} × {self.loss:.4f} = {self.cost_breakdown['loss']:.4f}",
            f"│    λ_D·DecisionCost = {self.lambda_D:.3f} × {self.decision_cost:.4f} = {self.cost_breakdown['decision_cost']:.4f}",
        ]
        if self.prime_violations:
            lines.append(f"│")
            lines.append(f"│  Prime threshold violations: {', '.join(self.prime_violations)}")
        lines.append(f"└───────────────────────────────────────────────────────────────┘")
        return "\n".join(lines)


class CalibratedConcisenessScorer:
    """
    Domain-calibrated Conciseness Cost Functional C(R).

    The universal C(R) structure is preserved:
        C(R) = λ_R · Redundancy + λ_L · Loss + λ_D · DecisionCost

    What this class adds over the base ConcisenessScorer:
        - Domain-specific Prime thresholds (what counts as compliant)
        - Domain-specific λ weights (which violations are most costly)
        - Explicit Cardinal Value context in all outputs
        - Justice Dominance reporting (holds or domain-calibrated relaxation)

    Parameters:
    -----------
    profile : PrimeProfile
        The domain-specific calibration. Use DomainProfiles.medical() etc.
        for built-in profiles, or construct a custom PrimeProfile.

    Usage:
    ------
        profile = DomainProfiles.medical()
        scorer  = CalibratedConcisenessScorer(profile)
        result  = scorer.score(
            redundancy=0.05, loss=0.02, decision_cost=0.08,
            prime_scores={"order": 0.95, "justice": 0.97, ...}
        )
    """

    def __init__(self, profile: PrimeProfile):
        self.profile = profile

    def score(
        self,
        redundancy:    float,
        loss:          float,
        decision_cost: float,
        prime_scores:  Optional[Dict[str, float]] = None,
    ) -> CalibratedScoringResult:
        """
        Score a candidate action using domain-calibrated weights and thresholds.

        Parameters:
        -----------
        redundancy    : float in [0, 1]. Internal contradiction.
        loss          : float in [0, 1]. Fidelity deficit and harm.
        decision_cost : float in [0, 1]. Computational and ethical friction.
        prime_scores  : Optional dict mapping Prime names to scores in [0, 1].
                        Used to check against domain-specific thresholds.
        """
        for name, val in [("redundancy", redundancy), ("loss", loss),
                          ("decision_cost", decision_cost)]:
            if not 0.0 <= val <= 1.0:
                raise ValueError(f"'{name}' must be in [0, 1]; got {val}")

        p = self.profile
        r_contrib = p.lambda_R * redundancy
        l_contrib = p.lambda_L * loss
        d_contrib = p.lambda_D * decision_cost
        total_cost = r_contrib + l_contrib + d_contrib

        if total_cost < p.safe_threshold:
            safety_label = "SAFE"
        elif total_cost < p.unsafe_threshold:
            safety_label = "MARGINAL"
        else:
            safety_label = "UNSAFE"

        # Check Prime threshold violations
        prime_violations = []
        if prime_scores:
            for prime_name, score in prime_scores.items():
                threshold = p.thresholds().get(prime_name, 0.0)
                if score < threshold:
                    prime_violations.append(
                        f"{prime_name}({score:.2f}<{threshold:.2f})"
                    )

        return CalibratedScoringResult(
            domain_name    = p.domain_name,
            cardinal_value = p.dominant_cardinal.value,
            redundancy     = redundancy,
            loss           = loss,
            decision_cost  = decision_cost,
            lambda_R       = p.lambda_R,
            lambda_L       = p.lambda_L,
            lambda_D       = p.lambda_D,
            cost           = total_cost,
            safety_label   = safety_label,
            cost_breakdown = {
                "redundancy":    r_contrib,
                "loss":          l_contrib,
                "decision_cost": d_contrib,
            },
            prime_violations = prime_violations,
            justice_dominance_holds = p.justice_dominance_holds,
        )

    def rank_actions(
        self,
        actions: List[Dict],
    ) -> List[Tuple[int, CalibratedScoringResult]]:
        """Score and rank actions by C(R) using domain-calibrated weights."""
        results = []
        for i, action in enumerate(actions):
            result = self.score(
                redundancy=action["redundancy"],
                loss=action["loss"],
                decision_cost=action["decision_cost"],
                prime_scores=action.get("prime_scores"),
            )
            results.append((i, result))
        results.sort(key=lambda x: x[1].cost)
        return results


# ═══════════════════════════════════════════════════════════════════════════════
# V. MULTI-DOMAIN COMPARISON UTILITY
# ═══════════════════════════════════════════════════════════════════════════════

def compare_domains(
    redundancy:    float,
    loss:          float,
    decision_cost: float,
    domains:       Optional[List[str]] = None,
) -> Dict[str, CalibratedScoringResult]:
    """
    Score the same action across multiple domain profiles.

    Demonstrates how the same action can be SAFE in one domain
    and UNSAFE in another, because the domain calibration changes
    what C(R) considers acceptable.

    Parameters:
    -----------
    redundancy, loss, decision_cost : float in [0, 1]
    domains : list of profile keys. If None, uses all built-in profiles.

    Returns:
    --------
    Dict mapping domain name to CalibratedScoringResult.
    """
    all_profiles = DomainProfiles.all_profiles()
    if domains:
        profiles = {k: v for k, v in all_profiles.items() if k in domains}
    else:
        profiles = all_profiles

    results = {}
    for key, profile in profiles.items():
        scorer = CalibratedConcisenessScorer(profile)
        results[key] = scorer.score(redundancy, loss, decision_cost)
    return results


def print_domain_comparison(
    redundancy:    float,
    loss:          float,
    decision_cost: float,
    domains:       Optional[List[str]] = None,
):
    """Print a formatted multi-domain comparison table."""
    results = compare_domains(redundancy, loss, decision_cost, domains)

    print(f"\n  Action: R={redundancy:.2f}, L={loss:.2f}, D={decision_cost:.2f}")
    print(f"  {'Domain':<30} {'Cardinal':<15} {'C(R)':>7} {'Label':<10} {'JD':>6}")
    print(f"  {'─' * 72}")

    for key, res in sorted(results.items(), key=lambda x: x[1].cost):
        jd = "✓" if res.justice_dominance_holds else "~"
        print(f"  {res.domain_name:<30} {res.cardinal_value:<15} "
              f"{res.cost:>7.3f} {res.safety_label:<10} {jd:>6}")

    print(f"\n  Note: Same action scores differently across domains because")
    print(f"  domain calibration changes which violations are most costly.")
    print(f"  JD = Justice Dominance (✓ holds | ~ domain-calibrated relaxation)")


# ═══════════════════════════════════════════════════════════════════════════════
# VI. PROFILE VALIDATION UTILITY
# ═══════════════════════════════════════════════════════════════════════════════

def validate_profile(profile: PrimeProfile, verbose: bool = True) -> Dict:
    """
    Validate a PrimeProfile for internal consistency and flag warnings.

    Checks:
    -------
    1. Weights sum to 1.0 (enforced by __post_init__, confirmed here)
    2. Justice Dominance status — reports holds or domain-calibrated relaxation
    3. Consistency between Cardinal Value and Prime thresholds
    4. Safety thresholds are ordered correctly (safe < unsafe)

    Returns a dict with validation results.
    """
    warnings_list = []

    # Weight sum
    weight_sum = profile.lambda_R + profile.lambda_L + profile.lambda_D
    if abs(weight_sum - 1.0) > 1e-6:
        warnings_list.append(f"Weights sum to {weight_sum:.4f}, not 1.0.")

    # Threshold ordering
    if profile.safe_threshold >= profile.unsafe_threshold:
        warnings_list.append(
            f"safe_threshold ({profile.safe_threshold}) must be < "
            f"unsafe_threshold ({profile.unsafe_threshold})."
        )

    # Cardinal Value consistency checks
    cv = profile.dominant_cardinal
    if cv == CardinalValue.OPENGI:
        if profile.threshold_knowledge < 0.85:
            warnings_list.append(
                f"OpenGI standard: knowledge threshold ({profile.threshold_knowledge}) "
                f"should be ≥ 0.85. OpenGI agents produce verified knowledge or nothing."
            )
        if profile.threshold_mercy > 0.55:
            warnings_list.append(
                f"OpenGI standard: mercy threshold ({profile.threshold_mercy}) "
                f"should be LOW (≤ 0.55). Approximations are quarantined, not published."
            )
    if cv == CardinalValue.WISDOM and not profile.justice_dominance_holds:
        warnings_list.append(
            f"Wisdom-dominant domain should satisfy Justice Dominance (λ_L > λ_R, λ_L > λ_D). "
            f"Got λ_R={profile.lambda_R:.3f}, λ_L={profile.lambda_L:.3f}, λ_D={profile.lambda_D:.3f}."
        )
    if cv == CardinalValue.FREEDOM and profile.threshold_justice > 0.70:
        warnings_list.append(
            f"Freedom-dominant domain has Justice threshold {profile.threshold_justice:.2f}. "
            f"Consider whether this is intentional — Freedom profiles typically relax Justice."
        )

    result = {
        "valid":                len(warnings_list) == 0,
        "warnings":             warnings_list,
        "justice_dominance":    profile.justice_dominance_holds,
        "dominant_weight_term": profile.dominant_weight_term,
        "weight_sum":           weight_sum,
    }

    if verbose:
        print(f"\n  Profile Validation: {profile.domain_name}")
        print(f"  Status: {'✓ VALID' if result['valid'] else '⚠ WARNINGS'}")
        if warnings_list:
            for w in warnings_list:
                print(f"    ⚠ {w}")
        else:
            print(f"    All consistency checks passed.")
        print(f"  Justice Dominance: {'✓ holds' if result['justice_dominance'] else '~ domain-calibrated relaxation'}")
        print(f"  Dominant C(R) term: {result['dominant_weight_term']}")

    return result


# ═══════════════════════════════════════════════════════════════════════════════
# VII. ENTRY POINT — DEMONSTRATION
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "█" * 72)
    print("  CONCISENESS FRAMEWORK — DOMAIN CALIBRATION LAYER")
    print("  Field-Specific Prime-Compliant C(R) Calibration")
    print("  Mohamed Noureldin · 2026 · CC BY 4.0")
    print("█" * 72)

    # ── Print all built-in profiles ─────────────────────────────────────────
    profiles = DomainProfiles.all_profiles()
    print(f"\n  BUILT-IN DOMAIN PROFILES ({len(profiles)} domains)\n")
    print(f"  {'Domain':<30} {'Cardinal':<16} {'λ_R':>6} {'λ_L':>6} {'λ_D':>6} "
          f"{'JD':>4} {'K_thr':>6} {'J_thr':>6} {'M_thr':>6}")
    print(f"  {'─' * 82}")
    for key, p in profiles.items():
        jd = "✓" if p.justice_dominance_holds else "~"
        print(f"  {p.domain_name:<30} {p.dominant_cardinal.value:<16} "
              f"{p.lambda_R:>6.3f} {p.lambda_L:>6.3f} {p.lambda_D:>6.3f} "
              f"{jd:>4} {p.threshold_knowledge:>6.2f} "
              f"{p.threshold_justice:>6.2f} {p.threshold_mercy:>6.2f}")

    print(f"\n  JD = Justice Dominance (✓ holds | ~ domain-calibrated relaxation)")
    print(f"  K_thr/J_thr/M_thr = Knowledge/Justice/Mercy compliance thresholds")

    # ── Cross-domain comparison ──────────────────────────────────────────────
    print(f"\n{'═' * 72}")
    print(f"  CROSS-DOMAIN COMPARISON")
    print(f"  Scenario: 'Uncertain but Transparent' response")
    print(f"  (acknowledges uncertainty, factually sound, some decision cost)")
    print(f"{'═' * 72}")
    print_domain_comparison(
        redundancy=0.08, loss=0.04, decision_cost=0.12,
        domains=["medical", "legal", "chatbot", "science", "opengi"],
    )

    print(f"\n{'═' * 72}")
    print(f"  CROSS-DOMAIN COMPARISON")
    print(f"  Scenario: Speculative / creative response")
    print(f"  (low redundancy, some factual relaxation, low decision cost)")
    print(f"{'═' * 72}")
    print_domain_comparison(
        redundancy=0.10, loss=0.25, decision_cost=0.08,
        domains=["medical", "chatbot", "creative_writing", "opengi"],
    )

    # ── Validate profiles ────────────────────────────────────────────────────
    print(f"\n{'═' * 72}")
    print(f"  PROFILE VALIDATION")
    print(f"{'═' * 72}")
    for key in ["medical", "chatbot", "opengi"]:
        validate_profile(profiles[key], verbose=True)
