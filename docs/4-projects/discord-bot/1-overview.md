# Overview

## Introduction

This is the documentation for the
[exyleio-discord-bot](https://github.com/exyleio/exyleio-discord-bot)
repository.

## Getting started

1. Clone the repository and open it

   ```
   git clone https://github.com/exyleio/exyleio-discord-bot.git
   ```

   ```
   cd exyleio-discord-bot
   ```

2. [Setup Docker](/docs/contribution-guides/developers/docker) and install
   [Node.JS](https://nodejs.org) 16.6.0+

3. [Create a discord bot](https://discordjs.guide/preparations/setting-up-a-bot-application.html).
   You must also enable all Privileged Gateway Intents.

   ![](/img/privileged-gateway-intents.png)

4. Create `.env` file

   ```dosini
   DISCORD_BOT_TOKEN=<DISCORD_BOT_TOKEN>
   DISCORD_BOT_ID=<DISCORD_BOT_ID>
   ```

5. Start the bot

   ```
   ./run.sh
   ```

## Learning

Minimum required skills to contribute to this project:

- NodeJS
- npm CLI
- JavaScript
- Typescript
- discord.js

### Learning material

- [Discord developers documentation](https://discord.com/developers/docs)
- [Discord.js Guide](https://discordjs.guide)
- [Sapphire framework Documentation](https://sapphirejs.dev/docs/General/Welcome)
- [TypeScript Tutorial](https://www.typescripttutorial.net)
