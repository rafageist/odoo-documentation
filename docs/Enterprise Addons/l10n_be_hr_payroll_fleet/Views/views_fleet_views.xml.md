---
tags: [odoo, enterprise, generated, views]
---

# views/fleet_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_fleet/l10n_be_hr_payroll_fleet|l10n_be_hr_payroll_fleet]]
- Scope: Enterprise Addons
- Source file: `views/fleet_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `fleet_vehicle_model_view_search`
- Name: fleet.vehicle.model.search
- Model: `fleet.vehicle.model`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_model_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `fleet_vehicle_model_view_form`
- Name: fleet.vehicle.model.form
- Model: `fleet.vehicle.model`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_model_view_form`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `can_be_requested`, `co2_fee`, `current_country_code`, `default_atn`, `default_car_value`, `default_recurring_cost_amount_depreciated`, `default_total_depreciated_cost`, `tax_deduction`
- XPath or positional patches: 3

### `fleet_vehicle_model_view_tree`
- Name: fleet.vehicle.model.list
- Model: `fleet.vehicle.model`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_model_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `can_be_requested`
- XPath or positional patches: 1

### `fleet_vehicle_log_contract_view_form`
- Name: fleet.vehicle.log.contract.form
- Model: `fleet.vehicle.log.contract`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_log_contract_view_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `date`, `recurring_cost_amount_depreciated`
- XPath or positional patches: 0

### `fleet_vehicle_view_form`
- Name: fleet.vehicle.form
- Model: `fleet.vehicle`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_view_form`
- Root tag: `group`
- Field references: 5
- Sample fields: `atn`, `co2_fee`, `horsepower_tax`, `tax_deduction`, `total_depreciated_cost`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_fleet/Views]]

