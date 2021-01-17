#!/bin/sh

docker build -t api ./api
docker build -t client ./client
docker build -t nginx ./client

docker compose up

# docker run --rm -p 5000:5000 tweetodo:api 