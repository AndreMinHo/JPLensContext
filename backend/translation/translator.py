from translatepy import Translator
from backend.schemas.translation_schema import (
    TranslationResponse,
    TranslationResult,
    ContextInfo,
    AmbiguityInfo
)


# Initialize translator once
_translator = Translator()


def translate_text(text: str) -> TranslationResponse:
    """
    Translate Japanese text to English with context information.

    Args:
        text: Japanese text to translate

    Returns:
        TranslationResponse with translation, context, and ambiguity info
    """
    if not text.strip():
        return TranslationResponse(
            raw_text=text,
            detected_language="ja",
            translation=TranslationResult(literal="", natural=""),
            context=ContextInfo(usage="", formality="", cultural_notes=[]),
            ambiguity=AmbiguityInfo(is_ambiguous=False, possible_meanings=[])
        )

    try:
        # Translate to English
        translation = _translator.translate(text, 'en', 'ja')
        translated_text = str(translation)

        # For now, use same text for literal and natural translation
        # TODO: Implement more sophisticated natural translation
        literal_translation = translated_text
        natural_translation = translated_text

        # Basic context analysis
        context = _analyze_context(text)
        ambiguity = _analyze_ambiguity(text)

        return TranslationResponse(
            raw_text=text,
            detected_language="ja",
            translation=TranslationResult(
                literal=literal_translation,
                natural=natural_translation
            ),
            context=context,
            ambiguity=ambiguity
        )

    except Exception as e:
        # Return empty response on translation failure
        return TranslationResponse(
            raw_text=text,
            detected_language="ja",
            translation=TranslationResult(literal="", natural=""),
            context=ContextInfo(usage="", formality="", cultural_notes=[]),
            ambiguity=AmbiguityInfo(is_ambiguous=False, possible_meanings=[])
        )


def _analyze_context(text: str) -> ContextInfo:
    """
    Basic context analysis for Japanese text.
    TODO: Implement more sophisticated analysis with AI.
    """
    usage = "general"  # Default usage context

    # Simple formality detection based on common polite endings
    polite_markers = ['です', 'ます', 'ございます', 'いたします']
    formal_markers = ['ございます', 'いたします', 'お', 'ご']

    has_polite = any(marker in text for marker in polite_markers)
    has_formal = any(marker in text for marker in formal_markers)

    if has_formal:
        formality = "formal"
    elif has_polite:
        formality = "polite"
    else:
        formality = "casual"

    # No cultural notes for basic implementation
    cultural_notes = []

    return ContextInfo(
        usage=usage,
        formality=formality,
        cultural_notes=cultural_notes
    )


def _analyze_ambiguity(text: str) -> AmbiguityInfo:
    """
    Basic ambiguity analysis.
    TODO: Implement with AI for better detection.
    """
    # For now, assume no ambiguity
    return AmbiguityInfo(
        is_ambiguous=False,
        possible_meanings=[]
    )
