<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk Sale Loyalty

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_sale_loyalty
- Dependencies: [[docs/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]], [[docs/Community Addons/sale_loyalty/sale_loyalty|sale_loyalty]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





