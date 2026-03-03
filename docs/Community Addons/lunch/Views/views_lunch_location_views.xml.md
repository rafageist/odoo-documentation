---
tags: [odoo, community, generated, views]
---

# views/lunch_location_views.xml

- Module: [[docs/Community Addons/lunch/lunch|lunch]]
- Scope: Community Addons
- Source file: `views/lunch_location_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `lunch_location_kanban_view`
- Name: lunch.location.view.kanban
- Model: `lunch.location`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `address`, `company_id`, `name`
- XPath or positional patches: 0

### `lunch_location_tree_view`
- Name: lunch.location.view.form
- Model: `lunch.location`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `address`, `company_id`, `name`
- XPath or positional patches: 0

### `lunch_location_form_view`
- Name: lunch.location.view.form
- Model: `lunch.location`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `address`, `company_id`, `name`
- XPath or positional patches: 0

### `lunch_location_view_search`
- Name: lunch.location.view.search
- Model: `lunch.location`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `address`, `name`
- XPath or positional patches: 0

## Actions

- `lunch_location_action`: `act_window` Lunch Locations

## Navigation

- **Parent:** [[docs/Community Addons/lunch/Views]]

