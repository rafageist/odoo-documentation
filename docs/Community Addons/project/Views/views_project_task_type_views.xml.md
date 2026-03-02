<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/project_task_type_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `views/project_task_type_views.xml`
- Views: 5
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `view_project_task_type_kanban`
- Name: project.task.type.kanban
- Model: `project.task.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `color`, `name`, `project_ids`
- XPath or positional patches: 0

### `task_type_tree_inherited`
- Name: project.task.type.list.inherited
- Model: `project.task.type`
- Type: inferred from arch
- Inherits: `task_type_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `rating_template_id`
- XPath or positional patches: 1

### `task_type_tree`
- Name: project.task.type.list
- Model: `project.task.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `color`, `fold`, `mail_template_id`, `name`, `project_ids`, `rotting_threshold_days`, `sequence`
- XPath or positional patches: 0

### `task_type_edit`
- Name: project.task.type.form
- Model: `project.task.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `active`, `auto_validation_state`, `color`, `fold`, `mail_template_id`, `name`, `project_ids`, `rating_active`, `rating_status`, `rating_status_period`, and 4 more
- XPath or positional patches: 0

### `task_type_search`
- Name: project.task.type.search
- Model: `project.task.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `mail_template_id`, `name`, `project_ids`, `rating_template_id`
- XPath or positional patches: 0

## Actions

- `unlink_task_type_action`: `server` Delete
- `open_task_type_form_domain`: `act_window` Task Stages
- `open_task_type_form`: `act_window` Task Stages

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

<!-- GENERATED:VIEWFILE -->
