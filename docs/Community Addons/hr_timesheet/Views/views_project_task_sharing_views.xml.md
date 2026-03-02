<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/project_task_sharing_views.xml

- Module: [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]
- Scope: Community Addons
- Source file: `views/project_task_sharing_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `project_sharing_kanban_inherit_project_task_view_kanban`
- Name: project.sharing.project.task.timesheet.kanban.inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_kanban`
- Root tag: `templates`
- Field references: 6
- Sample fields: `allocated_hours`, `allow_timesheets`, `encode_uom_in_days`, `priority`, `progress`, `remaining_hours`
- XPath or positional patches: 1

### `project_sharing_inherit_project_task_view_form`
- Name: project.sharing.project.task.view.form.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_form`
- Root tag: `xpath`
- Field references: 16
- Sample fields: `allocated_hours`, `allow_timesheets`, `analytic_account_active`, `date`, `effective_hours`, `employee_id`, `encode_uom_in_days`, `name`, `progress`, `remaining_hours`, and 6 more
- Buttons: `action_view_subtask_timesheet`
- XPath or positional patches: 6

## Navigation

- **Parent:** [[docs/Community Addons/hr_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
