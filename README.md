# JPLENSCONTEXT

## Objective

A lightweight API service that recognizes Japanese text from images using **[manga-ocr](https://github.com/kha-white/manga-ocr)**, translates it to English using **[translatepy](https://github.com/Animenosekai/translate)**.

## Features

- ✅ Japanese text recognition (OCR) from images
- ✅ Confidence scoring for detected text
- ✅ English translation with basic context analysis (formality detection)
- ✅ REST API with FastAPI for easy integration
- ✅ Automatic interactive API documentation

## Quick Start

### Local Development (Python Virtual Environment)

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

### Local Development (Docker)

1. **Build and run with Docker Compose:**
```bash
docker-compose up --build
```

2. **Access the API:**
- **Interactive Documentation:** http://localhost:8000/docs
- **API Base URL:** http://localhost:8000

### Production Deployment (Railway)

#### Docker Deployment
Docker deployment is required for consistent dependency management:

1. **Keep `railway.json`** (forces Docker builder)
2. **Connect your GitHub repository to Railway**
3. **Railway will build and deploy using the optimized Dockerfile**
4. **Railway automatically sets the PORT environment variable**
5. **Deploy!**

**Note:** The startup script (`start.sh`) properly handles Railway's PORT environment variable.

The application will be available at the Railway-provided URL with the same API endpoints.

## API Endpoints

### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "ok"
}
```

### `POST /translate-image`
Upload an image containing Japanese text for OCR and translation.

**Response Example:**
```json
{
  "ocr": {
    "text": "ご飯 定食",
    "confidence": 0.9919165516812564
  },
  "translation": {
    "raw_text": "ご飯 定食",
    "detected_language": "ja",
    "translation": {
      "literal": "rice set meal",
      "natural": "rice set meal"
    },
    "context": {
      "usage": "general",
      "formality": "formal",
      "cultural_notes": []
    },
    "ambiguity": {
      "is_ambiguous": false,
      "possible_meanings": []
    }
  }
}
```

### `POST /translate-text`
Translate Japanese text directly.

**Request Body:**
```json
{
  "text": "こんにちは"
}
```

**Response:** Same structure as translation field above.

### API Documentation
- **Interactive Docs:** `http://localhost:8000/docs`
- **Alternative Docs:** `http://localhost:8000/redoc`

## Testing the API

**Run the test suite:**
```bash
python -m tests.test_ocr
python -m tests.test_translation
```
