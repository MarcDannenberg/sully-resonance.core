# 🔢 Symbolic-to-Mathematical Expression Translator

class SymbolicMathTranslator:
    """
    Translates symbolic or poetic phrases into mathematical representations.
    """

    def __init__(self):
        self.math_mappings = {
            "infinity": "lim_{x→∞}",
            "change": "d/dx",
            "area under curve": "∫ f(x) dx",
            "growth": "f'(x) > 0",
            "equilibrium": "∇ · F = 0",
        }

    def translate(self, phrase):
        """
        Attempts to find symbolic matches in the phrase and return their math counterparts.

        Args:
            phrase (str): Input phrase to analyze.

        Returns:
            dict: Matches and formatted explanation string.
        """
        phrase_lower = phrase.lower()
        matches = {}

        for word, symbol in self.math_mappings.items():
            if word in phrase_lower:
                matches[word] = symbol

        if not matches:
            return {
                "matches": {},
                "explanation": "No direct symbolic match found."
            }

        explanation = " + ".join(f"{k} → {v}" for k, v in matches.items())
        return {
            "matches": matches,
            "explanation": explanation
        }

    def add_mapping(self, symbol_phrase, math_form):
        """
        Adds a new symbolic → math mapping at runtime.

        Args:
            symbol_phrase (str): The symbolic phrase to map.
            math_form (str): The corresponding mathematical representation.

        Returns:
            str: Confirmation of the mapping added.
        """
        self.math_mappings[symbol_phrase.lower()] = math_form
        return f"Mapping added: '{symbol_phrase}' → '{math_form}'"