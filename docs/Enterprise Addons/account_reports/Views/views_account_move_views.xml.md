<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 6
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_draft_entries_tree`
- Name: account.invoice.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_journal_report_audit_move_line_search`
- Name: account.journal.report.audit.move.line.search
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_account_move_line_filter`
- Root tag: `filter`
- Field references: 2
- Sample fields: `exclude_bank_lines`, `journal_id`
- XPath or positional patches: 3

### `view_journal_report_audit_bank_move_line_tree`
- Name: account.journal.report.audit.bank.move.line.tree
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account_reports.view_journal_report_audit_move_line_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `date`, `invoice_date`, `matching_number`, `partner_id`
- XPath or positional patches: 0

### `view_journal_report_audit_move_line_tree`
- Name: account.journal.report.audit.move.line.list
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `field`
- Field references: 7
- Sample fields: `account_id`, `date`, `invoice_date`, `matching_number`, `move_name`, `partner_id`, `tax_ids`
- Buttons: `button_set_checked`, `edit`, `open_partner`
- XPath or positional patches: 2

### `view_archived_tag_move_tree`
- Name: account.archived.tax.tag.list
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `view_move_form_vat_return`
- Name: account.move.form.vat.return
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_open_tax_return`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Views]]

<!-- GENERATED:VIEWFILE -->
