---
tags: [odoo, community, generated, views]
---

# views/website_rewrite.xml

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Source file: `views/website_rewrite.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_rewrite_search`
- Name: website.rewrite.search
- Model: `website.rewrite`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `url_from`, `url_to`
- XPath or positional patches: 0

### `action_website_rewrite_tree`
- Name: website.rewrite.list
- Model: `website.rewrite`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `active`, `create_date`, `create_uid`, `name`, `redirect_type`, `sequence`, `url_from`, `url_to`, `website_id`, `write_date`, and 1 more
- XPath or positional patches: 0

### `view_website_rewrite_form`
- Name: unnamed
- Model: `website.rewrite`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `active`, `name`, `redirect_type`, `route_id`, `sequence`, `url_from`, `url_to`, `website_id`
- Buttons: `refresh_routes`
- XPath or positional patches: 0

## Actions

- `action_website_rewrite_list`: `act_window` Rewrite

## Menus

- `menu_website_rewrite`: Redirects

## Navigation

- **Parent:** [[docs/Community Addons/website/Views]]

