---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_hk_ir56f_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_hk_ir56f_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_hk_ir56f_view_tree`
- Name: l10n_hk.ir56f.view.list
- Model: `l10n_hk.ir56f`
- Type: inferred from arch
- Inherits: `l10n_hk_hr_payroll.l10n_hk_ird_view_list`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `l10n_hk_ir56f_view_form`
- Name: l10n_hk_ir56f.view.form
- Model: `l10n_hk.ir56f`
- Type: inferred from arch
- Inherits: `l10n_hk_hr_payroll.l10n_hk_ird_view_form`
- Root tag: `form`
- Field references: 0
- Buttons: `action_generate_xml`
- XPath or positional patches: 3

## Actions

- `l10n_hk_ir56f_action`: `act_window` IR56F Sheet

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Views]]

