FROM node:18.0-alpine3.14

EXPOSE 3000

WORKDIR /client

COPY /src/Business_Assistant_Client/ ./
CMD npm install && npm start