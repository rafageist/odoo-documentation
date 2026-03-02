<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/pos_order_views.xml

- Module: [[docs/Enterprise Addons/pos_settle_due/pos_settle_due|pos_settle_due]]
- Scope: Enterprise Addons
- Source file: `views/pos_order_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `pos_order_form_inherit_pos_settle_due`
- Name: pos.order.form.inherit
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_pos_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `settled_orders_count`
- Buttons: `action_view_settled_orders`
- XPath or positional patches: 1

### `customer_due_pos_order_list_view`
- Name: pos.order.list
- Model: `pos.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `amount_total`, `currency_id`, `customer_due_total`, `date_order`, `name`, `pos_reference`, `session_id`, `state`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_settle_due/Views]]

<!-- GENERATED:VIEWFILE -->
