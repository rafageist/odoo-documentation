<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Community Addons/project_todo/project_todo|project_todo]]
- Scope: Community Addons
- Source file: `views/project_task_views.xml`
- Views: 8
- Actions: 8
- Menus: 0
- Rules: 0

## View records

### `project_task_view_todo_search`
- Name: project.task.view.todo.search
- Model: `project.task`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `name`, `personal_stage_type_ids`, `tag_ids`, `user_ids`
- XPath or positional patches: 0

### `project_task_view_todo_activity`
- Name: project.task.view.todo.activity
- Model: `project.task`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 2
- Sample fields: `name`, `user_ids`
- XPath or positional patches: 0

### `project_task_view_todo_calendar`
- Name: project.task.calendar
- Model: `project.task`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 4
- Sample fields: `name`, `personal_stage_id`, `priority`, `tag_ids`
- XPath or positional patches: 0

### `project_task_view_todo_conversion_form`
- Name: project.task.view.todo.conversion.form
- Model: `project.task`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `company_id`, `project_id`, `tag_ids`, `user_ids`
- Buttons: `action_convert_to_task`
- XPath or positional patches: 0

### `project_task_view_todo_quick_create_form`
- Name: project.task.view.todo.quick.create.todo
- Model: `project.task`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `date_deadline`, `display_name`
- XPath or positional patches: 0

### `project_task_view_todo_form`
- Name: project.task.view.todo.form
- Model: `project.task`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `active`, `date_deadline`, `description`, `html_field_history_metadata`, `name`, `personal_stage_type_id`, `priority`, `state`, `tag_ids`, `user_ids`
- XPath or positional patches: 0

### `project_task_view_todo_tree`
- Name: project.task.todo.list
- Model: `project.task`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `activity_ids`, `date_deadline`, `name`, `personal_stage_type_id`, `priority`, `state`, `tag_ids`, `user_ids`
- XPath or positional patches: 0

### `project_task_view_todo_kanban`
- Name: project.task.kanban
- Model: `project.task`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 11
- Sample fields: `active`, `activity_ids`, `color`, `date_deadline`, `displayed_image_id`, `name`, `priority`, `sequence`, `state`, `tag_ids`, and 1 more
- XPath or positional patches: 0

## Actions

- `project_task_action_convert_todo_to_task_form_view`: `view`
- `project_task_action_convert_todo_to_task`: `act_window` Convert to Task
- `project_task_action_todo_activity_view`: `view`
- `project_task_action_todo_calendar_view`: `view`
- `project_task_action_todo_tree_view`: `view`
- `project_task_action_todo_form_view`: `view`
- `project_task_action_todo_kanban_view`: `view`
- `project_task_action_todo`: `act_window` To-dos

## Navigation

- **Parent:** [[docs/Community Addons/project_todo/Views]]

<!-- GENERATED:VIEWFILE -->
