<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/planning_slot_views.xml

- Module: [[docs/Enterprise Addons/project_timesheet_forecast/project_timesheet_forecast|project_timesheet_forecast]]
- Scope: Enterprise Addons
- Source file: `views/planning_slot_views.xml`
- Views: 6
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `planning_view_pivot_view_inherit_timesheet`
- Name: planning.action.schedule.project.view.pivot.inherit.update
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `project_forecast.planning_action_schedule_by_project_pivot_inherit`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `planning_view_graph_inherit_timesheet`
- Name: planning.slot.graph.inherit
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_graph`
- Root tag: `field`
- Field references: 3
- Sample fields: `allocated_hours`, `effective_hours`, `percentage_hours`
- XPath or positional patches: 0

### `planning_view_pivot_inherit_timesheet`
- Name: planning.slot.pivot.inherit
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_pivot`
- Root tag: `field`
- Field references: 3
- Sample fields: `allocated_hours`, `effective_hours`, `percentage_hours`
- XPath or positional patches: 0

### `planning_view_gantt`
- Name: planning.slot.gantt
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `project_forecast.planning_view_gantt`
- Root tag: `gantt`
- Field references: 1
- Sample fields: `percentage_hours`
- XPath or positional patches: 2

### `project_forecast_view_tree_inherit_project_timesheet_forecast`
- Name: planning.slot.list.inherit.timesheet
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `project_forecast.planning_slot_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `effective_hours`
- XPath or positional patches: 1

### `project_forecast_view_form_inherit_project_timesheet_forecast`
- Name: planning.slot.form.inherit.timesheet
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `project_forecast.planning_slot_view_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `allocation_type`, `allow_timesheets`, `can_open_timesheets`, `company_id`, `effective_hours`, `encode_uom_in_days`, `timesheet_ids`
- Buttons: `action_open_timesheets`
- XPath or positional patches: 2

## Actions

- `planning_menu_schedule_by_role_graph`: `view`
- `planning_menu_schedule_by_role_pivot`: `view`
- `planning_menu_schedule_by_role_kanban`: `view`
- `planning_menu_schedule_by_role_tree`: `view`
- `planning_menu_schedule_by_role_calendar`: `view`
- `planning_menu_schedule_by_role`: `view`
- `project_timesheet_action_schedule_by_role`: `act_window` Schedule by Role

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_timesheet_forecast/Views]]

<!-- GENERATED:VIEWFILE -->
