# Overview

## Introduction

This is the documentation for the
[exyleio-api](https://github.com/exyleio/exyleio-api) repository.

## Getting started

1. [Setup Docker](/docs/contribution-guides/developers/docker)

2. Clone the repository and open it

   ```
   git clone https://github.com/exyleio/exyleio-api.git
   ```

   ```
   cd exyleio-api
   ```

3. Start a local development server at http://localhost:8000

   ```
   docker compose up --build
   ```

4. Open http://localhost:8000/ping in your browser and see if you get `PONG`

## How does it work?

### API Endpoint Documentation Generation

To simplify the documentation process, [okapi](https://github.com/GREsau/okapi)
was used to automate the generation of [OpenAPI](https://www.openapis.org)
document. You can check this file at http://127.0.0.1/openapi.json. However, it
is much simpler to open http://127.0.0.1/rapidoc and use the interactive
[Rapidoc](https://rapidocweb.com) interface.

### Code Documentation Generation

In the Rust programming language, you can document the project right in the code
using
[Doc Comments](https://doc.rust-lang.org/stable/reference/comments.html#doc-comments).
This allows you to use markdown to write documentations with awesome features
such as links, tables, etc. If you're using vscode, installing the
[Rust Analyzer extension](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer).
will allow you to jump to definitions or get helpful tooltips.

To view the documentation in a more readable form, simply run:

```
cargo doc --open
```

which will open a rendered documentation on your browser.

## Learning

To contribute to this project, you will need:

- a solid web backend fundamentals such as:
  - [OSI model](https://en.wikipedia.org/wiki/OSI_model)
  - [REST](https://en.wikipedia.org/wiki/Representational_state_transfer)
  - [API](https://en.wikipedia.org/wiki/API)
  - etc
- some level of familiarity with databases. Especially with
  [redis](https://redis.io)
- basic Rust programming skill

### Learning material

- [Rocket Framework](https://rocket.rs)
- [Redis Documentation](https://redis.io/docs)
- [Rust By Example](https://doc.rust-lang.org/rust-by-example)
- [The Rust Book](https://doc.rust-lang.org/book)