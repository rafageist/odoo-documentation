<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/fleet_vehicle_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_fiscal_categories_fleet/l10n_be_fiscal_categories_fleet|l10n_be_fiscal_categories_fleet]]
- Scope: Enterprise Addons
- Source file: `views/fleet_vehicle_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `l10n_be_disallowed_expenses_view_tree`
- Name: fleet.disallowed.expenses.rate.list
- Model: `fleet.disallowed.expenses.rate`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `date_from`, `rate`, `tax_deduction`
- XPath or positional patches: 0

### `fleet_vehicle_view_form`
- Name: fleet.vehicle.form
- Model: `fleet.vehicle`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_view_form`
- Root tag: `div`
- Field references: 0
- Buttons: `action_view_disallowed_expenses_rate`
- XPath or positional patches: 2

## Actions

- `action_view_disallowed_expenses_rate`: `act_window` Disallowed Expenses Rate History

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_fiscal_categories_fleet/Views]]

<!-- GENERATED:VIEWFILE -->
