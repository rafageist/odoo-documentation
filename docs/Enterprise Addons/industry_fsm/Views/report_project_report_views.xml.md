---
tags: [odoo, enterprise, generated, views]
---

# report/project_report_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]]
- Scope: Enterprise Addons
- Source file: `report/project_report_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `report_project_task_user_fsm_view_search`
- Name: report.project.task.user.fsm.search
- Model: `report.project.task.user.fsm`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_view_search_fsm_base`
- Root tag: `search`
- Field references: 2
- Sample fields: `partner_id`, `partner_zip`
- XPath or positional patches: 2

### `report_project_task_user_fsm_view_tree`
- Name: report.project.task.user.fsm.view.list
- Model: `report.project.task.user.fsm`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `company_id`, `effective_hours`, `name`, `partner_id`, `project_id`, `user_ids`
- XPath or positional patches: 0

### `project_task_user_view_graph`
- Name: report.project.task.user.graph
- Model: `report.project.task.user.fsm`
- Type: inferred from arch
- Inherits: `project.view_task_project_user_fsm_graph_base`
- Root tag: `field`
- Field references: 6
- Sample fields: `allocated_hours`, `create_date`, `effective_hours`, `project_id`, `remaining_hours`, `stage_id`
- XPath or positional patches: 0

### `project_task_user_view_pivot`
- Name: report.project.task.user.pivot
- Model: `report.project.task.user.fsm`
- Type: inferred from arch
- Inherits: `project.view_task_project_user_fsm_pivot_base`
- Root tag: `field`
- Field references: 7
- Sample fields: `allocated_hours`, `create_date`, `overtime`, `project_id`, `remaining_hours`, `working_hours_close`, `working_hours_open`
- XPath or positional patches: 0

## Actions

- `project_task_user_action_report_fsm`: `act_window` Tasks Analysis

## Menus

- `fsm_menu_reporting_task_analysis`: Tasks Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm/Views]]

