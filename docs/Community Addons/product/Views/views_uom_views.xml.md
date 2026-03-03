---
tags: [odoo, community, generated, views]
---

# views/uom_views.xml

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Source file: `views/uom_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `uom_uom_form_view_inherit`
- Name: uom.uom.form.inherit
- Model: `uom.uom`
- Type: inferred from arch
- Inherits: `uom.product_uom_form_view`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_open_packaging_barcodes`
- XPath or positional patches: 1

### `product_uom_list_view`
- Name: product.uom.list
- Model: `product.uom`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `barcode`, `product_id`, `uom_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/product/Views]]

