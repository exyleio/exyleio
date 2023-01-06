// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github")
const darkCodeTheme = require("prism-react-renderer/themes/dracula")

const organizationName = "exyleio"
const projectName = "exyleio"
const iconPath = "img/logos-icons/icon.png"

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Exyle.io",
  tagline: "Documentation and Blog for exyle.io",
  favicon: iconPath,

  // todo: change it to https://docs.exyle.io once the domain has been acquired
  url: "https://exyleio-docs.web.app",
  baseUrl: "/",

  organizationName,
  projectName,

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "throw",

  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  markdown: {
    mermaid: true,
  },
  themes: [
    "@docusaurus/theme-mermaid",
    // https://github.com/easyops-cn/docusaurus-search-local#theme-options
    [
      // @ts-ignore
      require.resolve("@easyops-cn/docusaurus-search-local"),
      /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
      // @ts-ignore
      ({
        hashed: true,
        indexPages: true,
      }),
    ],
  ],

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          editUrl: `https://github.com/${organizationName}/${projectName}/tree/master/`,
        },
        blog: {
          showReadingTime: true,
          editUrl: `https://github.com/${organizationName}/${projectName}/tree/master/`,
        },
        theme: {
          customCss: require.resolve("./src/css/style.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: iconPath,
      navbar: {
        title: "Exyle.io",
        logo: {
          alt: "Exyle.io Logo",
          src: iconPath,
        },
        items: [
          {
            type: "doc",
            docId: "intro",
            position: "left",
            label: "Docs",
          },
          { to: "/blog", label: "Blog", position: "left" },

          {
            position: "right",
            href: `https://github.com/${organizationName}/${projectName}`,
            className: "header-github-icon",
            "aria-label": "GitHub repository",
          },
          {
            position: "right",
            href: "https://discord.gg/synPSeuNFK",
            className: "header-discord-icon",
            "aria-label": "Discord community",
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Links",
            items: [
              {
                label: "ToS",
                to: "/tos",
              },
              {
                label: "EULA",
                to: "/eula",
              },
              {
                label: "Software License",
                to: "https://github.com/exyleio/exyleio/blob/master/LICENSE.md",
              },
            ],
          },
        ],
      },
      colorMode: {
        defaultMode: "dark",
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
      mermaid: {
        theme: { light: "neutral", dark: "dark" },
      },
    }),
}

module.exports = config
