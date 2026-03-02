<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mrp_view_employee_filter`
- Name: mrp_workorder.employee.search
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_employee_tree_workorder`
- Name: mrp_workorder.hr_employee.list
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `avatar_128`, `id`, `name`
- XPath or positional patches: 0

### `view_employee_form_account`
- Name: hr.employee.view.form.inherit.mrp.workorder.hr
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_workorder/Views]]

<!-- GENERATED:VIEWFILE -->
