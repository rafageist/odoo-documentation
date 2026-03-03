---
tags: [odoo, community, generated, views]
---

# views/stock_lot_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_lot_views.xml`
- Views: 4
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `search_product_lot_filter`
- Name: Production Lots Filter
- Model: `stock.lot`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `create_date`, `lot_properties`, `name`, `partner_ids`, `product_id`
- XPath or positional patches: 0

### `view_production_lot_kanban`
- Name: stock.production.lot.kanban
- Model: `stock.lot`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `activity_ids`, `lot_properties`, `name`, `product_id`
- XPath or positional patches: 0

### `view_production_lot_tree`
- Name: stock.production.lot.list
- Model: `stock.lot`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `activity_ids`, `company_id`, `create_date`, `lot_properties`, `name`, `partner_ids`, `product_id`, `product_qty`, `ref`
- XPath or positional patches: 0

### `view_production_lot_form`
- Name: stock.production.lot.form
- Model: `stock.lot`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `company_id`, `delivery_count`, `display_complete`, `location_id`, `lot_properties`, `name`, `note`, `partner_ids`, `product_id`, `product_qty`, and 2 more
- Buttons: `%(action_stock_report)d`, `action_lot_open_quants`, `action_lot_open_transfers`
- XPath or positional patches: 0

## Actions

- `action_product_production_lot_form`: `act_window` Lots/Serial Numbers
- `action_production_lot_form`: `act_window` Lots / Serial Numbers

## Menus

- `menu_action_production_lot_form`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

