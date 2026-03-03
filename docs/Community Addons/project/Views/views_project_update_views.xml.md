---
tags: [odoo, community, generated, views]
---

# views/project_update_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `views/project_update_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `project_update_view_tree`
- Name: project.update.view.list
- Model: `project.update`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `color`, `date`, `name`, `progress`, `status`, `user_id`
- XPath or positional patches: 0

### `project_update_view_kanban`
- Name: project.update.view.kanban
- Model: `project.update`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 10
- Sample fields: `closed_task_count`, `closed_task_percentage`, `color`, `date`, `label_tasks`, `name_cropped`, `progress_percentage`, `status`, `task_count`, `user_id`
- XPath or positional patches: 0

### `project_update_view_form`
- Name: project.update.view.form
- Model: `project.update`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `color`, `date`, `description`, `name`, `progress`, `project_id`, `status`, `user_id`
- XPath or positional patches: 0

### `project_update_view_search`
- Name: project.update.view.search
- Model: `project.update`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `description`, `name`, `project_id`, `status`, `user_id`
- XPath or positional patches: 0

## Actions

- `project_update_all_action`: `act_window` Dashboard

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

