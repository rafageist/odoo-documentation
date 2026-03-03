---
tags: [odoo, community, generated, views]
---

# views/purchase_views.xml

- Module: [[docs/Community Addons/purchase_requisition/purchase_requisition|purchase_requisition]]
- Scope: Community Addons
- Source file: `views/purchase_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `purchase_order_line_compare_tree`
- Name: purchase.order.line.compare.list
- Model: `purchase.order.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `company_currency_id`, `currency_id`, `date_planned`, `name`, `order_id`, `partner_id`, `price_subtotal`, `price_total_cc`, `price_unit`, `product_id`, and 3 more
- Buttons: `action_choose`, `action_clear_quantities`
- XPath or positional patches: 0

### `purchase_order_search_inherit`
- Name: purchase.order.list.select.inherit
- Model: `purchase.order`
- Type: inferred from arch
- Inherits: `purchase.view_purchase_order_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `product_id`, `requisition_id`
- XPath or positional patches: 1

### `purchase_order_form_inherit`
- Name: purchase.order.form.inherit
- Model: `purchase.order`
- Type: inferred from arch
- Inherits: `purchase.purchase_order_form`
- Root tag: `field`
- Field references: 12
- Sample fields: `alternative_po_ids`, `amount_total`, `amount_total_cc`, `company_currency_id`, `currency_id`, `date_planned`, `name`, `partner_id`, `partner_ref`, `requisition_id`, and 2 more
- Buttons: `action_compare_alternative_lines`, `action_create_alternative`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/purchase_requisition/Views]]

