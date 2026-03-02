<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Mexico - Electronic Delivery Guide

- Scope: Enterprise Addons
- Source: enterprise/l10n_mx_edi_stock
- Dependencies: [[docs/Community Addons/fleet/fleet|fleet]], [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Enterprise Addons/l10n_mx_edi_extended/l10n_mx_edi_extended|l10n_mx_edi_extended]], [[docs/Enterprise Addons/web_map/web_map|web_map]]

## XML Artifacts (detected)

- Views: 10
- Actions: 3
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `FleetVehicle`
- `l10n_mx_edi.customs.document.type`
- `l10n_mx_edi.customs.regime`
- `L10n_Mx_EdiDocument`
- `l10n_mx_edi.figure`
- `l10n_mx_edi.part`
- `l10n_mx_edi.hazardous.material`
- `l10n_mx_edi.trailer`
- `ProductUnspscCode`
- `ProductTemplate`
- `ResPartner`
- `StockMove`
- `StockMoveLine`
- `StockPicking`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Mexico - Electronic Delivery Guide - Models and Relations
class FleetVehicle
class "l10n_mx_edi.customs.document.type" as l10n_mx_edi_customs_document_type
class "l10n_mx_edi.customs.regime" as l10n_mx_edi_customs_regime
class L10n_Mx_EdiDocument
class "l10n_mx_edi.figure" as l10n_mx_edi_figure
class "l10n_mx_edi.part" as l10n_mx_edi_part
class "l10n_mx_edi.hazardous.material" as l10n_mx_edi_hazardous_material
class "l10n_mx_edi.trailer" as l10n_mx_edi_trailer
class ProductUnspscCode
class ProductTemplate
class ResPartner
class StockMove
class StockMoveLine
class StockPicking
FleetVehicle --|> l10n_mx_edi_trailer : one2many
FleetVehicle --|> l10n_mx_edi_figure : one2many
class "stock.picking" as stock_picking
L10n_Mx_EdiDocument --> stock_picking : many2one
class "fleet.vehicle" as fleet_vehicle
l10n_mx_edi_figure --> fleet_vehicle : many2one
class "res.partner" as res_partner
l10n_mx_edi_figure --> res_partner : many2one
l10n_mx_edi_figure .. l10n_mx_edi_part : many2many
l10n_mx_edi_trailer --> fleet_vehicle : many2one
ProductTemplate --> l10n_mx_edi_hazardous_material : many2one
class "l10n_mx_edi.document" as l10n_mx_edi_document
StockPicking --|> l10n_mx_edi_document : one2many
class "ir.attachment" as ir_attachment
StockPicking --> ir_attachment : many2one
StockPicking --> stock_picking : many2one
StockPicking --> fleet_vehicle : many2one
StockPicking .. l10n_mx_edi_customs_regime : many2many
StockPicking --> l10n_mx_edi_customs_document_type : many2one
StockPicking --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



