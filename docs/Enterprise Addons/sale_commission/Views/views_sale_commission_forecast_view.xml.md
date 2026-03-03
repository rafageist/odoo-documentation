---
tags: [odoo, enterprise, generated, views]
---

# views/sale_commission_forecast_view.xml

- Module: [[docs/Enterprise Addons/sale_commission/sale_commission|sale_commission]]
- Scope: Enterprise Addons
- Source file: `views/sale_commission_forecast_view.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `sale_commission_plan_target_forecast_view_pivot`
- Name: sale.commission.plan.target.forecast.view.pivot
- Model: `sale.commission.plan.target.forecast`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `amount`, `currency_id`, `target_id`
- XPath or positional patches: 0

### `sale_commission_plan_target_forecast_view_graph`
- Name: sale.commission.plan.target.forecast.view.graph
- Model: `sale.commission.plan.target.forecast`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `amount`, `target_id`
- XPath or positional patches: 0

### `sale_commission_plan_target_forecast_view_list`
- Name: sale.commission.plan.target.forecast.view.list
- Model: `sale.commission.plan.target.forecast`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `amount`, `currency_id`, `plan_id`, `target_id`, `user_id`
- XPath or positional patches: 0

### `sale_commission_plan_target_forecast_view_search`
- Name: sale.commission.plan.target.forecast.view.search
- Model: `sale.commission.plan.target.forecast`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `team_id`, `user_id`
- XPath or positional patches: 0

## Actions

- `sale_commission_action_forecast`: `act_window` Forecast
- `sale_commission_action_my_forecast`: `act_window` My Forecast

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_commission/Views]]

