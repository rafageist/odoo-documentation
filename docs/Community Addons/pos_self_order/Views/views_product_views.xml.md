<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/pos_self_order/pos_self_order|pos_self_order]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_template_tree_view`
- Name: product.template.product.list.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `point_of_sale.product_template_tree_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `available_in_pos`, `self_order_available`
- XPath or positional patches: 0

### `product_template_form_view`
- Name: product.template.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `group`
- Field references: 1
- Sample fields: `self_order_available`
- XPath or positional patches: 1

### `product_template_search_view_pos`
- Name: product.template.search.pos.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `point_of_sale.product_template_search_view_pos`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/pos_self_order/Views]]

<!-- GENERATED:VIEWFILE -->
