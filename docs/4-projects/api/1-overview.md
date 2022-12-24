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
   docker compose up --build
   ```
4. Open http://127.0.0.1:8000/ping in the browser and see if you get `PONG`

## How does it work?

### execution

When you run `docker compose up`, it launches three things in the background:

- port `6379` - the redis database
- port `80` - the pocketbase authentication backend
- port `8000` - and the API itself

The API depends on both the pocketbase and the redis database to work properly.

### Documentation generation

To simplify the documentation process, [okapi](https://github.com/GREsau/okapi)
was used to automate the generation of [OpenAPI](https://www.openapis.org)
document. You can check this file at http://127.0.0.1/openapi.json. However, it
is much simpler to open http://127.0.0.1/rapidoc and use the interactive
[Rapidoc](https://rapidocweb.com) interface.

## Learning

To contribute to this project, you will need:

- a solid web backend fundamentals such as:
  - [OSI model](https://en.wikipedia.org/wiki/OSI_model)
  - [REST](https://en.wikipedia.org/wiki/Representational_state_transfer)
  - [API](https://en.wikipedia.org/wiki/API)
  - etc
- some level of familiarity with databases. Especially with
  [redis](https://redis.io)
- intermediate level Javascript/Typescript programming skill

### Learning material

- [Rocket Framework](https://rocket.rs)
- [Redis Documentation](https://redis.io/docs)
- [Rust By Example](https://doc.rust-lang.org/rust-by-example)
- [The Rust Book](https://doc.rust-lang.org/book)
