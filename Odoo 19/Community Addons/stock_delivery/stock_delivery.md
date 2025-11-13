<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Delivery - Stock

- Version: v19
- Category: community
- Source: odoo19/addons/stock_delivery
- Dependencies: [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 19/Community Addons/delivery/delivery|delivery]]
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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
