---
tags: [odoo, enterprise, generated, views]
---

# views/iot_views.xml

- Module: [[docs/Enterprise Addons/pos_iot/pos_iot|pos_iot]]
- Scope: Enterprise Addons
- Source file: `views/iot_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `pos_iot_inherit_device_view_form`
- Name: pos.iot.inherit.iot.device.view.form
- Model: `iot.device`
- Type: inferred from arch
- Inherits: `iot.iot_device_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `associated_pos_config_ids`
- XPath or positional patches: 1

### `pos_iot_inherit_device_view_kanban`
- Name: pos.iot.inherit.iot.device.view.kanban
- Model: `iot.device`
- Type: inferred from arch
- Inherits: `iot.iot_device_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `associated_pos_config_ids`
- XPath or positional patches: 1

### `pos_iot_inherit_iot_box_view_form`
- Name: pos.iot.inherit.iot.box.view.form
- Model: `iot.box`
- Type: inferred from arch
- Inherits: `iot.iot_box_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `associated_pos_config_ids`
- XPath or positional patches: 2

### `pos_iot_inherit_iot_box_view_kanban`
- Name: pos.iot.inherit.iot.box.view.kanban
- Model: `iot.box`
- Type: inferred from arch
- Inherits: `iot.iot_box_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `associated_pos_config_ids`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_iot/Views]]

