#!/bin/bash
#gcc -o bof_cnry bof_cnry.c -no-pie -fno-pic #-mpreferred-stack-boundary=4 #-fno-stack-protector
gcc -fstack-protector -z execstack -no-pie -fno-pie -mpreferred-stack-boundary=4 -o bof_cnry bof_cnry.c
docker-compose down

docker-compose build
docker-compose up -d
