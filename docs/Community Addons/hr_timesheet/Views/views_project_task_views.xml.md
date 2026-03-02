<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]
- Scope: Community Addons
- Source file: `views/project_task_views.xml`
- Views: 6
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `project_task_view_pivot`
- Name: project.task.view.pivot.inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_pivot`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `allocated_hours`, `effective_hours`, `overtime`, `progress`, `remaining_hours`, `subtask_effective_hours`, `total_hours_spent`
- XPath or positional patches: 2

### `project_task_view_graph`
- Name: project.task.view.graph.inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_graph`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `allocated_hours`, `effective_hours`, `overtime`, `progress`, `remaining_hours`, `subtask_effective_hours`, `total_hours_spent`
- XPath or positional patches: 1

### `project_task_view_search`
- Name: project.task.view.search.inherit.sale.timesheet.enterprise
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_search_form_project_fsm_base`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_task_kanban_inherited_progress`
- Name: project.task.timesheet.kanban.inherited.progress
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_kanban`
- Root tag: `templates`
- Field references: 5
- Sample fields: `allocated_hours`, `allow_timesheets`, `encode_uom_in_days`, `progress`, `remaining_hours`
- XPath or positional patches: 2

### `view_task_tree2_inherited`
- Name: project.task.list.inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_task_view_tree_main_base`
- Root tag: `field`
- Field references: 7
- Sample fields: `allocated_hours`, `effective_hours`, `priority`, `progress`, `remaining_hours`, `subtask_effective_hours`, `total_hours_spent`
- XPath or positional patches: 0

### `view_task_form2_inherited`
- Name: project.task.form.inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_form2`
- Root tag: `xpath`
- Field references: 21
- Sample fields: `allocated_hours`, `allow_timesheets`, `analytic_account_active`, `company_id`, `date`, `effective_hours`, `employee_id`, `encode_uom_in_days`, `name`, `progress`, and 11 more
- Buttons: `action_view_subtask_timesheet`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Community Addons/hr_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
