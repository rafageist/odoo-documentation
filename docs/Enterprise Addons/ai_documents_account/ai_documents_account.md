<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# AI Documents Account

- Scope: Enterprise Addons
- Source: enterprise/ai_documents_account
- Dependencies: [[docs/Enterprise Addons/ai_documents/ai_documents|ai_documents]], [[docs/Enterprise Addons/documents_account/documents_account|documents_account]]

## Summary

AI Documents Account

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DocumentsDocument`
- `IrActionsServer`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title AI Documents Account - Models and Relations
class DocumentsDocument
class IrActionsServer
class "res.company" as res_company
DocumentsDocument --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





