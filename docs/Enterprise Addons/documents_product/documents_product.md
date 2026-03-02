<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Documents - Product

- Scope: Enterprise Addons
- Source: enterprise/documents_product
- Dependencies: [[docs/Enterprise Addons/documents/documents|documents]], [[docs/Community Addons/product/product|product]]

## Summary

Products from Documents

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DocumentsDocument`
- `product.product`
- `product.template`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Documents - Product - Models and Relations
class DocumentsDocument
class "product.product" as product_product
class "product.template" as product_template
class ResCompany
DocumentsDocument --> product_template : many2one
DocumentsDocument --> product_product : many2one
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



