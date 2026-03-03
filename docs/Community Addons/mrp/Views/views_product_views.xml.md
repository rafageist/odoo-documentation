---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 6
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `product_product_form_view_bom_button`
- Name: product.product.procurement
- Model: `product.product`
- Type: inferred from arch
- Inherits: `stock.product_form_view_procurement_button`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `bom_count`, `mrp_product_qty`, `uom_name`, `used_in_bom_count`
- Buttons: `action_used_in_bom`, `action_view_bom`, `action_view_mos`
- XPath or positional patches: 1

### `product_template_form_view_bom_button`
- Name: product.template.procurement
- Model: `product.template`
- Type: inferred from arch
- Inherits: `stock.product_template_form_view_procurement_button`
- Root tag: `button`
- Field references: 4
- Sample fields: `bom_count`, `mrp_product_qty`, `uom_name`, `used_in_bom_count`
- Buttons: `%(template_open_bom)d`, `action_open_documents`, `action_used_in_bom`, `action_view_mos`
- XPath or positional patches: 0

### `product_view_search_catalog`
- Name: product.view.search.catalog.inherit.mrp
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_view_search_catalog`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `mrp_product_product_search_view`
- Name: mrp.product.product.search
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_search_form_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `mrp_product_template_search_view`
- Name: mrp.product.template.search
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_mrp_product_template_form_inherited`
- Name: product.form.mrp.inherited
- Model: `product.template`
- Type: inferred from arch
- Inherits: `stock.view_template_property_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `is_kits`
- XPath or positional patches: 1

## Actions

- `mrp_product_variant_action`: `act_window` Product Variants
- `product_template_action`: `act_window` Products

## Menus

- `product_variant_mrp`: Product Variants
- `menu_mrp_product_form`: Products

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

