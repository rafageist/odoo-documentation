<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/project_sharing_views.xml

- Module: [[docs/Enterprise Addons/project_enterprise/project_enterprise|project_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/project_sharing_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `project_task_view_gantt_inherited_project_sharing_task`
- Name: project.task.view.gantt.project.sharing.task
- Model: `project.task`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 6
- Sample fields: `allow_milestones`, `dependent_tasks_count`, `milestone_id`, `partner_id`, `portal_user_names`, `project_id`
- Buttons: `action_unschedule_task`
- XPath or positional patches: 0

### `project_sharing_project_task_view_form_inherited_in_gantt`
- Name: project.task.form.inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_sharing_project_task_view_form_inherited`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_unschedule_task`
- XPath or positional patches: 1

### `project_sharing_project_task_view_tree_inherited`
- Name: project_enterprise.project.task.view.list.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `planned_date_begin`
- XPath or positional patches: 2

### `project_sharing_project_task_view_kanban_inherited`
- Name: project.sharing.project.task.view.kanban.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_kanban`
- Root tag: `field`
- Field references: 2
- Sample fields: `date_deadline`, `planned_date_begin`
- XPath or positional patches: 0

### `project_sharing_project_task_view_form_inherited`
- Name: project.task.form.timesheet.inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `planned_date_begin`
- XPath or positional patches: 6

## Actions

- `project_sharing_task_gantt_action_view`: `view`

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
