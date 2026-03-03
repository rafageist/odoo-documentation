---
tags: [odoo, enterprise, generated, views]
---

# views/planning_slot_views.xml

- Module: [[docs/Enterprise Addons/project_timesheet_forecast_sale/project_timesheet_forecast_sale|project_timesheet_forecast_sale]]
- Scope: Enterprise Addons
- Source file: `views/planning_slot_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `planning_slot_view_form_inherit_project_timesheet_forecast_sale`
- Name: planning.slot.form.inherit.project.timesheet.forecast.sale
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `sale_planning.planning_slot_view_form_inherit_sale_planning`
- Root tag: `field`
- Field references: 1
- Sample fields: `sale_line_id`
- XPath or positional patches: 0

## Actions

- `project_timesheet_forecast.project_timesheet_action_schedule_by_role`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/project_timesheet_forecast_sale/Views]]

