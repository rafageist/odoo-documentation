---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/mrp_account/mrp_account|mrp_account]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `product_variant_easy_edit_view_bom_inherit`
- Name: product.product.product.view.form.easy.bom.inherit
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_variant_easy_edit_view`
- Root tag: `data`
- Field references: 3
- Sample fields: `bom_count`, `cost_method`, `valuation`
- Buttons: `button_bom_cost`
- XPath or positional patches: 1

### `product_product_view_form_normal_inherit_extended`
- Name: product.product.view.form.normal.inherit.extended
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `bom_count`, `cost_method`, `valuation`
- Buttons: `button_bom_cost`
- XPath or positional patches: 1

### `product_product_ext_form_view2`
- Name: product_extended.product.form.view
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_only_form_view`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `bom_count`, `cost_method`, `valuation`
- Buttons: `button_bom_cost`
- XPath or positional patches: 1

## Actions

- `action_compute_price_bom_product`: `server` Compute Price from BoM
- `action_compute_price_bom_template`: `server` Compute Price from BoM

## Navigation

- **Parent:** [[docs/Community Addons/mrp_account/Views]]

