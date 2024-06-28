FROM python:3.8-slim

RUN apt-get update -y
RUN apt-get install -y wget unzip chromium-driver
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY app /app
COPY flag.txt /app/flag.txt
WORKDIR /app

RUN pip3 install flask selenium

EXPOSE 8000