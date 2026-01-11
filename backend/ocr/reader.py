import os
from typing import Tuple

# Disable PaddleOCR model connectivity check for deployment environments
os.environ.setdefault('DISABLE_MODEL_SOURCE_CHECK', 'True')

from paddleocr import PaddleOCR
import numpy as np
from PIL import Image

# Get the directory where models are stored (works for both local dev and Docker)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)  # Go up one level from backend/ocr/
models_dir = os.path.join(project_root, 'models')

# Load the reader ONCE (expensive operation) with local models
_reader = PaddleOCR(
    use_angle_cls=True,
    lang='japan'
)


def read_text(image_path: str) -> Tuple[str, float]:

    results = _reader.ocr(image_path)

    if not results or not results[0]:
        return "", 0.0

    # Extract texts and scores from the result dictionary
    texts = results[0].get('rec_texts', [])
    confidences = results[0].get('rec_scores', [])

    if not texts:
        return "", 0.0

    combined_text = " ".join(texts)
    avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0

    return combined_text, avg_confidence
