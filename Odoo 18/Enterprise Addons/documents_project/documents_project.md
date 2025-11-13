<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Documents - Projects

- Version: v18
- Category: enterprise
- Source: enterprise18/documents_project
- Dependencies: [[Odoo 18/Enterprise Addons/documents/documents|documents]], [[Odoo 18/Community Addons/project/project|project]]

## Summary

Project from documents

## XML Artifacts (detected)

- Views: 5
- Actions: 20
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Document`
- `DocumentsTag`
- `IrAttachment`
- `project.project`
- `project.task`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Projects - Models and Relations
class Document
class DocumentsTag
class IrAttachment
class "project.project" as project_project
class "project.task" as project_task
Document --> project_project : many2one
Document --> project_task : many2one
Document --|> project_project : one2many
class "documents.document" as documents_document
IrAttachment --|> documents_document : one2many
project_project --> documents_document : many2one
class "documents.tag" as documents_tag
project_project .. documents_tag : many2many
project_project --|> documents_document : one2many
project_task --|> documents_document : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
