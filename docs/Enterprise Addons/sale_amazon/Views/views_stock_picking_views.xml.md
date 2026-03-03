---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Enterprise Addons/sale_amazon/sale_amazon|sale_amazon]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `picking_view_form`
- Name: amazon.picking.form
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `button`
- Field references: 2
- Sample fields: `amazon_feed_ref`, `origin`
- Buttons: `action_confirm`, `action_retry_amazon_sync`
- XPath or positional patches: 1

### `picking_list`
- Name: Amazon Picking List
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `field`
- Field references: 3
- Sample fields: `amazon_feed_ref`, `amazon_sync_status`, `state`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_amazon/Views]]

