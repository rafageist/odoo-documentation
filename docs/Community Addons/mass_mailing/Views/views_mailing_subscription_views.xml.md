---
tags: [odoo, community, generated, views]
---

# views/mailing_subscription_views.xml

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `views/mailing_subscription_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mailing_subscription_view_search`
- Name: mailing.subscription.view.search
- Model: `mailing.subscription`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `contact_id`, `list_id`, `opt_out_datetime`, `opt_out_reason_id`
- XPath or positional patches: 0

### `mailing_subscription_view_tree`
- Name: mailing.subscription.view.list
- Model: `mailing.subscription`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `contact_id`, `create_date`, `is_blacklisted`, `list_id`, `message_bounce`, `opt_out_datetime`, `opt_out_reason_id`
- XPath or positional patches: 0

### `mailing_subscription_view_pivot`
- Name: mailing.subscription.view.pivot
- Model: `mailing.subscription`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `list_id`, `opt_out_datetime`
- XPath or positional patches: 0

### `mailing_subscription_view_graph`
- Name: mailing.subscription.view.graph
- Model: `mailing.subscription`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `message_bounce`, `opt_out_datetime`
- XPath or positional patches: 0

### `mailing_subscription_view_form`
- Name: mailing.subscription.view.form
- Model: `mailing.subscription`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `contact_id`, `create_date`, `is_blacklisted`, `list_id`, `message_bounce`, `opt_out`, `opt_out_datetime`, `opt_out_reason_id`
- XPath or positional patches: 0

## Actions

- `mailing_subscription_action_report_optout`: `act_window` Opt-Out Report

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Views]]

