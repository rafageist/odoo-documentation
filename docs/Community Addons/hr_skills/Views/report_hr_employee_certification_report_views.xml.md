<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/hr_employee_certification_report_views.xml

- Module: [[docs/Community Addons/hr_skills/hr_skills|hr_skills]]
- Scope: Community Addons
- Source file: `report/hr_employee_certification_report_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `hr_employee_certification_report_view_search`
- Name: unnamed
- Model: `hr.employee.certification.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `department_id`, `employee_id`, `skill_id`, `skill_type_id`
- XPath or positional patches: 0

### `hr_employee_certification_report_view_list`
- Name: unnamed
- Model: `hr.employee.certification.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `employee_id`, `level_progress`, `skill_id`, `skill_level`, `skill_type_id`
- XPath or positional patches: 0

### `hr_employee_certification_report_view_pivot`
- Name: unnamed
- Model: `hr.employee.certification.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `employee_id`, `level_progress`, `skill_id`, `skill_type_id`
- XPath or positional patches: 0

## Actions

- `hr_employee_certification_report_action`: `act_window` Certification

## Menus

- `hr_employee_certification_report_menu`: Certifications

## Navigation

- **Parent:** [[docs/Community Addons/hr_skills/Views]]

<!-- GENERATED:VIEWFILE -->
