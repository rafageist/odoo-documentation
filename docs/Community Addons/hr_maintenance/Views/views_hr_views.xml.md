<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_views.xml

- Module: [[docs/Community Addons/hr_maintenance/hr_maintenance|hr_maintenance]]
- Scope: Community Addons
- Source file: `views/hr_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_public_view_form`
- Name: hr.employee.public.form.inherit.maintenance
- Model: `hr.employee.public`
- Type: inferred from arch
- Inherits: `hr.hr_employee_public_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `employee_id`, `equipment_count`
- Buttons: `%(maintenance.hr_equipment_action)d`
- XPath or positional patches: 1

### `hr_employee_view_form`
- Name: hr.employee.view.form.inherit.maintenance
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `button`
- Field references: 1
- Sample fields: `equipment_count`
- Buttons: `%(maintenance.hr_equipment_action)d`, `action_open_versions`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/hr_maintenance/Views]]

<!-- GENERATED:VIEWFILE -->
