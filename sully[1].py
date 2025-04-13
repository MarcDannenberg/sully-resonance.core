# --- Imports ---
import os
import json
from sully_engine.identity import SullyIdentity
from sully_engine.codex import SullyCodex
from sully_engine.reasoning import SymbolicReasoningNode
from sully_engine.memory import SullySearchMemory

# Kernel Modules
from sully_engine.kernel_modules.judgment import JudgmentProtocol
from sully_engine.kernel_modules.dream import DreamCore
from sully_engine.kernel_modules.math_translator import SymbolicMathTranslator
from sully_engine.kernel_modules.fusion import SymbolFusionEngine
from sully_engine.kernel_modules.paradox import ParadoxLibrary
from sully_engine.kernel_modules.ocr_engine import SullyOCREngine
from sully_engine.kernel_modules.ingest_books import BookIngestor

MEMORY_PATH = "sully_ingested.json"


class Sully:
    def __init__(self):
        self.identity = SullyIdentity()
        self.memory = SullySearchMemory()
        self.codex = SullyCodex()

        self.translator = SymbolicMathTranslator()
        self.judgment = JudgmentProtocol()
        self.dream = DreamCore()
        self.paradox = ParadoxLibrary()
        self.fusion = SymbolFusionEngine()
        self.reasoning_node = SymbolicReasoningNode(
            codex=self.codex,
            translator=self.translator,
            memory=self.memory
        )

        self.ocr = SullyOCREngine()
        self.book_ingestor = BookIngestor(ocr_enabled=True)
        self.knowledge = []

    def speak_identity(self):
        return self.identity.speak_identity()

    def evaluate_claim(self, text):
        return self.judgment.evaluate(text)

    def dream(self, seed):
        return self.dream.generate(seed)

    def translate_math(self, phrase):
        return self.translator.translate(phrase)

    def fuse(self, *inputs):
        return self.fusion.fuse(*inputs)

    def reveal_paradox(self, topic):
        return self.paradox.get(topic)

    def reason(self, message, tone="emergent"):
        return self.reasoning_node.reason(message, tone)

    def remember(self, message):
        self.knowledge.append(message)
        return f"📘 Stored: '{message}'"

    def ingest_and_store_text(self, file_path):
        content = self.book_ingestor.ingest(file_path)
        if content:
            self.knowledge.append(content)
            self.save_to_disk(file_path, content)
            return f"[Book Ingested: {file_path}]"
        return "[No Content Extracted]"

    def save_to_disk(self, path, content):
        data = {path: content}
        if os.path.exists(MEMORY_PATH):
            with open(MEMORY_PATH, "r", encoding="utf-8") as f:
                existing = json.load(f)
            existing.update(data)
        else:
            existing = data
        with open(MEMORY_PATH, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=2)

    def load_books_from_folder(self, folder_path="sullybooks"):
        if not os.path.exists(folder_path):
            return f"❌ Folder '{folder_path}' not found."

        results = []
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".pdf"):
                full_path = os.path.join(folder_path, filename)
                result = self.ingest_and_store_text(full_path)
                results.append(result)
        return results
