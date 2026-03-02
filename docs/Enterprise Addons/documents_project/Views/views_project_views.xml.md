<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/project_views.xml

- Module: [[docs/Enterprise Addons/documents_project/documents_project|documents_project]]
- Scope: Enterprise Addons
- Source file: `views/project_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `project_view_kanban_inherit_documents`
- Name: project.kanban.inherit.documents
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `edit_project_document_form_inherit`
- Name: project.project.form.inherit
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.edit_project`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `documents_folder_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents_project/Views]]

<!-- GENERATED:VIEWFILE -->
