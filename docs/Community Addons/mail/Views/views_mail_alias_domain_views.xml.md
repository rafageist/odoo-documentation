---
tags: [odoo, community, generated, views]
---

# views/mail_alias_domain_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_alias_domain_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_alias_domain_view_search`
- Name: mail.alias.domain.view.search
- Model: `mail.alias.domain`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `bounce_alias`, `catchall_alias`, `company_ids`, `name`
- XPath or positional patches: 0

### `mail_alias_domain_view_tree`
- Name: mail.alias.domain.view.list
- Model: `mail.alias.domain`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `bounce_alias`, `catchall_alias`, `company_ids`, `default_from`, `name`, `sequence`
- XPath or positional patches: 0

### `mail_alias_domain_view_form`
- Name: mail.alias.domain.view.form
- Model: `mail.alias.domain`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `bounce_alias`, `catchall_alias`, `company_ids`, `default_from`, `name`
- XPath or positional patches: 0

## Actions

- `mail_alias_domain_action`: `act_window` Alias Domains

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

