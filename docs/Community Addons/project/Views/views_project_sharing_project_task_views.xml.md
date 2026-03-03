---
tags: [odoo, community, generated, views]
---

# views/project_sharing_project_task_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `views/project_sharing_project_task_views.xml`
- Views: 6
- Actions: 16
- Menus: 0
- Rules: 0

## View records

### `open_view_blocked_by_list_view`
- Name: open.view.blocked.by.list.view
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.open_view_all_tasks_list_view`
- Root tag: `list`
- Field references: 2
- Sample fields: `portal_user_names`, `user_ids`
- XPath or positional patches: 1

### `project_sharing_project_task_view_search`
- Name: project.task.search.form
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_search_form_base`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

### `project_sharing_project_task_view_form`
- Name: project.sharing.project.task.view.form
- Model: `project.task`
- Type: inferred from arch
- Root tag: `form`
- Field references: 36
- Sample fields: `active`, `allow_milestones`, `allow_task_dependencies`, `child_ids`, `closed_subtask_count`, `company_id`, `current_user_same_company_partner`, `date_deadline`, `depend_on_count`, `depend_on_ids`, and 26 more
- Buttons: `action_open_task`, `action_project_sharing_open_blocking`, `action_project_sharing_open_subtasks`, `action_project_sharing_recurring_tasks`, `action_project_sharing_view_parent_task`
- XPath or positional patches: 0

### `project_sharing_project_task_view_tree`
- Name: project.sharing.project.task.list
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_tree_main_base`
- Root tag: `list`
- Field references: 6
- Sample fields: `is_rotting`, `partner_id`, `portal_user_names`, `rotting_days`, `stage_id`, `user_ids`
- XPath or positional patches: 3

### `project_sharing_project_task_view_kanban`
- Name: project.sharing.project.task.view.kanban
- Model: `project.task`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 13
- Sample fields: `allow_milestones`, `color`, `date_deadline`, `displayed_image_id`, `has_late_and_unreached_milestone`, `milestone_id`, `name`, `partner_id`, `portal_user_names`, `priority`, and 3 more
- XPath or positional patches: 0

### `project_sharing_quick_create_task_form`
- Name: project.task.form.quick_create
- Model: `project.task`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `project_sharing_recurring_tasks_form_action_view`: `view`
- `project_sharing_recurring_tasks_kanban_action_view`: `view`
- `project_sharing_recurring_tasks_tree_action_view`: `view`
- `project_sharing_project_task_recurring_tasks_action`: `act_window` Project Sharing Recurrence
- `project_sharing_subtasks_form_action_view`: `view`
- `project_sharing_subtasks_kanban_action_view`: `view`
- `project_sharing_subtasks_tree_action_view`: `view`
- `project_sharing_project_task_action_sub_task`: `act_window` Sub-tasks
- `project_sharing_blocking_form_action_view`: `view`
- `project_sharing_blocking_kanban_action_view`: `view`
- `project_sharing_blocking_tree_action_view`: `view`
- `project_sharing_project_task_action_blocking_tasks`: `act_window` Blocking
- `project_sharing_form_action_view`: `view`
- `project_sharing_tree_action_view`: `view`
- `project_sharing_kanban_action_view`: `view`
- `project_sharing_project_task_action`: `act_window` Project Sharing

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

