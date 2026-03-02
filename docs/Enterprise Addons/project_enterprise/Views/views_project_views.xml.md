<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/project_views.xml

- Module: [[docs/Enterprise Addons/project_enterprise/project_enterprise|project_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/project_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `project_templates_view_gantt`
- Name: project.project.template.gantt
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project_enterprise.project_project_view_gantt`
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 1

### `view_task_kanban_inherited`
- Name: project.enterprise.task.kanban.nonprimary
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_kanban`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `date_deadline`, `planned_date_begin`, `planning_overlap`
- XPath or positional patches: 1

### `project_project_view_gantt`
- Name: project.project.view.gantt
- Model: `project.project`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 3
- Sample fields: `partner_id`, `stage_id_color`, `user_id`
- Buttons: `action_view_tasks`
- XPath or positional patches: 0

## Actions

- `project.open_view_project_all_config_group_stage`: `act_window`
- `project.open_view_project_all_group_stage`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
