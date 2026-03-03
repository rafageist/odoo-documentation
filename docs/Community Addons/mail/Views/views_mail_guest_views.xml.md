---
tags: [odoo, community, generated, views]
---

# views/mail_guest_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_guest_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_guest_view_form`
- Name: mail.guest.form
- Model: `mail.guest`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `channel_ids`, `country_id`, `lang`, `name`, `timezone`
- XPath or positional patches: 0

### `mail_guest_view_tree`
- Name: mail.guest.list
- Model: `mail.guest`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `country_id`, `id`, `lang`, `name`, `timezone`
- XPath or positional patches: 0

## Actions

- `mail_guest_action`: `act_window` Guests

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

