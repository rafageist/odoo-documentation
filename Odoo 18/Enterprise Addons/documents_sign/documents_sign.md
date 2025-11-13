<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Documents - Signatures

- Version: v18
- Category: enterprise
- Source: enterprise18/documents_sign
- Dependencies: [[Odoo 18/Enterprise Addons/documents/documents|documents]], [[Odoo 18/Enterprise Addons/sign/sign|sign]]

## Summary

Signature templates from Documents

## XML Artifacts (detected)

- Views: 2
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DocumentsDocument`
- `ResCompany`
- `sign.request`
- `sign.request.item`
- `sign.template`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Signatures - Models and Relations
class DocumentsDocument
class ResCompany
class "sign.request" as sign_request
class "sign.request.item" as sign_request_item
class "sign.template" as sign_template
class "documents.document" as documents_document
ResCompany --> documents_document : many2one
sign_template --> documents_document : many2one
class "documents.tag" as documents_tag
sign_template .. documents_tag : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
