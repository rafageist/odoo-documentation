---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_line_views.xml

- Module: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_line_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `sale_order_line_gantt_schedule`
- Name: sale.order.line.gantt.schedule
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 4
- Sample fields: `is_late`, `order_id`, `rental_status`, `state`
- XPath or positional patches: 0

### `sale_order_line_form_schedule`
- Name: sale.order.line.form.schedule
- Model: `sale.order.line`
- Type: inferred from arch
- Inherits: `sale.sale_order_line_view_form_readonly`
- Root tag: `div`
- Field references: 5
- Sample fields: `name`, `order_id`, `rental_status`, `return_date`, `start_date`
- XPath or positional patches: 2

### `sale_order_line_search_schedule`
- Name: sale.order.line.search.schedule
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `company_id`, `order_partner_id`, `product_id`, `salesman_id`, `start_date`
- XPath or positional patches: 0

## Actions

- `action_rental_order_schedule`: `act_window` Scheduled Rentals

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_renting/Views]]

