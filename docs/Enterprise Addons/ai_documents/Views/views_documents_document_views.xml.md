<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/documents_document_views.xml

- Module: [[docs/Enterprise Addons/ai_documents/ai_documents|ai_documents]]
- Scope: Enterprise Addons
- Source file: `views/documents_document_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `documents_document_view_activity`
- Name: documents.document.view.activity.inherit.ai
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents.documents_view_activity`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `ai_sort_prompt`, `ai_sortable`
- XPath or positional patches: 1

### `documents_document_view_list`
- Name: documents.document.view.list.inherit.ai
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents.documents_view_list`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `ai_sort_prompt`, `ai_sortable`
- XPath or positional patches: 1

### `documents_document_view_kanban`
- Name: documents.document.view.kanban.inherit.ai
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents.document_view_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `ai_sort_prompt`, `ai_sortable`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/ai_documents/Views]]

<!-- GENERATED:VIEWFILE -->
