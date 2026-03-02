<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/data_cleaning_record_views.xml

- Module: [[docs/Enterprise Addons/data_cleaning/data_cleaning|data_cleaning]]
- Scope: Enterprise Addons
- Source file: `views/data_cleaning_record_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_data_cleaning_record_search`
- Name: Field Cleaning Record Search
- Model: `data_cleaning.record`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `cleaning_model_id`
- XPath or positional patches: 0

### `view_data_cleaning_record_list`
- Name: Field Cleaning Record List
- Model: `data_cleaning.record`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `action`, `active`, `cleaning_model_id`, `current_value`, `field_id`, `name`, `res_id`, `res_model_name`, `suggested_value_display`
- Buttons: `action_discard`, `action_validate`
- XPath or positional patches: 0

## Actions

- `action_data_cleaning_record_notification`: `act_window` Field Cleaning Records
- `action_data_cleaning_record`: `act_window` Field Cleaning Records

## Navigation

- **Parent:** [[docs/Enterprise Addons/data_cleaning/Views]]

<!-- GENERATED:VIEWFILE -->
