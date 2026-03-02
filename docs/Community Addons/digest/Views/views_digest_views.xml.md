<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/digest_views.xml

- Module: [[docs/Community Addons/digest/digest|digest]]
- Scope: Community Addons
- Source file: `views/digest_views.xml`
- Views: 6
- Actions: 2
- Menus: 2
- Rules: 0

## View records

### `digest_tip_view_search`
- Name: digest.tip.view.search
- Model: `digest.tip`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `group_id`, `name`, `tip_description`
- XPath or positional patches: 0

### `digest_tip_view_form`
- Name: digest.tip.view.form
- Model: `digest.tip`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `group_id`, `name`, `tip_description`, `user_ids`
- XPath or positional patches: 0

### `digest_tip_view_tree`
- Name: digest.tip.view.list
- Model: `digest.tip`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `group_id`, `name`, `sequence`
- XPath or positional patches: 0

### `digest_digest_view_search`
- Name: digest.digest.view.search
- Model: `digest.digest`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `user_ids`
- XPath or positional patches: 0

### `digest_digest_view_form`
- Name: digest.digest.view.form
- Model: `digest.digest`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `company_id`, `email`, `is_subscribed`, `kpi_mail_message_total`, `kpi_res_users_connected`, `name`, `next_run_date`, `periodicity`, `state`, `user_ids`
- Buttons: `action_activate`, `action_deactivate`, `action_send_manual`
- XPath or positional patches: 0

### `digest_digest_view_tree`
- Name: digest.digest.view.list
- Model: `digest.digest`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `name`, `next_run_date`, `periodicity`, `state`
- XPath or positional patches: 0

## Actions

- `digest_tip_action`: `act_window` Digest Tips
- `digest_digest_action`: `act_window` Digest Emails

## Menus

- `digest_tip_menu`: unnamed
- `digest_menu`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/digest/Views]]

<!-- GENERATED:VIEWFILE -->
