<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/documents_folder_views.xml

- Module: [[docs/Enterprise Addons/documents/documents|documents]]
- Scope: Enterprise Addons
- Source file: `views/documents_folder_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `folder_deletion_form`
- Name: Folder Deletion
- Model: `documents.document`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `deletion_delay`
- Buttons: `action_archive`
- XPath or positional patches: 0

### `document_view_form_new_folder`
- Name: New Folder form
- Model: `documents.document`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `active`, `name`, `type`
- XPath or positional patches: 0

## Actions

- `action_folder_form`: `act_window` Add Folder

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents/Views]]

<!-- GENERATED:VIEWFILE -->
