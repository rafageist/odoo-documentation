<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/employee_views.xml

- Module: [[docs/Community Addons/hr_fleet/hr_fleet|hr_fleet]]
- Scope: Community Addons
- Source file: `views/employee_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_employee_filter`
- Name: hr.employee.filter.inherit.hr.fleet
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `license_plate`
- XPath or positional patches: 1

### `view_employee_form`
- Name: hr.employee.form.inherit.hr.fleet
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `button`
- Field references: 2
- Sample fields: `employee_cars_count`, `mobility_card`
- Buttons: `action_open_employee_cars`, `action_open_versions`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/hr_fleet/Views]]

<!-- GENERATED:VIEWFILE -->
