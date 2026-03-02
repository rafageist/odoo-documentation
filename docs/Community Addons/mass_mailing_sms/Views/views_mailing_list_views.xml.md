<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mailing_list_views.xml

- Module: [[docs/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]]
- Scope: Community Addons
- Source file: `views/mailing_list_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mailing_list_view_form`
- Name: mailing.list.view.form.inherit.sms
- Model: `mailing.list`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_list_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_send_mailing_sms`
- XPath or positional patches: 1

### `mailing_list_view_kanban`
- Name: mailing.list.view.kanban.inherit.mass.mailing.sms
- Model: `mailing.list`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_list_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `contact_count_sms`
- XPath or positional patches: 1

## Actions

- `mailing_list_action_sms`: `act_window` Mailing Lists

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_sms/Views]]

<!-- GENERATED:VIEWFILE -->
