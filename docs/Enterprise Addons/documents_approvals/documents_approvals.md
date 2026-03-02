<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Documents - Approvals

- Scope: Enterprise Addons
- Source: enterprise/documents_approvals
- Dependencies: [[docs/Enterprise Addons/documents/documents|documents]], [[docs/Enterprise Addons/approvals/approvals|approvals]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



