<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ch_avs_income_splits_views.xml

- Module: [[docs/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ch_avs_income_splits_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_l10n_ch_avs_splits_form`
- Name: l10n.ch.avs.splits.form
- Model: `l10n.ch.avs.splits`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `additional_delivery_date`, `avs_split_lines`, `date_from`, `date_to`, `employee_id`, `income`, `income_to_split`, `state`, `year`
- Buttons: `action_cancel`, `action_confirm`
- XPath or positional patches: 0

### `view_l10n_ch_avs_splits_tree`
- Name: l10n.ch.avs.splits.tree
- Model: `l10n.ch.avs.splits`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `additional_delivery_date`, `employee_id`, `income_to_split`, `year`
- XPath or positional patches: 0

## Actions

- `action_l10n_ch_avs_splits`: `act_window` Negative AVS Salary Splitting

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ch_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
