---
tags: [odoo, enterprise, generated, views]
---

# views/sale_commission_plan_view.xml

- Module: [[docs/Enterprise Addons/sale_commission/sale_commission|sale_commission]]
- Scope: Enterprise Addons
- Source file: `views/sale_commission_plan_view.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `sale_commission_plan_view_search`
- Name: sale.commission.plan.view.search
- Model: `sale.commission.plan`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `sale_commission_plan_view_list`
- Name: sale.commission.plan.view.list
- Model: `sale.commission.plan`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `date_from`, `date_to`, `name`, `periodicity`, `state`, `type`
- XPath or positional patches: 0

### `sale_commission_plan_view_form`
- Name: sale.commission.plan.view.form
- Model: `sale.commission.plan`
- Type: inferred from arch
- Root tag: `form`
- Field references: 26
- Sample fields: `achievement_ids`, `amount`, `amount_rate`, `commission_amount`, `company_id`, `currency_id`, `date_from`, `date_to`, `name`, `other_plans`, and 16 more
- Buttons: `%(sale_commission.sale_subscription_change_customer_wizard_action)d`, `action_approve`, `action_cancel`, `action_done`, `action_draft`, `action_export_targets`, `action_open_commission`
- XPath or positional patches: 0

### `sale_commission_plan_user_view_search`
- Name: sale.commission.plan.user.view.search
- Model: `sale.commission.plan.user`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `plan_id`, `user_id`
- XPath or positional patches: 0

### `sale_commission_plan_user_view_list`
- Name: sale.commission.plan.user.view.list
- Model: `sale.commission.plan.user`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `date_from`, `date_to`, `plan_id`, `user_id`
- XPath or positional patches: 0

## Actions

- `sale_commission_action_plan`: `act_window` Commission Plans

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_commission/Views]]

