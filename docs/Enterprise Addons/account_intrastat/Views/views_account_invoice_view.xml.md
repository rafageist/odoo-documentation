---
tags: [odoo, enterprise, generated, views]
---

# views/account_invoice_view.xml

- Module: [[docs/Enterprise Addons/account_intrastat/account_intrastat|account_intrastat]]
- Scope: Enterprise Addons
- Source file: `views/account_invoice_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `invoice_line_be_intrastat_data_form`
- Name: account.move.form.inherit.account.be.intrastat
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `intrastat_product_origin_country_id`
- XPath or positional patches: 1

### `invoice_form_inherit_account_intrastat`
- Name: account.move.form.inherit.account.intrastat
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `intrastat_country_id`, `intrastat_transaction_id`, `intrastat_transport_mode_id`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_intrastat/Views]]

