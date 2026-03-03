---
tags: [odoo, enterprise, generated, views]
---

# views/ir_model_views.xml

- Module: [[docs/Enterprise Addons/data_cleaning/data_cleaning|data_cleaning]]
- Scope: Enterprise Addons
- Source file: `views/ir_model_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `ir_model_view_search`
- Name: ir.model.view.search.inherit.data.merge
- Model: `ir.model`
- Type: inferred from arch
- Inherits: `base.view_model_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `ir_model_view_tree_primary`
- Name: ir.model.view.list.inherit.data.merge.primary
- Model: `ir.model`
- Type: inferred from arch
- Inherits: `ir_model_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `ir_model_view_tree`
- Name: ir.model.view.list.inherit.data.merge
- Model: `ir.model`
- Type: inferred from arch
- Inherits: `base.view_model_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `is_merge_enabled`
- XPath or positional patches: 1

### `ir_model_view_form`
- Name: ir.model.view.form.inherit.data.merge
- Model: `ir.model`
- Type: inferred from arch
- Inherits: `base.view_model_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `hide_merge_action`, `is_merge_enabled`
- Buttons: `action_merge_contextual_disable`, `action_merge_contextual_enable`
- XPath or positional patches: 1

## Actions

- `ir_model_action_merge`: `act_window` Manual Merge

## Menus

- `ir_model_menu_merge_action_manager`: Manual Merge

## Navigation

- **Parent:** [[docs/Enterprise Addons/data_cleaning/Views]]

