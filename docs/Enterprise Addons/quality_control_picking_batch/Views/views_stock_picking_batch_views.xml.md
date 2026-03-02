<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_batch_views.xml

- Module: [[docs/Enterprise Addons/quality_control_picking_batch/quality_control_picking_batch|quality_control_picking_batch]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_batch_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_line_tree`
- Name: stock_picking_batch.move.line.list.inherit
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock_picking_batch.view_move_line_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `check_state`
- Buttons: `action_open_quality_check_wizard`
- XPath or positional patches: 1

### `stock_picking_batch_form`
- Name: stock.picking.batch.form.quality.control.inherit
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `quality_check_todo`
- Buttons: `action_done`, `action_open_quality_check_wizard`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_control_picking_batch/Views]]

<!-- GENERATED:VIEWFILE -->
