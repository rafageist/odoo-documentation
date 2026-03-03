---
tags: [odoo, enterprise, generated, views]
---

# views/delivery_carrier_views.xml

- Module: [[docs/Enterprise Addons/delivery_shiprocket/delivery_shiprocket|delivery_shiprocket]]
- Scope: Enterprise Addons
- Source file: `views/delivery_carrier_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_delivery_carrier_form_inherit_delivery_shiprocket`
- Name: delivery.carrier.form.inherit.delivery.shiprocket
- Model: `delivery.carrier`
- Type: inferred from arch
- Inherits: `delivery.view_delivery_carrier_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `shiprocket_channel_id`, `shiprocket_courier_ids`, `shiprocket_default_package_type_id`, `shiprocket_email`, `shiprocket_manifests_generate`, `shiprocket_password`, `shiprocket_pickup_request`
- Buttons: `action_get_channels`, `action_get_couriers`, `action_shiprocket_test_connection`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_shiprocket/Views]]

