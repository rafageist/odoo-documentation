---
tags: [odoo, enterprise, generated, views]
---

# wizard/hr_tds_calculation.xml

- Module: [[docs/Enterprise Addons/l10n_in_hr_payroll/l10n_in_hr_payroll|l10n_in_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `wizard/hr_tds_calculation.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_in_tds_computation_wizard_view_form`
- Name: l10n.in.tds.computation.wizard.view.form
- Model: `l10n.in.tds.computation.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `cess`, `currency_id`, `rebate`, `standard_deduction`, `surcharge`, `tax_on_taxable_income`, `taxable_income`, `tds_monthly`, `total_income`, `total_tax`, and 1 more
- Buttons: `set_tds_on_contracts`
- XPath or positional patches: 0

## Actions

- `action_tds_calculation`: `act_window` Employee TDS Calculation

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_hr_payroll/Views]]

