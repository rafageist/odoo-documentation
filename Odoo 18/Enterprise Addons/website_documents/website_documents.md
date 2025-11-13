<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Website Documents

- Version: v18
- Category: enterprise
- Source: enterprise18/website_documents
- Dependencies: [[Odoo 18/Enterprise Addons/documents/documents|documents]], [[Odoo 18/Community Addons/website/website|website]]

## Summary

Choose the website on which documents/folder are shared

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `documents.document`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Documents - Models and Relations
class "documents.document" as documents_document
class website
documents_document --> website : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
