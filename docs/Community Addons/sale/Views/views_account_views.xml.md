<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `views/account_views.xml`
- Views: 3
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `account_invoice_form`
- Name: Account Invoice
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `campaign_id`, `is_downpayment`, `medium_id`, `sale_order_count`, `sale_warning_text`, `source_id`, `team_id`
- Buttons: `action_view_source_sale_orders`
- XPath or positional patches: 7

### `account_invoice_view_tree`
- Name: account.move.list.inherit.sale
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_invoice_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `invoice_user_id`, `team_id`
- XPath or positional patches: 0

### `account_invoice_groupby_inherit`
- Name: account.move.groupby
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `invoice_user_id`, `team_id`
- XPath or positional patches: 1

## Actions

- `action_invoice_salesteams_view_form`: `view`
- `action_invoice_salesteams_view_tree`: `view`
- `action_invoice_salesteams`: `act_window` Invoices

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

<!-- GENERATED:VIEWFILE -->
