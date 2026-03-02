<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_be_onss_declaration_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_be_onss_declaration_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_onss_declaration_view_list`
- Name: l10n.be.onss.declaration.view.list
- Model: `l10n.be.onss.declaration`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `dmfa_id`, `environment`, `onss_file_count`, `state`
- XPath or positional patches: 0

### `l10n_be_onss_declaration_view_form`
- Name: l10n.be.onss.declaration.view.form
- Model: `l10n.be.onss.declaration`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `dmfa_id`, `environment`, `error_message`, `onss_file_count`, `state`
- Buttons: `action_open_onss_file`, `action_post`, `action_test_sftp_connection`
- XPath or positional patches: 1

## Actions

- `action_l10n_be_onss_declaration`: `act_window` ONSS Declarations

## Menus

- `menu_l10n_be_onss_declaration`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
