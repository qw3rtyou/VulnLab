#!/bin/bash

docker build -t change-header .
docker run -d -p 10001:5000 change-header
