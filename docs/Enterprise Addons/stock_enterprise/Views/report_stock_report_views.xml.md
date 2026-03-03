---
tags: [odoo, enterprise, generated, views]
---

# report/stock_report_views.xml

- Module: [[docs/Enterprise Addons/stock_enterprise/stock_enterprise|stock_enterprise]]
- Scope: Enterprise Addons
- Source file: `report/stock_report_views.xml`
- Views: 6
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `stock_report_cohort_view`
- Name: stock.report.cohort.view
- Model: `stock.report`
- Type: inferred from arch
- Root tag: `cohort`
- Field references: 0
- XPath or positional patches: 0

### `stock_report_form_view`
- Name: stock.report.view.form
- Model: `stock.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `creation_date`, `cycle_time`, `date_done`, `delay`, `operation_type_id`, `partner_id`, `picking_id`, `product_id`, `product_qty`, `scheduled_date`, and 1 more
- XPath or positional patches: 0

### `stock_report_tree_view`
- Name: stock.report.view.list
- Model: `stock.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `company_id`, `creation_date`, `cycle_time`, `date_done`, `delay`, `operation_type_id`, `product_id`, `reference`, `scheduled_date`, `state`
- XPath or positional patches: 0

### `stock_report_pivot_view`
- Name: stock.report.view.pivot
- Model: `stock.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `categ_id`, `cycle_time`, `delay`, `operation_type_id`
- XPath or positional patches: 0

### `stock_report_graph_view`
- Name: stock.report.view.graph
- Model: `stock.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `date_done`
- XPath or positional patches: 0

### `stock_report_search_view`
- Name: stock.report.view.search
- Model: `stock.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `reference`
- XPath or positional patches: 0

## Actions

- `stock_report_action_performance`: `act_window` Warehouse Analysis

## Menus

- `stock_dashboard_menuitem`: Performance

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_enterprise/Views]]

