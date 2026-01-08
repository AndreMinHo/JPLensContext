# JPLENSCONTEXT

## Objective

Create a lightweight application that can recognize and provide a confidence score for Japanese text using **[EasyOCR](https://github.com/JaidedAI/EasyOCR)** and then translate it to English using **[translatepy](https://github.com/Animenosekai/translate)** while also providing AI-generated context and explanation. 

##  Current Features

- ✅ Japanese text recognition (OCR)
- ✅ Confidence scoring for detected text
- ✅ English translation with basic context analysis
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

3. Run translation test:
```bash
python -m tests.test_translation
```

