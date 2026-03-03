---
tags: [odoo, community, generated, views]
---

# views/lunch_cashmove_views.xml

- Module: [[docs/Community Addons/lunch/lunch|lunch]]
- Scope: Community Addons
- Source file: `views/lunch_cashmove_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_lunch_cashmove_kanban`
- Name: lunch.cashmove.kanban
- Model: `lunch.cashmove`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `amount`, `currency_id`, `date`, `description`, `user_id`
- XPath or positional patches: 0

### `lunch_cashmove_view_form`
- Name: lunch.cashmove.form
- Model: `lunch.cashmove`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `amount`, `currency_id`, `date`, `description`, `user_id`
- XPath or positional patches: 0

### `lunch_cashmove_view_tree`
- Name: lunch.cashmove.list
- Model: `lunch.cashmove`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `amount`, `currency_id`, `date`, `description`, `user_id`
- XPath or positional patches: 0

### `lunch_cashmove_view_search`
- Name: lunch.cashmove.search
- Model: `lunch.cashmove`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `description`, `user_id`
- XPath or positional patches: 0

## Actions

- `lunch_cashmove_action_payment`: `act_window` Cash Moves

## Navigation

- **Parent:** [[docs/Community Addons/lunch/Views]]

