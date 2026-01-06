# JPLENSCONTEXT

## Objective

Create a lightweight application that can recognize and provide a confidence score for Japanese text using **[EasyOCR](https://github.com/JaidedAI/EasyOCR)** and then translate it to English while also providing AI-generated context and explanation. 

##  Current Features

- ✅ Japanese text recognition (OCR)
- ✅ Confidence scoring for detected text
- 🚧 Translation (in progress)
- 🚧 AI-generated context explanations (planned)
- 🚧 Camera-based input & frontend UI (planned)

## Usage

1. Set up virtual environment:
```bash
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run OCR test:
```bash
python -m tests.test_ocr
```

