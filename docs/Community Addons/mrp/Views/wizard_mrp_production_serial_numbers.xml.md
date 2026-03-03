---
tags: [odoo, community, generated, views]
---

# wizard/mrp_production_serial_numbers.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `wizard/mrp_production_serial_numbers.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_mrp_production_serials_form`
- Name: mrp_production_serials
- Model: `mrp.production.serials`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `lot_name`, `lot_quantity`, `production_id`, `serial_numbers`
- Buttons: `action_apply`, `action_generate_serial_numbers`
- XPath or positional patches: 0

## Actions

- `action_assign_serial_numbers`: `act_window` Assign Serial Numbers

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

