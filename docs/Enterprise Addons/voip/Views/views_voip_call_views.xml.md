<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/voip_call_views.xml

- Module: [[docs/Enterprise Addons/voip/voip|voip]]
- Scope: Enterprise Addons
- Source file: `views/voip_call_views.xml`
- Views: 6
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `voip_call_view_form`
- Name: voip.call.form
- Model: `voip.call`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `avatar_128`, `call_count`, `country_flag_url`, `create_date`, `direction`, `duration`, `id`, `image_1920`, `partner_id`, `phone_number`, and 2 more
- Buttons: `action_open_calls`
- XPath or positional patches: 0

### `voip_call_view_search`
- Name: voip.call.view.search
- Model: `voip.call`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `partner_id`, `phone_number`, `user_id`
- XPath or positional patches: 0

### `voip_call_view_graph`
- Name: voip.call.view.graph
- Model: `voip.call`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `user_id`
- XPath or positional patches: 0

### `voip_call_view_pivot`
- Name: voip.call.view.pivot
- Model: `voip.call`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `create_date`, `user_id`
- XPath or positional patches: 0

### `voip_call_view_calendar`
- Name: voip.call.view.calendar
- Model: `voip.call`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 3
- Sample fields: `partner_id`, `state`, `user_id`
- XPath or positional patches: 0

### `voip_call_tree_view`
- Name: VoIP Calls list view
- Model: `voip.call`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `country_flag_url`, `country_id`, `create_date`, `direction`, `duration`, `id`, `partner_id`, `phone_number`, `state`, `user_id`
- XPath or positional patches: 0

## Actions

- `voip_call_view`: `act_window` Calls
- `voip_call_action_history`: `act_window` History

## Navigation

- **Parent:** [[docs/Enterprise Addons/voip/Views]]

<!-- GENERATED:VIEWFILE -->
