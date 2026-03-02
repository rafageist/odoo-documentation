<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_fleet/l10n_be_hr_payroll_fleet|l10n_be_hr_payroll_fleet]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_view_list`
- Name: hr.employee.list.view
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `car_id`
- XPath or positional patches: 1

### `hr_employee_view_form`
- Name: hr.employee.view.form
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.payroll_hr_employee_view_form`
- Root tag: `label`
- Field references: 11
- Sample fields: `bike_id`, `car_atn`, `car_id`, `fuel_type`, `new_bike`, `new_bike_model_id`, `new_car`, `new_car_model_id`, `ordered_car_id`, `transport_mode_bike`, and 1 more
- XPath or positional patches: 6

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_fleet/Views]]

<!-- GENERATED:VIEWFILE -->
