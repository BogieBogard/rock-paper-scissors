FROM python:3.7-alpine

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn

EXPOSE 8000

CMD ["uvicorn", "simple:app", "--host", "0.0.0.0", "--port", "8000"]