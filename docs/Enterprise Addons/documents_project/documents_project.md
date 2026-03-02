<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Documents - Projects

- Scope: Enterprise Addons
- Source: enterprise/documents_project
- Dependencies: [[docs/Enterprise Addons/documents/documents|documents]], [[docs/Community Addons/project/project|project]]

## Summary

Project from documents

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DocumentsDocument`
- `DocumentsTag`
- `IrAttachment`
- `project.project`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Documents - Projects - Models and Relations
class DocumentsDocument
class DocumentsTag
class IrAttachment
class "project.project" as project_project
class ResCompany
DocumentsDocument --|> project_project : one2many
class "documents.document" as documents_document
project_project --> documents_document : many2one
project_project --|> documents_document : one2many
ResCompany --> documents_document : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




