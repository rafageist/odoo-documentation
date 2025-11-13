<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Master Production Schedule

- Version: v18
- Category: enterprise
- Source: enterprise18/mrp_mps
- Dependencies: [[Odoo 18/Community Addons/base_import/base_import|base_import]], [[Odoo 18/Community Addons/mrp/mrp|mrp]], [[Odoo 18/Community Addons/purchase_stock/purchase_stock|purchase_stock]]

## Summary

Master Production Schedule

## XML Artifacts (detected)

- Views: 8
- Actions: 2
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 5

## Detected Models

- `MrpBom`
- `mrp.production.schedule`
- `mrp.product.forecast`
- `ProductProduct`
- `ProductTemplate`
- `PurchaseOrder`
- `Company`
- `StockRule`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Master Production Schedule - Models and Relations
class MrpBom
class "mrp.production.schedule" as mrp_production_schedule
class "mrp.product.forecast" as mrp_product_forecast
class ProductProduct
class ProductTemplate
class PurchaseOrder
class Company
class StockRule
mrp_production_schedule --|> mrp_product_forecast : one2many
class "res.company" as res_company
mrp_production_schedule --> res_company : many2one
class "product.product" as product_product
mrp_production_schedule --> product_product : many2one
class "product.template" as product_template
mrp_production_schedule --> product_template : many2one
class "product.category" as product_category
mrp_production_schedule --> product_category : many2one
class "uom.uom" as uom_uom
mrp_production_schedule --> uom_uom : many2one
class "stock.warehouse" as stock_warehouse
mrp_production_schedule --> stock_warehouse : many2one
class "mrp.bom" as mrp_bom
mrp_production_schedule --> mrp_bom : many2one
mrp_product_forecast --> mrp_production_schedule : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
