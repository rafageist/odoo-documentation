<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/auth_oauth_views.xml

- Module: [[docs/Community Addons/auth_oauth/auth_oauth|auth_oauth]]
- Scope: Community Addons
- Source file: `views/auth_oauth_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_oauth_provider_tree`
- Name: auth.oauth.provider.list
- Model: `auth.oauth.provider`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `client_id`, `enabled`, `name`, `sequence`
- XPath or positional patches: 0

### `view_oauth_provider_form`
- Name: auth.oauth.provider.form
- Model: `auth.oauth.provider`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `auth_endpoint`, `body`, `client_id`, `css_class`, `data_endpoint`, `enabled`, `name`, `scope`, `validation_endpoint`
- XPath or positional patches: 0

## Actions

- `action_oauth_provider`: `act_window` Providers

## Menus

- `menu_oauth_providers`: OAuth Providers

## Navigation

- **Parent:** [[docs/Community Addons/auth_oauth/Views]]

<!-- GENERATED:VIEWFILE -->
