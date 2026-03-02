<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_hk_empf_contribution_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/l10n_hk_hr_payroll_empf|l10n_hk_hr_payroll_empf]]
- Scope: Enterprise Addons
- Source file: `views/l10n_hk_empf_contribution_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `l10n_hk_empf_contribution_report_form`
- Name: l10n_hk.empf.contribution.report.form
- Model: `l10n_hk.empf.contribution.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 26
- Sample fields: `basic_salary`, `contribution_end_date`, `contribution_line_ids`, `contribution_period_end`, `contribution_period_start`, `contribution_start_date`, `currency_id`, `eemc`, `eevc`, `employee_id`, and 16 more
- Buttons: `action_display_errors`, `action_draft`, `action_generate_report`, `action_validate`
- XPath or positional patches: 0

### `l10n_hk_empf_contribution_report_tree`
- Name: l10n_hk.empf.contribution.report.list
- Model: `l10n_hk.empf.contribution.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `display_name`, `state`
- XPath or positional patches: 0

## Actions

- `l10n_hk_empf_contribution_report_recompute_line`: `server` Recompute Contributions
- `l10n_hk_empf_action`: `act_window` eMPF Contributions

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/Views]]

<!-- GENERATED:VIEWFILE -->
