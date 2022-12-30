# Overview

## Introduction

This is the documentation for the
[exyleio-web](https://github.com/exyleio/exyleio-web)
repository.

It contains source code for the Exyle.io website (https://exyleio-web.web.app).
The domain will change to https://web.exyle.io in the future.

## Getting started

1. [Setup Docker](/docs/contribution-guides/developers/docker) and install
   [Node.JS](https://nodejs.org)

2. Install yarn CLI

   ```
   npm install --global yarn
   ```

3. Clone the repository and open it

   ```
   git clone https://github.com/exyleio/exyleio-web.git
   ```

   ```
   cd exyleio-web
   ```

4. Install dependencies

   ```
   yarn install
   ```

5. Setup a firebase project at https://console.firebase.google.com

   - Copy `firebaseConfig` you got from the the setup process and paste it in
     [`src/lib/constants.ts`](https://github.com/exyleio/exyleio-web/blob/master/src/lib/constants.ts).
     You can see the code again in the
     [Project settings](https://console.firebase.google.com/project/_/settings/general/web)
     (select your project).

6. Install and setup firebase CLI

   ```
   npm install -g firebase-tools
   ```

   ```
   firebase emulator login
   ```

7. Start a local development server at http://127.0.0.1:5173

   - Start firebase authentication emulator

   ```
   firebase emulators:start --only auth
   ```

   - Start servers

   ```
   docker compose up --build
   ```

## Learning

Minimum required skills to contribute to this project:

- Fundamental web skills
  - JavaScript
  - CSS
  - HTML
- NodeJS
  - yarn CLI
- Typescript
- Svelte
  - SvelteKit
- TailwindCSS

### Learning material

- Fundamentals
  - [MDN (JavaScript, CSS, HTML, Web API, etc)](https://developer.mozilla.org/docs/Web)
- Svelte
  - [Svelte Tutorial](https://svelte.dev/tutorial)
  - [Svelte Documentation](https://svelte.dev/docs)
  - [Learn Svelte (Experimental)](https://learn.svelte.dev)
  - [Svelte Kit Documentation](https://kit.svelte.dev/docs)
- Styling
  - [TailwindCSS](https://tailwindcss.com/docs)
  - [SASS Tutorial](https://sass-lang.com/guide)
- Firebase
  - [Documentation](https://firebase.google.com/docs)
  - [Authentication Documentation](https://firebase.google.com/docs/auth)
- Etc
  - [TypeScript Tutorial](https://www.typescripttutorial.net)
