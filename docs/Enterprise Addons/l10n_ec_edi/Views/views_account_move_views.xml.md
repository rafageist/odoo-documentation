<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/l10n_ec_edi/l10n_ec_edi|l10n_ec_edi]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_invoice_tree`
- Name: Add withhold date to invoice.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_ec_withhold_date`
- XPath or positional patches: 1

### `view_move_tree`
- Name: Add withhold date to move general.list
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `date`, `l10n_ec_withhold_date`
- XPath or positional patches: 0

### `account_move_form_invoice_and_withhold_view`
- Name: account.move.form.invoice.and.withhold.view
- Model: `account.move`
- Type: inferred from arch
- Inherits: `l10n_latam_invoice_document.view_move_form`
- Root tag: `button`
- Field references: 33
- Sample fields: `balance`, `document_number`, `invoice_origin`, `l10n_ec_authorization_date`, `l10n_ec_authorization_number`, `l10n_ec_code_taxsupport`, `l10n_ec_dividend_fiscal_year`, `l10n_ec_dividend_income_tax`, `l10n_ec_dividend_payment_date`, `l10n_ec_is_dividend_withhold`, and 23 more
- Buttons: `action_reverse`, `l10n_ec_action_compute_lines_from_reimbursements`, `l10n_ec_action_send_withhold`, `l10n_ec_action_view_invoices`, `l10n_ec_action_view_withholds`, `l10n_ec_add_withhold`
- XPath or positional patches: 7

## Actions

- `action_receive_withhold`: `server` Create Withholds

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ec_edi/Views]]

<!-- GENERATED:VIEWFILE -->
