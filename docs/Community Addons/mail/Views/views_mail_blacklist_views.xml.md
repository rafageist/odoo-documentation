---
tags: [odoo, community, generated, views]
---

# views/mail_blacklist_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_blacklist_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_blacklist_view_search`
- Name: mail.blacklist.view.search
- Model: `mail.blacklist`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `email`
- XPath or positional patches: 0

### `mail_blacklist_view_form`
- Name: mail.blacklist.view.form
- Model: `mail.blacklist`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `email`
- Buttons: `action_add`, `mail_action_blacklist_remove`
- XPath or positional patches: 0

### `mail_blacklist_view_tree`
- Name: mail.blacklist.view.list
- Model: `mail.blacklist`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `create_date`, `email`
- XPath or positional patches: 0

## Actions

- `mail_blacklist_action`: `act_window` Blacklisted Email Addresses

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

