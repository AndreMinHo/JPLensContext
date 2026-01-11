from typing import Tuple

from manga_ocr import MangaOcr

# Load the reader ONCE (expensive operation)
_reader = MangaOcr()


def read_text(image_path: str) -> Tuple[str, float]:

    text = _reader(image_path)

    if not text:
        return "", 0.0

    return text, 1.0
