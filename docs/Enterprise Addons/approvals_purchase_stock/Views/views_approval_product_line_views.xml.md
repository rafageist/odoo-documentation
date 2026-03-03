---
tags: [odoo, enterprise, generated, views]
---

# views/approval_product_line_views.xml

- Module: [[docs/Enterprise Addons/approvals_purchase_stock/approvals_purchase_stock|approvals_purchase_stock]]
- Scope: Enterprise Addons
- Source file: `views/approval_product_line_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `approval_purchase_stock_product_line_view_form_inherit`
- Name: approval.purchase.stock.product.line.view.form.inherit
- Model: `approval.product.line`
- Type: inferred from arch
- Inherits: `approvals.approval_product_line_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `warehouse_id`
- XPath or positional patches: 1

### `approval_purchase_stock_product_line_view_tree_inherit`
- Name: approval.purchase.stock.product.line.view.list.inherit
- Model: `approval.product.line`
- Type: inferred from arch
- Inherits: `approvals.approval_product_line_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `warehouse_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/approvals_purchase_stock/Views]]

