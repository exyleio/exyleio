# Overview

## Introduction

This is the documentation for the
[exyleio-api](https://github.com/exyleio/exyleio-api) repository.

## Getting started

1. Clone the repository and open it

   ```
   git clone https://github.com/exyleio/exyleio-api.git
   ```

   ```
   cd exyleio-api
   ```

2. [Setup Docker](/docs/contribution-guides/developers/docker)

3. Create a firebase project if you haven't already,
   [generate](https://console.firebase.google.com/u/0/project/_/settings/serviceaccounts/adminsdk)
   and download a service account key and place it inside the `app` directory
   as `serviceAccountKey,json`. Beware, **THIS FILE MUST REMAIN PRIVATE**.

4. Start a local development server

   - http://127.0.0.1/v1 - API
   - http://127.0.0.1:4000 - Firebase emulation suite
   - http://127.0.0.1/rapidoc - interactive API Documentation
   - http://127.0.0.1:5173 - [website](https://github.com/exyleio/exyleio-web)
     instance

   ```
   ./run.sh
   ```

## Testing

1. Install pytest

   ```
   pip install pytest
   ```

2. Run tests

   ```
   ./test.py
   ```

## How does it work?

### API Endpoint Documentation Generation

To simplify the documentation process, [okapi](https://github.com/GREsau/okapi)
was used to automate the generation of [OpenAPI](https://www.openapis.org)
document. You can check this file at http://127.0.0.1/v1/openapi.json. However, it
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

- [Authentication in Exyle.io](/docs/game-design/authentication)
- [Rocket Framework](https://rocket.rs)
- [Redis Documentation](https://redis.io/docs)
- [Rust By Example](https://doc.rust-lang.org/rust-by-example)
- [The Rust Book](https://doc.rust-lang.org/book)
