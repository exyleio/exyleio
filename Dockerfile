FROM node:hydrogen-alpine
VOLUME /app
WORKDIR /app
ENTRYPOINT ["yarn", "start", "--host", "0.0.0.0"]
