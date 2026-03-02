<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/data_merge_record_views.xml

- Module: [[docs/Enterprise Addons/data_cleaning/data_cleaning|data_cleaning]]
- Scope: Enterprise Addons
- Source file: `views/data_merge_record_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `data_merge_record_view_search_merge_action`
- Name: Deduplication Record Search
- Model: `data_merge.record`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `model_id`
- XPath or positional patches: 0

### `view_data_merge_record_search`
- Name: Deduplication Record Search
- Model: `data_merge.record`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `model_id`
- XPath or positional patches: 0

### `view_data_merge_record_list`
- Name: Deduplication Record List
- Model: `data_merge.record`
- Type: inferred from arch
- Root tag: `list`
- Field references: 14
- Sample fields: `active`, `differences`, `field_values`, `group_id`, `is_deleted`, `is_master`, `name`, `record_create_date`, `record_create_uid`, `record_write_date`, and 4 more
- Buttons: `discard_records`, `merge_records`
- XPath or positional patches: 0

## Actions

- `action_data_merge_record_notification`: `act_window` Duplicates
- `action_data_merge_record`: `act_window` Duplicates

## Navigation

- **Parent:** [[docs/Enterprise Addons/data_cleaning/Views]]

<!-- GENERATED:VIEWFILE -->
