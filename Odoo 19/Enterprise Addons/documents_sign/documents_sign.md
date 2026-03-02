<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Documents - Signatures

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/documents_sign
- Dependencies: [[Odoo 19/Enterprise Addons/documents/documents|documents]], [[Odoo 19/Enterprise Addons/sign/sign|sign]]

## Summary

Signature templates from Documents

## XML Artifacts (detected)

- Views: 4
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `DocumentsDocument`
- `sign.document`
- `sign.request`
- `SignRequestItem`
- `sign.template`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Signatures - Models and Relations
class DocumentsDocument
class "sign.document" as sign_document
class "sign.request" as sign_request
class SignRequestItem
class "sign.template" as sign_template
class "documents.document" as documents_document
sign_template --> documents_document : many2one
class "documents.tag" as documents_tag
sign_template .. documents_tag : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

