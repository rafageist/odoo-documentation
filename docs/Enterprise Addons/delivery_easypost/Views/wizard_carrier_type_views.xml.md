---
tags: [odoo, enterprise, generated, views]
---

# wizard/carrier_type_views.xml

- Module: [[docs/Enterprise Addons/delivery_easypost/delivery_easypost|delivery_easypost]]
- Scope: Enterprise Addons
- Source file: `wizard/carrier_type_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_delivery_easypost_carrier_type`
- Name: EasyPost Select Carrier
- Model: `delivery.carrier.easypost`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `carrier_type`, `delivery_carrier_id`
- Buttons: `action_validate`
- XPath or positional patches: 0

## Actions

- `act_delivery_easypost_carrier_type`: `act_window` Select a carrier

## Navigation

- **Parent:** [[docs/Enterprise Addons/delivery_easypost/Views]]

