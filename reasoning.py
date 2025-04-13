# sully_engine/reasoning.py
# 🧠 Sully's Symbolic Reasoning Node

class SymbolicReasoningNode:
    """
    Core reasoning node that synthesizes meaning from symbolic input.
    Combines memory, codex search, and math translation for insight.
    """
    def __init__(self, codex, translator, memory):
        self.codex = codex
        self.translator = translator
        self.memory = memory

    def reason(self, phrase, tone="emergent"):
        """
        Processes a symbolic phrase and returns layered insight.

        Args:
            phrase (str): Input message or symbolic statement.
            tone (str): Cognitive mood or framing style.

        Returns:
            dict: Symbolic reflection, math hint, memory context, and decision.
        """
        # Step 1: Reframe the phrase (symbolic insight)
        reframed = f"'{phrase}' reflects a symbolic shift in perception."

        # Step 2: Math translation (if applicable)
        math_hint = self.translator.translate(phrase)
        math_hint = math_hint if math_hint else "∅"

        # Step 3: Codex memory lookup
        related = self.codex.search(phrase)
        memory_links = [
            f"Echo from {k}: {v.get('reframed', '...')}" for k, v in related.items()
        ] if related else ["No echoes found."]

        # Step 4: Add to memory
        self.memory.store_query(phrase, {"reframed": reframed})

        # Step 5: Symbolic response
        return {
            "reframed": reframed,
            "math_hint": math_hint,
            "tone_interpretation": f"In tone '{tone}', this unfolds like a recursive blossom.",
            "memory_context": memory_links,
            "decision": f"The symbol '{phrase}' resonates as transformation."
        }

    def analyze(self, phrase):
        """
        Returns a deep-dive symbolic diagnostic (internal inspection mode).
        """
        return {
            "raw_input": phrase,
            "codex_matches": self.codex.search(phrase),
            "memory_status": self.memory.export_memory(),
            "math_translation": self.translator.translate(phrase)
        }
