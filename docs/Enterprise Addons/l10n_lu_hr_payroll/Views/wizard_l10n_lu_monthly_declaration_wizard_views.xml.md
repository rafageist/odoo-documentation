---
tags: [odoo, enterprise, generated, views]
---

# wizard/l10n_lu_monthly_declaration_wizard_views.xml

- Module: [[docs/Enterprise Addons/l10n_lu_hr_payroll/l10n_lu_hr_payroll|l10n_lu_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/l10n_lu_monthly_declaration_wizard_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_lu_monthly_declaration_view_form`
- Name: unnamed
- Model: `l10n.lu.monthly.declaration.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `amount`, `currency_id`, `decsal_file`, `decsal_name`, `employee_id`, `hours`, `month`, `payslip_id`, `situational_unemployment_ids`, `year`
- Buttons: `action_generate_declaration`
- XPath or positional patches: 0

## Actions

- `l10n_lu_hr_payroll_monthly_declaration_action`: `act_window` Monthly Salary Declaration (DECSAL)

## Menus

- `menu_l10n_lu_hr_payroll_monthly_declaration`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_lu_hr_payroll/Views]]

