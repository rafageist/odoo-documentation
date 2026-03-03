---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_view.xml

- Module: [[docs/Enterprise Addons/account_intrastat/account_intrastat|account_intrastat]]
- Scope: Enterprise Addons
- Source file: `views/account_move_view.xml`
- Views: 6
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `account_move_tree_view_account_intrastat_transport_codes`
- Name: account.move.list.account.intrastat.transport.code
- Model: `account.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `amount_total`, `date`, `display_name`, `id`, `intrastat_transport_mode_id`, `partner_id`
- XPath or positional patches: 0

### `account_intrastat_aml_missing_product_tree`
- Name: account.intrastat.aml.missing.product.list
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `move_id`, `name`, `partner_id`, `price_subtotal`
- XPath or positional patches: 0

### `account_move_line_tree_view_account_intrastat_product_origin_country_id`
- Name: account.move.line.list.account.intrastat.product.origin.country.id
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `intrastat_product_origin_country_id`, `move_id`, `partner_id`, `price_subtotal`, `product_id`
- XPath or positional patches: 0

### `account_move_line_tree_view_account_intrastat_transaction_codes`
- Name: account.move.line.list.account.intrastat
- Model: `account.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `date`, `intrastat_transaction_id`, `move_id`, `partner_id`, `price_subtotal`, `product_id`
- XPath or positional patches: 0

### `view_deferred_entries_tree_intrastat`
- Name: account.move.line.deferral.entries.list.intrastat
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account_accountant.view_deferred_entries_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `view_move_line_tree_grouped_inherit_intrastat_fields`
- Name: account.move.line.list.grouped.inherit.intrastat.fields
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `intrastat_product_origin_country_id`, `intrastat_transaction_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_intrastat/Views]]

