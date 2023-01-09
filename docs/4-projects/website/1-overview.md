# Overview

## Introduction

This is the documentation for the
[exyleio-web](https://github.com/exyleio/exyleio-web)
repository.

It contains source code for the Exyle.io website (https://exyleio-web.web.app).
The domain will change to https://web.exyle.io in the future.

## Getting started

1. Clone the repository and open it

   ```
   git clone https://github.com/exyleio/exyleio-web.git
   ```

   ```
   cd exyleio-web
   ```

2. [Setup Docker](/docs/contribution-guides/developers/docker) and install
   [Node.JS](https://nodejs.org)

3. Create a firebase project if you haven't already.

   - Copy `firebaseConfig` you got from the the setup process and paste it in
     [`src/lib/constants.ts`](https://github.com/exyleio/exyleio-web/blob/master/src/lib/constants.ts).
     You can see the code again in the
     [Project settings](https://console.firebase.google.com/project/_/settings/general/web)
     (select your project).

   - [generate](https://console.firebase.google.com/u/0/project/_/settings/serviceaccounts/adminsdk)
     and download a service account key as `serviceAccountKey,json`.
     Beware, **THIS FILE MUST REMAIN PRIVATE**.

4. Create `.env` file

   - set `PUBLIC_USE_PRODUCTION_API` to `false` if you want to use your own API
     server hosted locally.

   ```dosini
   PUBLIC_USE_PRODUCTION_API=true
   ```

5. Start a local development server

   - http://127.0.0.1:5173 - Website
   - http://127.0.0.1:4000 - Firebase Emulator Suite

   ```
   ./run.sh
   ```

## Learning

Minimum required skills to contribute to this project:

- Fundamental web skills
  - JavaScript
  - CSS
  - HTML
- NodeJS
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
- UI Framework
  - [Flowbite Documentation](https://flowbite.com/docs)
  - [Flowbite-Svelte](https://flowbite-svelte.com)
- Styling
  - [TailwindCSS](https://tailwindcss.com/docs)
  - [SASS Tutorial](https://sass-lang.com/guide)
- Firebase
  - [Documentation](https://firebase.google.com/docs)
  - [Authentication Documentation](https://firebase.google.com/docs/auth)
  - [Authentication in Exyle.io](/docs/game-design/authentication)
- Etc
  - [TypeScript Tutorial](https://www.typescripttutorial.net)
