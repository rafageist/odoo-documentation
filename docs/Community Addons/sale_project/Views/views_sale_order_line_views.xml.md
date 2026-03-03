---
tags: [odoo, community, generated, views]
---

# views/sale_order_line_views.xml

- Module: [[docs/Community Addons/sale_project/sale_project|sale_project]]
- Scope: Community Addons
- Source file: `views/sale_order_line_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `sale_order_line_view_form_editable`
- Name: sale.order.line.view.form.editable
- Model: `sale.order.line`
- Type: inferred from arch
- Inherits: `sale.sale_order_line_view_form_readonly`
- Root tag: `form`
- Field references: 1
- Sample fields: `product_id`
- XPath or positional patches: 1

### `view_order_line_tree_with_create`
- Name: sale.order.line.list.with.create
- Model: `sale.order.line`
- Type: inferred from arch
- Inherits: `sale.view_order_line_tree`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/sale_project/Views]]

