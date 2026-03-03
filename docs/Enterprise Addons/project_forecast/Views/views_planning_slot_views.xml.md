---
tags: [odoo, enterprise, generated, views]
---

# views/planning_slot_views.xml

- Module: [[docs/Enterprise Addons/project_forecast/project_forecast|project_forecast]]
- Scope: Enterprise Addons
- Source file: `views/planning_slot_views.xml`
- Views: 11
- Actions: 23
- Menus: 0
- Rules: 0

## View records

### `planning_action_schedule_by_project_graph_inherit`
- Name: planning.action.schedule.project.view.graph.inherit
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_action_schedule_by_resource_view_graph_inherit`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 1

### `planning_action_schedule_by_project_pivot_inherit`
- Name: planning.action.schedule.project.view.pivot.inherit
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_pivot`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `project_id`, `resource_id`
- XPath or positional patches: 1

### `planning_view_gantt_group_by_project`
- Name: planning.slot.gantt.inherit.project.project.forecast
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `planning_view_gantt_inherit`
- Name: planning.slot.gantt
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `planning_view_form_in_gantt_inherit_project_forecast`
- Name: planning.slot.form.gantt
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_form_in_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `planning_view_gantt`
- Name: planning.slot.gantt
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `planning_slot_view_search`
- Name: planning.slot.search
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_search_base`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 3

### `planning_view_kanban`
- Name: planning.slot.kanban
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 2

### `planning_slot_view_calendar`
- Name: planning.slot.calendar
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_calendar`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 1

### `planning_slot_view_form`
- Name: planning.slot.form
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 1

### `planning_slot_view_tree`
- Name: planning.slot.list
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 1

## Actions

- `project_forecast_action_from_project_view_pivot`: `view`
- `project_forecast_action_from_project_view_tree`: `view`
- `project_forecast_action_from_project_view_calendar`: `view`
- `project_forecast_action_from_project_view_gantt`: `view`
- `project_forecast_action_from_project`: `act_window` Planning
- `planning.planning_action_schedule_by_role`: `act_window`
- `planning.planning_action_schedule_by_resource`: `act_window`
- `planning.planning_action_my_calendar`: `act_window`
- `project_forecast_action_schedule_by_employee_view_graph`: `view`
- `project_forecast_action_schedule_by_employee_view_pivot`: `view`
- `project_forecast_action_schedule_by_employee_view_kanban`: `view`
- `project_forecast_action_schedule_by_employee_view_tree`: `view`
- `project_forecast_action_schedule_by_employee_view_calendar`: `view`
- `project_forecast_action_schedule_by_employee_view_gantt`: `view`
- `project_forecast_action_schedule_by_employee`: `act_window` Schedule by Resource
- `planning_action_schedule_by_project_view_graph`: `view`
- `planning_action_schedule_by_project_view_pivot`: `view`
- `planning_action_schedule_by_project_view_kanban`: `view`
- `planning_action_schedule_by_project_view_tree`: `view`
- `planning_action_schedule_by_project_view_calendar`: `view`

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_forecast/Views]]

