---
tags: [odoo, community, generated, views]
---

# views/purchase_views.xml

- Module: [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]
- Scope: Community Addons
- Source file: `views/purchase_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `purchase_order_view_tree_inherit`
- Name: purchase.order.list.inherit
- Model: `purchase.order`
- Type: inferred from arch
- Inherits: `purchase.purchase_order_view_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `effective_date`, `invoice_status`, `receipt_status`
- XPath or positional patches: 1

### `purchase_order_line_view_form_inherit`
- Name: purchase.order.line.form.inherit
- Model: `purchase.order.line`
- Type: inferred from arch
- Inherits: `purchase.purchase_order_line_form2`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `move_ids`
- XPath or positional patches: 1

### `purchase_order_view_form_inherit`
- Name: purchase.order.form.inherit
- Model: `purchase.order`
- Type: inferred from arch
- Inherits: `purchase.purchase_order_form`
- Root tag: `xpath`
- Field references: 15
- Sample fields: `default_location_dest_id_usage`, `dest_address_id`, `effective_date`, `forecasted_issue`, `incoming_picking_count`, `incoterm_id`, `incoterm_location`, `invoice_status`, `is_shipped`, `move_dest_ids`, and 5 more
- Buttons: `%(action_purchase_vendor_delay_report)d`, `action_product_forecast_report`, `action_view_picking`
- XPath or positional patches: 15

## Navigation

- **Parent:** [[docs/Community Addons/purchase_stock/Views]]

