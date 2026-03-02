<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# report/data_storage_views.xml

- Module: [[docs/Enterprise Addons/data_cleaning/data_cleaning|data_cleaning]]
- Scope: Enterprise Addons
- Source file: `report/data_storage_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_data_storage_attachment_tree`
- Name: Storage Detail
- Model: `ir.attachment`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `file_size`, `name`
- XPath or positional patches: 0

### `view_data_storage_search`
- Name: Data Cleaning Storage Search
- Model: `ir.attachment.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `res_id`, `res_model`
- XPath or positional patches: 0

### `view_data_storage_tree`
- Name: Storage
- Model: `ir.attachment.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `res_id`, `res_model`, `size`
- Buttons: `action_attachment_detail`
- XPath or positional patches: 0

## Actions

- `action_data_storage`: `act_window` Storage

## Navigation

- **Parent:** [[docs/Enterprise Addons/data_cleaning/Views]]

<!-- GENERATED:VIEWFILE -->
