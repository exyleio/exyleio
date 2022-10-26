# Exyle.io API Documentation

## Introduction

This is the documentation for the
[exyleio-api](https://github.com/exyleio/exyleio-api)
repository.

## Setting up

1. [Install rustup](https://www.rust-lang.org/tools/install)

   - make sure you're using the **nightly version** of rust.
     It's a good idea to run this command every once in a while
     to keep the rust toolchain up to date.

   ```
   rustup default nightly
   ```

2. Build / Launch using cargo commands

   ```
   cargo build
   ```

   ```
   cargo run
   ```

## Learning

To contribute to this project, you will need a intermediate knowledge
of web backend technologies such as networking layers and protocols,
API patterns, databases, as well as intermediate level rust skill.

### Rust

[Rust](https://www.rust-lang.org) is a systems programming
language meant to replace C++. You can start learning about it
by reading the [The rust book](https://doc.rust-lang.org/book).

### AWS

[AWS](https://aws.amazon.com) (**A**mazon **W**eb **S**ervice) is a
collection of backend services provided by Amazon. They're the one
providing servers for Exyle.io. We use:

- [Route53](https://aws.amazon.com/route53) for domain management
- [EC2](https://aws.amazon.com/ec2) for master server hosting
- [S3](https://aws.amazon.com/s3) for long-term storage
- [EBS](https://aws.amazon.com/ko/ebs) for fast master server storage
- [GameLift](https://aws.amazon.com/gamelift) for region server

### Redis

[Redis](https://redis.io) is the database used by
Exyle.io to manage sessions and user data. Read their
[Documentations](https://redis.io/docs) to learn more.

### Rocket

[Rocket](https://github.com/SergioBenitez/Rocket) is a web framework
built with the rust programming language. Read their
[Guide](https://rocket.rs/guide) to get started.

### okapi

[okapi](https://github.com/GREsau/okapi) is a documentation generation
tool for rust projects. It works by generating
[OpenAPI](https://spec.openapis.org/oas/v3.0.0) files that can be used by
any number of visualization tools such as
[swagger](https://petstore.swagger.io) or
[scribe](https://demo.scribe.knuckles.wtf).