---
tags: [odoo, community, generated, views]
---

# views/mailing_subscription_optout_views.xml

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `views/mailing_subscription_optout_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mailing_subscription_optout_view_search`
- Name: mailing.subscription.optout.view.search
- Model: `mailing.subscription.optout`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `mailing_subscription_optout_view_tree`
- Name: mailing.subscription.optout.view.list
- Model: `mailing.subscription.optout`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `is_feedback`, `name`, `sequence`
- XPath or positional patches: 0

### `mailing_subscription_optout_view_form`
- Name: mailing.subscription.optout.view.form
- Model: `mailing.subscription.optout`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `is_feedback`, `name`
- XPath or positional patches: 0

## Actions

- `mailing_subscription_optout_action`: `act_window` Optout Reasons

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Views]]

