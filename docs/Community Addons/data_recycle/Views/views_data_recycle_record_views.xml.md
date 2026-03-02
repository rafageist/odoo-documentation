<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/data_recycle_record_views.xml

- Module: [[docs/Community Addons/data_recycle/data_recycle|data_recycle]]
- Scope: Community Addons
- Source file: `views/data_recycle_record_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_data_recycle_record_search`
- Name: Field Recycle Record Search
- Model: `data_recycle.record`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `recycle_model_id`
- XPath or positional patches: 0

### `view_data_recycle_record_list`
- Name: Field Recycle Record List
- Model: `data_recycle.record`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `active`, `name`, `recycle_model_id`, `res_id`, `res_model_name`
- Buttons: `action_discard`, `action_validate`
- XPath or positional patches: 0

## Actions

- `action_data_recycle_record_notification`: `act_window` Field Recycle Records
- `action_data_recycle_record`: `act_window` Field Recycle Records

## Navigation

- **Parent:** [[docs/Community Addons/data_recycle/Views]]

<!-- GENERATED:VIEWFILE -->
