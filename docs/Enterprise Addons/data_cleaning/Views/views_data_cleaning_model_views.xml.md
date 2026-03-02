<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/data_cleaning_model_views.xml

- Module: [[docs/Enterprise Addons/data_cleaning/data_cleaning|data_cleaning]]
- Scope: Enterprise Addons
- Source file: `views/data_cleaning_model_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_data_cleaning_model_form`
- Name: Field Cleaning Model Form
- Model: `data_cleaning.model`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `action_display`, `active`, `cleaning_mode`, `field_id`, `name`, `notify_frequency`, `notify_frequency_period`, `notify_user_ids`, `records_to_clean_count`, `res_model_id`, and 3 more
- Buttons: `action_clean_records`, `open_records`
- XPath or positional patches: 0

### `view_data_cleaning_model_list`
- Name: Field Cleaning Model List
- Model: `data_cleaning.model`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `active`, `cleaning_mode`, `name`, `res_model_id`
- XPath or positional patches: 0

## Actions

- `action_data_cleaning_config`: `act_window` Field Cleaning Rules

## Navigation

- **Parent:** [[docs/Enterprise Addons/data_cleaning/Views]]

<!-- GENERATED:VIEWFILE -->
