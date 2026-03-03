---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/l10n_hk_hr_payroll_empf|l10n_hk_hr_payroll_empf]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_employee_tree`
- Name: hr.employee.tree.inherit.l10n_hk_hr_payroll_empf
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `l10n_hk_mpf_scheme_id`, `l10n_hk_payroll_group_id`, `parent_id`
- XPath or positional patches: 0

### `view_employee_form`
- Name: hr.employee.form.inherit.l10n_hk_hr_payroll_empf
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `l10n_hk_hr_payroll.view_employee_form`
- Root tag: `label`
- Field references: 15
- Sample fields: `l10n_hk_member_class_id`, `l10n_hk_mpf_account_number`, `l10n_hk_mpf_contribution_start`, `l10n_hk_mpf_exempt`, `l10n_hk_mpf_manulife_account`, `l10n_hk_mpf_registration_status`, `l10n_hk_mpf_scheme_id`, `l10n_hk_mpf_scheme_join_date`, `l10n_hk_mpf_vc_option`, `l10n_hk_mpf_vc_percentage`, and 5 more
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll_empf/Views]]

