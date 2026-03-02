<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/pos_order_view.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/pos_order_view.xml`
- Views: 11
- Actions: 8
- Menus: 1
- Rules: 0

## View records

### `pos_rounding_form_view_inherited`
- Name: pos.cash.rounding.form.inherited
- Model: `account.cash.rounding`
- Type: inferred from arch
- Inherits: `account.rounding_form_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_pos_order_filter`
- Name: pos.order.list.select
- Model: `pos.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 9
- Sample fields: `config_id`, `date_order`, `lines`, `name`, `partner_id`, `pos_reference`, `session_id`, `tracking_number`, `user_id`
- XPath or positional patches: 0

### `view_pos_order_tree_all_sales_lines`
- Name: pos.order.line.all.sales.list
- Model: `pos.order.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `create_date`, `currency_id`, `order_id`, `price_unit`, `product_id`, `qty`
- XPath or positional patches: 0

### `view_pos_order_line_form`
- Name: pos.order.line.form
- Model: `pos.order.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `create_date`, `currency_id`, `discount`, `price_unit`, `product_id`, `qty`
- XPath or positional patches: 0

### `view_pos_order_line`
- Name: pos.order.line.list
- Model: `pos.order.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `create_date`, `currency_id`, `discount`, `price_subtotal`, `price_subtotal_incl`, `price_unit`, `product_id`, `qty`
- XPath or positional patches: 0

### `view_pos_order_search`
- Name: pos.order.search.view
- Model: `pos.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `config_id`, `name`
- XPath or positional patches: 0

### `view_pos_order_tree_no_session_id`
- Name: pos.order.tree_no_session_id
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_pos_order_tree`
- Name: pos.order.list
- Model: `pos.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `amount_total`, `config_id`, `currency_id`, `date_order`, `invoice_status`, `is_edited`, `name`, `partner_id`, `pos_reference`, `session_id`, and 3 more
- Buttons: `action_create_invoices`
- XPath or positional patches: 0

### `view_pos_order_pivot`
- Name: pos.order.pivot
- Model: `pos.order`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `amount_total`, `date_order`, `margin`, `margin_percent`
- XPath or positional patches: 0

### `view_pos_order_kanban`
- Name: pos.order.kanban
- Model: `pos.order`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `amount_total`, `currency_id`, `date_order`, `name`, `partner_id`, `pos_reference`, `state`
- XPath or positional patches: 0

### `view_pos_pos_form`
- Name: pos.order.form
- Model: `pos.order`
- Type: inferred from arch
- Root tag: `form`
- Field references: 59
- Sample fields: `amount`, `amount_difference`, `amount_paid`, `amount_tax`, `amount_total`, `card_brand`, `card_no`, `cardholder_name`, `company_id`, `country_code`, and 49 more
- Buttons: `%(action_pos_payment)d`, `action_pos_order_invoice`, `action_send_mail`, `action_stock_picking`, `action_view_invoice`, `action_view_refund_orders`, `action_view_refunded_order`, `refund`
- XPath or positional patches: 0

## Actions

- `model_pos_order_send_mail`: `server` Send Email
- `pos_order_set_cancel`: `server` Cancel Order
- `action_pos_all_sales_lines`: `act_window` All sales lines
- `action_pos_order_line_day`: `act_window` Sale line
- `action_pos_order_line_form`: `act_window` Sale line
- `action_pos_order_line`: `act_window` Sale line
- `action_pos_sale_graph`: `act_window` Orders
- `action_pos_pos_form`: `act_window` Orders

## Menus

- `menu_point_ofsale`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

<!-- GENERATED:VIEWFILE -->
