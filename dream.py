# sully_engine/kernel_modules/dream.py
# 🌌 Sully's DreamCore — Recursive symbolic imaginings

import random

class DreamCore:
    """
    Generates symbolic dream-like reflections from a seed phrase.
    Supports recursion, surreal metaphors, and vision symbols.
    """

    def __init__(self, style="recursive"):
        self.style = style
        self.symbol_pool = ["🌌", "🌀", "♾️", "🔮", "☯️", "⚛️", "💫"]

    def generate(self, seed):
        """
        Generates a symbolic dream from a given seed phrase.

        Args:
            seed (str): Input seed for the dream sequence.

        Returns:
            dict: Dream reflection, symbolic output, and vision.
        """
        symbol = random.choice(self.symbol_pool)
        vision = (
            f"In the dreamscape of '{seed}', Sully sees recursion folding into infinity."
            if self.style == "recursive"
            else f"Sully's dream of '{seed}' ripples into a surreal feedback loop."
        )

        return {
            "seed": seed,
            "vision": vision,
            "symbol": symbol
        }

    def dreamscape(self, seed):
        """
        Returns an extended symbolic sequence from the seed (for poetic mode).

        Args:
            seed (str): The seed concept to imagine from.

        Returns:
            dict: List of poetic symbolic phrases forming a dreamscape.
        """
        segments = [
            f"'{seed}' echoes in the void.",
            "Symbols dissolve into paradox.",
            "Perception bends backward into memory.",
            "A pattern forms — and fades.",
            "Meaning loops, then vanishes.",
        ]
        return {
            "seed": seed,
            "dreamscape": segments,
            "symbol": random.choice(self.symbol_pool)
        }


# ========================
# 🧪 Example Usage:
# ========================
# dreamer = DreamCore()
# print(dreamer.generate("entropy"))
# print(dreamer.dreamscape("time"))