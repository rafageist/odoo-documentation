---
tags: [odoo, community, generated, views]
---

# report/sale_report_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `report/sale_report_views.xml`
- Views: 6
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `view_order_product_search`
- Name: sale.report.search
- Model: `sale.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 10
- Sample fields: `categ_id`, `company_id`, `country_id`, `date`, `industry_id`, `partner_id`, `product_id`, `product_tmpl_id`, `team_id`, `user_id`
- XPath or positional patches: 0

### `sale_report_view_tree`
- Name: sale.report.view.list
- Model: `sale.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `company_id`, `currency_id`, `date`, `line_invoice_status`, `order_reference`, `partner_id`, `price_subtotal`, `price_total`, `price_unit`, `pricelist_id`, and 5 more
- XPath or positional patches: 0

### `sale_report_graph_bar`
- Name: sale.report.graph.bar
- Model: `sale.report`
- Type: inferred from arch
- Inherits: `view_order_product_graph`
- Root tag: `graph`
- Field references: 0
- XPath or positional patches: 1

### `sale_report_graph_pie`
- Name: sale.report.graph.pie
- Model: `sale.report`
- Type: inferred from arch
- Inherits: `view_order_product_graph`
- Root tag: `graph`
- Field references: 0
- XPath or positional patches: 1

### `view_order_product_graph`
- Name: sale.report.graph
- Model: `sale.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `date`, `product_uom_qty`
- XPath or positional patches: 0

### `view_order_product_pivot`
- Name: sale.report.pivot
- Model: `sale.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `date`, `product_uom_qty`, `team_id`
- XPath or positional patches: 0

## Actions

- `action_order_report_so_salesteam`: `act_window` Sales Analysis
- `action_order_report_quotation_salesteam`: `act_window` Quotations Analysis
- `report_all_channels_sales_action`: `act_window` Sales Analysis
- `action_order_report_customers`: `act_window` Sales Analysis By Customers
- `action_order_report_products`: `act_window` Sales Analysis By Products
- `action_order_report_salesperson`: `act_window` Sales Analysis By Salespersons
- `action_order_report_all`: `act_window` Sales Analysis

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

