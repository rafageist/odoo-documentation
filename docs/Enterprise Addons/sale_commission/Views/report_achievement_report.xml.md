<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/achievement_report.xml

- Module: [[docs/Enterprise Addons/sale_commission/sale_commission|sale_commission]]
- Scope: Enterprise Addons
- Source file: `report/achievement_report.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `sale_achievement_report_view_search`
- Name: sale.commission.achievement.report.view.search
- Model: `sale.commission.achievement.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `company_id`, `plan_id`, `target_id`, `team_id`, `user_id`
- XPath or positional patches: 0

### `sale_achievement_report_view_graph`
- Name: sale.commission.achievement.report.view.graph
- Model: `sale.commission.achievement.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `achieved`, `plan_id`, `target_id`, `user_id`
- XPath or positional patches: 0

### `sale_achievement_report_view_pivot`
- Name: sale.commission.achievement.report.view.pivot
- Model: `sale.commission.achievement.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `achieved`, `target_id`
- XPath or positional patches: 0

### `sale_achievement_report_view_list`
- Name: sale.commission.achievement.report.view.list
- Model: `sale.commission.achievement.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `achieved`, `commission_rate`, `commission_target_amount`, `currency_id`, `date`, `partner_id`, `plan_id`, `related_res_id`, `target_amount`, `target_id`, and 3 more
- XPath or positional patches: 0

## Actions

- `sale_achievement_action_report`: `act_window` Achievements

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_commission/Views]]

<!-- GENERATED:VIEWFILE -->
