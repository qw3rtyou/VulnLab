FROM ubuntu:22.04@sha256:bcc511d82482900604524a8e8d64bf4c53b2461868dac55f4d04d660e61983cb

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y > /dev/null
RUN apt-get install xinetd python3 -y > /dev/null

RUN useradd -ms /bin/bash pickle
WORKDIR /home/pickle

COPY ./myPickle.py /home/pickle/myPickle.py
COPY ./flag.py /home/pickle/flag.py
COPY ./run.sh /home/pickle/run.sh
COPY ./start.sh /start.sh

RUN chmod -R 750 /home/pickle
RUN chmod +x /start.sh

RUN chown -R root:pickle /home/pickle
RUN echo "service pickle\n{\n\tdisable = no\n\tflags = REUSE\n\tsocket_type = stream\n\tprotocol = tcp\n\tuser = pickle\n\twait = no\n\tserver = /home/pickle/run.sh\n\ttype = UNLISTED\n\tport = 13000\n}" \
        > /etc/xinetd.d/pickle
