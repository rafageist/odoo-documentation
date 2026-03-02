<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# stock.picking

- Module: [[docs/Enterprise Addons/sale_shopee/sale_shopee|sale_shopee]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/stock_picking.py`
- Python classes: `StockPicking`

## Field footprint

- Detected fields: 4
- Field types: `Char` x 1, `Datetime` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `last_picking_sync_date`: `Datetime`
- `shopee_delivery_status`: `Selection` (related `sale_id.shopee_delivery_status`)
- `shopee_label_status`: `Selection`
- `shopee_order_ref`: `Char` (related `sale_id.shopee_order_ref`)

## Method hints

- Detected methods: 9
- Action methods: `action_shopee_sync_pickings`
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_shopee/Models]]

<!-- GENERATED:MODEL -->
