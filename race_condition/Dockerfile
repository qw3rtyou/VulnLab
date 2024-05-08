# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app
COPY ./server /app
RUN pip install --no-cache-dir flask
EXPOSE 8000

CMD ["python", "./app.py"]
