<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk After Sales

- Version: v18
- Category: enterprise
- Source: enterprise18/helpdesk_sale
- Dependencies: [[Odoo 18/Enterprise Addons/helpdesk/helpdesk|helpdesk]], [[Odoo 18/Community Addons/sale_management/sale_management|sale_management]]

## Summary

Project, Tasks, After Sales

## XML Artifacts (detected)

- Views: 6
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HelpdeskTeam`
- `HelpdeskTicket`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk After Sales - Models and Relations
class HelpdeskTeam
class HelpdeskTicket
class "sale.order" as sale_order
HelpdeskTicket --> sale_order : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
