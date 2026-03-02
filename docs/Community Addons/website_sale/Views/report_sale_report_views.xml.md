<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/sale_report_views.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `report/sale_report_views.xml`
- Views: 4
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `sale_report_view_tree`
- Name: sale.report.view.list.inherit.website.sale
- Model: `sale.report`
- Type: inferred from arch
- Inherits: `sale.sale_report_view_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `order_reference`, `public_categ_ids`, `website_id`
- XPath or positional patches: 0

### `sale_report_view_graph_website`
- Name: sale.report.view.graph.website
- Model: `sale.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `date`, `price_subtotal`
- XPath or positional patches: 0

### `sale_report_view_pivot_website`
- Name: sale.report.view.pivot.website
- Model: `sale.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `date`, `price_subtotal`, `state`
- XPath or positional patches: 0

### `sale_report_view_search_website`
- Name: sale.report.search
- Model: `sale.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `categ_id`, `company_id`, `country_id`, `partner_id`, `product_id`, `website_id`
- XPath or positional patches: 0

## Actions

- `sale_report_action_view_graph_carts`: `view`
- `sale_report_action_view_pivot_carts`: `view`
- `sale_report_action_carts`: `act_window` Sales
- `sale_report_action_view_graph_website`: `view`
- `sale_report_action_view_pivot_website`: `view`
- `sale_report_action_dashboard`: `act_window` Online Sales Analysis

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

<!-- GENERATED:VIEWFILE -->
