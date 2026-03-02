<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/social_account_views.xml

- Module: [[docs/Enterprise Addons/social/social|social]]
- Scope: Enterprise Addons
- Source file: `views/social_account_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `social_account_view_search`
- Name: social.account.view.search
- Model: `social.account`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `company_id`, `name`
- XPath or positional patches: 0

### `social_account_view_form`
- Name: social.account.view.form
- Model: `social.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `active`, `company_id`, `display_name`, `image`, `media_id`, `name`, `social_account_handle`
- XPath or positional patches: 0

### `social_account_view_list`
- Name: social.account.view.list
- Model: `social.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `create_uid`, `media_id`, `name`, `social_account_handle`
- XPath or positional patches: 0

## Actions

- `action_social_account`: `act_window` Social Accounts

## Menus

- `menu_social_account`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/social/Views]]

<!-- GENERATED:VIEWFILE -->
