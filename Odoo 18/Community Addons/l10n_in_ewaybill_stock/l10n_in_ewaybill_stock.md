<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Indian - E-waybill Stock

- Version: v18
- Category: community
- Source: odoo/addons/l10n_in_ewaybill_stock
- Dependencies: [[Odoo 18/Community Addons/l10n_in_stock/l10n_in_stock|l10n_in_stock]], [[Odoo 18/Community Addons/l10n_in_edi_ewaybill/l10n_in_edi_ewaybill|l10n_in_edi_ewaybill]]
## XML Artifacts (detected)

- Views: 3
- Actions: 2
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `l10n.in.ewaybill`
- `StockMove`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - E-waybill Stock - Models and Relations
class "l10n.in.ewaybill" as l10n_in_ewaybill
class StockMove
class StockPicking
class "stock.picking" as stock_picking
l10n_in_ewaybill --> stock_picking : many2one
class "res.company" as res_company
l10n_in_ewaybill --> res_company : many2one
class "res.partner" as res_partner
l10n_in_ewaybill --> res_partner : many2one
l10n_in_ewaybill --> res_partner : many2one
l10n_in_ewaybill --> res_partner : many2one
l10n_in_ewaybill --> res_partner : many2one
class "account.fiscal.position" as account_fiscal_position
l10n_in_ewaybill --> account_fiscal_position : many2one
class "l10n.in.ewaybill.type" as l10n_in_ewaybill_type
l10n_in_ewaybill --> l10n_in_ewaybill_type : many2one
l10n_in_ewaybill --> res_partner : many2one
class "account.tax" as account_tax
StockMove .. account_tax : many2many
StockPicking --|> l10n_in_ewaybill : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
