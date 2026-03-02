<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# AI Documents

- Scope: Enterprise Addons
- Source: enterprise/ai_documents
- Dependencies: [[docs/Enterprise Addons/ai/ai|ai]], [[docs/Enterprise Addons/documents/documents|documents]], [[docs/Community Addons/base_automation/base_automation|base_automation]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




