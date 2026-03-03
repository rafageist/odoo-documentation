---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona_auto/l10n_be_hr_payroll_dimona_auto|l10n_be_hr_payroll_dimona_auto]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_employee_view_list`
- Name: hr.employee.view.list
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `job_id`, `l10n_be_dimona_next_action`
- XPath or positional patches: 0

### `hr_employee_view_search`
- Name: hr.employee.view.search
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

### `hr_employee_view_form`
- Name: hr.employee.view.form.inherit.l10n.be.hr.payroll
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `l10n_be_hr_payroll_dimona.hr_employee_view_form`
- Root tag: `button`
- Field references: 9
- Sample fields: `l10n_be_dimona_declaration_id`, `l10n_be_dimona_declaration_state`, `l10n_be_dimona_in_declaration_number`, `l10n_be_dimona_last_declaration_number`, `l10n_be_last_dimona_declaration_id`, `l10n_be_needs_dimona_cancel`, `l10n_be_needs_dimona_in`, `l10n_be_needs_dimona_out`, `l10n_be_needs_dimona_update`
- Buttons: `action_cancel_dimona`, `action_check_dimona`, `action_close_dimona`, `action_open_dimona`, `action_open_relation`, `action_update_dimona`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona_auto/Views]]

