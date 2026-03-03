---
tags: [odoo, enterprise, generated, views]
---

# wizard/l10n_be_double_pay_recovery_wizard_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/l10n_be_double_pay_recovery_wizard_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_be_double_pay_recovery_wizard_view_form`
- Name: l10n.be.double.pay.recovery.wizard.view.form
- Model: `l10n.be.double.pay.recovery.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `amount`, `company_calendar`, `currency_id`, `double_pay_to_recover`, `employee_id`, `gross_salary`, `line_ids`, `months_count`, `months_count_description`, `occupation_rate`, and 2 more
- Buttons: `action_validate`
- XPath or positional patches: 0

## Actions

- `l10n_be_double_pay_recovery_wizard_action`: `act_window` Double Pay Recovery Computation

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

