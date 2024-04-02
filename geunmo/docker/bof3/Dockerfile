FROM ubuntu:22.04

RUN apt update
RUN apt-get install -y socat
RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y libc6:i386

ENV user bof3
RUN adduser $user

WORKDIR /home/$user

COPY bof3 /home/$user/$user
COPY flag /home/$user/flag

RUN chown root:$user /home/$user/flag
RUN chown root:$user /home/$user/$user
RUN chmod 755 /home/$user/flag
RUN chmod 755 /home/$user/$user

USER $user

EXPOSE 10054

CMD ["socat", "TCP-LISTEN:10054,reuseaddr,fork", "EXEC:/home/bof3/bof3"]