---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/purchase_requisition/purchase_requisition|purchase_requisition]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `supplier_info_form_inherit`
- Name: product.supplierinfo.requisition.view
- Model: `product.supplierinfo`
- Type: inferred from arch
- Inherits: `product.product_supplierinfo_form_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `product_code`, `purchase_requisition_id`
- XPath or positional patches: 0

### `product_supplierinfo_tree_view_inherit`
- Name: product.template.product.form.inherit
- Model: `product.supplierinfo`
- Type: inferred from arch
- Inherits: `product.product_supplierinfo_tree_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `purchase_requisition_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/purchase_requisition/Views]]

