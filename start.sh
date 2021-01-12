#!/bin/sh
# start api inside docker container
cd ./api 
docker build -t tweetodo:latest .
docker run -p 5000:5000 tweetodo:latest 