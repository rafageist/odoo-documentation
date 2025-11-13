<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Product Email Template

- Version: v18
- Category: community
- Source: odoo/addons/product_email_template
- Dependencies: [[Odoo 18/Community Addons/account/account|account]]
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
!include ../../../Templates/DiagramStyles.puml
title Product Email Template - Models and Relations
class AccountMove
class ProductTemplate
class "mail.template" as mail_template
ProductTemplate --> mail_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
