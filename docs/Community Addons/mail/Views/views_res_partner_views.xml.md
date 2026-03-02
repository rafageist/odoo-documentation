<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 5
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `res_partner_view_activity`
- Name: res.partner.activity
- Model: `res.partner`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `id`, `name`, `parent_id`
- XPath or positional patches: 0

### `res_partner_view_tree_inherit_mail`
- Name: res.partner.view.list.inherit.mail
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `activity_ids`
- XPath or positional patches: 1

### `res_partner_view_search_inherit_mail`
- Name: res.partner.view.search.inherit.mail
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_res_partner_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `res_partner_view_kanban_inherit_mail`
- Name: res.partner.view.kanban.inherit.mail
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.res_partner_kanban_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `activity_ids`
- XPath or positional patches: 1

### `res_partner_view_form_inherit_mail`
- Name: res.partner.view.form.inherit.mail
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `is_blacklisted`
- Buttons: `mail_action_blacklist_remove`
- XPath or positional patches: 2

## Actions

- `action_partner_mass_mail`: `act_window` Send email
- `base.action_partner_supplier_form`: `act_window`
- `base.action_partner_customer_form`: `act_window`
- `base.action_partner_form`: `act_window`

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

<!-- GENERATED:VIEWFILE -->
