#!/bin/bash
gcc -o bof_pie bof_PIE.c -fno-stack-protector -mpreferred-stack-boundary=3 #-no-pie -fno-pic
docker-compose down

docker-compose build
docker-compose up -d