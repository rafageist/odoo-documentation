<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Helpdesk Stock

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/helpdesk_stock
- Dependencies: [[Odoo 19/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]], [[Odoo 19/Community Addons/stock/stock|stock]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

