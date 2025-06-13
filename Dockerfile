FROM python:3.10-slim

WORKDIR /app

COPY backend /app/backend
COPY frontend_live /app/frontend_live
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE