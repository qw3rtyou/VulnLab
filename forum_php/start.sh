#!/bin/bash

docker-compose down

docker-compose build
#docker-compose build --no-cache
docker-compose build --no-cache

docker-compose up -d