<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/iot_views.xml

- Module: [[docs/Enterprise Addons/quality_iot/quality_iot|quality_iot]]
- Scope: Enterprise Addons
- Source file: `views/iot_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `quality_point_view_tree`
- Name: quality.point.view.list.inherit.quality.iot
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `quality.quality_point_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `device_id`
- XPath or positional patches: 1

### `quality_point_view_form_inherit_quality_control_iot`
- Name: quality.point.view.form.inherit.iot.quality.control
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `quality.quality_point_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `device_id`
- XPath or positional patches: 1

### `iot_device_view_form_inherit`
- Name: iot.device.view.form.inherit
- Model: `iot.device`
- Type: inferred from arch
- Inherits: `iot.iot_device_view_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `name`, `picking_type_ids`, `product_ids`, `qcp_test_type`, `quality_point_ids`, `title`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_iot/Views]]

<!-- GENERATED:VIEWFILE -->
