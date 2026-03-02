<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]]
- Scope: Community Addons
- Source file: `views/account_move_view.xml`
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
- Root tag: `form`
- Field references: 6
- Sample fields: `l10n_latam_available_document_type_ids`, `l10n_latam_document_number`, `l10n_latam_document_type_id`, `l10n_latam_manual_document_number`, `l10n_latam_use_documents`, `name`
- XPath or positional patches: 1

### `view_account_move_filter`
- Name: account.move.filter
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_move_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_latam_document_type_id`, `partner_id`
- XPath or positional patches: 0

### `view_account_invoice_filter`
- Name: account.move.select
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_latam_document_type_id`, `partner_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/l10n_latam_invoice_document/Views]]

<!-- GENERATED:VIEWFILE -->
