<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mail_alias_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_alias_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_alias_view_search`
- Name: mail.alias.view.search
- Model: `mail.alias`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `alias_domain_id`, `alias_force_thread_id`, `alias_model_id`, `alias_name`, `alias_parent_model_id`, `alias_parent_thread_id`, `create_uid`
- XPath or positional patches: 0

### `mail_alias_view_tree`
- Name: mail.alias.view.list
- Model: `mail.alias`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `alias_contact`, `alias_defaults`, `alias_domain_id`, `alias_force_thread_id`, `alias_incoming_local`, `alias_model_id`, `alias_name`, `alias_parent_model_id`, `alias_parent_thread_id`, `alias_status`
- Buttons: `open_document`, `open_parent_document`
- XPath or positional patches: 0

### `mail_alias_view_form`
- Name: mail.alias.view.form
- Model: `mail.alias`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `alias_bounced_content`, `alias_contact`, `alias_defaults`, `alias_domain_id`, `alias_force_thread_id`, `alias_incoming_local`, `alias_model_id`, `alias_name`, `alias_parent_model_id`, `alias_parent_thread_id`, and 1 more
- Buttons: `open_document`, `open_parent_document`
- XPath or positional patches: 0

## Actions

- `mail_alias_action`: `act_window` Aliases

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

<!-- GENERATED:VIEWFILE -->
