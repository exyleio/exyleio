# Exyleio-Web Documentation

## Introduction

This is the documentation for the
[exyleio/exyleio-web](https://github.com/exyleio/exyleio-web)
repository.

## Setting up

1. Install [Node.js](https://nodejs.org) (v16) and
   [yarn](https://yarnpkg.com)
2. Install dependencies
   ```
   yarn install
   ```
3. Start a local server
   ```
   yarn start
   ```

## Learning

To contribute to this project, you will need a strong knowledge of
web frontend technologies, namely JavaScript, TypeScript, CSS, HTML,
JSX, and TSX. As well as a bit of networking/browser fundamentals such
as the HTTP protocol, localStorage API, and polyfills.

### SolidJS

[SolidJS](https://www.solidjs.com) is a framework extremely similar
to [ReactJS](https://reactjs.org), the most widely used web frontend
framework in the world.

- [Tutorial](https://www.solidjs.com/tutorial)
- [Guides](https://www.solidjs.com/guides)
- [Examples](https://www.solidjs.com/examples/counter)
- [API Reference](https://www.solidjs.com/docs/latest)
- [new documentation (WIP)](https://docs.solidjs.com)
  - contains everything mentioned above but is still incomplete

### Vite

[Vite](https://github.com/vitejs/vite) is a tool used to locally
serve a test version and to create optimized build for production.
Though it is rare that you will ever have to touch vite config
files, it is helpful to know what we're using when we're trying to
track down and squash bugs.

### Styling

#### Styled-components

[styled components](https://github.com/styled-components/styled-components)
is a library used to integrate css stylesheets directly in the
javascript files. SolidJS uses its own version which you can
learn more about it in their
[GitHub repository](https://github.com/solidjs/solid-styled-components).

#### Tailwind

We use [TailwindCSS](https://github.com/tailwindlabs/tailwindcss) to create
a consistent look throughout our websites and to reduce CSS length.
