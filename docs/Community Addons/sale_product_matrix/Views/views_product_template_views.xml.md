---
tags: [odoo, community, generated, views]
---

# views/product_template_views.xml

- Module: [[docs/Community Addons/sale_product_matrix/sale_product_matrix|sale_product_matrix]]
- Scope: Community Addons
- Source file: `views/product_template_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_template_view_form`
- Name: product.template.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `sale.product_template_view_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `optional_product_ids`, `product_add_mode`
- XPath or positional patches: 0

### `product_template_grid_view_form`
- Name: product.template.form.inherit.sale.product.matrix
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_only_form_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `has_configurable_attributes`, `product_add_mode`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/sale_product_matrix/Views]]

