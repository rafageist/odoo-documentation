<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/planning_views.xml

- Module: [[docs/Enterprise Addons/planning/planning|planning]]
- Scope: Enterprise Addons
- Source file: `views/planning_views.xml`
- Views: 28
- Actions: 33
- Menus: 12
- Rules: 0

## View records

### `planning_action_schedule_by_role_view_graph_inherit`
- Name: planning.action.schedule.role.view.graph.inherit
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning_action_schedule_by_resource_view_graph_inherit`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `role_id`
- XPath or positional patches: 1

### `planning_action_schedule_by_role_view_pivot_inherit`
- Name: planning.action.schedule.role.view.pivot.inherit
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_pivot`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `role_id`
- XPath or positional patches: 2

### `planning_action_schedule_by_resource_view_graph_inherit`
- Name: planning.action.schedule.resource.view.graph.inherit
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_graph`
- Root tag: `field`
- Field references: 1
- Sample fields: `start_datetime`
- XPath or positional patches: 0

### `planning_action_schedule_by_resource_view_pivot_inherit`
- Name: planning.action.schedule.resource.view.pivot.inherit
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_pivot`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `start_datetime`
- XPath or positional patches: 1

### `open_shifts_graph_view`
- Name: open.shifts.graph.view
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning_view_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `role_id`
- XPath or positional patches: 2

### `open_shifts_list_view`
- Name: open.shifts.list.view
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_tree`
- Root tag: `field`
- Field references: 1
- Sample fields: `resource_id`
- XPath or positional patches: 0

### `open_shifts_gantt_view`
- Name: open.shifts.gantt.view
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning_view_gantt`
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 1

### `open_shifts_pivot_view`
- Name: open.shifts.pivot.view
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `resource_color`, `role_id`, `self_unassign_days_before`, `start_datetime`
- XPath or positional patches: 0

### `planning_view_gantt_no_sample`
- Name: planning.slot.gantt.inherit.nosample
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `planning_role_view_search`
- Name: planning.role.view.search
- Model: `planning.role`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `resource_ids`
- XPath or positional patches: 0

### `planning_role_view_kanban`
- Name: planning.role.view.kanban
- Model: `planning.role`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `color`, `name`, `resource_ids`
- XPath or positional patches: 0

### `planning_role_view_form`
- Name: planning.role.form
- Model: `planning.role`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `color`, `name`, `resource_ids`, `sequence`
- XPath or positional patches: 0

### `planning_role_view_tree`
- Name: planning.role.list
- Model: `planning.role`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `color`, `name`, `resource_ids`, `sequence`
- XPath or positional patches: 0

### `planning_view_gantt_group_by_role`
- Name: planning.slot.gantt.inherit.group.role
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_gantt`
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 1

### `planning_view_gantt`
- Name: planning.slot.gantt
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 9
- Sample fields: `allocated_hours`, `allocated_percentage`, `allow_self_unassign`, `employee_id`, `recurrency_id`, `repeat`, `request_to_switch`, `resource_id`, `state`
- XPath or positional patches: 0

### `planning_view_kanban_inherit`
- Name: planning.slot.kanban
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_kanban`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `allow_self_unassign`, `is_past`, `name`, `overlap_slot_count`, `publication_warning`, `request_to_switch`
- XPath or positional patches: 1

### `shifts_template_for_multi_create_in_calendar_view`
- Name: planning.slot.form
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `template_id`
- XPath or positional patches: 0

### `planning_view_my_calendar`
- Name: planning.slot.my.calendar
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 7
- Sample fields: `allocated_hours`, `allocated_percentage`, `name`, `resource_id`, `resource_type`, `role_id`, `state`
- XPath or positional patches: 0

### `planning_view_graph`
- Name: planning.slot.graph
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 5
- Sample fields: `allocated_hours`, `resource_color`, `resource_id`, `self_unassign_days_before`, `start_datetime`
- XPath or positional patches: 0

### `planning_view_pivot`
- Name: planning.slot.pivot
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `allocated_hours`, `resource_color`, `resource_id`, `self_unassign_days_before`, `start_datetime`
- XPath or positional patches: 0

### `planning_view_calendar`
- Name: planning.slot.calendar
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 12
- Sample fields: `allocated_hours`, `allocated_percentage`, `is_hatched`, `name`, `repeat`, `request_to_switch`, `resource_color`, `resource_id`, `resource_type`, `role_id`, and 2 more
- XPath or positional patches: 0

### `planning_view_search`
- Name: planning.slot.search
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning_view_search_base`
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 2

### `planning_view_search_base`
- Name: planning.slot.search.base
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `search`
- Field references: 8
- Sample fields: `company_id`, `department_id`, `job_title`, `manager_id`, `name`, `request_to_switch`, `resource_id`, `role_id`
- XPath or positional patches: 0

### `planning_view_form_in_gantt`
- Name: planning.slot.form.gantt
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning_view_form_inherit`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `allow_template_creation`, `confirm_delete`, `is_past`, `is_unassign_deadline_passed`, `publication_warning`, `request_to_switch`
- Buttons: `action_cancel_switch`, `action_save_template`, `action_self_assign`, `action_self_unassign`, `action_send`, `action_switch_shift`, `action_unpublish`, `auto_plan_id`, `unlink`
- XPath or positional patches: 1

### `planning_view_form_inherit`
- Name: planning.slot.form
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `planning_view_kanban`
- Name: planning.slot.kanban
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 11
- Sample fields: `allocated_hours`, `allocated_percentage`, `employee_id`, `repeat`, `resource_color`, `resource_id`, `resource_type`, `role_id`, `slot_properties`, `start_datetime`, and 1 more
- XPath or positional patches: 0

### `planning_view_form`
- Name: planning.slot.form
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `form`
- Field references: 35
- Sample fields: `allocated_hours`, `allocated_percentage`, `allow_self_unassign`, `allow_template_creation`, `color`, `company_id`, `conflicting_slot_ids`, `employee_id`, `end_datetime`, `is_past`, and 25 more
- Buttons: `action_cancel_switch`, `action_self_assign`, `action_self_unassign`, `action_send`, `action_switch_shift`, `action_unpublish`, `auto_plan_id`
- XPath or positional patches: 0

### `planning_view_tree`
- Name: planning.slot.list
- Model: `planning.slot`
- Type: inferred from arch
- Root tag: `list`
- Field references: 17
- Sample fields: `allocated_percentage`, `allow_self_unassign`, `company_id`, `end_datetime`, `is_past`, `is_unassign_deadline_passed`, `is_users_role`, `name`, `recurrency_id`, `request_to_switch`, and 7 more
- Buttons: `action_cancel_switch`, `action_planning_publish_and_send`, `action_self_assign`, `action_self_unassign`, `action_switch_shift`
- XPath or positional patches: 0

## Actions

- `model_planning_slot_action_reset_to_draft`: `server` Reset to Draft
- `model_planning_slot_action_publish_and_send`: `server` Publish & Send
- `planning_action_open_shifts_view_graph`: `view`
- `planning_action_open_shifts_view_pivot`: `view`
- `planning_action_open_shifts_view_kanban`: `view`
- `planning_action_open_shifts_view_list`: `view`
- `planning_action_open_shifts_view_gantt`: `view`
- `planning_action_open_shifts_view_calendar`: `view`
- `planning_action_open_shifts`: `act_window` Open Shifts
- `planning_action_shift_template`: `act_window` Shift Templates
- `planning_action_roles`: `act_window` Roles
- `planning_action_settings`: `act_window` Settings
- `planning_action_schedule_by_role_view_graph`: `view`
- `planning_action_schedule_by_role_view_pivot`: `view`
- `planning_action_schedule_by_role_view_kanban`: `view`
- `planning_action_schedule_by_role_view_tree`: `view`
- `planning_action_schedule_by_role_view_calendar`: `view`
- `planning_action_schedule_by_role_view_gantt`: `view`
- `planning_action_schedule_by_role`: `act_window` Schedule by Role
- `planning_action_schedule_by_resource_view_graph`: `view`

## Menus

- `planning_menu_settings_shift_template`: Shift Templates
- `planning_menu_settings_role`: Roles
- `planning_menu_settings_resource`: Materials
- `planning_menu_settings_employee`: Employees
- `planning_menu_settings_config`: Settings
- `planning_menu_settings`: Configuration
- `planning_menu_schedule_by_role`: By Role
- `planning_menu_schedule_by_resource`: By Resource
- `planning_menu_schedule`: Schedule
- `planning_menu_open_shifts`: Open Shifts
- `planning_menu_my_planning`: My Planning
- `planning_menu_root`: Planning

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning/Views]]

<!-- GENERATED:VIEWFILE -->
