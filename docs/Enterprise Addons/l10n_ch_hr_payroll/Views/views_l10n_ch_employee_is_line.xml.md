<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_employee_is_line.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_employee_is_line.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_ch_employee_is_manual_correction_form`
- Name: hr.employee.is.line.correction.view.form
- Model: `hr.employee.is.line.correction`
- Type: inferred from arch
- Root tag: `form`
- Field references: 20
- Sample fields: `children`, `employee_id`, `insurance_days`, `l10n_ch_church_tax`, `l10n_ch_open_tax_scale`, `l10n_ch_pre_defined_tax_scale`, `l10n_ch_source_tax_canton`, `l10n_ch_source_tax_municipality`, `l10n_ch_tax_scale`, `l10n_ch_tax_scale_type`, and 10 more
- XPath or positional patches: 0

### `l10n_ch_employee_is_line_form`
- Name: hr.employee.is.line.view.form
- Model: `hr.employee.is.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 25
- Sample fields: `allowed_correction_payslips_ids`, `amount`, `code`, `corrected_slip_id`, `correction_method`, `correction_type`, `employee_id`, `is_code`, `is_ema_ids`, `is_log_line_ids`, and 15 more
- Buttons: `action_draft`, `action_pending`
- XPath or positional patches: 0

### `l10n_ch_employee_is_line_view_tree`
- Name: hr.employee.is.line.list
- Model: `hr.employee.is.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `correction_method`, `correction_type`, `employee_id`, `payslips_to_correct`, `reason`
- XPath or positional patches: 0

## Actions

- `action_l10n_ch_is_line`: `act_window` IS Line

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
