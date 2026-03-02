<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_be_dimona_period_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona_auto/l10n_be_hr_payroll_dimona_auto|l10n_be_hr_payroll_dimona_auto]]
- Scope: Enterprise Addons
- Source file: `views/l10n_be_dimona_period_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_dimona_period_view_search`
- Name: l10n.be.dimona.period.search
- Model: `l10n.be.dimona.period`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `company_id`, `employee_id`, `name`
- XPath or positional patches: 0

### `l10n_be_dimona_period_view_tree`
- Name: l10n.be.dimona.period.tree
- Model: `l10n.be.dimona.period`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `date_end`, `date_start`, `declaration_ids`, `employee_id`, `name`, `relation_id`
- XPath or positional patches: 0

### `l10n_be_dimona_period_view_form`
- Name: l10n.be.dimona.period.form
- Model: `l10n.be.dimona.period`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `company_id`, `content`, `date_end`, `date_start`, `declaration_count`, `employee_id`, `name`
- Buttons: `action_open_declarations`
- XPath or positional patches: 0

## Actions

- `l10n_be_dimona_period_action`: `act_window` Dimona Periods

## Menus

- `menu_l10n_be_dimona_period`: Dimona Periods

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona_auto/Views]]

<!-- GENERATED:VIEWFILE -->
