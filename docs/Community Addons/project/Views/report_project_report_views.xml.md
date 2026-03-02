<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/project_report_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `report/project_report_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_task_project_user_search`
- Name: report.project.task.user.search
- Model: `report.project.task.user`
- Type: inferred from arch
- Inherits: `project.view_task_search_form_project_fsm_base`
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 1

### `view_task_project_user_fsm_graph_base`
- Name: report.project.task.user.graph
- Model: `report.project.task.user`
- Type: inferred from arch
- Inherits: `view_task_project_user_graph`
- Root tag: `graph`
- Field references: 0
- XPath or positional patches: 1

### `view_task_project_user_graph`
- Name: report.project.task.user.graph
- Model: `report.project.task.user`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 6
- Sample fields: `nbr`, `project_id`, `rating_avg`, `stage_id`, `working_hours_close`, `working_hours_open`
- XPath or positional patches: 0

### `view_task_project_user_fsm_pivot_base`
- Name: report.project.task.user.pivot
- Model: `report.project.task.user`
- Type: inferred from arch
- Inherits: `view_task_project_user_pivot`
- Root tag: `pivot`
- Field references: 0
- XPath or positional patches: 1

### `view_task_project_user_pivot`
- Name: report.project.task.user.pivot
- Model: `report.project.task.user`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `nbr`, `project_id`, `rating_avg`, `working_hours_close`, `working_hours_open`
- XPath or positional patches: 0

## Actions

- `action_project_task_user_tree`: `act_window` Tasks Analysis

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

<!-- GENERATED:VIEWFILE -->
