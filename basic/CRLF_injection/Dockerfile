FROM python:3.10-slim-buster

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80

WORKDIR /app
COPY deploy .

RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["flask", "run"]