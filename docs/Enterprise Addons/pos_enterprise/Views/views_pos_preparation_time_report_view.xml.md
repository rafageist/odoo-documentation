---
tags: [odoo, enterprise, generated, views]
---

# views/pos_preparation_time_report_view.xml

- Module: [[docs/Enterprise Addons/pos_enterprise/pos_enterprise|pos_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/pos_preparation_time_report_view.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `preparation_time_report_view_form`
- Name: preparation.time.report.view.form
- Model: `preparation.time.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `create_date`, `order_id`, `pos_config_id`, `preparation_time`, `product_id`, `qty`
- XPath or positional patches: 0

### `preparation_time_report_view_list`
- Name: preparation.time.report.view.list
- Model: `preparation.time.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `create_date`, `order_id`, `pos_config_id`, `preparation_time`, `product_id`, `qty`
- XPath or positional patches: 0

### `preparation_time_report_graph`
- Name: preparation.time.report.graph
- Model: `preparation.time.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `avg_preparation_time`, `order_hour`, `pos_config_id`
- XPath or positional patches: 0

### `preparation_time_report_search`
- Name: preparation.time.report.search.view
- Model: `preparation.time.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

## Actions

- `pos_preparation_time_report_action`: `act_window` Preparation Time Report

## Menus

- `menu_report_preparation_time`: Preparation Time

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_enterprise/Views]]

