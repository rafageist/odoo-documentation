<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/fsm_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]]
- Scope: Enterprise Addons
- Source file: `views/fsm_views.xml`
- Views: 35
- Actions: 141
- Menus: 20
- Rules: 0

## View records

### `project_project_view_form_simplified_inherit`
- Name: project.project.view.form.simplified.inherit
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.project_project_view_form_simplified`
- Root tag: `field`
- Field references: 2
- Sample fields: `is_fsm`, `user_id`
- XPath or positional patches: 0

### `edit_fsm_project_inherit`
- Name: project.project.fsm.form.inherit
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.edit_project`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `is_fsm`
- XPath or positional patches: 2

### `view_project_kanban_fsm`
- Name: project.project.kanban
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 4

### `project_project_view_form_simplified_footer_fsm`
- Name: project.project.view.form.simplified
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.project_project_view_form_simplified`
- Root tag: `xpath`
- Field references: 0
- Buttons: `%(industry_fsm.project_tasks_action_fsm)d`
- XPath or positional patches: 1

### `project_view_tree_primary`
- Name: project.view.list.primary
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `last_update_status`, `partner_id`, `sequence`, `stage_id`
- XPath or positional patches: 1

### `view_project_fsm`
- Name: project.view.tree.fsm
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project`
- Root tag: `field`
- Field references: 2
- Sample fields: `display_name`, `name`
- XPath or positional patches: 0

### `project_tasks_view_kanban_action_fsm`
- Name: project.tasks.kanban.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_view_kanban_fsm_all`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_kanban_fsm_all`
- Name: project.task.kanban.fsm.all
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_view_kanban_fsm`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_activity`
- Name: industry_fsm.project.task.activity.view
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_task_view_activity`
- Root tag: `activity`
- Field references: 0
- XPath or positional patches: 1

### `fsm_project_task_view_gantt`
- Name: fsm.project.task.view.gantt
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.project_task_view_gantt`
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 1

### `fsm_project_task_view_calendar2`
- Name: project.task.calendar.fsm2
- Model: `project.task`
- Type: inferred from arch
- Inherits: `fsm_project_task_view_calendar`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `fsm_project_task_view_calendar`
- Name: fsm.project.task.calendar
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_calendar_fsm`
- Root tag: `calendar`
- Field references: 0
- XPath or positional patches: 1

### `project_task_graph_view_grouped_by_location`
- Name: project.task.view.graph.fsm.group.by.location
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `partner_zip`
- XPath or positional patches: 1

### `project_task_pivot_view_grouped_by_location`
- Name: project.task.view.pivot.fsm.group.by.location
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_pivot`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_zip`, `user_ids`
- XPath or positional patches: 1

### `project_task_gantt_view_grouped_by_location`
- Name: project.task.view.gantt.fsm.group.by.location
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.project_task_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_pivot_view_grouped_by_project_and_users`
- Name: project.task.pivot.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_pivot`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `user_ids`
- XPath or positional patches: 1

### `project_task_gantt_view_grouped_by_project_and_users`
- Name: project.task.gantt.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.project_task_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_pivot_group_by_users_fsm`
- Name: project.task.view.pivot.fsm.group.by.users
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_pivot`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `user_ids`
- XPath or positional patches: 2

### `project_task_view_pivot_group_by_planned_date_begin_fsm`
- Name: project.task.view.pivot.fsm.group.by.planned_date_begin
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_pivot`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `planned_date_begin`
- XPath or positional patches: 1

### `project_task_view_graph_group_by_planned_date_begin_fsm`
- Name: project.task.view.graph.fsm.group.by.planned_date_begin
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_project_task_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `planned_date_begin`
- XPath or positional patches: 1

### `project_task_action_fsm_no_quick_create`
- Name: project.task.kanban.fsm.no.quick.create
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_kanban_fsm_my_task`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_kanban_fsm_my_task`
- Name: project.task.kanban.fsm.my.task
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_kanban_fsm`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_kanban_fsm`
- Name: project.task.kanban.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `quick_create_task_form_fsm_inherited`
- Name: project.task.form.quick_create_inherited
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.quick_create_task_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `display_name`, `project_id`
- XPath or positional patches: 0

### `project_task_view_kanban`
- Name: project.task.kanban.fsm.nonprimary
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.view_task_kanban_inherited`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `fsm_done`, `is_fsm`, `partner_city`, `partner_id`, `partner_phone`
- XPath or positional patches: 2

### `project_task_map_view_fsm_my_task2`
- Name: project.task.view.map.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_map_view_fsm_my_task`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_map_view_fsm_my_task`
- Name: project.task.view.map.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_map_view_fsm`
- Root tag: `map`
- Field references: 0
- XPath or positional patches: 1

### `project_task_map_view_fsm2`
- Name: project.task.view.map.fsm2
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_map_view_fsm`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_map_view_fsm`
- Name: project.task.view.map.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.project_task_map_view`
- Root tag: `map`
- Field references: 2
- Sample fields: `partner_id`, `partner_phone`
- XPath or positional patches: 1

### `project_task_view_calendar_fsm2`
- Name: project.task.calendar.fsm2
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_calendar_fsm`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_calendar_fsm`
- Name: project.task.calendar.fsm
- Model: `project.task`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 8
- Sample fields: `is_closed`, `name`, `partner_id`, `partner_phone`, `partner_zip`, `project_id`, `tag_ids`, `user_ids`
- XPath or positional patches: 0

### `project_task_view_search_fsm`
- Name: project.task.search.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_search_fsm_base`
- Root tag: `filter`
- Field references: 3
- Sample fields: `partner_id`, `partner_zip`, `task_properties`
- XPath or positional patches: 4

### `project_task_view_search_fsm_base`
- Name: project.task.search.fsm.base
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_search_form_project_fsm_base`
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_list_fsm_my_task`
- Name: project.task.list.fsm.my.task
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_task_view_list_fsm`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `project_task_view_list_fsm`
- Name: project.task.list.fsm
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_task_view_tree_base`
- Root tag: `list`
- Field references: 5
- Sample fields: `activity_exception_decoration`, `date_deadline`, `is_fsm`, `partner_id`, `planned_date_begin`
- XPath or positional patches: 2

## Actions

- `project_task_type_action_fsm`: `act_window` Stages
- `project_project_action_only_fsm_view_kanban`: `view`
- `project_project_action_only_fsm_view_tree`: `view`
- `project_project_action_only_fsm`: `act_window` Projects
- `open_create_project_fsm`: `act_window` Create a Project
- `res_config_settings_action_fsm`: `act_window` Settings
- `project_task_action_planning_groupby_location_fsm2_view_form`: `view`
- `project_task_action_planning_groupby_location_fsm2_view_graph`: `view`
- `project_task_action_planning_groupby_location_fsm2_view_pivot`: `view`
- `project_task_action_fsm_planning_groupby_location2_view_activity`: `view`
- `project_task_action_planning_groupby_location_fsm2_view_kanban`: `view`
- `project_task_action_planning_groupby_location_fsm2_view_list`: `view`
- `project_task_action_planning_groupby_location_fsm2_view_map`: `view`
- `project_task_action_planning_groupby_location_fsm2_view_calendar`: `view`
- `project_task_action_planning_groupby_location2_fsm2_view_gantt`: `view`
- `project_task_action_fsm_planning_groupby_location2`: `act_window` Planning by Location
- `project_task_action_planning_groupby_location_fsm_view_form`: `view`
- `project_task_action_planning_groupby_location_fsm_view_graph`: `view`
- `project_task_action_planning_groupby_location_fsm_view_pivot`: `view`
- `project_task_action_fsm_planning_groupby_location_view_activity`: `view`

## Menus

- `fsm_menu_settings`: Configuration
- `mail_activity_plan_menu_config_task`: Activity Plans
- `fsm_menu_config_activity_type`: Activity Types
- `menu_project_tags_act`: Tags
- `fsm_menu_settings_stage`: Stages
- `fsm_menu_settings_project`: Projects
- `fsm_menu_settings_res_config`: Settings
- `fsm_menu_reporting_customer_ratings`: Customer Ratings
- `fsm_menu_reporting`: Reporting
- `project_task_menu_planning_by_location_fsm`: By Location
- `project_task_menu_planning_by_project_fsm`: By Project
- `project_task_menu_planning_by_user_fsm`: By User
- `fsm_menu_planning`: Planning
- `fsm_menu_all_tasks_schedule`: To Schedule
- `fsm_menu_all_tasks_todo`: All Tasks
- `fsm_menu_all_tasks_root`: All Tasks
- `fsm_menu_tasks_map`: Map
- `fsm_menu_tasks_kanban`: Tasks
- `fsm_tasks_menu`: My Tasks
- `fsm_menu_root`: Field Service

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm/Views]]

<!-- GENERATED:VIEWFILE -->
