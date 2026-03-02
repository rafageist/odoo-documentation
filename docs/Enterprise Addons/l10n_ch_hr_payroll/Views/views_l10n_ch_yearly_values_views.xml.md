<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_yearly_values_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_yearly_values_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_l10n_ch_employee_yearly_values_search`
- Name: l10n.ch.employee.yearly.values.search
- Model: `l10n.ch.employee.yearly.values`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `employee_id`, `year`
- XPath or positional patches: 0

### `view_l10n_ch_employee_monthly_values_form`
- Name: l10n.ch.employee.monthly.values.form
- Model: `l10n.ch.employee.monthly.values`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `additional_particular`, `bvg_lpp_annual_basis`, `employee_meta_data`, `lpp_mutations`, `month`, `monthly_statistics`, `payroll_month_closed`, `person`, `yearly_values_id`
- XPath or positional patches: 0

### `view_l10n_ch_employee_yearly_values_form`
- Name: l10n.ch.employee.yearly.values.form
- Model: `l10n.ch.employee.yearly.values`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `employee_id`, `month`, `monthly_value_ids`, `year`
- XPath or positional patches: 0

### `view_l10n_ch_employee_yearly_values_tree`
- Name: l10n.ch.employee.yearly.values.tree
- Model: `l10n.ch.employee.yearly.values`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `employee_id`, `year`
- XPath or positional patches: 0

## Actions

- `action_l10n_ch_employee_yearly_values`: `act_window` Yearly Snapshot

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
