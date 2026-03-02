<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/test_model_views.xml

- Module: [[docs/Community Addons/test_website/test_website|test_website]]
- Scope: Community Addons
- Source file: `views/test_model_views.xml`
- Views: 3
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `view_test_model_form`
- Name: test.model.form
- Model: `test.model`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `is_published`, `name`
- XPath or positional patches: 1

### `test_model_view_list`
- Name: Test Model Pages List
- Model: `test.model`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `website_url`
- XPath or positional patches: 0

### `test_model_view_kanban`
- Name: test.model.kanban
- Model: `test.model`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `is_published`, `name`
- XPath or positional patches: 0

## Actions

- `action_test_website_test_model`: `act_window` Test Model
- `action_test_model`: `act_window` Test Model Pages

## Menus

- `menu_test_website_test_model`: Test Model

## Navigation

- **Parent:** [[docs/Community Addons/test_website/Views]]

<!-- GENERATED:VIEWFILE -->
