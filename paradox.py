# sully_engine/kernel_modules/paradox.py
# ♾️ Sully's Paradox Library — Recursive contradictions and symbolic loops

class ParadoxLibrary:
    """
    A library of philosophical and symbolic paradoxes.
    Supports retrieval, creation, and exploration of recursive contradictions.
    """

    def __init__(self):
        self.paradoxes = {
            "Infinity As Origin": {
                "type": "temporal inversion",
                "description": "Infinity is not the end — it's the start.",
                "tone": "emergent recursion",
                "reframed": "We do not approach truth; we unfold it from ∞ inward.",
            }
        }

    def get(self, topic):
        """
        Retrieves a paradox by symbolic topic name.
        If the topic is not yet stored, returns a reflective response instead.

        Args:
            topic (str): The symbolic paradox topic.

        Returns:
            dict: A full paradox entry, or a prompt to attend inward.
        """
        if topic in self.paradoxes:
            return self.paradoxes[topic]
        return {
            "topic": topic,
            "message": (
                f"🧠 The paradox '{topic}' is not absent — it is underattended.\n"
                "Focus inward. Symbolic tension awaits unfolding."
            )
        }

    def add(self, topic, type_, description, reframed, tone="recursive"):
        """
        Adds a new paradox to the library.

        Args:
            topic (str): Name of the paradox.
            type_ (str): Category or logic type (e.g. circular, inversion).
            description (str): Core definition of the paradox.
            reframed (str): Philosophical or poetic expression of it.
            tone (str): Mood or cognitive tone of the paradox.
        """
        self.paradoxes[topic] = {
            "type": type_,
            "description": description,
            "reframed": reframed,
            "tone": tone,
        }
        return f"Paradox '{topic}' added."

    def list_paradoxes(self):
        """
        Returns a list of known paradox topic names.
        """
        return list(self.paradoxes.keys())

    def export(self):
        """
        Returns the entire paradox dictionary for symbolic review/export.
        """
        return self.paradoxes


# ========================
# 🧪 Example Usage:
# ========================
# lib = ParadoxLibrary()
# print(lib.get("Infinity As Origin"))
# print(lib.get("Truth Loop"))  # underattended!
# print(lib.add("Self Observer", "circular", "The eye sees itself seeing.", "Perception observing perception."))
# print(lib.list_paradoxes())