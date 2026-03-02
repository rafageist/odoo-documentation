<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/fleet_vehicle_views.xml

- Module: [[docs/Community Addons/hr_fleet/hr_fleet|hr_fleet]]
- Scope: Community Addons
- Source file: `views/fleet_vehicle_views.xml`
- Views: 7
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_attachment_kanban_inherit_hr`
- Name: ir.attachment.kanban.inherit.hr
- Model: `ir.attachment`
- Type: inferred from arch
- Inherits: `mail.view_document_file_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `fleet_vehicle_view_tree_inherit_hr`
- Name: unnamed
- Model: `fleet.vehicle`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_view_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `driver_employee_id`, `driver_id`, `future_driver_employee_id`, `future_driver_id`
- XPath or positional patches: 0

### `fleet_vehicle_view_search_inherit_hr`
- Name: fleet.vehicle.search.inherit.hr
- Model: `fleet.vehicle`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_view_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `mobility_card`
- XPath or positional patches: 2

### `fleet_vehicle_view_form_inherit_hr`
- Name: fleet.vehicle.form.inherit.hr
- Model: `fleet.vehicle`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `driver_employee_id`, `future_driver_employee_id`, `mobility_card`
- Buttons: `action_open_employee`, `open_assignation_logs`
- XPath or positional patches: 2

### `fleet_vehicle_assignation_log_employee_view_list`
- Name: fleet.vehicle.assignation.log.view.list.inherit.hr.fleet
- Model: `fleet.vehicle.assignation.log`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_assignation_log_view_list`
- Root tag: `field`
- Field references: 3
- Sample fields: `attachment_number`, `date_end`, `driver_id`
- Buttons: `action_get_attachment_view`
- XPath or positional patches: 0

### `fleet_vehicle_assignation_log_view_list`
- Name: fleet.vehicle.assignation.log.view.list.inherit.hr.fleet
- Model: `fleet.vehicle.assignation.log`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_assignation_log_view_list`
- Root tag: `field`
- Field references: 5
- Sample fields: `attachment_number`, `date_end`, `driver_employee_id`, `driver_id`, `vehicle_id`
- Buttons: `action_get_attachment_view`
- XPath or positional patches: 0

### `fleet_vehicle_odometer_view_tree`
- Name: fleet.vehicle.odometer.view.list.inherit.hr.fleet
- Model: `fleet.vehicle.odometer`
- Type: inferred from arch
- Inherits: `fleet.fleet_vehicle_odometer_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `driver_employee_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/hr_fleet/Views]]

<!-- GENERATED:VIEWFILE -->
