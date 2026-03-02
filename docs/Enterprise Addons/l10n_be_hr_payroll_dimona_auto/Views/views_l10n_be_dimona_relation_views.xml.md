<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_be_dimona_relation_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona_auto/l10n_be_hr_payroll_dimona_auto|l10n_be_hr_payroll_dimona_auto]]
- Scope: Enterprise Addons
- Source file: `views/l10n_be_dimona_relation_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_be_dimona_relation_view_search`
- Name: l10n.be.dimona.relation.search
- Model: `l10n.be.dimona.relation`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `company_id`, `employee_id`, `name`
- XPath or positional patches: 0

### `l10n_be_dimona_relation_view_tree`
- Name: l10n.be.dimona.relation.tree
- Model: `l10n.be.dimona.relation`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `company_id`, `date_end`, `date_start`, `employee_id`, `name`, `period_ids`
- XPath or positional patches: 0

### `l10n_be_dimona_relation_view_form`
- Name: l10n.be.dimona.relation.form
- Model: `l10n.be.dimona.relation`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `company_id`, `content`, `date_end`, `date_start`, `employee_id`, `name`, `period_count`
- Buttons: `action_open_periods`
- XPath or positional patches: 0

## Actions

- `l10n_be_dimona_relation_action`: `act_window` Dimona Relations

## Menus

- `menu_l10n_be_dimona_relation`: Dimona Relations

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona_auto/Views]]

<!-- GENERATED:VIEWFILE -->
