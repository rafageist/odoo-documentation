<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `views/project_task_views.xml`
- Views: 35
- Actions: 39
- Menus: 0
- Rules: 0

## View records

### `view_task_template_search_form`
- Name: project.task.search.form
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_search_form`
- Root tag: `filter`
- Field references: 2
- Sample fields: `role_ids`, `user_ids`
- XPath or positional patches: 4

### `project_task_templates_kanban`
- Name: project.task.templates.list
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_kanban`
- Root tag: `kanban`
- Field references: 0
- XPath or positional patches: 2

### `project_task_templates_list`
- Name: project.task.templates.list
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_tree_base`
- Root tag: `field`
- Field references: 4
- Sample fields: `partner_id`, `project_id`, `role_ids`, `user_ids`
- XPath or positional patches: 0

### `view_task_kanban_res_partner`
- Name: project.task.kanban.res.partner
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_kanban_inherit_all_task`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `quick_create_task_form_res_partner`
- Name: project.task.form.quick_create.res.partner
- Model: `project.task`
- Type: inferred from arch
- Inherits: `quick_create_task_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_task_form_res_partner`
- Name: project.task.form.res.partner
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_form2`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_graph_view_project_milestone`
- Name: project.task.view.graph.project.milestone
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_project_task_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `milestone_id`
- XPath or positional patches: 1

### `project_task_pivot_view_project_milestone`
- Name: project.task.view.pivot.project.milestone
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_project_task_pivot`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `milestone_id`, `stage_id`
- XPath or positional patches: 1

### `project_task_tree_view_project_milestone`
- Name: project.task.view.tree.project.milestone
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_tree_base`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `project_task_kanban_view_project_milestone`
- Name: project.task.kanban.inherit.project.milestone
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `quick_create_task_form_inherit_view_default_project`
- Name: project.task.form.quick.create
- Model: `project.task`
- Type: inferred from arch
- Inherits: `quick_create_task_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 0

### `view_task_kanban_inherit_view_default_project`
- Name: project.task.kanban
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_kanban`
- Root tag: `kanban`
- Field references: 0
- XPath or positional patches: 1

### `open_view_all_tasks_list_view`
- Name: open.view.all.tasks.list.view
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_tree2`
- Root tag: `list`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 1

### `open_view_my_tasks_list_view`
- Name: open.view.my.tasks.list.view
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_tree2`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `view_task_kanban_inherit_all_task`
- Name: project.task.kanban.inherit.all.task
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_task_kanban_inherit_my_task`
- Name: project.task.kanban.inherit.my.task
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_activity`
- Name: project.task.activity
- Model: `project.task`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `name`, `project_id`, `user_ids`
- XPath or positional patches: 0

### `view_task_all_calendar`
- Name: project.task.all.calendar
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_calendar`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `stage_id`
- XPath or positional patches: 3

### `view_task_calendar`
- Name: project.task.calendar
- Model: `project.task`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 13
- Sample fields: `allow_milestones`, `display_in_project`, `milestone_id`, `partner_id`, `personal_stage_id`, `priority`, `project_id`, `stage_id`, `stage_id_color`, `subtask_count`, and 3 more
- XPath or positional patches: 0

### `view_task_tree2`
- Name: project.task.list
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_tree_base`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_tree_base`
- Name: project.task.view.list.base
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_tree_main_base`
- Root tag: `list`
- Field references: 9
- Sample fields: `activity_ids`, `my_activity_date_deadline`, `parent_id`, `personal_stage_type_id`, `priority`, `rating_active`, `rating_last_text`, `recurrence_id`, `task_properties`
- XPath or positional patches: 4

### `project_task_view_tree_main_base`
- Name: project.task.view.list.main.base
- Model: `project.task`
- Type: inferred from arch
- Root tag: `list`
- Field references: 21
- Sample fields: `allow_milestones`, `closed_subtask_count`, `company_id`, `create_date`, `date_deadline`, `date_last_stage_update`, `id`, `is_rotting`, `milestone_id`, `name`, and 11 more
- XPath or positional patches: 0

### `project_sub_task_view_kanban_mobile`
- Name: project.task.kanban
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 2

### `view_task_kanban`
- Name: project.task.kanban
- Model: `project.task`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 24
- Sample fields: `activity_ids`, `allow_milestones`, `color`, `date_deadline`, `displayed_image_id`, `has_late_and_unreached_milestone`, `is_rotting`, `is_template`, `milestone_id`, `name`, and 14 more
- XPath or positional patches: 0

### `project_task_convert_to_subtask_view_form`
- Name: project.task.convert.to.subtask.form
- Model: `project.task`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `company_id`, `parent_id`, `project_id`
- XPath or positional patches: 0

### `quick_create_task_form`
- Name: project.task.form.quick_create
- Model: `project.task`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `company_id`, `description`, `display_name`, `parent_id`, `project_id`, `user_ids`
- XPath or positional patches: 0

### `view_task_form2`
- Name: project.task.form
- Model: `project.task`
- Type: inferred from arch
- Root tag: `form`
- Field references: 59
- Sample fields: `active`, `activity_ids`, `allocated_hours`, `allow_milestones`, `allow_task_dependencies`, `child_ids`, `closed_depend_on_count`, `closed_subtask_count`, `company_id`, `create_date`, and 49 more
- Buttons: `%(project_task_action_sub_task)d`, `action_dependent_tasks`, `action_open_parent_task`, `action_open_ratings`, `action_recurring_tasks`
- XPath or positional patches: 0

### `view_project_task_pivot_inherit`
- Name: project.task.pivot.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_pivot`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `stage_id`, `user_ids`
- XPath or positional patches: 3

### `view_project_task_pivot`
- Name: project.task.pivot
- Model: `project.task`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 7
- Sample fields: `allocated_hours`, `color`, `project_id`, `sequence`, `stage_id_color`, `working_hours_close`, `working_hours_open`
- XPath or positional patches: 0

### `view_project_task_graph_inherit`
- Name: project.task.graph.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `user_ids`
- XPath or positional patches: 2

### `view_project_task_graph`
- Name: project.task.graph
- Model: `project.task`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 8
- Sample fields: `color`, `project_id`, `rating_last_value`, `sequence`, `stage_id`, `stage_id_color`, `working_hours_close`, `working_hours_open`
- XPath or positional patches: 0

### `view_task_search_form`
- Name: project.task.search.form
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_search_form_project_base`
- Root tag: `filter`
- Field references: 1
- Sample fields: `task_properties`
- XPath or positional patches: 4

### `view_task_search_form_project_base`
- Name: project.task.search.form.project.base
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_search_form_project_fsm_base`
- Root tag: `filter`
- Field references: 2
- Sample fields: `activity_type_id`, `activity_user_id`
- XPath or positional patches: 2

### `view_task_search_form_project_fsm_base`
- Name: project.task.search.form.project.base
- Model: `project.task`
- Type: inferred from arch
- Inherits: `view_task_search_form_base`
- Root tag: `field`
- Field references: 5
- Sample fields: `company_id`, `partner_id`, `project_id`, `stage_id`, `user_ids`
- XPath or positional patches: 2

### `view_task_search_form_base`
- Name: project.task.search.form
- Model: `project.task`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `milestone_id`, `name`, `partner_id`, `stage_id`, `tag_ids`
- XPath or positional patches: 0

## Actions

- `project_milestone_action_view_graph`: `view`
- `project_milestone_action_view_pivot`: `view`
- `project_milestone_action_view_tasks_calendar`: `view`
- `project_milestone_action_view_tasks_list`: `view`
- `project_milestone_action_view_tasks_kanban`: `view`
- `project_milestone_action_view_tasks`: `act_window` Tasks.test
- `mail_followers_edit_action_from_task`: `act_window` Add/Remove Followers
- `action_view_task_from_milestone`: `act_window` Tasks
- `dblc_proj`: `act_window` Project's tasks
- `action_view_task_overpassed_draft`: `act_window` Overpassed Tasks
- `project_task_action_from_partner_calendar_view`: `view`
- `project_task_action_from_partner_form_view`: `view`
- `project_task_action_from_partner_kanban_view`: `view`
- `project_task_action_from_partner_tree_view`: `view`
- `project_task_action_from_partner`: `act_window` Partner's Tasks
- `action_server_convert_to_template`: `server` Convert to Template
- `action_server_convert_to_subtask`: `server` Convert to Task/Sub-Task
- `open_view_all_task_list_calendar`: `view`
- `open_view_all_task_list_kanban`: `view`
- `open_view_all_task_list_tree`: `view`

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

<!-- GENERATED:VIEWFILE -->
