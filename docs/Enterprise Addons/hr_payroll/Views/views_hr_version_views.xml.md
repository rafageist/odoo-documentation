<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_version_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_version_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_version_search_view`
- Name: hr.version.search.fix
- Model: `hr.version`
- Type: inferred from arch
- Inherits: `hr.hr_version_search_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

### `payroll_hr_version_list_view_filter_payrun`
- Name: payroll.hr.version.view.list.filter.payrun
- Model: `hr.version`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `company_id`, `department_id`, `employee_id`, `job_id`, `resource_calendar_id`
- XPath or positional patches: 0

### `payroll_hr_version_list_view_payrun`
- Name: payroll.hr.version.view.list.payrun
- Model: `hr.version`
- Type: inferred from arch
- Root tag: `list`
- Field references: 17
- Sample fields: `company_id`, `contract_date_end`, `contract_date_start`, `contract_type_id`, `create_date`, `create_uid`, `currency_id`, `date_version`, `department_id`, `employee_id`, and 7 more
- XPath or positional patches: 0

## Actions

- `action_payroll_hr_version_list_view_payrun`: `act_window` Select Employees

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
