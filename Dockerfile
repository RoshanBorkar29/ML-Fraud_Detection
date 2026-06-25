FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Streamlit default port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "fraud_detection.py", "--server.address=0.0.0.0"]