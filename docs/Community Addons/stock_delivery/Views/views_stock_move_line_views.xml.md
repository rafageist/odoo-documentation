---
tags: [odoo, community, generated, views]
---

# views/stock_move_line_views.xml

- Module: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]]
- Scope: Community Addons
- Source file: `views/stock_move_line_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_move_line_view_search_delivery`
- Name: stock.move.line.search.delivery
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.stock_move_line_view_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `carrier_id`
- XPath or positional patches: 2

### `stock_location_route_view_form_inherit_stock_delivery`
- Name: stock.route.form
- Model: `stock.route`
- Type: inferred from arch
- Inherits: `stock.stock_location_route_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `shipping_selectable`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/stock_delivery/Views]]

