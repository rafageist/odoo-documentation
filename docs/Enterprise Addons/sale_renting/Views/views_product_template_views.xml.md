<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/product_template_views.xml

- Module: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]]
- Scope: Enterprise Addons
- Source file: `views/product_template_views.xml`
- Views: 5
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `product_template_kanban_view`
- Name: product.template.product.kanban.inherit.rental
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_kanban_view`
- Root tag: `field`
- Field references: 4
- Sample fields: `activity_state`, `display_price`, `list_price`, `product_pricing_ids`
- XPath or positional patches: 0

### `rental_product_template_search_view`
- Name: product.template.search.inherit.rental
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `product_template_tree_view`
- Name: product.template.product.list.inherit.rental
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_tree_view`
- Root tag: `field`
- Field references: 3
- Sample fields: `display_price`, `list_price`, `standard_price`
- XPath or positional patches: 0

### `product_template_form_view_rental_gantt`
- Name: product.template.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `sale.product_template_form_view_sale_order_button`
- Root tag: `button`
- Field references: 2
- Sample fields: `qty_in_rent`, `uom_name`
- Buttons: `action_view_rentals`, `action_view_sales`
- XPath or positional patches: 0

### `product_template_form_view_rental`
- Name: product.template.form.inherit.rental
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `page`
- Field references: 9
- Sample fields: `currency_id`, `extra_daily`, `extra_hourly`, `price`, `pricelist_id`, `product_pricing_ids`, `product_variant_ids`, `recurrence_id`, `rent_ok`
- XPath or positional patches: 3

## Actions

- `rental_product_template_tree`: `view`
- `rental_product_template_kanban`: `view`
- `rental_product_template_action`: `act_window` Products

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_renting/Views]]

<!-- GENERATED:VIEWFILE -->
