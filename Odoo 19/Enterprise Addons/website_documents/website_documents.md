<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Website Documents

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/website_documents
- Dependencies: [[Odoo 19/Enterprise Addons/documents/documents|documents]], [[Odoo 19/Community Addons/website/website|website]]

## Summary

Choose the website on which documents/folder are shared

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DocumentsDocument`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website Documents - Models and Relations
class DocumentsDocument
class website
DocumentsDocument --> website : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

