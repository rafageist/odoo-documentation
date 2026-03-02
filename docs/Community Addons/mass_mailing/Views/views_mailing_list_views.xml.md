<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mailing_list_views.xml

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `views/mailing_list_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mailing_list_view_kanban`
- Name: mailing.list.view.kanban
- Model: `mailing.list`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `active`, `contact_count`, `contact_count_email`, `contact_pct_blacklisted`, `contact_pct_bounce`, `contact_pct_opt_out`, `mailing_count`, `name`
- Buttons: `action_open_import`, `action_send_mailing`, `action_view_contacts`
- XPath or positional patches: 0

### `mailing_list_view_form_simplified`
- Name: mailing.list.form.simplified
- Model: `mailing.list`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `is_public`, `name`
- XPath or positional patches: 0

### `mailing_list_view_form`
- Name: mailing.list.form
- Model: `mailing.list`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `active`, `contact_count`, `contact_pct_blacklisted`, `contact_pct_bounce`, `contact_pct_opt_out`, `is_public`, `mailing_count`, `name`
- Buttons: `action_open_import`, `action_send_mailing`, `action_view_contacts`, `action_view_contacts_blacklisted`, `action_view_contacts_bouncing`, `action_view_contacts_opt_out`, `action_view_mailings`
- XPath or positional patches: 0

### `mailing_list_view_tree`
- Name: mailing.list.view.list
- Model: `mailing.list`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `contact_count`, `contact_pct_blacklisted`, `contact_pct_bounce`, `contact_pct_opt_out`, `is_public`, `mailing_count`, `name`
- XPath or positional patches: 0

### `mailing_list_view_search`
- Name: mailing.list.view.search
- Model: `mailing.list`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `create_date`, `name`
- XPath or positional patches: 0

## Actions

- `action_view_mass_mailing_lists`: `act_window` Mailing Lists

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Views]]

<!-- GENERATED:VIEWFILE -->
