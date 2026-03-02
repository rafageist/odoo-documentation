<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Helpdesk After Sales

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/helpdesk_sale
- Dependencies: [[Odoo 19/Enterprise Addons/helpdesk/helpdesk|helpdesk]], [[Odoo 19/Community Addons/sale_management/sale_management|sale_management]]

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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

