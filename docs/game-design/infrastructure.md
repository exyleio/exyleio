# Infrastructure

## Introduction

The Exyle.io online infrastructure is a complex intertwined
collection of programs and services that powers the entire
game by connecting users with each other and managing their data.
On the surface, this looks simple enough, but there are many technical
challenges people are not usually aware of such as seamlessly scaling
the servers up and down depending on the load, protecting the servers
from hackers, managing backups and recovering from one when needed,
making the services crash-tolerant, efficiently organizing all the user
data, and of course, balancing everything for the minimum operation cost.
And that's just the tip of the iceberg.

In this document, we'll go over the surface level information about
the entire system with the goal of having a better understanding of how
things fit with each other.

Below is a simplified diagram of the said system.

![infrastructure plan](../../img/infrastructure.png)

<details>
<summary>Click to see mermaid</summary>

Nah, [this mermaid](https://mermaid-js.github.io) LMAO.

```
flowchart LR
    subgraph firebase[Firebase]
        direction LR
        web-client["Web Client\n(exyle.io)"]
        website["Website\n(web.exyle.io)"]
        status-site["Status site\n(web.exyle.io)"]
    end
    firebase --- browser

    subgraph discord[Discord]
        discord-api[Discord API]
    end
    discord-api --- discord-bot
    discord-api --- desktop-client

    subgraph user[User]
        browser[Web Browser]
        desktop-client[Desktop Client]
    end
    user --- nginx-proxy
    user --- aws-gamelift-fleet

    subgraph aws[AWS]
        classDef aws_padding fill:none,stroke:none
        subgraph aws_padding [ ]
            subgraph aws-gamelift-fleet[AWS GameLift Fleet]
                direction LR
                region-servers-stable[stable version pool]
                region-servers-dev[development version pool]
            end
            aws-gamelift-fleet --- nginx-proxy

            subgraph master-server[Master Server]
                discord-bot[Discord Bot]
                nginx-proxy[ \n\n\n NGINX \n reverse \n proxy \n\n\n\n]

                subgraph api[Exyle.io API]
                    direction LR
                    api-stable[stable version]
                    api-dev[development version]
                end

                subgraph data[Data]
                    direction LR
                    redis-db[(Redis Database)]
                    long-term-storage[(Long-term Storage)]
                end
            end
            nginx-proxy --- api
            api --- data
        end
        class aws_padding aws_padding
    end
```

</details>

## Discord

- TODO

## Firebase

- TODO

## User

- TODO

## AWS

- TODO

## GameLift fleet

- TODO

## Master server

- TODO

## Nginx

- TODO

## API

The Exyle.io API is an [GraphQL](https://graphql.org)-based interface
between the data and the users. It acts as a middleman that safely
reads from and writes to the database so no one can view or modify the
it without authorization.

## Redis Database

- TODO

## Long-term storage

- TODO
