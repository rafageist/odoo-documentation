---
tags: [odoo, community, generated, views]
---

# views/mail_blacklist_views.xml

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `views/mail_blacklist_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mail_blacklist_view_search`
- Name: mail.blacklist.view.search
- Model: `mail.blacklist`
- Type: inferred from arch
- Inherits: `mail.mail_blacklist_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mail_blacklist_view_form`
- Name: mail.blacklist.view.form.inherit.mailing
- Model: `mail.blacklist`
- Type: inferred from arch
- Inherits: `mail.mail_blacklist_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `opt_out_reason_id`
- XPath or positional patches: 1

### `mail_blacklist_view_tree`
- Name: mail.blacklist.view.list.inherit.mailing
- Model: `mail.blacklist`
- Type: inferred from arch
- Inherits: `mail.mail_blacklist_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `opt_out_reason_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Views]]

