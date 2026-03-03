---
tags: [odoo, enterprise, generated, views]
---

# views/vehicle_views.xml

- Module: [[docs/Enterprise Addons/l10n_pe_edi_stock/l10n_pe_edi_stock|l10n_pe_edi_stock]]
- Scope: Enterprise Addons
- Source file: `views/vehicle_views.xml`
- Views: 3
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `vehicle_tree_view`
- Name: vehicle.list
- Model: `l10n_pe_edi.vehicle`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `license_plate`, `name`, `operator_id`
- XPath or positional patches: 0

### `vehicle_search_view`
- Name: vehicle.search
- Model: `l10n_pe_edi.vehicle`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `license_plate`, `name`, `operator_id`
- XPath or positional patches: 0

### `vehicle_form_view`
- Name: vehicle.form
- Model: `l10n_pe_edi.vehicle`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `authorization_issuing_entity`, `authorization_issuing_entity_number`, `company_id`, `is_m1l`, `license_plate`, `name`, `operator_id`
- XPath or positional patches: 0

## Actions

- `l10n_pe_edi_vehicle_actions`: `act_window` Vehicles (PE)
- `vehicle_list_action`: `act_window` vehicles

## Menus

- `menu_stock_pe_vehicles`: Vehicles
- `menu_stock_config_settings_pe`: Peru

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_pe_edi_stock/Views]]

