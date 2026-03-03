---
tags: [odoo, community, generated, views]
---

# views/pos_order_view.xml

- Module: [[docs/Community Addons/pos_hr/pos_hr|pos_hr]]
- Scope: Community Addons
- Source file: `views/pos_order_view.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_pos_order_tree_inherit`
- Name: pos.order.list.inherit
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_id`
- XPath or positional patches: 1

### `pos_order_list_select_inherit`
- Name: pos.order.list.select.inherit
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `cashier`
- XPath or positional patches: 2

### `pos_order_form_inherit`
- Name: pos.order.form.inherit
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_pos_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `employee_id`, `user_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/pos_hr/Views]]

