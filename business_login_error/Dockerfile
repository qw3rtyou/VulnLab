FROM python:3.7
WORKDIR /app
COPY deploy /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
