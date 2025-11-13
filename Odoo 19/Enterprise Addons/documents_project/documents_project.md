<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Documents - Projects

- Version: v19
- Category: enterprise
- Source: enterprise19/documents_project
- Dependencies: [[Odoo 19/Enterprise Addons/documents/documents|documents]], [[Odoo 19/Community Addons/project/project|project]]

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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
