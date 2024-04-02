FROM ubuntu:22.04

RUN apt update
RUN apt-get install -y socat

ENV user bof_pie
RUN adduser $user

WORKDIR /home/$user

COPY bof_pie /home/$user/$user
COPY flag /home/$user/flag

RUN chown root:$user /home/$user/flag
RUN chown root:$user /home/$user/$user
RUN chmod 755 /home/$user/flag
RUN chmod 755 /home/$user/$user

USER $user

EXPOSE 10051

CMD ["socat", "TCP-LISTEN:10051,reuseaddr,fork", "EXEC:/home/bof_pie/bof_pie"]