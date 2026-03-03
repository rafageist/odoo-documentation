---
tags: [odoo, community, generated, views]
---

# views/subcontracting_portal_views.xml

- Module: [[docs/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]]
- Scope: Community Addons
- Source file: `views/subcontracting_portal_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `subcontracting_portal_production_form_view`
- Name: subcontracting.portal.production.view.form
- Model: `stock.picking`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `date`, `date_deadline`, `description_picking`, `id`, `move_ids`, `name`, `origin`, `product_id`, `product_qty`, `product_uom`, and 6 more
- Buttons: `action_show_details`, `action_show_subcontract_details`
- XPath or positional patches: 0

## Actions

- `subcontracting_portal_view_production_action`: `act_window` Subcontracting Portal

## Navigation

- **Parent:** [[docs/Community Addons/mrp_subcontracting/Views]]

