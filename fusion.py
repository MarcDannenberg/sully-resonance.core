# sully_engine/kernel_modules/fusion.py
# 🔗 Symbol Fusion Engine — Synthesize new meaning from multiple symbols

class SymbolFusionEngine:
    """
    Combines multiple symbolic inputs into a unified expression.
    """

    def __init__(self):
        self.style = "entanglement"

    def fuse(self, *symbols):
        """
        Combines symbols into a symbolic 'fusion'.

        Args:
            *symbols: Any number of string-based symbolic terms.

        Returns:
            dict: Inputs, fused result, and comment on synthesis.
        """
        if not symbols:
            return {
                "inputs": [],
                "result": "",
                "comment": "No symbols provided to fuse."
            }

        fused = " ⨁ ".join(symbols)
        return {
            "inputs": list(symbols),
            "result": fused,
            "comment": "Sully perceives this as symbolic entanglement."
        }

    def fuse_with_style(self, *symbols, style=None):
        """
        Fuses symbols using a style such as poetic, numeric, or recursive.

        Args:
            *symbols: Input symbolic terms.
            style (str): Optional style override.

        Returns:
            dict: Styled symbolic fusion.
        """
        style = style or self.style
        fused = " → ".join(symbols) if style == "poetic" else " ⨁ ".join(symbols)

        return {
            "style": style,
            "inputs": list(symbols),
            "fusion": fused,
            "comment": f"Fusion executed in '{style}' style."
        }