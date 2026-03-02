<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_views.xml`
- Views: 7
- Actions: 16
- Menus: 0
- Rules: 0

## View records

### `rental_order_view_search_without_searchpanel`
- Name: rental.order.search.bis
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `rental_order_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `rental_order_view_search`
- Name: rental.order.search
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `invoice_status`, `name`, `order_line`, `partner_id`, `rental_status`, `team_id`, `user_id`
- XPath or positional patches: 0

### `rental_order_view_calendar`
- Name: rental.order.calendar
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sale_order_calendar`
- Root tag: `calendar`
- Field references: 2
- Sample fields: `rental_status`, `state`
- XPath or positional patches: 1

### `rental_order_view_kanban`
- Name: rental.order.kanban
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sale_order_kanban`
- Root tag: `kanban`
- Field references: 7
- Sample fields: `currency_id`, `has_rented_products`, `is_late`, `name`, `next_action_date`, `rental_status`, `state`
- XPath or positional patches: 2

### `rental_order_view_tree`
- Name: rental.order.list
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `amount_total`, `currency_id`, `date_order`, `name`, `next_action_date`, `partner_id`, `rental_status`, `team_id`, `user_id`
- XPath or positional patches: 0

### `rental_order_primary_form_view`
- Name: rental.order.form
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `rental_order_form_view`
- Root tag: `data`
- Field references: 0
- XPath or positional patches: 0

### `rental_order_form_view`
- Name: rental.order.form
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `header`
- Field references: 7
- Sample fields: `duration_days`, `is_rental_order`, `payment_term_id`, `qty_returned`, `remaining_hours`, `rental_return_date`, `rental_start_date`
- Buttons: `action_open_pickup`, `action_open_return`, `action_quotation_send`, `action_update_rental_prices`
- XPath or positional patches: 3

## Actions

- `action_create_rental_order`: `act_window` Create Rental Orders
- `rental_order_today_return_action_view_calendar`: `view`
- `rental_order_today_return_form`: `view`
- `rental_order_today_return_tree`: `view`
- `rental_order_today_return_kanban`: `view`
- `rental_order_today_return_action`: `act_window` Rental Orders
- `rental_order_today_pickup_action_view_calendar`: `view`
- `rental_order_today_pickup_form`: `view`
- `rental_order_today_pickup_tree`: `view`
- `rental_order_today_pickup_kanban`: `view`
- `rental_order_today_pickup_action`: `act_window` Rental Orders
- `rental_order_action_view_calendar`: `view`
- `rental_order_form`: `view`
- `rental_order_tree`: `view`
- `rental_order_kanban`: `view`
- `rental_order_action`: `act_window` Rental Orders

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_renting/Views]]

<!-- GENERATED:VIEWFILE -->
