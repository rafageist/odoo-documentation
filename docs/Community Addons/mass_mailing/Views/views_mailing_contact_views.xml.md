---
tags: [odoo, community, generated, views]
---

# views/mailing_contact_views.xml

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `views/mailing_contact_views.xml`
- Views: 8
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mailing_contact_view_form_split_name`
- Name: mailing.contact.view.form.split.name
- Model: `mailing.contact`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_contact_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `first_name`, `last_name`
- XPath or positional patches: 4

### `mailing_contact_view_tree_split_name`
- Name: mailing.contact.view.list.split.name
- Model: `mailing.contact`
- Type: inferred from arch
- Inherits: `mass_mailing.mailing_contact_view_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `first_name`, `last_name`
- XPath or positional patches: 1

### `mailing_contact_view_graph`
- Name: mailing.contact.view.graph
- Model: `mailing.contact`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `create_date`
- XPath or positional patches: 0

### `mailing_contact_view_pivot`
- Name: mailing.contact.pivot
- Model: `mailing.contact`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 1
- Sample fields: `create_date`
- XPath or positional patches: 0

### `mailing_contact_view_form`
- Name: mailing.contact.view.form
- Model: `mailing.contact`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `company_name`, `country_id`, `create_date`, `email`, `id`, `is_blacklisted`, `list_id`, `message_bounce`, `name`, `opt_out`, and 5 more
- Buttons: `mail_action_blacklist_remove`
- XPath or positional patches: 0

### `mailing_contact_view_kanban`
- Name: mailing.contact.view.kanban
- Model: `mailing.contact`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `company_name`, `email`, `message_bounce`, `name`, `properties`, `tag_ids`
- Buttons: `action_import`
- XPath or positional patches: 0

### `mailing_contact_view_tree`
- Name: mailing.contact.view.list
- Model: `mailing.contact`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `company_name`, `country_id`, `create_date`, `email`, `is_blacklisted`, `list_ids`, `message_bounce`, `name`, `opt_out`, `properties`
- Buttons: `action_add_to_mailing_list`, `action_import`
- XPath or positional patches: 0

### `mailing_contact_view_search`
- Name: mailing.contact.view.search
- Model: `mailing.contact`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `list_ids`, `name`, `properties`, `tag_ids`
- XPath or positional patches: 0

## Actions

- `action_view_mass_mailing_contacts`: `act_window` Mailing List Contacts

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Views]]

