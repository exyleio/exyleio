# Overview

## Introduction

This is the documentation for the
[exyleio-scripts](https://github.com/exyleio/exyleio-scripts)
repository.

It is used to deploy and manage Exyle.io related services.

## Getting started

### Master server

1. [Setup Docker](/docs/contribution-guides/developers/docker)

2. Clone the repository and open it

   ```
   git clone https://github.com/exyleio/exyleio-scripts.git
   ```

   ```
   cd exyleio-scripts
   ```

3. Navigate to the `master-server` directory

   ```
   cd master-server
   ```

4. Create `.env` file

   - Check [Discord Bot Setup Guide](/docs/projects/discord-bot/overview#getting-started) for
     more information.

   ```dosini
   DISCORD_BOT_TOKEN=<DISCORD_BOT_TOKEN>
   DISCORD_BOT_ID=<DISCORD_BOT_ID>
   ```

5. Create a firebase project if you haven't already,
   [generate](https://console.firebase.google.com/u/0/project/_/settings/serviceaccounts/adminsdk)
   and download a service account key as `serviceAccountKey,json`.
   Beware, **THIS FILE MUST REMAIN PRIVATE**.

6. Start a local development server at http://localhost (same as
   http://localhost:80)

## Learning

Minimum required skills to contribute to this project:

- GitHub action
- Docker
- Nginx
