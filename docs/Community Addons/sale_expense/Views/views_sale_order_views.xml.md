---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/sale_expense/sale_expense|sale_expense]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `sale_order_form_view_inherit`
- Name: sale.order.form.inherit.sale.expense
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `button`
- Field references: 1
- Sample fields: `expense_count`
- Buttons: `%(sale_expense.hr_expense_action_from_sale_order)d`, `action_view_invoice`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/sale_expense/Views]]

