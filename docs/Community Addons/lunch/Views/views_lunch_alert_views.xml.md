---
tags: [odoo, community, generated, views]
---

# views/lunch_alert_views.xml

- Module: [[docs/Community Addons/lunch/lunch|lunch]]
- Scope: Community Addons
- Source file: `views/lunch_alert_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `lunch_alert_view_kanban`
- Name: lunch.alert.kanban
- Model: `lunch.alert`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `location_ids`, `mode`, `name`, `notification_moment`, `notification_time`, `recipients`
- XPath or positional patches: 0

### `lunch_alert_view_form`
- Name: lunch.alert.form
- Model: `lunch.alert`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `active`, `location_ids`, `message`, `mode`, `name`, `notification_moment`, `notification_time`, `recipients`, `tz`, `until`
- XPath or positional patches: 0

### `lunch_alert_view_tree`
- Name: lunch.alert.list
- Model: `lunch.alert`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `active`, `available_today`, `message`, `mode`, `name`
- XPath or positional patches: 0

### `lunch_alert_view_search`
- Name: lunch.alert.search
- Model: `lunch.alert`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `message`
- XPath or positional patches: 0

## Actions

- `lunch_alert_action`: `act_window` Lunch Alerts

## Navigation

- **Parent:** [[docs/Community Addons/lunch/Views]]

