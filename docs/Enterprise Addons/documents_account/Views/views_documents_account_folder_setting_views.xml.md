---
tags: [odoo, enterprise, generated, views]
---

# views/documents_account_folder_setting_views.xml

- Module: [[docs/Enterprise Addons/documents_account/documents_account|documents_account]]
- Scope: Enterprise Addons
- Source file: `views/documents_account_folder_setting_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `documents_folder_setting_view_form`
- Name: documents folder setting form view
- Model: `documents.account.folder.setting`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `company_id`, `folder_id`, `journal_id`, `tag_ids`
- XPath or positional patches: 0

### `documents_folder_setting_view_list`
- Name: documents folder setting list view
- Model: `documents.account.folder.setting`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `folder_id`, `journal_id`, `tag_ids`
- XPath or positional patches: 0

## Actions

- `action_folder_settings_installer`: `act_window` Journals to synchronize

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents_account/Views]]

