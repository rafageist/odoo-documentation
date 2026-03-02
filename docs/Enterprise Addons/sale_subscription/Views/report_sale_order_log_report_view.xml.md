<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/sale_order_log_report_view.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `report/sale_order_log_report_view.xml`
- Views: 5
- Actions: 3
- Menus: 2
- Rules: 0

## View records

### `sale_order_log_report_search`
- Name: sale.order.log.report.search
- Model: `sale.order.log.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 10
- Sample fields: `close_reason_id`, `company_id`, `end_date`, `order_id`, `origin_order_id`, `partner_id`, `subscription_state`, `team_id`, `template_id`, `user_id`
- XPath or positional patches: 0

### `view_sale_order_log_analysis_graph`
- Name: sale.order.log.report.graph
- Model: `sale.order.log.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 6
- Sample fields: `amount_signed`, `arr_change_normalized`, `event_date`, `mrr_change_normalized`, `recurring_monthly`, `recurring_yearly`
- XPath or positional patches: 0

### `view_sale_order_log_growth_tree`
- Name: sale.order.log.report.list
- Model: `sale.order.log.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 14
- Sample fields: `amount_signed`, `company_id`, `effective_date`, `event_date`, `event_type`, `id`, `log_currency_id`, `order_id`, `origin_order_id`, `partner_id`, and 4 more
- XPath or positional patches: 0

### `view_sale_order_log_growth_graph`
- Name: sale.order.log.report.graph
- Model: `sale.order.log.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 6
- Sample fields: `amount_signed`, `arr_change_normalized`, `event_date`, `mrr_change_normalized`, `recurring_monthly`, `recurring_yearly`
- XPath or positional patches: 0

### `view_sale_order_log_growth_pivot`
- Name: sale.order.log.report.pivot
- Model: `sale.order.log.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 6
- Sample fields: `amount_signed`, `arr_change_normalized`, `event_date`, `mrr_change_normalized`, `recurring_monthly`, `recurring_yearly`
- XPath or positional patches: 0

## Actions

- `sale_order_log_analysis_action_graph`: `view`
- `sale_order_log_analysis_action`: `act_window` MRR Analysis
- `sale_order_log_growth_action`: `act_window` MRR Breakdown

## Menus

- `menu_sale_order_log_analysis_report`: MRR Timeline
- `menu_sale_order_log_growth_report`: MRR Breakdown

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

<!-- GENERATED:VIEWFILE -->
