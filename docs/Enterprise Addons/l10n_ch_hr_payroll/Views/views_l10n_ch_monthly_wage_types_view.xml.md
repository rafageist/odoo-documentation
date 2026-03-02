<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_monthly_wage_types_view.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_monthly_wage_types_view.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_l10n_ch_hr_contract_wage_tree`
- Name: l10n.ch.hr.contract.wage.tree
- Model: `l10n.ch.hr.contract.wage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `amount`, `date_start`, `input_type_id`, `uom`
- XPath or positional patches: 0

### `view_l10n_ch_hr_contract_wage_calendar`
- Name: l10n.ch.hr.contract.wage.calendar
- Model: `l10n.ch.hr.contract.wage`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 4
- Sample fields: `amount`, `description`, `input_type_id`, `version_id`
- XPath or positional patches: 0

### `view_l10n_ch_hr_contract_wage_form_calendar`
- Name: l10n.ch.hr.contract.wage.form.calendar
- Model: `l10n.ch.hr.contract.wage`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `amount`, `currency_id`, `date_start`, `description`, `input_type_id`, `uom`, `version_id`
- XPath or positional patches: 0

## Actions

- `action_l10n_ch_hr_contract_wage`: `act_window` Planned Wage Types

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
