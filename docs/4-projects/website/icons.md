# Icons

The Exyle.io website uses the [Iconify](https://icon-sets.iconify.design)
library to put icons in the website. Although they provide many different icon
sets, we're only using Font Awesome icons (unless inevitable) for consistency.

You can add icons by first importing iconify svelte component:

```ts
import Icon from "@iconify/svelte"
```

then putting it in the markup section with the icon id
(e.g. `fa6-brands:github`):

```html
<Icon icon="<icon-id>" />
```

You can search for icon ids in the iconify website.
