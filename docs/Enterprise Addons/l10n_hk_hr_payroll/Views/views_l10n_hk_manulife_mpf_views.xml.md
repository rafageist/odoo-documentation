---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_hk_manulife_mpf_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_hk_manulife_mpf_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_hk_manulife_mpf_view_tree`
- Name: l10n_hk.manulife.mpf.view.list
- Model: `l10n_hk.manulife.mpf`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `display_name`, `month`, `year`
- XPath or positional patches: 0

### `l10n_hk_manulife_mpf_view_form`
- Name: l10n_hk.manulife.mpf.view.form
- Model: `l10n_hk.manulife.mpf`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `amount_surcharge`, `cheque_no`, `display_name`, `employee_id`, `line_ids`, `month`, `second_cheque_no`, `sequence_no`, `surcharge_percentage`, `xlsx_file`, and 2 more
- Buttons: `action_generat_xlsx`
- XPath or positional patches: 0

## Actions

- `l10n_hk_manulife_mpf_action`: `act_window` Manulife MPF Sheet

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Views]]

