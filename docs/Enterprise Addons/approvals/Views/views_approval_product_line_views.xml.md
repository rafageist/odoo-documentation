<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/approval_product_line_views.xml

- Module: [[docs/Enterprise Addons/approvals/approvals|approvals]]
- Scope: Enterprise Addons
- Source file: `views/approval_product_line_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `approval_product_kanban_mobile_view`
- Name: approval.product.kanban.mobile
- Model: `approval.product.line`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `product_id`, `quantity`
- XPath or positional patches: 0

### `approval_product_line_view_form`
- Name: approval.product.line.view.form
- Model: `approval.product.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `company_id`, `description`, `product_id`, `product_uom_id`, `quantity`
- XPath or positional patches: 0

### `approval_product_line_view_tree`
- Name: approval.product.line.view.list
- Model: `approval.product.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `description`, `product_id`, `product_uom_id`, `quantity`
- XPath or positional patches: 0

### `approval_product_line_view_tree_independent`
- Name: approval.product.line.view.list
- Model: `approval.product.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `approval_request_id`, `company_id`, `description`, `product_id`, `product_uom_id`, `quantity`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/approvals/Views]]

<!-- GENERATED:VIEWFILE -->
