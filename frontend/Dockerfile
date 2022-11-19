#
FROM node:latest

#
WORKDIR /code

#
COPY ./app /code/app

#
WORKDIR /code/app

#
RUN npm install

#
CMD ["npm", "run", "dev"]
