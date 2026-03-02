<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Helpdesk Repair

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/helpdesk_repair
- Dependencies: [[Odoo 19/Enterprise Addons/helpdesk_stock/helpdesk_stock|helpdesk_stock]], [[Odoo 19/Community Addons/repair/repair|repair]]

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
- `RepairOrder`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk Repair - Models and Relations
class HelpdeskTicket
class RepairOrder
class "repair.order" as repair_order
HelpdeskTicket --|> repair_order : one2many
class "helpdesk.ticket" as helpdesk_ticket
RepairOrder --> helpdesk_ticket : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

