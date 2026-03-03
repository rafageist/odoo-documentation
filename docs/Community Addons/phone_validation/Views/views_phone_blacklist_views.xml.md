---
tags: [odoo, community, generated, views]
---

# views/phone_blacklist_views.xml

- Module: [[docs/Community Addons/phone_validation/phone_validation|phone_validation]]
- Scope: Community Addons
- Source file: `views/phone_blacklist_views.xml`
- Views: 3
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `phone_blacklist_view_search`
- Name: phone.blacklist.view.search
- Model: `phone.blacklist`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `number`
- XPath or positional patches: 0

### `phone_blacklist_view_form`
- Name: phone.blacklist.view.form
- Model: `phone.blacklist`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `number`
- Buttons: `action_add`, `phone_action_blacklist_remove`
- XPath or positional patches: 0

### `phone_blacklist_view_tree`
- Name: phone.blacklist.view.list
- Model: `phone.blacklist`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `create_date`, `number`
- XPath or positional patches: 0

## Actions

- `phone_blacklist_action`: `act_window` Blacklisted Phone Numbers

## Menus

- `phone_blacklist_menu`: Phone Blacklist
- `phone_menu_main`: Phone / SMS

## Navigation

- **Parent:** [[docs/Community Addons/phone_validation/Views]]

