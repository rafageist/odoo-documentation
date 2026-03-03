---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_co_dian_operation_mode.xml

- Module: [[docs/Enterprise Addons/l10n_co_dian/l10n_co_dian|l10n_co_dian]]
- Scope: Enterprise Addons
- Source file: `views/l10n_co_dian_operation_mode.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_co_dian_operation_mode_view_tree`
- Name: l10n_co_dian.operation_mode.view.list
- Model: `l10n_co_dian.operation_mode`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `dian_software_id`, `dian_software_operation_mode`, `dian_software_security_code`, `dian_testing_id`
- Buttons: `unlink`
- XPath or positional patches: 0

### `l10n_co_dian_operation_mode_view_search`
- Name: l10n_co_dian.operation_mode.view.search
- Model: `l10n_co_dian.operation_mode`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `dian_software_security_code`
- XPath or positional patches: 0

### `l10n_co_dian_operation_mode_view_form`
- Name: l10n_co_dian.operation_mode.view.form
- Model: `l10n_co_dian.operation_mode`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `dian_software_id`, `dian_software_operation_mode`, `dian_software_security_code`, `dian_testing_id`
- XPath or positional patches: 0

## Actions

- `l10n_co_dian_operation_mode_action`: `act_window` l10n_co_dian.operation_mode.action

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_co_dian/Views]]

