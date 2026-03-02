<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/fleet_vehicle_model_views.xml

- Module: [[docs/Community Addons/fleet/fleet|fleet]]
- Scope: Community Addons
- Source file: `views/fleet_vehicle_model_views.xml`
- Views: 10
- Actions: 3
- Menus: 6
- Rules: 0

## View records

### `fleet_vehicle_model_category_view_form`
- Name: fleet.vehicle.model.category.view.form
- Model: `fleet.vehicle.model.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `name`, `sequence`
- XPath or positional patches: 0

### `fleet_vehicle_model_category_view_tree`
- Name: fleet.vehicle.model.category.view.list
- Model: `fleet.vehicle.model.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `sequence`
- XPath or positional patches: 0

### `fleet_vehicle_model_brand_view_search`
- Name: fleet.vehicle.model.brand.view.search
- Model: `fleet.vehicle.model.brand`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `fleet_vehicle_model_brand_view_kanban`
- Name: fleet.vehicle.model.brandkanban
- Model: `fleet.vehicle.model.brand`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `active`, `image_128`, `model_count`, `name`
- XPath or positional patches: 0

### `fleet_vehicle_model_brand_view_form`
- Name: fleet.vehicle.model.brand.form
- Model: `fleet.vehicle.model.brand`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `image_128`, `model_count`, `name`
- Buttons: `action_brand_model`
- XPath or positional patches: 0

### `fleet_vehicle_model_brand_view_tree`
- Name: fleet.vehicle.model.brand.list
- Model: `fleet.vehicle.model.brand`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `model_count`, `name`
- XPath or positional patches: 0

### `fleet_vehicle_model_view_search`
- Name: fleet.vehicle.model.search
- Model: `fleet.vehicle.model`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `brand_id`, `name`
- XPath or positional patches: 0

### `fleet_vehicle_model_view_kanban`
- Name: fleet.vehicle.model.kanban
- Model: `fleet.vehicle.model`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `brand_id`, `name`
- XPath or positional patches: 0

### `fleet_vehicle_model_view_tree`
- Name: fleet.vehicle.model.list
- Model: `fleet.vehicle.model`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `brand_id`, `category_id`, `default_co2`, `name`, `vehicle_count`, `vehicle_type`
- XPath or positional patches: 0

### `fleet_vehicle_model_view_form`
- Name: fleet.vehicle.model.form
- Model: `fleet.vehicle.model`
- Type: inferred from arch
- Root tag: `form`
- Field references: 28
- Sample fields: `active`, `brand_id`, `category_id`, `co2_emission_unit`, `co2_standard`, `color`, `default_co2`, `default_fuel_type`, `doors`, `drive_type`, and 18 more
- Buttons: `action_model_vehicle`
- XPath or positional patches: 0

## Actions

- `fleet_vehicle_model_category_action`: `act_window` Categories
- `fleet_vehicle_model_brand_action`: `act_window` Manufacturers
- `fleet_vehicle_model_action`: `act_window` Models

## Menus

- `fleet_vehicle_model_category_menu`: unnamed
- `fleet_vehicle_model_menu`: unnamed
- `fleet_vehicle_model_brand_menu`: unnamed
- `fleet_models_configuration`: Models
- `fleet_configuration`: Configuration
- `menu_root`: Fleet

## Navigation

- **Parent:** [[docs/Community Addons/fleet/Views]]

<!-- GENERATED:VIEWFILE -->
