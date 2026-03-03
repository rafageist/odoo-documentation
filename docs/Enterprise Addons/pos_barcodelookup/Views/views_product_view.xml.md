---
tags: [odoo, enterprise, generated, views]
---

# views/product_view.xml

- Module: [[docs/Enterprise Addons/pos_barcodelookup/pos_barcodelookup|pos_barcodelookup]]
- Scope: Enterprise Addons
- Source file: `views/product_view.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `product_template_view_form_normalized_pos_barcodelookup`
- Name: product.template.view.form.normalized
- Model: `product.template`
- Type: inferred from arch
- Inherits: `point_of_sale.product_template_view_form_normalized_pos`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `product_product_view_form_normalized_pos_barcodelookup`
- Name: product.product.view.form.normalized.pos.barcodelookup.inherit
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_product_view_form_normalized`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `point_of_sale.product_template_action_edit_pos`: `act_window`
- `point_of_sale.product_template_action_add_pos`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_barcodelookup/Views]]

