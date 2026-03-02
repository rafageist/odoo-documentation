<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_it_edi_doi/l10n_it_edi_doi|l10n_it_edi_doi]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_form`
- Name: account.move.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `div`
- Field references: 3
- Sample fields: `l10n_it_edi_doi_id`, `l10n_it_edi_doi_use`, `l10n_it_edi_doi_warning`
- Buttons: `action_open_declaration_of_intent`
- XPath or positional patches: 3

### `view_move_tree`
- Name: account.move.list
- Model: `account.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `currency_id`, `date`, `invoice_date`, `invoice_partner_display_name`, `l10n_it_edi_doi_amount`, `made_sequence_gap`, `name`, `state`
- XPath or positional patches: 0

### `view_account_invoice_filter`
- Name: account.invoice.select
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_it_edi_doi_id`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/l10n_it_edi_doi/Views]]

<!-- GENERATED:VIEWFILE -->
