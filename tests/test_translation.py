from backend.translation.translator import translate_text
from backend.ocr.reader import read_text

def test_translate_simple_text():
    """Test translation of a simple Japanese greeting."""
    japanese_text = "こんにちは"
    result = translate_text(japanese_text)

    assert result.raw_text == japanese_text
    assert result.detected_language == "ja"
    assert result.translation.literal is not None
    assert result.translation.natural is not None
    assert result.context.formality in ["casual", "polite", "formal"]
    assert isinstance(result.ambiguity.is_ambiguous, bool)
    assert isinstance(result.ambiguity.possible_meanings, list)

def test_translate_empty_text():
    """Test translation of empty text."""
    result = translate_text("")

    assert result.raw_text == ""
    assert result.translation.literal == ""
    assert result.translation.natural == ""

def test_translate_polite_text():
    """Test translation of polite Japanese text."""
    japanese_text = "こんにちは、よろしくお願いします。"
    result = translate_text(japanese_text)

    assert result.context.formality in ["polite", "formal"]

def test_ocr_and_translation_integration():
    """Test the full pipeline: OCR -> Translation."""
    # Run OCR on the sample image
    ocr_text, confidence = read_text("tests/sample_jp.png")

    print("=== OCR RESULT ===")
    print(f"TEXT: {repr(ocr_text)}")
    print(f"CONFIDENCE: {confidence}")

    # Translate the OCR result
    translation_result = translate_text(ocr_text)

    print("=== TRANSLATION RESULT ===")
    print(f"Raw text: {translation_result.raw_text}")
    print(f"Literal translation: {translation_result.translation.literal}")
    print(f"Natural translation: {translation_result.translation.natural}")
    print(f"Formality: {translation_result.context.formality}")

    # Basic assertions
    assert translation_result.raw_text == ocr_text
    assert translation_result.translation.literal is not None
    assert translation_result.context.formality in ["casual", "polite", "formal"]

if __name__ == "__main__":
    test_translate_simple_text()
    test_translate_empty_text()
    test_translate_polite_text()
    test_ocr_and_translation_integration()
    print("All tests passed!")
