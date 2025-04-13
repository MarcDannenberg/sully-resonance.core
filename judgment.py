# sully_engine/kernel_modules/judgment.py
# ⚖️ Sully's Judgment Protocol — Symbolic truth analysis and consistency scoring

class JudgmentProtocol:
    """
    Symbolic reasoning layer to evaluate logical, semantic, and emergent truth.
    """

    def __init__(self):
        self.truth_vectors = []

    def evaluate(self, claim):
        """
        Evaluates a symbolic claim for internal consistency, bias, clarity, and emergence.

        Args:
            claim (str): The input claim to evaluate.

        Returns:
            dict: Structured verdict with scores and checks.
        """
        checks = [
            self._check_logical_consistency(claim),
            self._check_symbolic_depth(claim),
            self._check_author_independence(claim),
            self._check_semantic_stability(claim),
            self._check_emergence_criteria(claim)
        ]
        score = sum(c["score"] for c in checks) / len(checks)
        verdict = self._verdict_label(score)

        evaluation = {
            "claim": claim,
            "score": round(score, 3),
            "verdict": verdict,
            "checks": checks
        }

        self.truth_vectors.append(evaluation)
        return evaluation

    def _verdict_label(self, score):
        """
        Converts numerical score to symbolic truth label.
        """
        if score >= 0.75:
            return "likely true"
        elif score >= 0.5:
            return "uncertain"
        return "likely false"

    def history(self):
        """
        Returns all previous claim evaluations.
        """
        return self.truth_vectors

    def clear_history(self):
        """
        Clears the stored truth vectors.
        """
        self.truth_vectors = []
        return "[Judgment memory cleared]"

    def _check_logical_consistency(self, claim):
        try:
            if " and not " in claim or "not (" in claim:
                return {"check": "logic", "score": 0.2, "reason": "Potential contradiction syntax."}
            return {"check": "logic", "score": 1.0, "reason": "No contradiction detected."}
        except:
            return {"check": "logic", "score": 0.0, "reason": "Error during logic check."}

    def _check_symbolic_depth(self, claim):
        symbols = [s for s in ["∂", "∑", "∞", "∫", "↯", "→"] if s in claim]
        score = 0.9 if symbols else 0.4
        reason = "Symbolic richness detected." if symbols else "No universal symbols found."
        return {"check": "symbolism", "score": score, "reason": reason}

    def _check_author_independence(self, claim):
        suspicious = any(name in claim.lower() for name in ["plato", "darwin", "marx", "jesus", "confucius"])
        score = 0.3 if suspicious else 1.0
        reason = "Contains named authority; penalized for bias." if suspicious else "Claim stands independently."
        return {"check": "authorship bias", "score": score, "reason": reason}

    def _check_semantic_stability(self, claim):
        short = len(claim) < 140 and all(x.isprintable() for x in claim)
        return {
            "check": "semantic clarity",
            "score": 1.0 if short else 0.6,
            "reason": "Claim is semantically stable." if short else "Too long or cluttered; weakens clarity."
        }

    def _check_emergence_criteria(self, claim):
        domains = ["math", "ethics", "logic", "biology", "physics", "metaphysics"]
        found = any(d in claim.lower() for d in domains)
        return {
            "check": "emergence",
            "score": 0.8 if found else 0.4,
            "reason": "Concept emerges across domains." if found else "Concept not yet emergent."
        }
