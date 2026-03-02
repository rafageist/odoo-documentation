<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_sales_order_filter_subscription`
- Name: sale.order.filter.subscription
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sales_order_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_order_tree`
- Name: sale.order.list
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_tree`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `sale_order_tree`
- Name: sale.order.tree
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.sale_order_tree`
- Root tag: `field`
- Field references: 5
- Sample fields: `plan_id`, `recurring_monthly`, `recurring_total`, `state`, `subscription_state`
- XPath or positional patches: 0

### `sale_subscription_order_view_form`
- Name: sale.subscription.order.form
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_management.sale_order_form_quote`
- Root tag: `sheet`
- Field references: 23
- Sample fields: `close_reason_id`, `currency_id`, `end_date`, `first_contract_date`, `history_count`, `internal_note_display`, `next_invoice_date`, `origin_order_id`, `payment_exception`, `payment_token_id`, and 13 more
- Buttons: `%(sale.action_view_sale_advance_payment_inv)d`, `%(sale_subscription.sale_subscription_close_reason_wizard_action)d`, `action_cancel`, `action_sale_order_log`, `action_unlock`, `create_alternative`, `open_subscription_history`, `open_subscription_renewal`, `open_subscription_upsell`, `prepare_renewal_order`, and 3 more
- XPath or positional patches: 15

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

<!-- GENERATED:VIEWFILE -->
