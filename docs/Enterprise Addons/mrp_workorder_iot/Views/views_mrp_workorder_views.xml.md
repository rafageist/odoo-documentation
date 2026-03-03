---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_workorder_views.xml

- Module: [[docs/Enterprise Addons/mrp_workorder_iot/mrp_workorder_iot|mrp_workorder_iot]]
- Scope: Enterprise Addons
- Source file: `views/mrp_workorder_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `iot_device_view_form`
- Name: iot.device.view.form.inherit.mrp.workorder.iot
- Model: `iot.device`
- Type: inferred from arch
- Inherits: `iot.iot_device_view_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `action`, `key`, `trigger_ids`, `workcenter_id`
- XPath or positional patches: 1

### `mrp_workcenter_view_form_iot`
- Name: mrp.workcenter.form.iot
- Model: `mrp.workcenter`
- Type: inferred from arch
- Inherits: `mrp.mrp_workcenter_view`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `action`, `device_id`, `key`, `sequence`, `trigger_ids`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_workorder_iot/Views]]

