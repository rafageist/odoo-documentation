---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_sickness_insurance_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_sickness_insurance_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_ch_sickness_insurance_line_view_form`
- Name: l10n.ch.sickness.insurance.line.view.form
- Model: `l10n.ch.sickness.insurance.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `date_from`, `date_to`, `employer_part`, `female_rate`, `male_rate`, `rate_ids`, `solution_name`, `solution_number`, `solution_type`, `wage_from`, and 1 more
- XPath or positional patches: 0

### `l10n_ch_sickness_insurance_view_form`
- Name: l10n.ch.sickness.insurance.view.form
- Model: `l10n.ch.sickness.insurance`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `company_id`, `contract_number`, `customer_number`, `insurance_code`, `line_ids`, `name`, `rate_ids`, `solution_name`, `solution_number`, `solution_type`
- XPath or positional patches: 0

### `l10n_ch_sickness_insurance_view_tree`
- Name: l10n.ch.sickness.insurance.view.list
- Model: `l10n.ch.sickness.insurance`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `contract_number`, `customer_number`, `name`
- XPath or positional patches: 0

## Actions

- `action_l10n_ch_sickness_insurance`: `act_window` Sickness Insurances

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

