<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Delivery - Stock

- Scope: Community Addons
- Source: odoo/addons/stock_delivery
- Dependencies: [[docs/Community Addons/sale_stock/sale_stock|sale_stock]], [[docs/Community Addons/delivery/delivery|delivery]]

## XML Artifacts (detected)

- Views: 16
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 5

## Detected Models

- `DeliveryCarrier`
- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`
- `StockRoute`
- `StockMove`
- `StockMoveLine`
- `StockPackage`
- `StockPackageType`
- `StockPicking`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Delivery - Stock - Models and Relations
class DeliveryCarrier
class ProductTemplate
class SaleOrder
class SaleOrderLine
class StockRoute
class StockMove
class StockMoveLine
class StockPackage
class StockPackageType
class StockPicking
class "stock.route" as stock_route
DeliveryCarrier .. stock_route : many2many
class "res.country" as res_country
ProductTemplate --> res_country : many2one
class "delivery.carrier" as delivery_carrier
StockPicking .. delivery_carrier : many2many
StockPicking --> delivery_carrier : many2one
class "ir.attachment" as ir_attachment
StockPicking --|> ir_attachment : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





