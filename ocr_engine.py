# sully_engine/kernel_modules/ocr_engine.py

import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import numpy as np

# ✅ Tell Tesseract where to find the binary
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class SullyOCREngine:
    def extract_text_from_pdf(self, pdf_path):
        """
        Convert PDF pages to images, then run OCR on each.
        Returns combined text.
        """
        try:
            images = convert_from_path(pdf_path)
            all_text = []

            for i, img in enumerate(images):
                text = pytesseract.image_to_string(img)
                print(f"[OCR] Page {i+1} extracted. Length: {len(text)} characters")
                all_text.append(text)

            return "\n".join(all_text)

        except Exception as e:
            return f"[OCR ERROR] {e}"

    def autoflatten_image(self, image_path, output_path="flattened_temp.png"):
        """
        Detect skew/rotation in an image and deskew it using OpenCV.
        Returns the path to the corrected image.
        """
        try:
            import cv2  # 🔁 Lazy import so no crash if unused

            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            blur = cv2.GaussianBlur(img, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            coords = np.column_stack(np.where(thresh > 0))
            angle = cv2.minAreaRect(coords)[-1]

            if angle < -45:
                angle = -(90 + angle)
            else:
                angle = -angle

            (h, w) = img.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

            cv2.imwrite(output_path, rotated)
            print(f"[Flatten] Image saved to {output_path}")
            return output_path

        except Exception as e:
            return f"[Autoflatten ERROR] {e}"