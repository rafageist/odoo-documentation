<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk Repair

- Version: v18
- Category: enterprise
- Source: enterprise18/helpdesk_repair
- Dependencies: [[Odoo 18/Enterprise Addons/helpdesk_stock/helpdesk_stock|helpdesk_stock]], [[Odoo 18/Community Addons/repair/repair|repair]]

## Summary

Project, Tasks, Repair

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HelpdeskTicket`
- `Repair`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk Repair - Models and Relations
class HelpdeskTicket
class Repair
class "repair.order" as repair_order
HelpdeskTicket --|> repair_order : one2many
class "helpdesk.ticket" as helpdesk_ticket
Repair --> helpdesk_ticket : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
