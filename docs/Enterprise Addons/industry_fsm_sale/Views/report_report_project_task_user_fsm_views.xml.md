---
tags: [odoo, enterprise, generated, views]
---

# report/report_project_task_user_fsm_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]]
- Scope: Enterprise Addons
- Source file: `report/report_project_task_user_fsm_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_task_project_user_fsm_graph_inherited`
- Name: report.project.task.user.fsm.graph.inherited
- Model: `report.project.task.user.fsm`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_user_view_graph`
- Root tag: `field`
- Field references: 1
- Sample fields: `remaining_hours_so`
- XPath or positional patches: 0

### `view_task_project_user_fsm_pivot_inherited`
- Name: report.project.task.user.fsm.pivot.inherited
- Model: `report.project.task.user.fsm`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_user_view_pivot`
- Root tag: `field`
- Field references: 1
- Sample fields: `remaining_hours_so`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_sale/Views]]

