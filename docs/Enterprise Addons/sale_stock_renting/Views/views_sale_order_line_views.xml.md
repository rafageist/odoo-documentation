---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_line_views.xml

- Module: [[docs/Enterprise Addons/sale_stock_renting/sale_stock_renting|sale_stock_renting]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_line_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `sale_order_line_form_lot_allocation`
- Name: sale.order.line.form.lot.allocation
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `name`, `product_id`, `ref`, `reserved_lot_ids`
- Buttons: `action_auto_assign_lots`
- XPath or positional patches: 0

### `sale_order_line_form_schedule`
- Name: sale.order.line.form.schedule.inherit.stock
- Model: `sale.order.line`
- Type: inferred from arch
- Inherits: `sale_renting.sale_order_line_form_schedule`
- Root tag: `field`
- Field references: 4
- Sample fields: `company_id`, `product_id`, `reserved_lot_ids`, `warehouse_id`
- XPath or positional patches: 0

### `sale_order_line_search_schedule`
- Name: sale.order.line.search.schedule.inherit.stock
- Model: `sale.order.line`
- Type: inferred from arch
- Inherits: `sale_renting.sale_order_line_search_schedule`
- Root tag: `field`
- Field references: 2
- Sample fields: `product_id`, `reserved_lot_ids`
- XPath or positional patches: 1

## Actions

- `sale_renting.action_rental_order_schedule`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_stock_renting/Views]]

