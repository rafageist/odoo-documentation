---
tags: [odoo, enterprise, generated, views]
---

# report/rental_report_views.xml

- Module: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]]
- Scope: Enterprise Addons
- Source file: `report/rental_report_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `rental_report_search_view`
- Name: sale.rental.report.search
- Model: `sale.rental.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `categ_id`, `company_id`, `date`, `partner_id`, `product_id`, `product_tmpl_id`, `user_id`
- XPath or positional patches: 0

### `sale_rental_report_view_tree`
- Name: sale.rental.report.view.list
- Model: `sale.rental.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `categ_id`, `company_id`, `currency_id`, `date`, `order_id`, `partner_id`, `price`, `product_id`, `qty_delivered`, `quantity`, and 2 more
- XPath or positional patches: 0

### `rental_report_graph_view`
- Name: sale.rental.report.graph
- Model: `sale.rental.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `date`, `quantity`
- XPath or positional patches: 0

### `rental_report_pivot_view`
- Name: sale.rental.report.pivot
- Model: `sale.rental.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `date`, `price`, `qty_delivered`, `quantity`
- XPath or positional patches: 0

## Actions

- `action_report_rental_saleorder`: `report` Pickup and Return Receipt
- `action_rental_report`: `act_window` Rental Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_renting/Views]]

