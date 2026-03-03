---
tags: [odoo, enterprise, generated, views]
---

# wizard/l10n_be_eco_vouchers_wizard_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/l10n_be_eco_vouchers_wizard_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_eco_vouchers_wizard_view_form`
- Name: l10n.be.eco.vouchers.wizard.view.form
- Model: `l10n.be.eco.vouchers.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `amount`, `company_id`, `currency_id`, `employee_id`, `line_ids`, `niss`, `reference_period`, `reference_year`
- Buttons: `action_export_xls`, `generate_payslips`
- XPath or positional patches: 0

## Actions

- `l10n_be_eco_vouchers_wizard_action`: `act_window` Eco-Vouchers

## Menus

- `menu_l10n_be_eco_vouchers_wizard`: Eco-Vouchers

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

