#!/bin/sh

cd ./api 
docker build -t tweetodo:api .
cd ..
cd client 
docker build -t tweetodo:client .
cd ..
cd nginx 
docker build -t tweetodo:nginx .

# docker run --rm -p 5000:5000 tweetodo:api 