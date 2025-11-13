<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Documents - Approvals

- Version: v19
- Category: enterprise
- Source: enterprise19/documents_approvals
- Dependencies: [[Odoo 19/Enterprise Addons/documents/documents|documents]], [[Odoo 19/Enterprise Addons/approvals/approvals|approvals]]

## Summary

Approval from documents

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `approval.request`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Approvals - Models and Relations
class "approval.request" as approval_request
class ResCompany
class "documents.document" as documents_document
ResCompany --> documents_document : many2one
class "documents.tag" as documents_tag
ResCompany .. documents_tag : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
