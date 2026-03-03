---
tags: [odoo, community, generated, views]
---

# report/vendor_delay_report.xml

- Module: [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]
- Scope: Community Addons
- Source file: `report/vendor_delay_report.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `vendor_delay_report_view_graph`
- Name: vendor.delay.report.view.graph
- Model: `vendor.delay.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `on_time_rate`, `product_id`
- XPath or positional patches: 0

### `vendor_delay_report_filter`
- Name: vendor.delay.report.search
- Model: `vendor.delay.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `partner_id`, `product_id`
- XPath or positional patches: 0

## Actions

- `action_purchase_vendor_delay_report`: `act_window` On-time Delivery

## Navigation

- **Parent:** [[docs/Community Addons/purchase_stock/Views]]

