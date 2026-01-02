from fastapi import FastAPI

app = FastAPI(title="JP Context Translator")


@app.get("/health")
def health_check():
    return {"status": "ok"}
