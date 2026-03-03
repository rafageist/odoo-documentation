---
tags: [odoo, community, generated, views]
---

# wizard/stock_picking_to_batch_views.xml

- Module: [[docs/Community Addons/stock_picking_batch/stock_picking_batch|stock_picking_batch]]
- Scope: Community Addons
- Source file: `wizard/stock_picking_to_batch_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `stock_picking_to_batch_form`
- Name: stock.picking.to.batch.form
- Model: `stock.picking.to.batch`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `batch_id`, `description`, `is_create_draft`, `mode`, `user_id`
- Buttons: `attach_pickings`
- XPath or positional patches: 0

## Actions

- `stock_picking_to_batch_action_stock_picking`: `act_window` Add to batch

## Navigation

- **Parent:** [[docs/Community Addons/stock_picking_batch/Views]]

