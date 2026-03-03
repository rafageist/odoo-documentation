---
tags: [odoo, enterprise, generated, views]
---

# views/sale_subscription_plan_views.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `views/sale_subscription_plan_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `sale_subscription_plan_search`
- Name: sale.subscription.plan.search
- Model: `sale.subscription.plan`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `auto_close_limit`, `name`
- XPath or positional patches: 0

### `sale_subscription_plan_view_tree`
- Name: sale.subscription.plan.view.list
- Model: `sale.subscription.plan`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `active_subs_count`, `auto_close_limit_display`, `billing_period_display`, `name`, `sequence`
- XPath or positional patches: 0

### `sale_subscription_plan_view_form`
- Name: sale.subscription.plan.view.form
- Model: `sale.subscription.plan`
- Type: inferred from arch
- Root tag: `form`
- Field references: 25
- Sample fields: `active`, `active_subs_count`, `auto_close_limit`, `base`, `billing_first_day`, `billing_period_unit`, `billing_period_value`, `company_id`, `compute_price`, `invoice_mail_template_id`, and 15 more
- Buttons: `action_open_active_sub`, `action_open_active_subscription_lines`
- XPath or positional patches: 0

## Actions

- `sale_subscription_plan_action`: `act_window` Recurring Plans

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

