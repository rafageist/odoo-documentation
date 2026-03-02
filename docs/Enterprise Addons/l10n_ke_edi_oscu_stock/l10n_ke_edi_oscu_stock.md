<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Kenya ETIMS EDI Stock Integration

- Scope: Enterprise Addons
- Source: enterprise/l10n_ke_edi_oscu_stock
- Dependencies: [[docs/Enterprise Addons/l10n_ke_edi_oscu/l10n_ke_edi_oscu|l10n_ke_edi_oscu]], [[docs/Community Addons/sale_management/sale_management|sale_management]], [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]

## Summary


            Kenya eTIMS Device EDI Stock Integration
        

## XML Artifacts (detected)

- Views: 12
- Actions: 2
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `l10n_ke_edi.customs.import`
- `ProductTemplate`
- `ProductProduct`
- `PurchaseOrder`
- `PurchaseOrderLine`
- `ResCompany`
- `StockMove`
- `StockPicking`
- `StockQuant`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Kenya ETIMS EDI Stock Integration - Models and Relations
class AccountMove
class AccountMoveLine
class "l10n_ke_edi.customs.import" as l10n_ke_edi_customs_import
class ProductTemplate
class ProductProduct
class PurchaseOrder
class PurchaseOrderLine
class ResCompany
class StockMove
class StockPicking
class StockQuant
class "res.country" as res_country
l10n_ke_edi_customs_import --> res_country : many2one
l10n_ke_edi_customs_import --> res_country : many2one
class "l10n_ke_edi_oscu.code" as l10n_ke_edi_oscu_code
l10n_ke_edi_customs_import --> l10n_ke_edi_oscu_code : many2one
l10n_ke_edi_customs_import --> l10n_ke_edi_oscu_code : many2one
class "uom.uom" as uom_uom
l10n_ke_edi_customs_import --> uom_uom : many2one
class "product.product" as product_product
l10n_ke_edi_customs_import --> product_product : many2one
class "res.company" as res_company
l10n_ke_edi_customs_import --> res_company : many2one
class "purchase.order" as purchase_order
l10n_ke_edi_customs_import --> purchase_order : many2one
class "res.partner" as res_partner
l10n_ke_edi_customs_import --> res_partner : many2one
PurchaseOrder --|> l10n_ke_edi_customs_import : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




