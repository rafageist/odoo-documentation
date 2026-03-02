<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/frontdesk_drink_views.xml

- Module: [[docs/Enterprise Addons/frontdesk/frontdesk|frontdesk]]
- Scope: Enterprise Addons
- Source file: `views/frontdesk_drink_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `frontdesk_drink_view_search`
- Name: frontdesk.drink.search
- Model: `frontdesk.drink`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `frontdesk_drink_view_kanban`
- Name: frontdesk.drink.view.kanban
- Model: `frontdesk.drink`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `drink_image`, `name`
- XPath or positional patches: 0

### `frontdesk_drink_view_form`
- Name: frontdesk.drink.view.form
- Model: `frontdesk.drink`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `drink_image`, `name`, `notify_user_ids`, `sequence`
- XPath or positional patches: 0

### `frontdesk_drink_view_tree`
- Name: frontdesk.drink.view.list
- Model: `frontdesk.drink`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `name`, `notify_user_ids`, `sequence`
- XPath or positional patches: 0

## Actions

- `action_frontdesk_drink`: `act_window` Drinks

## Navigation

- **Parent:** [[docs/Enterprise Addons/frontdesk/Views]]

<!-- GENERATED:VIEWFILE -->
