---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_map_views.xml

- Module: [[docs/Enterprise Addons/stock_enterprise/stock_enterprise|stock_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_map_views.xml`
- Views: 1
- Actions: 5
- Menus: 0
- Rules: 0

## View records

### `stock_map_view`
- Name: stock.picking.view.map
- Model: `stock.picking`
- Type: inferred from arch
- Root tag: `map`
- Field references: 2
- Sample fields: `name`, `scheduled_date`
- XPath or positional patches: 0

## Actions

- `stock.action_picking_tree_ready`: `act_window`
- `stock.stock_picking_action_picking_type`: `act_window`
- `stock.action_picking_tree_late`: `act_window`
- `stock.action_picking_tree_all`: `act_window`
- `stock.action_picking_tree_waiting`: `act_window`

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_enterprise/Views]]

