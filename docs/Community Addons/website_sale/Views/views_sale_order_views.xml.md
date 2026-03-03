---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 5
- Actions: 5
- Menus: 0
- Rules: 0

## View records

### `sale_order_tree`
- Name: sale.order.list.inherit.website.sale
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.sale_order_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `user_id`, `website_id`
- XPath or positional patches: 0

### `sale_order_view_form`
- Name: sale.order.form
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `button`
- Field references: 3
- Sample fields: `partner_id`, `team_id`, `website_id`
- Buttons: `action_quotation_send`, `action_recovery_email_send`
- XPath or positional patches: 0

### `view_sales_order_filter_ecommerce_abondand`
- Name: sale.order.ecommerce.abandonned.view
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_sales_order_filter_ecommerce_unpaid`
- Name: sale.order.ecommerce.search.unpaid.view
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sales_order_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

### `view_sales_order_filter_ecommerce`
- Name: sale.order.ecommerce.search.view
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sales_order_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `action_view_abandoned_tree`: `act_window` Abandoned Carts
- `action_view_unpaid_quotation_tree`: `act_window` Unpaid Orders
- `sale_order_action_to_invoice`: `act_window` Orders To Invoice
- `action_unpaid_orders_ecommerce`: `act_window` Unpaid Orders
- `action_orders_ecommerce`: `act_window` Orders

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

