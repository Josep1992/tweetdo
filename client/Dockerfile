FROM node
WORKDIR /client

# always cache dependencies
COPY package.json .
RUN yarn

ADD . /client

EXPOSE 3000
CMD ["npm", "run", "dev"]