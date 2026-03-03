---
tags: [odoo, enterprise, generated, views]
---

# views/iot_views.xml

- Module: [[docs/Enterprise Addons/iot/iot|iot]]
- Scope: Enterprise Addons
- Source file: `views/iot_views.xml`
- Views: 9
- Actions: 4
- Menus: 6
- Rules: 0

## View records

### `act_report_xml_view_tree_iot`
- Name: ir.actions.report.list.iot
- Model: `ir.actions.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `model`, `name`, `report_type`
- XPath or positional patches: 0

### `act_report_xml_view_iot`
- Name: ir.actions.report.iot
- Model: `ir.actions.report`
- Type: inferred from arch
- Inherits: `base.act_report_xml_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `device_ids`, `report_type`
- XPath or positional patches: 0

### `iot_device_search`
- Name: iot.device.view.search
- Model: `iot.device`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `iot_id`, `name`, `type`
- XPath or positional patches: 0

### `iot_device_view_list`
- Name: iot.device.view.list
- Model: `iot.device`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `connected_status`, `identifier`, `iot_id`, `name`
- XPath or positional patches: 0

### `iot_device_view_kanban`
- Name: iot.device.view.kanban
- Model: `iot.device`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `connected_status`, `connection`, `iot_id`, `name`, `type`
- XPath or positional patches: 0

### `iot_device_view_form`
- Name: iot.device.view.form
- Model: `iot.device`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `connected_status`, `connection`, `display_url`, `identifier`, `iot_id`, `is_scanner`, `keyboard_layout`, `manufacturer`, `name`, `report_ids`, and 2 more
- Buttons: `test_device`
- XPath or positional patches: 0

### `iot_box_view_list`
- Name: iot.box.view.list
- Model: `iot.box`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `identifier`, `name`
- Buttons: `iot.action_discover_iot_boxes`
- XPath or positional patches: 0

### `iot_box_view_kanban`
- Name: iot.box.view.kanban
- Model: `iot.box`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `create_date`, `device_count`, `name`
- Buttons: `iot.action_discover_iot_boxes`
- XPath or positional patches: 0

### `iot_box_view_form`
- Name: iot.box.view.form
- Model: `iot.box`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `company_id`, `connected_status`, `connection`, `device_ids`, `drivers_auto_update`, `identifier`, `ip`, `name`, `ssl_certificate_end_date`, `type`, and 1 more
- Buttons: `open_homepage`
- XPath or positional patches: 0

## Actions

- `iot_device_action`: `act_window` Devices
- `iot_box_action`: `act_window` IoT Boxes
- `action_discover_iot_boxes`: `client` Discover IoT boxes
- `action_iot_delete_linked_devices_menu`: `client` reset.linked.printers

## Menus

- `iot_clear_selected_devices`: Reset Linked Printers
- `iot_settings_menu_action`: Reporting
- `view_iot_selected_printer_local_action`: Configuration
- `iot_device_menu_action`: unnamed
- `iot_box_menu_action`: unnamed
- `iot_menu_root`: IoT

## Navigation

- **Parent:** [[docs/Enterprise Addons/iot/Views]]

