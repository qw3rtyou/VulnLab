# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app
COPY ./deploy /app
RUN mkdir -p /app/uploads
RUN pip install --no-cache-dir flask
RUN chmod 111 ./flag
EXPOSE 8000

CMD ["python", "./app.py"]
