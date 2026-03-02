<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Community Addons/l10n_bg_ledger/l10n_bg_ledger|l10n_bg_ledger]]
- Scope: Community Addons
- Source file: `views/account_move_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_bg_move_view_filter`
- Name: l10n_bg.move.view.filter
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `l10n_bg_move_view_tree`
- Name: l10n_bg.move.view.tree
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `l10n_bg_document_number`, `l10n_bg_document_type`
- XPath or positional patches: 1

### `l10n_bg_move_view_form`
- Name: l10n_bg.move.view.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `l10n_bg_document_number`, `l10n_bg_document_type`, `l10n_bg_exemption_reason`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/l10n_bg_ledger/Views]]

<!-- GENERATED:VIEWFILE -->
