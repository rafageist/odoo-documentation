---
tags: [odoo, enterprise, generated, views]
---

# views/dashboard_view.xml

- Module: [[docs/Enterprise Addons/website_sale_dashboard/website_sale_dashboard|website_sale_dashboard]]
- Scope: Enterprise Addons
- Source file: `views/dashboard_view.xml`
- Views: 3
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `sale_report_view_search_website_inherit`
- Name: sale.report.view.search.inherit
- Model: `sale.report`
- Type: inferred from arch
- Inherits: `website_sale.sale_report_view_search_website`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `order_reference`
- XPath or positional patches: 2

### `view_online_sales_pivot`
- Name: sale.report.pivot
- Model: `sale.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `categ_id`, `order_reference`, `price_subtotal`, `price_total`
- XPath or positional patches: 0

### `view_online_sales_graph`
- Name: sale.report.graph
- Model: `sale.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `date`, `price_subtotal`
- XPath or positional patches: 0

## Actions

- `sale_dashboard_view_pivot`: `view`
- `sale_dashboard_view_graph`: `view`
- `sale_dashboard`: `act_window` eCommerce Dashboard

## Menus

- `website.menu_website_dashboard`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_sale_dashboard/Views]]

