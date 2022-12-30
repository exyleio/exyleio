FROM node:hydrogen-alpine
VOLUME /app
WORKDIR /app
CMD ["yarn", "start", "--host", "0.0.0.0"]
