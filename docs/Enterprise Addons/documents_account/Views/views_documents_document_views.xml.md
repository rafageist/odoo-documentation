<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/documents_document_views.xml

- Module: [[docs/Enterprise Addons/documents_account/documents_account|documents_account]]
- Scope: Enterprise Addons
- Source file: `views/documents_document_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `documents_document_view_activity`
- Name: documents.document.view.activity.inherit.account
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents.documents_view_activity`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `has_embedded_pdf`
- XPath or positional patches: 1

### `documents_document_view_tree`
- Name: documents.document.view.list.inherit.account
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents.documents_view_list`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `has_embedded_pdf`
- XPath or positional patches: 1

### `documents_document_view_kanban`
- Name: documents.document.view.kanban.inherit.account
- Model: `documents.document`
- Type: inferred from arch
- Inherits: `documents.document_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `has_embedded_pdf`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents_account/Views]]

<!-- GENERATED:VIEWFILE -->
