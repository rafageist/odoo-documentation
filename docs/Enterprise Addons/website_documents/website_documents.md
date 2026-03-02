<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Website Documents

- Scope: Enterprise Addons
- Source: enterprise/website_documents
- Dependencies: [[docs/Enterprise Addons/documents/documents|documents]], [[docs/Community Addons/website/website|website]]

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
!include ../../../templates/DiagramStyles.puml
title Website Documents - Models and Relations
class DocumentsDocument
class website
DocumentsDocument --> website : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




