# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app
# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (default 8000, can be overridden)
EXPOSE 8003

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8003

# Run the application (use PORT env var if set, otherwise default to 8000)
CMD sh -c "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8003}"