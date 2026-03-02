<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/commission_report.xml

- Module: [[docs/Enterprise Addons/sale_commission/sale_commission|sale_commission]]
- Scope: Enterprise Addons
- Source file: `report/commission_report.xml`
- Views: 4
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `sale_commission_report_view_search`
- Name: sale.commission.report.view.search
- Model: `sale.commission.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `company_id`, `plan_id`, `user_id`
- XPath or positional patches: 0

### `sale_commission_report_view_pivot`
- Name: sale.commission.report.view.pivot
- Model: `sale.commission.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 8
- Sample fields: `achieved`, `achieved_rate`, `commission`, `forecast`, `payment_date`, `plan_id`, `target_amount`, `user_id`
- XPath or positional patches: 0

### `sale_commission_report_view_graph`
- Name: sale.commission.report.view.graph
- Model: `sale.commission.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `commission`, `payment_date`, `plan_id`
- XPath or positional patches: 0

### `sale_commission_report_view_list`
- Name: sale.commission.report.view.list
- Model: `sale.commission.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `achieved`, `achieved_rate`, `commission`, `currency_id`, `date_from`, `forecast`, `notes`, `payment_date`, `plan_id`, `target_amount`, and 1 more
- Buttons: `action_achievement_detail`
- XPath or positional patches: 0

## Actions

- `sale_commission_action_my_report`: `act_window` My Commissions
- `sale_commission_action_report_sale`: `act_window` Commissions
- `sale_commission_action_report`: `act_window` Commissions

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_commission/Views]]

<!-- GENERATED:VIEWFILE -->
