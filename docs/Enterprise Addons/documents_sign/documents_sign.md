<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Documents - Signatures

- Scope: Enterprise Addons
- Source: enterprise/documents_sign
- Dependencies: [[docs/Enterprise Addons/documents/documents|documents]], [[docs/Enterprise Addons/sign/sign|sign]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



