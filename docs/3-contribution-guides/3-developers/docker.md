# Docker

## Why use docker?

[Docker](https://docker.com) simplifies the creation and management of
containerized environments. This allows you to download and set up any Exyle.io
project within a minute without having to install and configure different
dependencies. Simply execute the `./run.sh` script which contains the commands
that does all the magic for you, and you will have a piece of the Exyle.io
infrastructure running right inside your computer.

To get started, read
"[Getting Started Guide](https://docs.docker.com/get-started)" from the Docker
documentation or watch
"[Docker Beginner Tutorial](https://www.youtube.com/watch?v=gAkwW2tuIqE)" on
YouTube.

## Useful commands

- Start a container to interact with in the background.

  - In the case of the
    Exyle.io documentation's
    [docker-compose.yml](https://github.com/exyleio/exyleio/blob/master/docker-compose.yml),
    you can replace `<CONTAINER_NAME>` with `docs`.

  - Must run before running `docker compose exec ...`

    ```
    docker compose run --no-deps --detach <CONTAINER_NAME>
    ```

- Run arbitrary command in a container

  - Replace `<YOUR_COMMAND_HERE>` with `sh` for a terminal, `yarn build` to build, etc.

    ```
    docker compose exec -t <CONTAINER_NAME> <YOUR_COMMAND_HERE>
    ```
