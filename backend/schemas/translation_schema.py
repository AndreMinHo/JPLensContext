from pydantic import BaseModel
from typing import List


class TranslationResult(BaseModel):
    literal: str
    natural: str


class ContextInfo(BaseModel):
    usage: str
    formality: str
    cultural_notes: List[str]


class AmbiguityInfo(BaseModel):
    is_ambiguous: bool
    possible_meanings: List[str]


class TranslationResponse(BaseModel):
    raw_text: str
    detected_language: str
    translation: TranslationResult
    context: ContextInfo
    ambiguity: AmbiguityInfo
