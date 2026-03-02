<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Community Addons/l10n_cl/l10n_cl|l10n_cl]]
- Scope: Community Addons
- Source file: `views/account_move_view.xml`
- Views: 3
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `view_complete_invoice_refund_tree`
- Name: account.move.list2
- Model: `account.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 20
- Sample fields: `amount_residual_signed`, `amount_tax_signed`, `amount_total_signed`, `amount_untaxed_signed`, `company_currency_id`, `company_id`, `currency_id`, `date`, `invoice_date`, `invoice_date_due`, and 10 more
- XPath or positional patches: 0

### `view_latam_form_inherit_l10n_cl`
- Name: account.move.latam.form.inherit.l10n.cl
- Model: `account.move`
- Type: inferred from arch
- Inherits: `l10n_latam_invoice_document.view_move_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `l10n_latam_document_number`
- XPath or positional patches: 0

### `view_move_form_inherit_l10n_cl`
- Name: account.move.form.inherit.l10n.cl
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `form`
- Field references: 1
- Sample fields: `l10n_latam_internal_type`
- XPath or positional patches: 0

## Actions

- `vendor_bills_and_refunds`: `act_window` Vendor Bills and Refunds
- `sale_invoices_credit_notes`: `act_window` Sale Invoices and Credit Notes

## Menus

- `menu_vendor_bills_and_refunds`: Vendor Bills and Refunds (CL)
- `menu_sale_invoices_credit_notes`: Sale Invoices and Credit Notes (CL)

## Navigation

- **Parent:** [[docs/Community Addons/l10n_cl/Views]]

<!-- GENERATED:VIEWFILE -->
