---
tags: [odoo, enterprise, generated, views]
---

# report/hr_referral_reward_report_views.xml

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Source file: `report/hr_referral_reward_report_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `employee_referral_reward_report_view_search`
- Name: employee.referral.reward.report.view.search
- Model: `hr.referral.reward.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `awarded_employee_id`, `reward_id`, `write_date`
- XPath or positional patches: 0

### `hr_referral_reward_report_view_tree`
- Name: hr.referral.reward.report.view.list
- Model: `hr.referral.reward.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `awarded_employee_id`, `company_id`, `cost`, `reward_id`, `rewarded_employees`
- XPath or positional patches: 0

### `employee_referral_reward_report_view_graph`
- Name: employee.referral.reward.report.view.graph
- Model: `hr.referral.reward.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `awarded_employee_id`, `cost`, `reward_id`, `rewarded_employees`
- XPath or positional patches: 0

### `employee_referral_reward_report_view_pivot`
- Name: employee.referral.reward.report.view.pivot
- Model: `hr.referral.reward.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `awarded_employee_id`, `cost`, `reward_id`, `rewarded_employees`
- XPath or positional patches: 0

## Actions

- `employee_referral_reward_report_action`: `act_window` Reward Analysis

## Menus

- `menu_report_employee_referral_reward_all`: Rewards

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Views]]

