---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_be_dimona_declaration_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona_auto/l10n_be_hr_payroll_dimona_auto|l10n_be_hr_payroll_dimona_auto]]
- Scope: Enterprise Addons
- Source file: `views/l10n_be_dimona_declaration_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_dimona_declaration_view_search`
- Name: l10n.be.dimona.declaration.search
- Model: `l10n.be.dimona.declaration`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `company_id`, `employee_id`, `name`
- XPath or positional patches: 0

### `l10n_be_dimona_declaration_view_tree`
- Name: l10n.be.dimona.declaration.tree
- Model: `l10n.be.dimona.declaration`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `company_id`, `date_end`, `date_start`, `declaration_type`, `employee_id`, `name`, `period_id`, `state`, `version_id`
- XPath or positional patches: 0

### `l10n_be_dimona_declaration_view_form`
- Name: l10n.be.dimona.declaration.form
- Model: `l10n.be.dimona.declaration`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `company_id`, `content`, `date_end`, `date_start`, `declaration_type`, `employee_id`, `name`, `period_id`, `state`, `version_id`
- XPath or positional patches: 0

## Actions

- `l10n_be_dimona_declaration_action`: `act_window` Dimona Declarations

## Menus

- `menu_l10n_be_dimona_declaration`: Dimona Declarations

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona_auto/Views]]

