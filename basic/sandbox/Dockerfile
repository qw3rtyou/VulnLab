FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y vim sudo man-db gcc net-tools build-essential netcat python3 tree ssh
RUN yes | unminimize

RUN useradd -ms /bin/bash guest
RUN echo 'guest:password' | chpasswd
RUN usermod -a -G sudo guest

USER guest
WORKDIR /home/guest