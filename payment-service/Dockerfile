# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy app code
COPY payment-app ./payment-app 

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "payment-app.main:app", "--host", "0.0.0.0", "--port", "8000"]
