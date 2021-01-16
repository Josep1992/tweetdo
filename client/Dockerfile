FROM node
WORKDIR /client

# always cache dependencies
COPY package.json .
RUN yarn

COPY . /client

EXPOSE 3000
CMD ["yarn","dev"]