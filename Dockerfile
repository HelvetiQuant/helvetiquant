# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY backend /app/backend
COPY frontend_live /app/frontend_live

RUN pip install flask

EXPOSE 8000

CMD ["python", "backend/app.py"]