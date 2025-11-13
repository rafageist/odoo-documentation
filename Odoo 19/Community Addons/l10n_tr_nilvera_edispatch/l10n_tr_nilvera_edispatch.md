<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Türkiye - e-Irsaliye (e-Dispatch)

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_tr_nilvera_edispatch
- Dependencies: [[Odoo 19/Community Addons/l10n_tr_nilvera/l10n_tr_nilvera|l10n_tr_nilvera]], [[Odoo 19/Community Addons/stock/stock|stock]]
## XML Artifacts (detected)

- Views: 5
- Actions: 3
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `l10n_tr.nilvera.trailer.plate`
- `ResPartner`
- `StockPicking`
- `StockPickingType`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Türkiye - e-Irsaliye (e-Dispatch) - Models and Relations
class "l10n_tr.nilvera.trailer.plate" as l10n_tr_nilvera_trailer_plate
class ResPartner
class StockPicking
class StockPickingType
class "res.partner" as res_partner
StockPicking --> res_partner : many2one
StockPicking --> res_partner : many2one
StockPicking --> res_partner : many2one
StockPicking --> res_partner : many2one
StockPicking --> l10n_tr_nilvera_trailer_plate : many2one
StockPicking .. l10n_tr_nilvera_trailer_plate : many2many
StockPicking .. res_partner : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
