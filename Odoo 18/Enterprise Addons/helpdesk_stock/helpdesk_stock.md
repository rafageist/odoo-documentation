<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk Stock

- Version: v18
- Category: enterprise
- Source: enterprise18/helpdesk_stock
- Dependencies: [[Odoo 18/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]], [[Odoo 18/Community Addons/stock/stock|stock]]

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
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
