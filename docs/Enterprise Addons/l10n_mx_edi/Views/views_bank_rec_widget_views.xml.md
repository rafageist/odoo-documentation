<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/bank_rec_widget_views.xml

- Module: [[docs/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]]
- Scope: Enterprise Addons
- Source file: `views/bank_rec_widget_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_accountant_view_bank_statement_line_form_bank_rec_widget_inherit_l10n_mx_edi`
- Name: account.accountant.view.bank.statement.line.form.bank.rec.widget.inherit.l10n.mx.edi
- Model: `account.bank.statement.line`
- Type: inferred from arch
- Inherits: `account_accountant.view_bank_statement_line_form_bank_rec_widget`
- Root tag: `field`
- Field references: 3
- Sample fields: `country_code`, `journal_id`, `l10n_mx_edi_payment_method_id`
- XPath or positional patches: 0

### `view_bank_statement_line_tree_bank_rec_widget_inherit_l10n_mx_edi`
- Name: account.bank.statement.line.list.bank_rec_widget.inherit.l10n.mx.edi
- Model: `account.bank.statement.line`
- Type: inferred from arch
- Inherits: `account_accountant.view_bank_statement_line_tree_bank_rec_widget`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_mx_edi_payment_method_id`, `statement_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi/Views]]

<!-- GENERATED:VIEWFILE -->
