<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/documents_document_views.xml

- Module: [[docs/Enterprise Addons/documents/documents|documents]]
- Scope: Enterprise Addons
- Source file: `views/documents_document_views.xml`
- Views: 10
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `documents_view_list_portal`
- Name: documents.document.list.portal
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents_view_list`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `documents_view_kanban_portal`
- Name: documents.document kanban portal
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `document_view_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `documents_view_activity`
- Name: documents.document activity
- Model: `documents.document`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 25
- Sample fields: `access_token`, `access_url`, `active`, `alias_domain_id`, `alias_email`, `alias_name`, `alias_tag_ids`, `attachment_id`, `company_id`, `file_size`, and 15 more
- XPath or positional patches: 0

### `documents_view_list_add_documents_attachment`
- Name: add documents attachment
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents_view_list_main`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 2

### `documents_view_list`
- Name: documents list
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents_view_list_main`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `activity_exception_decoration`, `create_date`
- XPath or positional patches: 1

### `documents_view_list_main`
- Name: documents list
- Model: `documents.document`
- Type: inferred from arch
- Root tag: `list`
- Field references: 36
- Sample fields: `access_token`, `access_url`, `active`, `alias_domain_id`, `alias_email`, `alias_name`, `alias_tag_ids`, `attachment_id`, `available_embedded_actions_ids`, `company_id`, and 26 more
- XPath or positional patches: 0

### `documents_upload_url_view`
- Name: upload url
- Model: `documents.document`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `folder_id`, `name`, `tag_ids`, `url`, `url_preview_image`
- XPath or positional patches: 0

### `document_view_form_rename`
- Name: Rename form
- Model: `documents.document`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `document_view_kanban`
- Name: documents.document kanban
- Model: `documents.document`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 45
- Sample fields: `access_internal`, `access_token`, `access_url`, `access_via_link`, `active`, `activity_ids`, `activity_state`, `alias_domain_id`, `alias_name`, `alias_tag_ids`, and 35 more
- XPath or positional patches: 0

### `document_view_search`
- Name: Document search view
- Model: `documents.document`
- Type: inferred from arch
- Root tag: `search`
- Field references: 9
- Sample fields: `access_ids`, `create_uid`, `index_content`, `name`, `owner_id`, `partner_id`, `tag_ids`, `type`, `user_folder_id`
- XPath or positional patches: 0

## Actions

- `document_action_portal`: `act_window` Documents
- `document_action`: `act_window` Documents
- `document_action_preference`: `client` Documents View Preference
- `action_url_form`: `act_window` Add Url

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents/Views]]

<!-- GENERATED:VIEWFILE -->
