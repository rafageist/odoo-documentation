<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/project_report_view.xml

- Module: [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]
- Scope: Community Addons
- Source file: `report/project_report_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_task_project_user_pivot_inherited`
- Name: report.project.task.user.pivot.inherited
- Model: `report.project.task.user`
- Type: inferred from arch
- Inherits: `project.view_task_project_user_pivot`
- Root tag: `pivot`
- Field references: 5
- Sample fields: `allocated_hours`, `effective_hours`, `overtime`, `remaining_hours`, `remaining_hours_percentage`
- XPath or positional patches: 1

### `view_task_project_user_graph_inherited`
- Name: report.project.task.user.graph.inherited
- Model: `report.project.task.user`
- Type: inferred from arch
- Inherits: `project.view_task_project_user_graph`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `allocated_hours`, `effective_hours`, `overtime`, `remaining_hours`, `remaining_hours_percentage`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/hr_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
