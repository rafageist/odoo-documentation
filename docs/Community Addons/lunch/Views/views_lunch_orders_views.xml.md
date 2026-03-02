<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/lunch_orders_views.xml

- Module: [[docs/Community Addons/lunch/lunch|lunch]]
- Scope: Community Addons
- Source file: `views/lunch_orders_views.xml`
- Views: 6
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `lunch_order_view_form`
- Name: lunch.order.view.form
- Model: `lunch.order`
- Type: inferred from arch
- Root tag: `form`
- Field references: 24
- Sample fields: `available_today`, `available_toppings_1`, `available_toppings_2`, `available_toppings_3`, `category_id`, `company_id`, `currency_id`, `date`, `image_1920`, `name`, and 14 more
- Buttons: `add_to_cart`
- XPath or positional patches: 0

### `lunch_order_view_graph`
- Name: lunch.order.graph
- Model: `lunch.order`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `product_id`
- XPath or positional patches: 0

### `lunch_order_view_pivot`
- Name: lunch.order.pivot
- Model: `lunch.order`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `date`, `supplier_id`
- XPath or positional patches: 0

### `lunch_order_view_kanban`
- Name: lunch.order.kanban
- Model: `lunch.order`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `currency_id`, `date`, `note`, `notified`, `price`, `product_id`, `state`, `user_id`
- XPath or positional patches: 0

### `lunch_order_view_tree`
- Name: lunch.order.list
- Model: `lunch.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `company_id`, `currency_id`, `date`, `display_reorder_button`, `display_toppings`, `lunch_location_id`, `note`, `notified`, `price`, `product_id`, and 5 more
- Buttons: `action_cancel`, `action_confirm`, `action_confirm_orders`, `action_notify`, `action_reorder`, `action_reset`, `action_send_orders`
- XPath or positional patches: 0

### `lunch_order_view_search`
- Name: lunch.order.search
- Model: `lunch.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `user_id`
- XPath or positional patches: 0

## Actions

- `lunch_order_action_control_suppliers`: `act_window` Control Vendors
- `lunch_order_action_by_supplier`: `act_window` Today's Orders
- `lunch_order_action`: `act_window` My Orders

## Navigation

- **Parent:** [[docs/Community Addons/lunch/Views]]

<!-- GENERATED:VIEWFILE -->
