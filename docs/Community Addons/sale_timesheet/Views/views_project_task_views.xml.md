---
tags: [odoo, community, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]]
- Scope: Community Addons
- Source file: `views/project_task_views.xml`
- Views: 6
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `project_task_view_search_inherit_sale_timesheet`
- Name: project.task.view.search.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `hr_timesheet.project_task_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_form_inherit_sale_timesheet`
- Name: project.task.form.inherit.timesheet
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_form2`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `has_multi_sol`, `is_project_map_empty`, `is_so_line_edited`, `pricing_type`, `remaining_hours_available`, `remaining_hours_so`, `sale_order_id`, `so_line`, `timesheet_invoice_id`
- XPath or positional patches: 6

### `view_task_tree2_inherited`
- Name: project.task.list.inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_task_tree2_inherited`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `remaining_hours_available`, `remaining_hours_so`, `sale_line_id`
- XPath or positional patches: 1

### `project_project_view_kanban_inherit_sale_timesheet_so_button`
- Name: project.project.kanban.inherit.sale.timesheet.so.button
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_project_view_kanban_inherit_sale_timesheet`
- Name: project.project.kanban.inherit.sale.timesheet
- Model: `project.project`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_project_kanban_inherited`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `allow_billable`, `pricing_type`, `sale_order_id`, `warning_employee_rate`
- XPath or positional patches: 2

### `project_project_view_form`
- Name: project.project.form.inherit
- Model: `project.project`
- Type: inferred from arch
- Inherits: `hr_timesheet.project_invoice_form`
- Root tag: `xpath`
- Field references: 13
- Sample fields: `billing_type`, `company_id`, `cost_currency_id`, `currency_id`, `display_cost`, `employee_id`, `existing_employee_ids`, `is_cost_changed`, `partner_id`, `price_unit`, and 3 more
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Community Addons/sale_timesheet/Views]]

