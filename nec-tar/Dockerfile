FROM python:3

RUN apt-get update
RUN apt-get upgrade -y
RUN pip3 install flask

WORKDIR /app
COPY deploy .
COPY flag.txt /flag.txt
RUN mkdir -p /uploads/
RUN mv /flag.txt /flag_$(cat /dev/urandom | tr -dc a-f0-9 | fold -w32 | head -n1)

RUN chmod -R 755 /uploads

CMD ["python3", "/app/server.py"]
EXPOSE 80
