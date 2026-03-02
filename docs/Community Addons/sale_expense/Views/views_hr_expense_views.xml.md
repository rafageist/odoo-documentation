<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_expense_views.xml

- Module: [[docs/Community Addons/sale_expense/sale_expense|sale_expense]]
- Scope: Community Addons
- Source file: `views/hr_expense_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_expense_split_view_inherit_sale_expense`
- Name: hr.expense.split.view.inherit.sale.expense
- Model: `hr.expense.split.wizard`
- Type: inferred from arch
- Inherits: `hr_expense.hr_expense_split`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `can_be_reinvoiced`, `sale_order_id`
- XPath or positional patches: 1

### `hr_expense_tree_view_inherit_sale_expense`
- Name: hr.expense.list.inherit.sale.expense
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense.view_expenses_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `can_be_reinvoiced`, `sale_order_id`
- XPath or positional patches: 1

### `hr_expense_form_view_inherit_sale_expense`
- Name: hr.expense.form.inherit.sale.expense
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense.hr_expense_view_form`
- Root tag: `button`
- Field references: 2
- Sample fields: `can_be_reinvoiced`, `sale_order_id`
- Buttons: `action_open_account_move`, `action_open_sale_order`
- XPath or positional patches: 1

## Actions

- `hr_expense_action_from_sale_order`: `act_window` Expenses

## Navigation

- **Parent:** [[docs/Community Addons/sale_expense/Views]]

<!-- GENERATED:VIEWFILE -->
