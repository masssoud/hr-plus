FROM node:12.16.2-alpine

EXPOSE 8080
RUN mkdir /code
WORKDIR /code
COPY package*.json /code/
RUN npm install
COPY . /code/