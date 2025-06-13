FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy backend and frontend
COPY backend /app/backend
COPY frontend_live /app/frontend
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port used by Flask
EXPOSE 8080

# Run the Flask app
CMD ["python3", "backend/app.py"]