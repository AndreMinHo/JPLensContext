from backend.ocr.reader import read_text

print("Starting OCR test...")

text, confidence = read_text("tests/sample_jp.png")

print("=== OCR RESULT ===")
print("TEXT:", repr(text))
print("CONFIDENCE:", confidence)
