<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/mpf_scheme_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/l10n_hk_hr_payroll_empf|l10n_hk_hr_payroll_empf]]
- Scope: Enterprise Addons
- Source file: `views/mpf_scheme_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_hk_mpf_scheme_view_list`
- Name: l10n_hk.mpf.scheme.list
- Model: `l10n_hk.mpf.scheme`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `employer_account_number`, `name`, `registration_number`
- XPath or positional patches: 0

### `l10n_hk_mpf_scheme_view_form`
- Name: l10n_hk.mpf.scheme.form
- Model: `l10n_hk.mpf.scheme`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `contribution_frequency`, `employer_account_number`, `group_id`, `is_default`, `member_class_ids`, `name`, `payroll_group_ids`, `registration_number`
- Buttons: `action_open_employee_list`
- XPath or positional patches: 0

## Actions

- `action_l10n_hk_mpf_schemes`: `act_window` MPF Schemes

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/Views]]

<!-- GENERATED:VIEWFILE -->
