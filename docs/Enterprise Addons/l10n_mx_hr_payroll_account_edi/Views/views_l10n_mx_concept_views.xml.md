---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_mx_concept_views.xml

- Module: [[docs/Enterprise Addons/l10n_mx_hr_payroll_account_edi/l10n_mx_hr_payroll_account_edi|l10n_mx_hr_payroll_account_edi]]
- Scope: Enterprise Addons
- Source file: `views/l10n_mx_concept_views.xml`
- Views: 3
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `view_l10n_mx_concept_filter`
- Name: l10n.mx.concept.select
- Model: `l10n.mx.concept`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `name`, `payroll_code`, `sat_code`
- XPath or positional patches: 0

### `view_l10n_mx_concept_form`
- Name: l10n.mx.concept.form
- Model: `l10n.mx.concept`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `cfdi_type`, `is_taxable`, `name`, `payroll_code`, `sat_code`
- XPath or positional patches: 0

### `view_l10n_mx_concept_list`
- Name: l10n.mx.concept.list
- Model: `l10n.mx.concept`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `cfdi_type`, `is_taxable`, `name`, `payroll_code`, `sat_code`
- XPath or positional patches: 0

## Actions

- `l10n_mx_action_concept`: `act_window` Concepts

## Menus

- `menu_l10n_mx_concept`: Concepts
- `menu_l10n_mx_hr_payroll_configuration`: Mexico

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_hr_payroll_account_edi/Views]]

