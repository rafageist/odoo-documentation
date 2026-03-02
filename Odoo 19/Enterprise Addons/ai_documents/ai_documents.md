<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# AI Documents

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/ai_documents
- Dependencies: [[Odoo 19/Enterprise Addons/ai/ai|ai]], [[Odoo 19/Enterprise Addons/documents/documents|documents]], [[Odoo 19/Community Addons/base_automation/base_automation|base_automation]]

## Summary

Automatically sort your documents.

## XML Artifacts (detected)

- Views: 4
- Actions: 4
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `BaseAutomation`
- `DocumentsDocument`
- `IrActionsServer`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title AI Documents - Models and Relations
class BaseAutomation
class DocumentsDocument
class IrActionsServer
class "documents.document" as documents_document
BaseAutomation --> documents_document : many2one
IrActionsServer --> documents_document : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

