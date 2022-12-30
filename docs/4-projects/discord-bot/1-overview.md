# Overview

## Introduction

This is the documentation for the
[exyleio-discord-bot](https://github.com/exyleio/exyleio-discord-bot)
repository.

## Getting started

1. [Setup Docker](/docs/contribution-guides/developers/docker) and install
   [Node.JS](https://nodejs.org)

2. Clone the repository and open it

   ```
   git clone https://github.com/exyleio/exyleio-discord-bot.git
   ```

   ```
   cd exyleio-discord-bot
   ```

3. [Create a discord bot](https://discordjs.guide/preparations/setting-up-a-bot-application.html).
   You must also enable all Privileged Gateway Intents.

4. Create `.env` file

   ```dosini
   DISCORD_BOT_TOKEN=<DISCORD_BOT_TOKEN>
   DISCORD_BOT_ID=<DISCORD_BOT_ID>
   ```

5. Install dependencies

   ```
   npm install
   ```

6. Run the bot

   ```
   docker compose up --build
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
- [TypeScript Tutorial](https://www.typescripttutorial.net)
