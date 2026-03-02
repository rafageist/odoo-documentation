<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Helpdesk Sale Loyalty

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/helpdesk_sale_loyalty
- Dependencies: [[Odoo 19/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]], [[Odoo 19/Community Addons/sale_loyalty/sale_loyalty|sale_loyalty]]

## Summary

Project, Tasks, Sale Loyalty

## XML Artifacts (detected)

- Views: 4
- Actions: 3
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
class "loyalty.program" as loyalty_program
HelpdeskTicket --> loyalty_program : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


