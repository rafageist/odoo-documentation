<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mailing_contact_views.xml

- Module: [[docs/Community Addons/mass_mailing_sms/mass_mailing_sms|mass_mailing_sms]]
- Scope: Community Addons
- Source file: `views/mailing_contact_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mailing_contact_view_kanban`
- Name: mailing.contact.view.kanban.inherit.sms
- Model: `mailing.contact`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_contact_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `mobile`
- XPath or positional patches: 1

### `mailing_contact_view_form`
- Name: mailing.contact.view.form.inherit.sms
- Model: `mailing.contact`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_contact_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `mobile`, `phone_sanitized`
- Buttons: `phone_action_blacklist_remove`
- XPath or positional patches: 1

### `mailing_contact_view_tree`
- Name: mailing.contact.view.list.inherit.sms
- Model: `mailing.contact`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_contact_view_tree`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `mobile`, `phone_sanitized`, `phone_sanitized_blacklisted`
- XPath or positional patches: 1

### `mailing_contact_view_search`
- Name: mailing.contact.view.search.inherit.sms
- Model: `mailing.contact`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_contact_view_search`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `mobile`, `phone_sanitized`
- XPath or positional patches: 4

## Actions

- `mailing_contact_action_sms`: `act_window` Mailing List Contacts

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_sms/Views]]

<!-- GENERATED:VIEWFILE -->
