<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk Stock

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_stock
- Dependencies: [[docs/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]], [[docs/Community Addons/stock/stock|stock]]

## Summary

Project, Tasks, Stock

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HelpdeskTicket`
- `StockPicking`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Helpdesk Stock - Models and Relations
class HelpdeskTicket
class StockPicking
class "product.product" as product_product
HelpdeskTicket --> product_product : many2one
HelpdeskTicket .. product_product : many2many
class "stock.lot" as stock_lot
HelpdeskTicket --> stock_lot : many2one
class "stock.picking" as stock_picking
HelpdeskTicket .. stock_picking : many2many
class "helpdesk.ticket" as helpdesk_ticket
StockPicking --> helpdesk_ticket : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




