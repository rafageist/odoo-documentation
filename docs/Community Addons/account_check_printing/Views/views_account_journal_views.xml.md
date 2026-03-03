---
tags: [odoo, community, generated, views]
---

# views/account_journal_views.xml

- Module: [[docs/Community Addons/account_check_printing/account_check_printing|account_check_printing]]
- Scope: Community Addons
- Source file: `views/account_journal_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_journal_form_inherited`
- Name: account.journal.form.inherited
- Model: `account.journal`
- Type: inferred from arch
- Inherits: `account.view_account_journal_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `bank_check_printing_layout`, `check_manual_sequencing`, `check_next_number`, `check_sequence_id`
- XPath or positional patches: 1

### `account_journal_dashboard_kanban_view_inherited`
- Name: account.journal.dashboard.kanban.inherited
- Model: `account.journal`
- Type: inferred from arch
- Inherits: `account.account_journal_dashboard_kanban_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/account_check_printing/Views]]

