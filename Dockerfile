FROM python:3.10-slim

WORKDIR /app

COPY backend /app/backend
COPY frontend_live /app/frontend
COPY .env.example /app/.env

RUN pip install flask requests python-dotenv

EXPOSE 8080

CMD ["python3", "backend/app.py"]