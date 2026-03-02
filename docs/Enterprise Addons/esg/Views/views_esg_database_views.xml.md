<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/esg_database_views.xml

- Module: [[docs/Enterprise Addons/esg/esg|esg]]
- Scope: Enterprise Addons
- Source file: `views/esg_database_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `database_search_view`
- Name: esg.database.search
- Model: `esg.database`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `database_form_view`
- Name: esg.database.form
- Model: `esg.database`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `image`, `name`, `url`
- Buttons: `action_load_data`
- XPath or positional patches: 0

### `database_kanban_view`
- Name: esg.database.kanban
- Model: `esg.database`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `image`, `kanban_text`, `name`
- Buttons: `action_load_data`
- XPath or positional patches: 0

## Actions

- `action_view_database`: `act_window` Databases

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg/Views]]

<!-- GENERATED:VIEWFILE -->
