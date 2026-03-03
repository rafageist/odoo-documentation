---
tags: [odoo, community, generated, views]
---

# wizard/stock_picking_return_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `wizard/stock_picking_return_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_stock_return_picking_form`
- Name: Return lines
- Model: `stock.return.picking`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `company_id`, `move_id`, `move_quantity`, `picking_id`, `product_id`, `product_return_moves`, `quantity`, `uom_id`
- Buttons: `action_create_exchanges`, `action_create_returns`, `action_create_returns_all`
- XPath or positional patches: 0

## Actions

- `act_stock_return_picking`: `act_window` Return

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

