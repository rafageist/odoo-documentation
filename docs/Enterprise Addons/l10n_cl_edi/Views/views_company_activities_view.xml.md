---
tags: [odoo, enterprise, generated, views]
---

# views/company_activities_view.xml

- Module: [[docs/Enterprise Addons/l10n_cl_edi/l10n_cl_edi|l10n_cl_edi]]
- Scope: Enterprise Addons
- Source file: `views/company_activities_view.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_partner_activities_tree`
- Name: l10n_cl.company.activities.list
- Model: `l10n_cl.company.activities`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `code`, `name`, `tax_category`
- XPath or positional patches: 0

### `view_partner_activities_form`
- Name: l10n_cl.company.activities.form
- Model: `l10n_cl.company.activities`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `active`, `code`, `name`, `tax_category`
- XPath or positional patches: 0

### `view_partner_activities_search`
- Name: l10n_cl.company.activities.search
- Model: `l10n_cl.company.activities`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `code`, `name`
- XPath or positional patches: 0

## Actions

- `act_partner_activities`: `act_window` SII Partner Activities

## Menus

- `menu_action_act_partner_activities`: SII Partner Activities

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_cl_edi/Views]]

