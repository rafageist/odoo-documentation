---
tags: [odoo, community, generated, views]
---

# views/mrp_production_views.xml

- Module: [[docs/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]]
- Scope: Community Addons
- Source file: `views/mrp_production_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mrp_production_subcontracting_filter`
- Name: mrp.production.subcontracting.select
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.view_mrp_production_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 1

### `mrp_production_subcontracting_tree_view`
- Name: mrp.production.subcontracting.list
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_tree_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `incoming_picking`
- XPath or positional patches: 3

### `mrp_production_subcontracting_portal_form_view`
- Name: mrp.production.subcontracting.portal.form.view
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp_production_subcontracting_form_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `bom_product_ids`, `move_line_raw_ids`
- XPath or positional patches: 4

### `mrp_production_subcontracting_form_view`
- Name: mrp.production.subcontracting.form.view
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_form_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `product_qty`, `state`
- XPath or positional patches: 22

## Navigation

- **Parent:** [[docs/Community Addons/mrp_subcontracting/Views]]

