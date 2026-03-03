---
tags: [odoo, enterprise, generated, views]
---

# views/hr_referral_reward_views.xml

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Source file: `views/hr_referral_reward_views.xml`
- Views: 5
- Actions: 4
- Menus: 1
- Rules: 0

## View records

### `view_hr_referral_reward_tree`
- Name: hr.referral.reward.list
- Model: `hr.referral.reward`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `activity_ids`, `awarded_employees`, `company_id`, `cost`, `gift_manager_id`, `name`, `sequence`
- XPath or positional patches: 0

### `view_hr_referral_reward_form`
- Name: hr.referral.reward.form
- Model: `hr.referral.reward`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `active`, `awarded_employees`, `company_id`, `cost`, `description`, `gift_manager_id`, `image`, `name`
- Buttons: `action_get_employee_awarded`
- XPath or positional patches: 0

### `hr_referral_view_form_reward_purchase_dialog`
- Name: hr.referral.reward.buy.form
- Model: `hr.referral.reward`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `cost`, `description`, `image`, `name`
- Buttons: `buy`
- XPath or positional patches: 0

### `view_hr_referral_reward_kanban`
- Name: hr.referral.reward.employee.referral.kanban
- Model: `hr.referral.reward`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `company_id`, `cost`, `description`, `gift_manager_id`, `image`, `name`, `points_missing`
- Buttons: `action_open_buy_view`, `buy`
- XPath or positional patches: 0

### `view_hr_referral_reward_backend_kanban`
- Name: hr.referral.reward.employee.referral.backend.kanban
- Model: `hr.referral.reward`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `awarded_employees`, `cost`, `description`, `gift_manager_id`, `id`, `image`, `name`
- XPath or positional patches: 0

## Actions

- `action_hr_referral_reward`: `act_window` Rewards
- `action_hr_referral_reward_configuration_view_form`: `view`
- `action_hr_referral_reward_configuration_view_tree`: `view`
- `action_hr_referral_reward_configuration`: `act_window` Rewards

## Menus

- `menu_hr_referral_reward_configuration`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Views]]

