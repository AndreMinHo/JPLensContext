from typing import Tuple
import easyocr
import numpy as np
from PIL import Image


# Load the reader ONCE (expensive operation)
_reader = easyocr.Reader(['ja', 'en'], gpu=False)


def read_text(image_path: str) -> Tuple[str, float]:

    image = Image.open(image_path).convert("RGB")
    image_np = np.array(image)

    results = _reader.readtext(image_np)

    if not results:
        return "", 0.0

    texts = []
    confidences = []

    for (_, text, confidence) in results:
        texts.append(text)
        confidences.append(confidence)

    combined_text = " ".join(texts)
    avg_confidence = sum(confidences) / len(confidences)

    return combined_text, avg_confidence
