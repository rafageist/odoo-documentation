---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_employee_form`
- Name: hr.employee.form.inherit.l10n_hk_hr_payroll
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr_payroll.payroll_hr_employee_view_form`
- Root tag: `xpath`
- Field references: 17
- Sample fields: `l10n_hk_autopay_account_type`, `l10n_hk_autopay_email`, `l10n_hk_autopay_mobile`, `l10n_hk_autopay_ref`, `l10n_hk_autopay_svid`, `l10n_hk_given_name`, `l10n_hk_internet`, `l10n_hk_mpf_manulife_account`, `l10n_hk_mpf_vc_option`, `l10n_hk_mpf_vc_percentage`, and 7 more
- Buttons: `action_open_rentals`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Views]]

