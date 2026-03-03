---
tags: [odoo, community, generated, views]
---

# views/stock_move_views.xml

- Module: [[docs/Community Addons/stock_account/stock_account|stock_account]]
- Scope: Community Addons
- Source file: `views/stock_move_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `stock_move_view_list_valuation`
- Name: stock.move.view.list.valuation
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `date`, `lot_ids`, `product_uom`, `quantity`, `reference`, `remaining_qty`, `remaining_value`, `standard_price`, `value`
- XPath or positional patches: 0

### `stock_move_view_list`
- Name: stock.move.view.list.inherit.stock.account
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_move_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `remaining_qty`, `remaining_value`, `state`, `value`
- XPath or positional patches: 0

## Actions

- `stock_move_action_adjust_valuation`: `server` Adjust Valuation
- `stock_move_valuation_action`: `act_window` Valuation

## Navigation

- **Parent:** [[docs/Community Addons/stock_account/Views]]

