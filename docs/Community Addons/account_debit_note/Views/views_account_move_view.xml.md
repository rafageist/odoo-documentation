<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Community Addons/account_debit_note/account_debit_note|account_debit_note]]
- Scope: Community Addons
- Source file: `views/account_move_view.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_move_line_filter_debit`
- Name: account.move.line.search.debit
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_account_move_line_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_account_invoice_filter_debit`
- Name: account.invoice.select.debit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_account_move_filter_debit`
- Name: account.move.filter.debit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_move_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_move_form_debit`
- Name: account.move.form.debit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `div`
- Field references: 3
- Sample fields: `debit_note_count`, `debit_origin_id`, `invoice_origin`
- Buttons: `action_debit_note`, `action_reverse`, `action_view_debit_notes`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/account_debit_note/Views]]

<!-- GENERATED:VIEWFILE -->
