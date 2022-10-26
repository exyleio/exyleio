# Infrastructure

![infrastructure plan](../../img/infrastructure.png)

<details>
<summary>Click to see mermaid</summary>

Nah, [this mermaid](https://mermaid-js.github.io) LMAO.

```
flowchart LR
subgraph firebase[Firebase]
web-client[Web Client]
website[Website]
end
web-client --- browser
website --- browser
subgraph discord[Discord]
discord-api[Discord API]
end
discord-api --- discord-bot
discord-api --- desktop
subgraph user[User]
browser[Browser]
desktop[Desktop]
end
user --- nginx-proxy
user --- aws-gamelift-fleet
subgraph aws[AWS]
subgraph aws-gamelift-fleet[AWS GameLift Fleet]
direction LR
region-servers-stable[stable version pool]
region-servers-dev[development version pool]
end
aws-gamelift-fleet --- nginx-proxy
subgraph master-server[Master Server]
discord-bot[Discord Bot]
nginx-proxy[ \n\n\n NGINX \n reverse \n proxy \n\n\n\n]
subgraph exyleio-api[Exyle.io API]
direction LR
exyleio-api-stable[stable version]
exyleio-api-dev[development version]
end
subgraph status-site[Status site]
direction LR
status-site-stable[stable version]
status-site-dev[development version]
end
end
nginx-proxy --- exyleio-api
nginx-proxy --- status-site
subgraph ebs[EBS storage]
redis-db[(Redis DB)]
object-storage[(Amazon S3 bucket)]
end
exyleio-api --- redis-db
exyleio-api --- object-storage
end
```

</details>
