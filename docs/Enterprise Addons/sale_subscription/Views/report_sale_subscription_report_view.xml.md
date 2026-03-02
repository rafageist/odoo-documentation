<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/sale_subscription_report_view.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `report/sale_subscription_report_view.xml`
- Views: 6
- Actions: 6
- Menus: 3
- Rules: 0

## View records

### `view_order_product_search_inherit`
- Name: sale.report.search
- Model: `sale.report`
- Type: inferred from arch
- Inherits: `sale.view_order_product_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `sale_subscription_report_search`
- Name: sale.subscription.report.search
- Model: `sale.subscription.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `client_order_ref`, `name`, `partner_id`, `product_id`, `team_id`, `template_id`, `user_id`
- XPath or positional patches: 0

### `sale_subscription_report_view_cohort`
- Name: sale.subscription.report.cohort
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `cohort`
- Field references: 12
- Sample fields: `amount_tax`, `amount_total`, `amount_untaxed`, `currency_rate`, `kpi_1month_mrr_delta`, `kpi_1month_mrr_percentage`, `kpi_3months_mrr_delta`, `kpi_3months_mrr_percentage`, `percentage_satisfaction`, `rating_last_value`, and 2 more
- XPath or positional patches: 0

### `sale_subscription_report_analysis_view_tree`
- Name: sale.subscription.report.view.list
- Model: `sale.subscription.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 16
- Sample fields: `categ_id`, `company_id`, `date`, `end_date`, `first_contract_date`, `name`, `partner_id`, `product_id`, `product_uom_qty`, `recurring_monthly`, and 6 more
- XPath or positional patches: 0

### `sale_subscription_report_analysis_view_pivot`
- Name: sale.subscription.report.view.pivot
- Model: `sale.subscription.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 17
- Sample fields: `discount`, `discount_amount`, `margin`, `nbr`, `price_total`, `product_uom_qty`, `qty_delivered`, `qty_invoiced`, `qty_to_deliver`, `qty_to_invoice`, and 7 more
- XPath or positional patches: 0

### `sale_subscription_report_analysis_view_graph`
- Name: sale.subscription.report.view.graph
- Model: `sale.subscription.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 15
- Sample fields: `discount`, `discount_amount`, `margin`, `nbr`, `price_total`, `product_uom_qty`, `qty_delivered`, `qty_invoiced`, `qty_to_deliver`, `qty_to_invoice`, and 5 more
- XPath or positional patches: 0

## Actions

- `sale.action_order_report_all`: `act_window` Sales Analysis
- `sale_subscription_report_cohort_action`: `act_window` Retention Analysis
- `sale_subscription_report_analysis_action_tree`: `view`
- `sale_subscription_report_analysis_action_pivot`: `view`
- `sale_subscription_report_analysis_action_graph`: `view`
- `sale_subscription_report_analysis_action`: `act_window` Subscriptions Analysis

## Menus

- `menu_sale_subscription_report_cohort`: Retention
- `menu_sale_subscription_analysis`: Subscriptions
- `menu_sale_subscription_report`: Reporting

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

<!-- GENERATED:VIEWFILE -->
