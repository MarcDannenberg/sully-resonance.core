# autoflatten.py

import cv2
import numpy as np

def autoflatten_image(image_path, output_path="flattened_temp.png"):
    """
    Auto-flattens a scanned image by deskewing based on contours and saves the output.
    """
    try:
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
        return output_path

    except Exception as e:
        return f"[Autoflatten ERROR] {e}"