<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Product Email Template

- Scope: Community Addons
- Source: odoo/addons/product_email_template
- Dependencies: [[docs/Community Addons/account/account|account]]

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `ProductTemplate`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Product Email Template - Models and Relations
class AccountMove
class ProductTemplate
class "mail.template" as mail_template
ProductTemplate --> mail_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





