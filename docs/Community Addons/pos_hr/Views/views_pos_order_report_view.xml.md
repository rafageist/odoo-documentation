---
tags: [odoo, community, generated, views]
---

# views/pos_order_report_view.xml

- Module: [[docs/Community Addons/pos_hr/pos_hr|pos_hr]]
- Scope: Community Addons
- Source file: `views/pos_order_report_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `report_pos_order_view_tree`
- Name: report.pos.order.view.list.inherit.pos.hr
- Model: `report.pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.report_pos_order_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `employee_id`, `product_categ_id`
- XPath or positional patches: 0

### `view_report_pos_order_search_inherit`
- Name: report.pos.order.search.inherit
- Model: `report.pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_report_pos_order_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/pos_hr/Views]]

