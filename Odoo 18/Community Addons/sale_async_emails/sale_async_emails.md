<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Sales - Async Emails

- Version: v18
- Category: community
- Source: odoo/addons/sale_async_emails
- Dependencies: [[Odoo 18/Community Addons/sale/sale|sale]]

## Summary

Send order status emails asynchronously

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SaleOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales - Async Emails - Models and Relations
class SaleOrder
class "mail.template" as mail_template
SaleOrder --> mail_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
