---
tags: [odoo, enterprise, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]
- Scope: Enterprise Addons
- Source file: `views/project_task_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `project_task_view_kanban`
- Name: project.task.kanban.timer
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `display_timesheet_timer`, `timer_start`
- XPath or positional patches: 1

### `project_task_view_gantt_timesheet`
- Name: project.task.view.gantt
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.project_task_view_gantt`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `progress`
- XPath or positional patches: 2

### `project_task_view_form`
- Name: project.task.view.form.inherit.sale.timesheet.enterprise
- Model: `project.task`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_task_form2_inherited`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `company_id`, `display_timesheet_timer`, `is_timer_running`, `timer_start`, `timesheet_unit_amount`, `validated`
- Buttons: `action_timer_start`, `action_timer_stop`
- XPath or positional patches: 6

## Navigation

- **Parent:** [[docs/Enterprise Addons/timesheet_grid/Views]]

