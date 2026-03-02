<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_department_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]]
- Scope: Enterprise Addons
- Source file: `views/hr_department_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_department_view_form`
- Name: hr.department.view.form
- Model: `hr.department`
- Type: inferred from arch
- Inherits: `hr.view_department_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `hr_department_view_kanban`
- Name: hr.department.kanban.inherit
- Model: `hr.department`
- Type: inferred from arch
- Inherits: `hr.hr_department_view_kanban`
- Root tag: `data`
- Field references: 1
- Sample fields: `appraisals_to_process_count`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal/Views]]

<!-- GENERATED:VIEWFILE -->
