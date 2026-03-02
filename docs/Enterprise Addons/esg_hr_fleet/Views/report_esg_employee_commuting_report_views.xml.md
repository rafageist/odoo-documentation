<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/esg_employee_commuting_report_views.xml

- Module: [[docs/Enterprise Addons/esg_hr_fleet/esg_hr_fleet|esg_hr_fleet]]
- Scope: Enterprise Addons
- Source file: `report/esg_employee_commuting_report_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `employee_commuting_report_pivot`
- Name: employee_commuting.report.pivot
- Model: `esg.employee.commuting.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `date_from`, `driver_id`, `total_co2`, `total_distance`
- XPath or positional patches: 0

### `action_employee_commuting_report_search`
- Name: employee_commuting.report.search
- Model: `esg.employee.commuting.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `driver_id`, `vehicle_id`
- XPath or positional patches: 0

## Actions

- `action_employee_commuting_report_views`: `act_window` Employee Commuting

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg_hr_fleet/Views]]

<!-- GENERATED:VIEWFILE -->
