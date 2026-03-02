<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/sale_subscription_views.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `views/sale_subscription_views.xml`
- Views: 12
- Actions: 25
- Menus: 0
- Rules: 0

## View records

### `sale_subscription_close_reason_view_form`
- Name: sale.subscription.reason.form
- Model: `sale.order.close.reason`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `empty_retention_message`, `name`, `retention_button_link`, `retention_button_text`, `retention_message`, `visible_in_portal`
- XPath or positional patches: 0

### `sale_subscription_close_reason_view_tree`
- Name: sale.subscription.reason.list
- Model: `sale.order.close.reason`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `name`, `sequence`, `visible_in_portal`
- XPath or positional patches: 0

### `sale_subscription_view_activity`
- Name: sale.subscription.activity
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 2
- Sample fields: `note`, `partner_id`
- XPath or positional patches: 0

### `sale_subscription_primary_form_view`
- Name: sale.subscription.order.primary.form
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_subscription.sale_subscription_order_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `next_invoice_date`, `sale_order_template_id`
- XPath or positional patches: 2

### `view_sale_subscription_calendar`
- Name: sale.order.calendar
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sale_order_calendar`
- Root tag: `field`
- Field references: 5
- Sample fields: `amount_total`, `plan_id`, `recurring_monthly`, `state`, `subscription_state`
- XPath or positional patches: 1

### `sale_subscription_quotation_tree_view`
- Name: sale.subscription.quotation.list
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_subscription.sale_subscription_view_tree`
- Root tag: `list`
- Field references: 3
- Sample fields: `amount_total`, `next_invoice_date`, `validity_date`
- XPath or positional patches: 1

### `sale_subscription_view_tree`
- Name: sale.subscription.order.list
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 22
- Sample fields: `activity_ids`, `amount_total`, `client_order_ref`, `company_id`, `currency_id`, `end_date`, `first_contract_date`, `name`, `next_invoice_date`, `non_recurring_total`, and 12 more
- XPath or positional patches: 0

### `sale_subscription_view_kanban`
- Name: sale.order.kanban
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 15
- Sample fields: `activity_ids`, `currency_id`, `name`, `partner_id`, `payment_exception`, `plan_id`, `rating_ids`, `rating_last_value`, `recurring_total`, `sale_order_template_id`, and 5 more
- XPath or positional patches: 0

### `sale_subscription_upsell_primary_view_tree`
- Name: sale.subscription.order.list
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_quotation_tree`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `sale_order_view_graph_subscription`
- Name: sale.order.graph
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `first_contract_date`, `recurring_monthly`
- XPath or positional patches: 0

### `sale_order_view_cohort`
- Name: sale.order.cohort
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `cohort`
- Field references: 0
- XPath or positional patches: 0

### `sale_subscription_view_search`
- Name: sale.order.search
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `name`, `order_line`, `partner_id`, `sale_order_template_id`, `team_id`, `user_id`
- XPath or positional patches: 0

## Actions

- `model_sale_order_subscription_pause_record`: `server` Pause Subscription
- `model_sale_order_subscription_change_customer`: `server` Change customer
- `sale_subscription_close_reason_action`: `act_window` Close Reasons
- `sale_subscription_form_pending`: `view`
- `sale_subscription_form_upsell`: `view`
- `sale_subscription_form_quotes`: `view`
- `sale_subscription_form`: `view`
- `sale_subscription_calendar_upsell`: `view`
- `sale_subscription_calendar_quotes`: `view`
- `sale_subscription_calendar_pending`: `view`
- `sale_subscription_calendar`: `view`
- `sale_subscription_action_quotes_view_graph`: `view`
- `sale_subscription_action_quotes`: `act_window` Quotations
- `sale_subscription_tree_pending`: `view`
- `sale_subscription_tree`: `view`
- `sale_subscription_kanban`: `view`
- `sale_subscription_action_upsell_view_graph`: `view`
- `sale_subscription_action_upsell`: `act_window` Upsells
- `sale_subscription_action_pending_view_graph`: `view`
- `sale_subscription_action_pending`: `act_window` To Renew

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

<!-- GENERATED:VIEWFILE -->
