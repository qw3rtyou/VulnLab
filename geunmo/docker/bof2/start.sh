#!/bin/bash
gcc -o bof2 bof2.c -fno-stack-protector -no-pie -fno-pic -mpreferred-stack-boundary=4
docker-compose down

docker-compose build
docker-compose up -d