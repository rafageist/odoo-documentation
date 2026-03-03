---
tags: [odoo, community, generated, views]
---

# views/maintenance_views.xml

- Module: [[docs/Community Addons/stock_maintenance/stock_maintenance|stock_maintenance]]
- Scope: Community Addons
- Source file: `views/maintenance_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `maintenance_stock_equipment_view_form`
- Name: equipment.form.stock.maintenance
- Model: `maintenance.equipment`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_view_form`
- Root tag: `button`
- Field references: 2
- Sample fields: `location_id`, `serial_no`
- Buttons: `%(maintenance.hr_equipment_request_action_from_equipment)d`, `action_open_matched_serial`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/stock_maintenance/Views]]

