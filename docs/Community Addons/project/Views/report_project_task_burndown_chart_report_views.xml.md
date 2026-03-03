---
tags: [odoo, community, generated, views]
---

# report/project_task_burndown_chart_report_views.xml

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Source file: `report/project_task_burndown_chart_report_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `project_task_burndown_chart_report_view_graph`
- Name: project.task.burndown.chart.report.view.graph
- Model: `project.task.burndown.chart.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `date`, `is_closed`, `stage_id`
- XPath or positional patches: 0

### `project_task_burndown_chart_report_view_search`
- Name: project.task.burndown.chart.report.view.search
- Model: `project.task.burndown.chart.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `is_closed`, `milestone_id`, `partner_id`, `project_id`, `stage_id`, `tag_ids`, `user_ids`
- XPath or positional patches: 0

## Actions

- `action_project_task_burndown_chart_report`: `act_window` Burndown Chart

## Navigation

- **Parent:** [[docs/Community Addons/project/Views]]

