from fastapi import FastAPI, UploadFile, File, HTTPException, Body
from fastapi.responses import JSONResponse
import tempfile
import os
from typing import Dict, Any
from pydantic import BaseModel

class TextTranslationRequest(BaseModel):
    text: str

from backend.ocr.reader import read_text
from backend.translation.translator import translate_text

app = FastAPI(title="JP Lens Context API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/translate-image")
async def translate_image(file: UploadFile = File(...)) -> Dict[str, Any]:
    """
    Upload an image, perform OCR, and translate the detected Japanese text.

    Returns combined OCR and translation results.
    """
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")

    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            temp_file.write(await file.read())
            temp_file_path = temp_file.name

        try:
            # Perform OCR
            ocr_text, confidence = read_text(temp_file_path)

            # Perform translation
            translation_result = translate_text(ocr_text)

            # Return combined result
            return {
                "ocr": {
                    "text": ocr_text,
                    "confidence": confidence
                },
                "translation": translation_result.dict()
            }

        finally:
            # Clean up temporary file
            os.unlink(temp_file_path)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")


@app.post("/translate-text")
async def translate_text_endpoint(request: TextTranslationRequest) -> Dict[str, Any]:
    """
    Translate Japanese text directly.

    Args:
        request: TextTranslationRequest containing the text to translate

    Returns:
        Translation result with context analysis
    """
    try:
        result = translate_text(request.text)
        return result.dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")
