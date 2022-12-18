# Overview

## Introduction

This is the documentation for the
[exyleio-api](https://github.com/exyleio/exyleio-api) repository.

## Getting started

1. Install docker and docker compose
2. Clone the repository
   ```
   git clone https://github.com/exyleio/exyleio-api.git
   ```
3. Start a test server locally
   ```
   docker compose up
   ```
4. Open the server in your browser and test it by sending a query. URL will be
   provided as you start the server.
   ```graphql
   query {
     ping
   }
   ```

## Learning

To contribute to this project, you will need:

- a solid understanding of web backend fundamentals such as the OSI model
- some level of familiarity with databases. Especially [redis](https://redis.io)
- intermediate level Javascript/Typescript programming skill

### Learning material

- Fundamentals
  - [GraphQL Tutorial](https://www.howtographql.com)
  - [Redis Documentation](https://redis.io/docs)
- Libraries
  - [GraphQL Yoga server](https://the-guild.dev/graphql/yoga-server)
  - [node-redis](https://github.com/redis/node-redis)
