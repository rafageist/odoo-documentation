---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_contract_wage_type_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll_elm_transmission_5_3/l10n_ch_hr_payroll_elm_transmission_5_3|l10n_ch_hr_payroll_elm_transmission_5_3]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_contract_wage_type_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_ch_hr_contract_wage_search_view`
- Name: l10n.ch.hr.contract.wage.search
- Model: `l10n.ch.hr.contract.wage`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `date_start`, `description`, `employee_id`, `input_type_id`, `type`, `uom`, `version_id`
- XPath or positional patches: 0

### `l10n_ch_hr_contract_wage_pivot_view`
- Name: l10n.ch.hr.contract.wage.pivot
- Model: `l10n.ch.hr.contract.wage`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `amount`, `date_start`, `employee_id`, `input_type_id`, `type`
- XPath or positional patches: 0

### `l10n_ch_hr_contract_wage_tree_view`
- Name: l10n.ch.hr.contract.wage.list
- Model: `l10n.ch.hr.contract.wage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `amount`, `date_start`, `description`, `employee_id`, `input_type_id`, `type`, `uom`, `version_id`
- XPath or positional patches: 0

## Actions

- `l10n_ch_hr_contract_wage_action`: `act_window` Monthly Recurring Wages

## Menus

- `l10n_ch_hr_global_contract_wage_menu`: Monthly Wage Types

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll_elm_transmission_5_3/Views]]

