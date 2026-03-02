<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# AI Documents Account

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/ai_documents_account
- Dependencies: [[Odoo 19/Enterprise Addons/ai_documents/ai_documents|ai_documents]], [[Odoo 19/Enterprise Addons/documents_account/documents_account|documents_account]]

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
!include ../../../Templates/DiagramStyles.puml
title AI Documents Account - Models and Relations
class DocumentsDocument
class IrActionsServer
class "res.company" as res_company
DocumentsDocument --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


