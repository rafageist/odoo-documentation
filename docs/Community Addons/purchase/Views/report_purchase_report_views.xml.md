<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/purchase_report_views.xml

- Module: [[docs/Community Addons/purchase/purchase|purchase]]
- Scope: Community Addons
- Source file: `report/purchase_report_views.xml`
- Views: 4
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `view_purchase_order_search`
- Name: report.purchase.order.search
- Model: `purchase.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `category_id`, `company_id`, `date_approve`, `date_order`, `partner_id`, `product_id`, `user_id`
- XPath or positional patches: 0

### `purchase_report_view_tree`
- Name: purchase.report.view.list
- Model: `purchase.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 14
- Sample fields: `category_id`, `company_id`, `currency_id`, `date_order`, `order_id`, `partner_id`, `price_total`, `product_id`, `qty_billed`, `qty_ordered`, and 4 more
- XPath or positional patches: 0

### `view_purchase_order_graph`
- Name: product.month.graph
- Model: `purchase.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `date_approve`, `untaxed_total`
- XPath or positional patches: 0

### `view_purchase_order_pivot`
- Name: product.month.pivot
- Model: `purchase.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `category_id`, `order_id`, `price_total`, `untaxed_total`
- XPath or positional patches: 0

## Actions

- `action_purchase_order_report_all`: `act_window` Purchase Analysis

## Menus

- `purchase_report`: Purchase
- `purchase_report_main`: Reporting

## Navigation

- **Parent:** [[docs/Community Addons/purchase/Views]]

<!-- GENERATED:VIEWFILE -->
