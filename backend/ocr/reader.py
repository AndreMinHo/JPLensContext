from typing import Tuple
from google.cloud import vision
from google.oauth2 import service_account
import os
import json
from PIL import Image
import io


def _get_vision_client():
    """Get Google Vision API client with authentication."""
    # Try to get credentials from environment
    credentials_value = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    if not credentials_value:
        # Use default credentials (for environments with Application Default Credentials)
        return vision.ImageAnnotatorClient()

    # Check if it's a file path
    if os.path.exists(credentials_value):
        credentials = service_account.Credentials.from_service_account_file(credentials_value)
        return vision.ImageAnnotatorClient(credentials=credentials)

    # Check if it's JSON content (starts with '{')
    if credentials_value.strip().startswith('{'):
        try:
            credentials_info = json.loads(credentials_value)
            credentials = service_account.Credentials.from_service_account_info(credentials_info)
            return vision.ImageAnnotatorClient(credentials=credentials)
        except json.JSONDecodeError:
            raise Exception(f"Invalid JSON in GOOGLE_APPLICATION_CREDENTIALS: {credentials_value[:100]}...")

    # If neither file nor JSON, try default credentials
    return vision.ImageAnnotatorClient()


def read_text(image_path: str) -> Tuple[str, float]:
    """
    Extract text from image using Google Cloud Vision API.

    Args:
        image_path: Path to the image file

    Returns:
        Tuple of (extracted_text, average_confidence)
    """

    client = _get_vision_client()

    # Load and prepare image
    with Image.open(image_path) as img:
        img = img.convert("RGB")

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_bytes = img_byte_arr.getvalue()

    # Create Vision API image object
    image = vision.Image(content=img_bytes)

    # Configure text detection request with Japanese language hint
    image_context = vision.ImageContext(
        language_hints=['ja-JP', 'en']
    )

    # Perform text detection
    response = client.text_detection(
        image=image,
        image_context=image_context
    )

    # Check for errors
    if response.error.message:
        raise Exception(f"Vision API error: {response.error.message}")

    # Extract text and confidence
    texts = response.text_annotations

    if not texts:
        return "", 0.0

    # The first text annotation contains all the detected text
    full_text = texts[0].description.strip()

    # Calculate average confidence from individual text blocks
    if len(texts) > 1:
        confidences = []
        for text_annotation in texts[1:]:  # Skip first annotation (full text)
            if hasattr(text_annotation, 'confidence') and text_annotation.confidence > 0:
                confidences.append(text_annotation.confidence)

        avg_confidence = sum(confidences) / len(confidences) if confidences else 0.8
    else:
        avg_confidence = 0.8  # Default confidence when we can't determine individual text confidence

    return full_text, avg_confidence
