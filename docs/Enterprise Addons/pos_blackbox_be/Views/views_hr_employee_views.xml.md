<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/pos_blackbox_be/pos_blackbox_be|pos_blackbox_be]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_right_employee_insz_number`
- Name: unnamed
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr_employee_form_view`
- Root tag: `field`
- Field references: 1
- Sample fields: `insz_or_bis_number`
- XPath or positional patches: 0

### `hr_employee_form_view`
- Name: hr.employee.form.view
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `insz_or_bis_number`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_blackbox_be/Views]]

<!-- GENERATED:VIEWFILE -->
