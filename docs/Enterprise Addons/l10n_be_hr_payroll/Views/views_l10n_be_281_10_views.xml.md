<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_be_281_10_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_be_281_10_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_281_10_action_view_tree`
- Name: l10n_be.281_10.view.list
- Model: `l10n_be.281_10`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payroll_declaration_mixin_view_list`
- Root tag: `list`
- Field references: 4
- Sample fields: `is_test`, `type_sending`, `type_treatment`, `year`
- XPath or positional patches: 1

### `l10n_be_281_10_form_wizard`
- Name: l10n_be.281_10.form
- Model: `l10n_be.281_10`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payroll_declaration_mixin_view_form`
- Root tag: `form`
- Field references: 7
- Sample fields: `error_message`, `is_test`, `type_sending`, `type_treatment`, `xml_file`, `xml_validation_state`, `year`
- Buttons: `action_generate_xml`
- XPath or positional patches: 4

## Actions

- `l10n_be_281_10_action`: `act_window` Create 281.10 Form

## Menus

- `menu_l10n_be_l10n_be_281_10`: 281.10 Sheet

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
