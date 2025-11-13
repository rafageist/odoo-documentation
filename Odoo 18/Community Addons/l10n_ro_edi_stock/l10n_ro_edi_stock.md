<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Romania - E-Transport

- Version: v18
- Category: community
- Source: odoo/addons/l10n_ro_edi_stock
- Dependencies: [[Odoo 18/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 18/Community Addons/l10n_ro_edi/l10n_ro_edi|l10n_ro_edi]]
## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DeliveryCarrier`
- `L10nRoEdiStockDocument`
- `Picking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Romania - E-Transport - Models and Relations
class DeliveryCarrier
class L10nRoEdiStockDocument
class Picking
class "res.partner" as res_partner
DeliveryCarrier --> res_partner : many2one
class "stock.picking" as stock_picking
L10nRoEdiStockDocument --> stock_picking : many2one
class "l10n_ro_edi.document" as l10n_ro_edi_document
Picking --|> l10n_ro_edi_document : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
