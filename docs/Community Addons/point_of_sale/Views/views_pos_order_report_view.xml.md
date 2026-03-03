---
tags: [odoo, community, generated, views]
---

# views/pos_order_report_view.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/pos_order_report_view.xml`
- Views: 4
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `view_report_pos_order_search`
- Name: report.pos.order.search
- Model: `report.pos.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `config_id`, `date`, `partner_id`, `product_categ_id`, `product_id`
- XPath or positional patches: 0

### `report_pos_order_view_tree`
- Name: report.pos.order.view.list
- Model: `report.pos.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `company_id`, `config_id`, `date`, `order_id`, `partner_id`, `price_total`, `product_categ_id`, `product_id`, `state`
- XPath or positional patches: 0

### `view_report_pos_order_graph`
- Name: report.pos.order.graph
- Model: `report.pos.order`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `price_total`, `product_categ_id`
- XPath or positional patches: 0

### `view_report_pos_order_pivot`
- Name: report.pos.order.pivot
- Model: `report.pos.order`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `date`, `order_id`, `price_total`, `product_categ_id`, `product_qty`
- XPath or positional patches: 0

## Actions

- `action_report_pos_details`: `act_window` Sales Details
- `action_report_pos_order_all`: `act_window` Orders Analysis

## Menus

- `menu_report_order_details`: Sales Details
- `menu_report_pos_order_all`: Orders

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

