<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/data_recycle_model_views.xml

- Module: [[docs/Community Addons/data_recycle/data_recycle|data_recycle]]
- Scope: Community Addons
- Source file: `views/data_recycle_model_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_data_merge_model_form`
- Name: Field Recyle Model Form
- Model: `data_recycle.model`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `active`, `domain`, `include_archived`, `name`, `notify_frequency`, `notify_frequency_period`, `notify_user_ids`, `records_to_recycle_count`, `recycle_action`, `recycle_mode`, and 5 more
- Buttons: `action_recycle_records`, `open_records`
- XPath or positional patches: 0

### `view_data_recycle_model_list`
- Name: Field Recyle Model List
- Model: `data_recycle.model`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `active`, `name`, `recycle_action`, `recycle_mode`, `res_model_id`
- XPath or positional patches: 0

## Actions

- `action_data_recycle_config`: `act_window` Recyle Records Rules

## Navigation

- **Parent:** [[docs/Community Addons/data_recycle/Views]]

<!-- GENERATED:VIEWFILE -->
