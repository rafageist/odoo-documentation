<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/documents_tag_views.xml

- Module: [[docs/Enterprise Addons/documents/documents|documents]]
- Scope: Enterprise Addons
- Source file: `views/documents_tag_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `tag_view_search`
- Name: tag search
- Model: `documents.tag`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `tag_view_list`
- Name: documents.tag.list
- Model: `documents.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `color`, `name`, `tooltip`
- XPath or positional patches: 0

### `tag_view_form`
- Name: documents.tag.form
- Model: `documents.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `color`, `name`, `tooltip`
- XPath or positional patches: 0

## Actions

- `tag_action`: `act_window` Tags

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents/Views]]

<!-- GENERATED:VIEWFILE -->
