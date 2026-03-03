---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_accident_insurance_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_accident_insurance_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_ch_accident_insurance_group_view_form`
- Name: l10n.ch.accident.group.view.form
- Model: `l10n.ch.accident.group`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `date_from`, `date_to`, `employer_aanp_part`, `group_unit`, `line_ids`, `name`, `non_occupational_male_rate`, `occupational_male_rate`, `threshold`
- XPath or positional patches: 0

### `l10n_ch_accident_insurance_line_view_form`
- Name: l10n.ch.accident.insurance.line.view.form
- Model: `l10n.ch.accident.insurance.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `date_from`, `date_to`, `employer_non_occupational_part`, `employer_occupational_part`, `non_occupational_female_rate`, `non_occupational_male_rate`, `occupational_female_rate`, `occupational_male_rate`, `rate_ids`, `solution_name`, and 3 more
- XPath or positional patches: 0

### `l10n_ch_accident_insurance_view_form`
- Name: l10n.ch.accident.insurance.view.form
- Model: `l10n.ch.accident.insurance`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `company_id`, `contract_number`, `customer_number`, `group_unit`, `insurance_code`, `laa_group_ids`, `name`, `uid_bfs_number`
- XPath or positional patches: 0

### `l10n_ch_accident_insurance_view_tree`
- Name: l10n.ch.accident.insurance.view.list
- Model: `l10n.ch.accident.insurance`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `contract_number`, `customer_number`, `name`
- XPath or positional patches: 0

## Actions

- `action_l10n_ch_accident_insurance`: `act_window` LAA Insurances

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

