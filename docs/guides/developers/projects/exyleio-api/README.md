# Exyle.io API Documentation

## Introduction

This is the documentation for the
[exyleio-api](https://github.com/exyleio/exyleio-api)
repository.

## Setting up

1. [Install rustup](https://www.rust-lang.org/tools/install)

2. Set the rust toolchain version to nightly

   ```
   rustup default nightly
   ```

3. Run the server

   ```
   cargo run
   ```

4. Build for production

   ```
   cargo build --release
   ```

5. It is also a good idea to keep the rust toolchain up to date
   by using the following command

   ```
   rustup update
   ```

## Learning

To contribute to this project, you will need a intermediate knowledge
of web backend technologies such as the networking layers and their
respective protocols, different API patterns (CRUD, REST, etc),
databases (especially redis DB), as well as some familiarity with the
rust programming language.

### Where to learn

- The rust programming language
  - https://doc.rust-lang.org/book
- Redis database
  - https://redis.io/docs
- Rocket framework
  - https://rocket.rs/guide
- GraphQL API query language
  - https://www.howtographql.com
