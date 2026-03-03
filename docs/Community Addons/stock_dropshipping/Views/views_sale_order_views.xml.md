---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/stock_dropshipping/stock_dropshipping|stock_dropshipping]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_order_form_inherit_sale_stock`
- Name: sale.order.form.sale.dropshipping
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_stock.view_order_form_inherit_sale_stock`
- Root tag: `button`
- Field references: 1
- Sample fields: `dropship_picking_count`
- Buttons: `action_view_delivery`, `action_view_dropship`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/stock_dropshipping/Views]]

