FROM python:3.10-slim

WORKDIR /app

COPY backend /app/backend
COPY frontend_live /app/frontend
COPY config.env /app/.env

RUN pip install flask requests python-dotenv

EXPOSE 8000

CMD ["python3", "backend/app.py"]