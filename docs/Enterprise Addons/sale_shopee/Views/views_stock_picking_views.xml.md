---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Enterprise Addons/sale_shopee/sale_shopee|sale_shopee]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `picking_view_form`
- Name: shopee.picking.form
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `button`
- Field references: 2
- Sample fields: `origin`, `shopee_order_ref`
- Buttons: `action_cancel`, `action_shopee_sync_pickings`
- XPath or positional patches: 1

### `picking_list`
- Name: Shopee Picking List
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `field`
- Field references: 2
- Sample fields: `shopee_delivery_status`, `state`
- XPath or positional patches: 0

## Actions

- `action_fetch_shipping_label`: `server` Fetch Shipping Label

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_shopee/Views]]

