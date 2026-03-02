<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mail_canned_response_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_canned_response_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_canned_response_view_kanban`
- Name: mail.canned.response.kanban
- Model: `mail.canned.response`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `group_ids`, `source`, `substitution`
- XPath or positional patches: 0

### `mail_canned_response_view_form`
- Name: mail.canned.response.form
- Model: `mail.canned.response`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `group_ids`, `is_editable`, `source`, `substitution`
- XPath or positional patches: 0

### `mail_canned_response_view_tree`
- Name: mail.canned.response.list
- Model: `mail.canned.response`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `create_uid`, `group_ids`, `is_editable`, `is_shared`, `last_used`, `source`, `substitution`
- XPath or positional patches: 0

### `mail_canned_response_view_search`
- Name: mail.canned.response.view.search
- Model: `mail.canned.response`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `source`, `substitution`
- XPath or positional patches: 0

## Actions

- `mail_canned_response_action`: `act_window` Canned Responses

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

<!-- GENERATED:VIEWFILE -->
