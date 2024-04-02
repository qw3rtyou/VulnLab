FROM ubuntu:22.04

RUN apt update
RUN apt-get install -y socat

ENV user bof1
RUN adduser $user

WORKDIR /home/$user

COPY bof1 /home/$user/$user
COPY flag /home/$user/flag

RUN chown root:$user /home/$user/flag
RUN chown root:$user /home/$user/$user
RUN chmod 755 /home/$user/flag
RUN chmod 755 /home/$user/$user

USER $user

EXPOSE 10050

CMD ["socat", "TCP-LISTEN:10050,reuseaddr,fork", "EXEC:/home/bof1/bof1"]