<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Delivery - Stock

- Version: v18
- Category: community
- Source: odoo/addons/stock_delivery
- Dependencies: [[Odoo 18/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 18/Community Addons/delivery/delivery|delivery]]
## XML Artifacts (detected)

- Views: 16
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `DeliveryCarrier`
- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`
- `StockRoute`
- `StockMove`
- `StockMoveLine`
- `PackageType`
- `StockPicking`
- `StockQuantPackage`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Delivery - Stock - Models and Relations
class DeliveryCarrier
class ProductTemplate
class SaleOrder
class SaleOrderLine
class StockRoute
class StockMove
class StockMoveLine
class PackageType
class StockPicking
class StockQuantPackage
class "stock.route" as stock_route
DeliveryCarrier .. stock_route : many2many
class "res.country" as res_country
ProductTemplate --> res_country : many2one
class "delivery.carrier" as delivery_carrier
StockPicking --> delivery_carrier : many2one
class "ir.attachment" as ir_attachment
StockPicking --|> ir_attachment : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
