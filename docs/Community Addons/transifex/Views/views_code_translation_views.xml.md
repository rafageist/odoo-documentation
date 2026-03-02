<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/code_translation_views.xml

- Module: [[docs/Community Addons/transifex/transifex|transifex]]
- Scope: Community Addons
- Source file: `views/code_translation_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `transifex_code_translation_view_search`
- Name: transifex.code.translation.view.search
- Model: `transifex.code.translation`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `lang`, `module`, `source`, `value`
- XPath or positional patches: 0

### `transifex_code_translation_tree_view`
- Name: transifex.code.translation.list
- Model: `transifex.code.translation`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `lang`, `module`, `source`, `transifex_url`, `value`
- XPath or positional patches: 0

## Actions

- `action_code_translations`: `server` Transifex Code Translations

## Menus

- `menu_transifex_code_translations`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/transifex/Views]]

<!-- GENERATED:VIEWFILE -->
