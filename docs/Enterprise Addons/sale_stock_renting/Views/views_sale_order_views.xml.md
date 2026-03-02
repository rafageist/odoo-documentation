<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Enterprise Addons/sale_stock_renting/sale_stock_renting|sale_stock_renting]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `rental_order_form_view_inherit_stock`
- Name: rental.order.form.inherit.stock
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_renting.rental_order_primary_form_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `available_reserved_lots`, `reserved_lot_ids`
- XPath or positional patches: 1

### `view_order_form`
- Name: rental.order.form.stock
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_renting.rental_order_form_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

## Actions

- `sale_renting.rental_product_template_action`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_stock_renting/Views]]

<!-- GENERATED:VIEWFILE -->
