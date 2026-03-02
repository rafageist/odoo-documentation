<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/fleet_vehicle_views.xml

- Module: [[docs/Community Addons/fleet/fleet|fleet]]
- Scope: Community Addons
- Source file: `views/fleet_vehicle_views.xml`
- Views: 18
- Actions: 6
- Menus: 8
- Rules: 0

## View records

### `fleet_vehicle_assignation_log_view_list`
- Name: fleet.vehicle.assignation.log.view.list
- Model: `fleet.vehicle.assignation.log`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `date_end`, `date_start`, `driver_id`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_tag_view_view_tree`
- Name: fleet.vehicle.tag.list
- Model: `fleet.vehicle.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `color`, `name`
- XPath or positional patches: 0

### `fleet_vehicle_tag_view_view_form`
- Name: fleet.vehicle.tag.form
- Model: `fleet.vehicle.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `fleet_vehicle_state_view_form`
- Name: fleet.vehicle.state.form
- Model: `fleet.vehicle.state`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `fold`, `name`, `sequence`
- XPath or positional patches: 0

### `fleet_vehicle_state_view_tree`
- Name: fleet.vehicle.state.list
- Model: `fleet.vehicle.state`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `fold`, `name`, `sequence`
- XPath or positional patches: 0

### `fleet_vehicle_service_types_view_search`
- Name: unnamed
- Model: `fleet.service.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `category`, `name`
- XPath or positional patches: 0

### `fleet_vehicle_service_types_view_tree`
- Name: fleet.service.type.list
- Model: `fleet.service.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `category`, `name`
- XPath or positional patches: 0

### `fleet_vehicle_odometer_view_graph`
- Name: fleet.vehicle.odometer.graph
- Model: `fleet.vehicle.odometer`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `value`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_odometer_view_search`
- Name: fleet.vehicle.odometer.search
- Model: `fleet.vehicle.odometer`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `date`, `driver_id`, `value`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_odometer_view_tree`
- Name: fleet.vehicle.odometer.list
- Model: `fleet.vehicle.odometer`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `date`, `driver_id`, `unit`, `value`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_odometer_view_form`
- Name: fleet.vehicle.odometer.form
- Model: `fleet.vehicle.odometer`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `date`, `unit`, `value`, `vehicle_id`
- XPath or positional patches: 0

### `fleet_vehicle_view_pivot`
- Name: unnamed
- Model: `fleet.vehicle`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `brand_id`, `license_plate`, `model_id`, `state_id`
- XPath or positional patches: 0

### `fleet_vehicle_view_activity`
- Name: fleet.vehicle.activity
- Model: `fleet.vehicle`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `id`, `license_plate`, `model_id`
- XPath or positional patches: 0

### `fleet_vehicle_view_kanban`
- Name: fleet.vehicle.kanban
- Model: `fleet.vehicle`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 12
- Sample fields: `activity_ids`, `contract_count`, `contract_renewal_due_soon`, `contract_renewal_overdue`, `driver_id`, `future_driver_id`, `image_128`, `license_plate`, `location`, `model_id`, and 2 more
- XPath or positional patches: 0

### `fleet_vehicle_view_form_quick_create`
- Name: fleet.vehicle.form.quick.create
- Model: `fleet.vehicle`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `license_plate`, `model_id`, `tag_ids`
- XPath or positional patches: 0

### `fleet_vehicle_view_search`
- Name: fleet.vehicle.search
- Model: `fleet.vehicle`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `license_plate`, `log_drivers`, `model_id`, `name`, `state_id`, `tag_ids`, `vehicle_properties`
- XPath or positional patches: 0

### `fleet_vehicle_view_tree`
- Name: fleet.vehicle.list
- Model: `fleet.vehicle`
- Type: inferred from arch
- Root tag: `list`
- Field references: 18
- Sample fields: `acquisition_date`, `active`, `activity_exception_decoration`, `category_id`, `co2`, `contract_renewal_due_soon`, `contract_renewal_overdue`, `contract_state`, `driver_id`, `future_driver_id`, and 8 more
- XPath or positional patches: 0

### `fleet_vehicle_view_form`
- Name: fleet.vehicle.form
- Model: `fleet.vehicle`
- Type: inferred from arch
- Root tag: `form`
- Field references: 54
- Sample fields: `acquisition_date`, `active`, `car_value`, `category_id`, `co2`, `co2_emission_unit`, `co2_standard`, `color`, `company_id`, `contract_count`, and 44 more
- Buttons: `action_accept_driver_change`, `action_open_odometer_report`, `open_assignation_logs`, `return_action_to_open`
- XPath or positional patches: 0

## Actions

- `action_fleet_vehicle_send_mail`: `server` Mail to Driver
- `fleet_vehicle_tag_action`: `act_window` Tags
- `fleet_vehicle_state_action`: `act_window` Status
- `fleet_vehicle_service_types_action`: `act_window` Types
- `fleet_vehicle_odometer_action`: `act_window` Odometers
- `fleet_vehicle_action`: `act_window` Vehicles

## Menus

- `fleet_vehicle_tag_menu`: unnamed
- `fleet_vehicle_state_menu`: unnamed
- `fleet_vehicles_configuration`: Vehicle
- `fleet_vehicle_service_types_menu`: Types
- `fleet_services_configuration`: Services
- `fleet_vehicle_odometer_menu`: unnamed
- `fleet_vehicle_menu`: Fleet
- `fleet_vehicles`: Fleet

## Navigation

- **Parent:** [[docs/Community Addons/fleet/Views]]

<!-- GENERATED:VIEWFILE -->
