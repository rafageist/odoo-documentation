<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_hk_ir56b_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_hk_ir56b_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_hk_ir56b_view_tree`
- Name: l10n_hk.ir56b.view.list
- Model: `l10n_hk.ir56b`
- Type: inferred from arch
- Inherits: `l10n_hk_hr_payroll.l10n_hk_ird_view_list`
- Root tag: `list`
- Field references: 3
- Sample fields: `display_name`, `submission_date`, `type_of_form`
- XPath or positional patches: 1

### `l10n_hk_ir56b_view_form`
- Name: l10n_hk_ir56b.view.form
- Model: `l10n_hk.ir56b`
- Type: inferred from arch
- Inherits: `l10n_hk_hr_payroll.l10n_hk_ird_view_form`
- Root tag: `form`
- Field references: 2
- Sample fields: `end_month`, `end_year`
- Buttons: `action_generate_declarations`, `action_generate_xml`
- XPath or positional patches: 4

## Actions

- `l10n_hk_ir56b_action`: `act_window` IR56B Sheet

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
