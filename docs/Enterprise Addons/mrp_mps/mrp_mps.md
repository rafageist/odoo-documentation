<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Master Production Schedule

- Scope: Enterprise Addons
- Source: enterprise/mrp_mps
- Dependencies: [[docs/Community Addons/base_import/base_import|base_import]], [[docs/Community Addons/mrp/mrp|mrp]], [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]

## Summary

Master Production Schedule

## XML Artifacts (detected)

- Views: 8
- Actions: 2
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 6

## Detected Models

- `MrpBom`
- `mrp.production.schedule`
- `mrp.product.forecast`
- `ProductProduct`
- `ProductTemplate`
- `PurchaseOrder`
- `ResCompany`
- `StockRule`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Master Production Schedule - Models and Relations
class MrpBom
class "mrp.production.schedule" as mrp_production_schedule
class "mrp.product.forecast" as mrp_product_forecast
class ProductProduct
class ProductTemplate
class PurchaseOrder
class ResCompany
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



