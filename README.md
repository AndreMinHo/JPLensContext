# JPLENSCONTEXT

## Objective

A lightweight API service that recognizes Japanese text from images using **[EasyOCR](https://github.com/JaidedAI/EasyOCR)**, translates it to English using **[translatepy](https://github.com/Animenosekai/translate)**, and provides contextual analysis for better understanding.

## Features

- ✅ Japanese text recognition (OCR) from images
- ✅ Confidence scoring for detected text
- ✅ English translation with basic context analysis (formality detection)
- ✅ REST API with FastAPI for easy integration
- ✅ Automatic interactive API documentation

## Quick Start

1. **Set up virtual environment:**
```bash
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. **Start the API server:**
```bash
uvicorn backend.main:app --reload
```

3. **Access the API:**
- **Interactive Documentation:** http://localhost:8000/docs
- **API Base URL:** http://localhost:8000

## API Endpoints

- `GET /health` - Health check
- `POST /translate-image` - Upload image for OCR + translation
- `POST /translate-text` - Direct text translation

## Testing the API

**Run the test suite:**
```bash
python -m tests.test_ocr
python -m tests.test_translation
```

