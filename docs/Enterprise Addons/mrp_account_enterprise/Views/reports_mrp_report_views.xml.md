<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# reports/mrp_report_views.xml

- Module: [[docs/Enterprise Addons/mrp_account_enterprise/mrp_account_enterprise|mrp_account_enterprise]]
- Scope: Enterprise Addons
- Source file: `reports/mrp_report_views.xml`
- Views: 5
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `mrp_report_form_view`
- Name: mrp.report.view.form
- Model: `mrp.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `byproduct_cost`, `component_cost`, `currency_id`, `operation_cost`, `product_id`, `production_id`, `qty_produced`, `total_cost`, `unit_component_cost`, `unit_cost`, and 1 more
- XPath or positional patches: 0

### `mrp_report_tree_view`
- Name: mrp.report.view.list
- Model: `mrp.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `date_finished`, `product_id`, `production_id`
- XPath or positional patches: 0

### `mrp_report_pivot_view`
- Name: mrp.report.view.pivot
- Model: `mrp.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `product_id`, `qty_produced`, `unit_component_cost`, `unit_cost`, `unit_operation_cost`
- XPath or positional patches: 0

### `mrp_report_graph_view`
- Name: mrp.report.view.graph
- Model: `mrp.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `date_finished`, `product_id`, `unit_cost`
- XPath or positional patches: 0

### `mrp_report_search_view`
- Name: mrp.report.view.search
- Model: `mrp.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `product_id`, `production_id`
- XPath or positional patches: 0

## Actions

- `mrp_report_dashboard_action`: `act_window` Production Analysis

## Menus

- `mrp_dashboard_menuitem`: Production Analysis

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_account_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
