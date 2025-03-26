# Base image
FROM python:3.11-slim

# Labels for metadata (opcional)
LABEL maintainer="rabbittrix@hotmail.com"
LABEL description="Docker image for Streamlit Data Deletion Dashboard"

# Install system dependencies and update pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

# Set working directory
WORKDIR /

# Copy all files from the root directory (including train.py)
COPY . /

# Install Python dependencies
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port and run Streamlit
EXPOSE 8501
CMD ["streamlit", "run", "/app/main.py", "--server.address=localhost", "--server.port=8501"]
