---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_be_onss_file_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_be_onss_file_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_onss_file_view_search`
- Name: l10n.be.onss.file.view.search
- Model: `l10n.be.onss.file`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `file_content`, `name`, `onss_declaration_id`
- XPath or positional patches: 0

### `l10n_be_onss_file_view_list`
- Name: l10n.be.onss.file.view.list
- Model: `l10n.be.onss.file`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `creation_date`, `declaration_type`, `employee_id`, `environment`, `expeditor_number`, `file`, `file_count`, `file_number`, `file_sequence`, `file_type`, and 2 more
- XPath or positional patches: 0

### `l10n_be_onss_file_view_form`
- Name: l10n.be.onss.file.view.form
- Model: `l10n.be.onss.file`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `creation_date`, `declaration_type`, `employee_id`, `environment`, `expeditor_number`, `file`, `file_content`, `file_count`, `file_number`, `file_sequence`, and 5 more
- XPath or positional patches: 0

## Actions

- `action_l10n_be_onss_file`: `act_window` ONSS Files

## Menus

- `menu_l10n_be_onss_file`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

