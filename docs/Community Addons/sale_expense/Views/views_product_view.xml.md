---
tags: [odoo, community, generated, views]
---

# views/product_view.xml

- Module: [[docs/Community Addons/sale_expense/sale_expense|sale_expense]]
- Scope: Community Addons
- Source file: `views/product_view.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_product_view_list_inherit_sale_expense`
- Name: product.product.view.list.inherit.sale.expense
- Model: `product.product`
- Type: inferred from arch
- Inherits: `hr_expense.product_product_expense_categories_tree_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `expense_policy`, `taxes_id`
- XPath or positional patches: 1

### `product_product_view_form_inherit_sale_expense`
- Name: product.template.expense
- Model: `product.product`
- Type: inferred from arch
- Inherits: `hr_expense.product_product_expense_form_view`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `expense_policy`, `expense_policy_tooltip`, `list_price`, `taxes_id`
- XPath or positional patches: 3

## Actions

- `hr_expense.hr_expense_product`: `act_window`

## Navigation

- **Parent:** [[docs/Community Addons/sale_expense/Views]]

