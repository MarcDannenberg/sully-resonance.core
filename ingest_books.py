# sully_engine/kernel_modules/ingest_books.py
# 📖 Sully's Book Ingestion Gateway

import os
from PyPDF2 import PdfReader
from ..kernel_modules.ocr_engine import SullyOCREngine

class BookIngestor:
    """
    Ingests various text-based document formats and extracts their content
    for symbolic learning. Supports optional OCR for scanned PDFs.
    """

    def __init__(self, ocr_enabled=False):
        self.ocr = SullyOCREngine() if ocr_enabled else None

    def ingest(self, file_path):
        """
        Ingests a file based on its extension.

        Returns:
            str: Extracted text, or error message.
        """
        try:
            ext = os.path.splitext(file_path)[1].lower()

            if ext == ".pdf":
                if self.ocr:
                    return self.ocr.extract_text_from_pdf(file_path)
                return self._extract_text_pdf(file_path)

            elif ext in [".txt", ".md"]:
                return self._extract_text_text(file_path)

            elif ext == ".docx":
                return self._extract_text_docx(file_path)

            return "[Unsupported file type]"

        except Exception as e:
            return f"[Ingestion Error] {e}"

    def _extract_text_pdf(self, pdf_path):
        """
        Extracts text from standard (non-scanned) PDFs using PyPDF2.
        """
        try:
            text = []
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                text.append(page.extract_text() or "")
            return "\n".join(text).strip()
        except Exception as e:
            return f"[PDF Parsing Error] {e}"

    def _extract_text_text(self, txt_path):
        """
        Reads raw text files (.txt, .md).
        """
        try:
            with open(txt_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception as e:
            return f"[Text File Error] {e}"

    def _extract_text_docx(self, docx_path):
        """
        Extracts paragraphs from a Word .docx file.
        """
        try:
            import docx
            doc = docx.Document(docx_path)
            return "\n".join(p.text for p in doc.paragraphs).strip()
        except ImportError:
            return "[Missing `python-docx`. Install it with `pip install python-docx`]"
        except Exception as e:
            return f"[DOCX Error] {e}"

    def summarize_file(self, file_path):
        """
        Returns basic info about a file (type, size) for logging/debug.
        """
        ext = os.path.splitext(file_path)[1].lower()
        size_kb = os.path.getsize(file_path) // 1024
        return {
            "path": file_path,
            "extension": ext,
            "size_kb": size_kb,
            "ocr_enabled": bool(self.ocr)
        }