#!/bin/bash
# Railway startup script
export DISABLE_MODEL_SOURCE_CHECK=True
PORT=${PORT:-8000}
exec uvicorn backend.main:app --host 0.0.0.0 --port $PORT
