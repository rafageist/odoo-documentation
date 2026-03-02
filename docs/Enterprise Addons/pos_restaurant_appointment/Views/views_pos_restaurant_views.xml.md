<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/pos_restaurant_views.xml

- Module: [[docs/Enterprise Addons/pos_restaurant_appointment/pos_restaurant_appointment|pos_restaurant_appointment]]
- Scope: Enterprise Addons
- Source file: `views/pos_restaurant_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_restaurant_floor_form`
- Name: Restaurant Floors
- Model: `restaurant.floor`
- Type: inferred from arch
- Inherits: `pos_restaurant.view_restaurant_floor_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `appointment_resource_id`
- XPath or positional patches: 1

### `view_restaurant_table_form`
- Name: Restaurant Table
- Model: `restaurant.table`
- Type: inferred from arch
- Inherits: `pos_restaurant.view_restaurant_table_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `appointment_resource_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_restaurant_appointment/Views]]

<!-- GENERATED:VIEWFILE -->
