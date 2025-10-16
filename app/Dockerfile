# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy only what's needed
COPY app.py requirements.txt ./

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt || true

# Default command (CLI app)
CMD ["python", "app.py"]
