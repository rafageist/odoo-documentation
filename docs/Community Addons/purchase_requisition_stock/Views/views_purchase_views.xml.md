<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/purchase_views.xml

- Module: [[docs/Community Addons/purchase_requisition_stock/purchase_requisition_stock|purchase_requisition_stock]]
- Scope: Community Addons
- Source file: `views/purchase_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `purchase_order_line_compare_tree_inherit_purchase_requisition_stock`
- Name: purchase.order.line.compare.list.purchase.requisition.stock
- Model: `purchase.order.line`
- Type: inferred from arch
- Inherits: `purchase_requisition.purchase_order_line_compare_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `on_time_rate_perc`, `partner_id`
- XPath or positional patches: 0

### `purchase_order_form_inherit_purchase_requisition_stock`
- Name: purchase.order.form.inherit.purchase.requisition.stock
- Model: `purchase.order`
- Type: inferred from arch
- Inherits: `purchase_requisition.purchase_order_form_inherit`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `on_time_rate_perc`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/purchase_requisition_stock/Views]]

<!-- GENERATED:VIEWFILE -->
