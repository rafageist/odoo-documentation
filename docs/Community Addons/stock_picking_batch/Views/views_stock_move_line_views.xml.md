<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_move_line_views.xml

- Module: [[docs/Community Addons/stock_picking_batch/stock_picking_batch|stock_picking_batch]]
- Scope: Community Addons
- Source file: `views/stock_move_line_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_picking_internal_search_inherit`
- Name: stock.picking.internal.search.inherit
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_internal_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_move_line_tree_detailed_wave`
- Name: stock_picking_wave.move.line.list.wave
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_move_line_tree_detailed`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `batch_id`
- Buttons: `action_open_add_to_wave`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/stock_picking_batch/Views]]

<!-- GENERATED:VIEWFILE -->
