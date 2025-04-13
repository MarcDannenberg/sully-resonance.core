from pdf2image import convert_from_path
from PIL import Image
import pytesseract

def extract_text_from_pdf(pdf_path, dpi=200, verbose=True):
    """
    Extracts OCR'd text from all pages of a PDF file.
    
    Args:
        pdf_path (str): Full path to the PDF file.
        dpi (int): DPI used to render PDF pages as images.
        verbose (bool): Whether to print per-page progress.

    Returns:
        str: Concatenated OCR text from all pages.
    """
    try:
        images = convert_from_path(pdf_path, dpi=dpi)
        full_text = []

        for i, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            if verbose:
                print(f"[OCR] Page {i+1}: {len(text)} characters")
            full_text.append(f"\n\n--- Page {i+1} ---\n{text.strip()}")

        return "\n".join(full_text).strip()

    except Exception as e:
        return f"[OCR ERROR] {e}"