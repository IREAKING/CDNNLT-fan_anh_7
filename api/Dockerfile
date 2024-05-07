FROM python:3.9-slim-bullseye

RUN pip install fastapi uvicorn sqlalchemy pymysql

COPY ./app /app


WORKDIR /app


CMD ["bash", "-c", "sleep 120 && uvicorn main:app --reload --host 0.0.0.0 --port 8000"]

