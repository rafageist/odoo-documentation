<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Community Addons/hr_expense/hr_expense|hr_expense]]
- Scope: Community Addons
- Source file: `views/hr_employee_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_search_view`
- Name: hr.employee.search.view
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_employee_tree_inherit_expense`
- Name: hr.employee.list.expense
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `expense_manager_id`
- XPath or positional patches: 1

### `hr_employee_view_form_inherit_expense`
- Name: hr.employee.view.form.expense
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `expense_manager_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/hr_expense/Views]]

<!-- GENERATED:VIEWFILE -->
