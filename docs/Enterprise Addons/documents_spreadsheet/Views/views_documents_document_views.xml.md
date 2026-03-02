<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/documents_document_views.xml

- Module: [[docs/Enterprise Addons/documents_spreadsheet/documents_spreadsheet|documents_spreadsheet]]
- Scope: Enterprise Addons
- Source file: `views/documents_document_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `document_view_search_spreadsheet`
- Name: unnamed
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents.document_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `documents_document_view_list`
- Name: documents.document.view.list
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents.documents_view_list`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `handler`
- XPath or positional patches: 1

### `spreadsheet_document_view_kanban`
- Name: spreadsheet.documents.document.kanban
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents.document_view_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `handler`, `spreadsheet_thumbnail_checksum`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents_spreadsheet/Views]]

<!-- GENERATED:VIEWFILE -->
