<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Mexico - Electronic Delivery Guide

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_mx_edi_stock
- Dependencies: [[Odoo 18/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 18/Enterprise Addons/l10n_mx_edi/l10n_mx_edi|l10n_mx_edi]], [[Odoo 18/Enterprise Addons/l10n_mx_edi_extended/l10n_mx_edi_extended|l10n_mx_edi_extended]], [[Odoo 18/Enterprise Addons/web_map/web_map|web_map]]
## XML Artifacts (detected)

- Views: 13
- Actions: 5
- Menus: 4
- Rules (ir.rule): 0
- Access CSV entries: 7

## Detected Models

- `l10n_mx_edi.customs.document.type`
- `l10n_mx_edi.customs.regime`
- `L10nMxEdiDocument`
- `l10n_mx_edi.hazardous.material`
- `l10n_mx_edi.vehicle`
- `l10n_mx_edi.figure`
- `l10n_mx_edi.part`
- `l10n_mx_edi.trailer`
- `ProductCode`
- `ProductTemplate`
- `Partner`
- `StockMove`
- `StockMoveLine`
- `Picking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mexico - Electronic Delivery Guide - Models and Relations
class "l10n_mx_edi.customs.document.type" as l10n_mx_edi_customs_document_type
class "l10n_mx_edi.customs.regime" as l10n_mx_edi_customs_regime
class L10nMxEdiDocument
class "l10n_mx_edi.hazardous.material" as l10n_mx_edi_hazardous_material
class "l10n_mx_edi.vehicle" as l10n_mx_edi_vehicle
class "l10n_mx_edi.figure" as l10n_mx_edi_figure
class "l10n_mx_edi.part" as l10n_mx_edi_part
class "l10n_mx_edi.trailer" as l10n_mx_edi_trailer
class ProductCode
class ProductTemplate
class Partner
class StockMove
class StockMoveLine
class Picking
class "stock.picking" as stock_picking
L10nMxEdiDocument --> stock_picking : many2one
l10n_mx_edi_vehicle --|> l10n_mx_edi_trailer : one2many
l10n_mx_edi_vehicle --|> l10n_mx_edi_figure : one2many
l10n_mx_edi_figure --> l10n_mx_edi_vehicle : many2one
class "res.partner" as res_partner
l10n_mx_edi_figure --> res_partner : many2one
l10n_mx_edi_figure .. l10n_mx_edi_part : many2many
l10n_mx_edi_trailer --> l10n_mx_edi_vehicle : many2one
ProductTemplate --> l10n_mx_edi_hazardous_material : many2one
class "l10n_mx_edi.document" as l10n_mx_edi_document
Picking --|> l10n_mx_edi_document : one2many
class "ir.attachment" as ir_attachment
Picking --> ir_attachment : many2one
Picking --> stock_picking : many2one
Picking --> l10n_mx_edi_vehicle : many2one
Picking .. l10n_mx_edi_customs_regime : many2many
Picking --> l10n_mx_edi_customs_document_type : many2one
Picking --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
