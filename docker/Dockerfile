# Multi-stage build for production
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.11-slim

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Copy application code (backend directory contents to /app)
COPY backend/ ./

# Copy docker scripts to a location that won't be overwritten by volume mounts
RUN mkdir -p /docker-scripts
COPY docker/scripts/entrypoint.sh /docker-scripts/entrypoint.sh
COPY docker/scripts/wait_for_db.sh /docker-scripts/wait_for_db.sh

# Make sure scripts are executable
RUN chmod +x /docker-scripts/*.sh

# Add local bin to PATH
ENV PATH=/root/.local/bin:$PATH

# Working directory is /app (contains backend code)
# No need to change since we copied backend/ to ./

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Use entrypoint script (in /docker-scripts to avoid volume mount conflicts)
ENTRYPOINT ["/docker-scripts/entrypoint.sh"]

# Default command
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
