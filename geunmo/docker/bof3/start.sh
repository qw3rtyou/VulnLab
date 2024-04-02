#!/bin/bash
gcc -o bof3 bof3.c -z execstack -fno-stack-protector -no-pie -fno-pic -m32 -mpreferred-stack-boundary=2
docker-compose down

docker-compose build
docker-compose up -d