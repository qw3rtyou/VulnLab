FROM python:3.10-slim-buster

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=10006

WORKDIR /app
COPY deploy .

RUN apt-get update && apt-get install -y python3-pip wget curl unzip gnupg2

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update -y && apt-get install -y google-chrome-stable
RUN wget https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.91/linux64/chromedriver-linux64.zip -O /tmp/chromedriver.zip && unzip /tmp/chromedriver.zip  -d /usr/local/bin/ && rm /tmp/chromedriver.zip

RUN pip3 install -r requirements.txt

EXPOSE 10006

CMD ["flask", "run"]
