<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_tax_views.xml

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_tax_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_tax_unit_tree`
- Name: account.tax.unit.list
- Model: `account.tax.unit`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `country_id`, `name`
- XPath or positional patches: 0

### `view_tax_unit_form`
- Name: account.tax.unit.form
- Model: `account.tax.unit`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `company_ids`, `country_id`, `fpos_synced`, `main_company_id`, `name`, `vat`
- Buttons: `action_sync_unit_fiscal_positions`
- XPath or positional patches: 0

## Actions

- `action_view_tax_units`: `act_window` Tax Units

## Menus

- `menu_view_tax_units`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Views]]

<!-- GENERATED:VIEWFILE -->
