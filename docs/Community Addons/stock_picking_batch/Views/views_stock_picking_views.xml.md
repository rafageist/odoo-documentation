<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Community Addons/stock_picking_batch/stock_picking_batch|stock_picking_batch]]
- Scope: Community Addons
- Source file: `views/stock_picking_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_picking_view_batch_tree_ref`
- Name: stock.picking.view.list.inherit.stock.picking.batch
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `batch_id`, `batch_sequence`, `company_id`, `priority`, `scheduled_date`
- XPath or positional patches: 1

### `vpicktree`
- Name: stock.picking.list.inherit.stock.picking.batch
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `field`
- Field references: 2
- Sample fields: `batch_id`, `picking_type_id`
- XPath or positional patches: 0

### `stock_picking_form_inherit`
- Name: stock.picking.form.inherit
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `div`
- Field references: 1
- Sample fields: `batch_id`
- Buttons: `action_view_batch`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/stock_picking_batch/Views]]

<!-- GENERATED:VIEWFILE -->
