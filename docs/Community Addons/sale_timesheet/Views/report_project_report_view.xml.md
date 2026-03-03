---
tags: [odoo, community, generated, views]
---

# report/project_report_view.xml

- Module: [[docs/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]]
- Scope: Community Addons
- Source file: `report/project_report_view.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_task_project_user_fsm_graph_base_inherited`
- Name: report.project.task.user.fsm.graph.base.inherited
- Model: `report.project.task.user`
- Type: inferred from arch
- Inherits: `project.view_task_project_user_fsm_graph_base`
- Root tag: `field`
- Field references: 2
- Sample fields: `remaining_hours`, `remaining_hours_so`
- XPath or positional patches: 0

### `view_task_project_user_fsm_pivot_base_inherited`
- Name: report.project.task.user.fsm.pivot.base.inherited
- Model: `report.project.task.user`
- Type: inferred from arch
- Inherits: `project.view_task_project_user_fsm_pivot_base`
- Root tag: `field`
- Field references: 1
- Sample fields: `remaining_hours_so`
- XPath or positional patches: 0

### `view_task_project_user_pivot_inherited`
- Name: report.project.task.user.pivot.inherited
- Model: `report.project.task.user`
- Type: inferred from arch
- Inherits: `project.view_task_project_user_pivot`
- Root tag: `field`
- Field references: 2
- Sample fields: `remaining_hours`, `remaining_hours_so`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/sale_timesheet/Views]]

