<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/fleet_vehicle_cost_views.xml

- Module: [[docs/Community Addons/fleet/fleet|fleet]]
- Scope: Community Addons
- Source file: `views/fleet_vehicle_cost_views.xml`
- Views: 14
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `fleet_vehicle_log_services_view_search`
- Name: fleet.vehicle.log.services.search
- Model: `fleet.vehicle.log.services`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `description`, `service_type_id`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_log_services_view_pivot`
- Name: unnamed
- Model: `fleet.vehicle.log.services`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `amount`, `currency_id`, `service_type_id`, `vehicle_id`, `vendor_id`
- XPath or positional patches: 0

### `fleet_vehicle_log_services_view_activity`
- Name: unnamed
- Model: `fleet.vehicle.log.services`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 2
- Sample fields: `description`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_log_services_view_graph`
- Name: fleet.vehicle.log.services.graph
- Model: `fleet.vehicle.log.services`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `amount`, `date`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_log_services_view_kanban`
- Name: fleet.vehicle.log.services.kanban
- Model: `fleet.vehicle.log.services`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `activity_ids`, `amount`, `currency_id`, `date`, `purchaser_id`, `service_type_id`, `state`, `vehicle_id`, `vendor_id`
- XPath or positional patches: 0

### `fleet_vehicle_log_services_view_tree`
- Name: fleet.vehicle.log.services.list
- Model: `fleet.vehicle.log.services`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `amount`, `currency_id`, `date`, `description`, `inv_ref`, `notes`, `purchaser_id`, `service_type_id`, `state`, `vehicle_id`, and 1 more
- XPath or positional patches: 0

### `fleet_vehicle_log_services_view_form`
- Name: fleet.vehicle.log.services.form
- Model: `fleet.vehicle.log.services`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `active`, `amount`, `currency_id`, `date`, `description`, `notes`, `odometer`, `odometer_unit`, `purchaser_id`, `service_type_id`, and 3 more
- XPath or positional patches: 0

### `fleet_vehicle_log_contract_view_pivot`
- Name: unnamed
- Model: `fleet.vehicle.log.contract`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `cost_subtype_id`, `expiration_date`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_log_contract_view_activity`
- Name: fleet.vehicle.log.contract.activity
- Model: `fleet.vehicle.log.contract`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 2
- Sample fields: `user_id`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_log_contract_view_search`
- Name: fleet.vehicle.log.contract.search
- Model: `fleet.vehicle.log.contract`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `activity_type_id`, `activity_user_id`, `insurer_id`, `purchaser_id`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_log_contract_view_graph`
- Name: fleet.vehicle.log.contract.graph
- Model: `fleet.vehicle.log.contract`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `amount`, `date`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_log_contract_view_kanban`
- Name: fleet.vehicle.log.contract.kanban
- Model: `fleet.vehicle.log.contract`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `expiration_date`, `insurer_id`, `start_date`, `state`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_log_contract_view_tree`
- Name: fleet.vehicle.log.contract.list
- Model: `fleet.vehicle.log.contract`
- Type: inferred from arch
- Root tag: `list`
- Field references: 14
- Sample fields: `active`, `activity_exception_decoration`, `cost_frequency`, `cost_generated`, `currency_id`, `days_left`, `expiration_date`, `expires_today`, `insurer_id`, `name`, and 4 more
- XPath or positional patches: 0

### `fleet_vehicle_log_contract_view_form`
- Name: fleet.vehicle.log_contract.form
- Model: `fleet.vehicle.log.contract`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `active`, `amount`, `company_id`, `cost_frequency`, `cost_generated`, `cost_subtype_id`, `currency_id`, `date`, `expiration_date`, `ins_ref`, and 9 more
- XPath or positional patches: 0

## Actions

- `fleet_vehicle_log_services_action`: `act_window` Services
- `fleet_vehicle_log_contract_action`: `act_window` Contracts

## Menus

- `fleet_vehicle_log_services_menu`: unnamed
- `fleet_vehicle_log_contract_menu`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/fleet/Views]]

<!-- GENERATED:VIEWFILE -->
