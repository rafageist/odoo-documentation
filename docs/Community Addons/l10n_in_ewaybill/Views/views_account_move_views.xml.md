<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_in_ewaybill/l10n_in_ewaybill|l10n_in_ewaybill]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_invoice_list_inherit_l10n_in_ewaybill`
- Name: account.move.list.inherit.l10n.in.ewaybill
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_in_ewaybill_name`
- XPath or positional patches: 1

### `invoice_form_inherit_l10n_in_ewaybill`
- Name: account.move.form.inherit.l10n.in.ewaybill
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_l10n_in_ewaybill_create`, `action_open_l10n_in_ewaybill`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/l10n_in_ewaybill/Views]]

<!-- GENERATED:VIEWFILE -->
