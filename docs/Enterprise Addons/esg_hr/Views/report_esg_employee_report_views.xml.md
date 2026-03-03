---
tags: [odoo, enterprise, generated, views]
---

# report/esg_employee_report_views.xml

- Module: [[docs/Enterprise Addons/esg_hr/esg_hr|esg_hr]]
- Scope: Enterprise Addons
- Source file: `report/esg_employee_report_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `esg_employee_report_pivot`
- Name: esg.employee.report.pivot
- Model: `esg.employee.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `count`, `job_id`, `sex`, `wage`
- XPath or positional patches: 0

### `esg_employee_report_graph`
- Name: esg.employee.report.graph
- Model: `esg.employee.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `leadership_level`, `sex`
- XPath or positional patches: 0

### `esg_employee_report_search`
- Name: esg.employee.report.search
- Model: `esg.employee.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `contract_type_id`, `department_id`
- XPath or positional patches: 0

## Actions

- `action_esg_employee_report_pay_gap`: `act_window` Pay Gap
- `action_esg_employee_report_sex_parity`: `act_window` Sex Parity

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg_hr/Views]]

