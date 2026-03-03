---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_hk_ir56e_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_hk_ir56e_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_hk_ir56e_view_tree`
- Name: l10n_hk.ir56e.view.list
- Model: `l10n_hk.ir56e`
- Type: inferred from arch
- Inherits: `l10n_hk_hr_payroll.l10n_hk_ird_view_list`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `l10n_hk_ir56e_view_form`
- Name: l10n_hk_ir56e.view.form
- Model: `l10n_hk.ir56e`
- Type: inferred from arch
- Inherits: `l10n_hk_hr_payroll.l10n_hk_ird_view_form`
- Root tag: `form`
- Field references: 2
- Sample fields: `type_of_form`, `year_of_employer_return`
- XPath or positional patches: 5

## Actions

- `l10n_hk_ir56e_action`: `act_window` IR56E Sheet

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Views]]

