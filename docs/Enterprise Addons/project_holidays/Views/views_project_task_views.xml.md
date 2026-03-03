---
tags: [odoo, enterprise, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Enterprise Addons/project_holidays/project_holidays|project_holidays]]
- Scope: Enterprise Addons
- Source file: `views/project_task_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `project_task_view_kanban_inherit_project_holidays`
- Name: project.task.task.kanban
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.view_task_kanban_inherited`
- Root tag: `field`
- Field references: 2
- Sample fields: `leave_warning`, `planning_overlap`
- XPath or positional patches: 0

### `project_task_view_gantt_fsm_inherit_holidays`
- Name: project.task.view.gantt.holidays
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.project_task_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_task_form2_inherit_holidays`
- Name: project.task.view.form.holidays
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.project_task_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `leave_warning`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_holidays/Views]]

