<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_journal_dashboard_view.xml

- Module: [[docs/Enterprise Addons/l10n_in_reports/l10n_in_reports|l10n_in_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_journal_dashboard_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_journal_form_inherit_l10n_in_enet_batch_payment`
- Name: view.account.journal.form.inherit.l10n.in.enet.batch.payment
- Model: `account.journal`
- Type: inferred from arch
- Inherits: `account.view_account_journal_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `bank_template_id`
- XPath or positional patches: 1

### `account_journal_dashboard_kanban_view_inherit_gstr`
- Name: account.journal.dashboard.kanban
- Model: `account.journal`
- Type: inferred from arch
- Inherits: `account.account_journal_dashboard_kanban_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `country_code`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_reports/Views]]

<!-- GENERATED:VIEWFILE -->
