<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona/l10n_be_hr_payroll_dimona|l10n_be_hr_payroll_dimona]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_view_form`
- Name: hr.employee.view.form.inherit.l10n.be.hr.payroll
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.payroll_hr_employee_view_form`
- Root tag: `header`
- Field references: 5
- Sample fields: `l10n_be_dimona_declaration_state`, `l10n_be_dimona_in_declaration_number`, `l10n_be_dimona_last_declaration_number`, `l10n_be_dimona_planned_hours`, `l10n_be_is_student`
- Buttons: `action_check_dimona`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona/Views]]

<!-- GENERATED:VIEWFILE -->
