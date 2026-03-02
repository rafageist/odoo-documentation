<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/discuss/discuss_call_history_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/discuss/discuss_call_history_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `discuss_call_history_view_form`
- Name: discuss.call.history.view.form
- Model: `discuss.call.history`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `channel_id`, `duration_hour`, `end_dt`, `start_dt`
- XPath or positional patches: 0

### `discuss_call_history_view_tree`
- Name: discuss.call.history.view.list
- Model: `discuss.call.history`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `channel_id`, `duration_hour`, `end_dt`, `start_dt`
- XPath or positional patches: 0

## Actions

- `discuss_call_history_action`: `act_window` Call History

## Menus

- `discuss_call_history_menu`: Call History

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

<!-- GENERATED:VIEWFILE -->
