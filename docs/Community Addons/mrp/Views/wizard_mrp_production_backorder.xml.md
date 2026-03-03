---
tags: [odoo, community, generated, views]
---

# wizard/mrp_production_backorder.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `wizard/mrp_production_backorder.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_mrp_production_backorder_form`
- Name: Create Backorder
- Model: `mrp.production.backorder`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `mrp_production_backorder_line_ids`, `mrp_production_id`, `show_backorder_lines`, `to_backorder`
- Buttons: `action_backorder`, `action_close_mo`
- XPath or positional patches: 0

## Actions

- `action_mrp_production_backorder`: `act_window` You produced less than the initial demand

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

