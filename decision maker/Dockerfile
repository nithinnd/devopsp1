# Use lightweight Python
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of your app
COPY . .

# Expose port
EXPOSE 5000

# Run your app
CMD ["python", "app.py"]