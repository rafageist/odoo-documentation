<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk Sale Loyalty

- Version: v18
- Category: enterprise
- Source: enterprise18/helpdesk_sale_loyalty
- Dependencies: [[Odoo 18/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]], [[Odoo 18/Community Addons/sale_loyalty/sale_loyalty|sale_loyalty]]

## Summary

Project, Tasks, Sale Loyalty

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 5

## Detected Models

- `HelpdeskTicket`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk Sale Loyalty - Models and Relations
class HelpdeskTicket
class "loyalty.card" as loyalty_card
HelpdeskTicket .. loyalty_card : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
