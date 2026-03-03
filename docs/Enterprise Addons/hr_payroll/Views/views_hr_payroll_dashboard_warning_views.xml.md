---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payroll_dashboard_warning_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_payroll_dashboard_warning_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_payroll_dashboard_warning_view_search`
- Name: hr.payroll.dashboard.warning.search
- Model: `hr.payroll.dashboard.warning`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `hr_payroll_dashboard_warning_view_tree`
- Name: hr.payroll.dashboard.warning.list
- Model: `hr.payroll.dashboard.warning`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `color`, `country_id`, `name`, `sequence`
- XPath or positional patches: 0

### `hr_payroll_dashboard_warning_view_form`
- Name: hr.payroll.dashboard.warning.form
- Model: `hr.payroll.dashboard.warning`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `active`, `color`, `country_id`, `evaluation_code`, `name`
- XPath or positional patches: 0

## Actions

- `action_hr_payroll_dashboard_warning`: `act_window` Payroll Dashboard Warnings

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

