---
tags: [odoo, enterprise, generated, views]
---

# views/hr_work_entry_report_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_work_entry_report_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_work_entry_report_view_tree`
- Name: hr.work.entry.report.view.list
- Model: `hr.work.entry.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `date`, `department_id`, `employee_id`, `number_of_days`, `state`, `work_entry_type_id`
- XPath or positional patches: 0

### `hr_work_entry_report_view_pivot`
- Name: hr.work.entry.report.view.pivot
- Model: `hr.work.entry.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `number_of_days`, `work_entry_type_id`
- XPath or positional patches: 0

### `hr_work_entry_report_view_search`
- Name: hr.work.entry.report.view.search
- Model: `hr.work.entry.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `company_id`, `date`, `department_id`, `employee_id`, `state`, `work_entry_type_id`
- XPath or positional patches: 0

## Actions

- `hr_work_entry_report_action`: `act_window` Work Entries Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

