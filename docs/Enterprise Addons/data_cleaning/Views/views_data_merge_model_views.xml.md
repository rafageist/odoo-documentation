---
tags: [odoo, enterprise, generated, views]
---

# views/data_merge_model_views.xml

- Module: [[docs/Enterprise Addons/data_cleaning/data_cleaning|data_cleaning]]
- Scope: Enterprise Addons
- Source file: `views/data_merge_model_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `data_merge_model_view_search`
- Name: data_merge.model.search
- Model: `data_merge.model`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_data_merge_model_form`
- Name: Deduplication Model Form
- Model: `data_merge.model`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `active`, `create_threshold`, `custom_merge_method`, `domain`, `field_id`, `match_mode`, `merge_mode`, `merge_threshold`, `mix_by_company`, `name`, and 9 more
- Buttons: `action_find_duplicates`, `open_records`
- XPath or positional patches: 0

### `view_data_merge_model_list`
- Name: Deduplication Model List
- Model: `data_merge.model`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `active`, `merge_mode`, `name`, `res_model_id`
- XPath or positional patches: 0

## Actions

- `action_data_merge_config`: `act_window` Deduplication Rules

## Navigation

- **Parent:** [[docs/Enterprise Addons/data_cleaning/Views]]

