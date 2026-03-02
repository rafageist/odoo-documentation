
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk After Sales

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_sale
- Dependencies: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]], [[docs/Community Addons/sale_management/sale_management|sale_management]]

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
!include ../../../templates/DiagramStyles.puml
title Helpdesk After Sales - Models and Relations
class HelpdeskTeam
class HelpdeskTicket
class "sale.order" as sale_order
HelpdeskTicket --> sale_order : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

