---
tags: [odoo, enterprise, generated, views]
---

# views/hr_timesheet_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]]
- Scope: Enterprise Addons
- Source file: `views/hr_timesheet_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `timesheet_view_tree_user_inherit`
- Name: account.analytic.line.view.list.with.user.inherit.industry.fsm
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.timesheet_view_tree_user`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `timesheet_view_form`
- Name: account.analytic.line.form
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `company_id`, `date`, `employee_id`, `name`, `project_id`, `task_id`, `unit_amount`, `user_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm/Views]]

