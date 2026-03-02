<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Romania - E-Transport Batch Pickings

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_ro_edi_stock_batch
- Dependencies: [[Odoo 19/Community Addons/l10n_ro_edi_stock/l10n_ro_edi_stock|l10n_ro_edi_stock]], [[Odoo 19/Community Addons/stock_picking_batch/stock_picking_batch|stock_picking_batch]]

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `L10nRoEdiStockDocument`
- `Picking`
- `StockPickingBatch`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Romania - E-Transport Batch Pickings - Models and Relations
class L10nRoEdiStockDocument
class Picking
class StockPickingBatch
class "stock.picking.batch" as stock_picking_batch
L10nRoEdiStockDocument --> stock_picking_batch : many2one
class "l10n_ro_edi.document" as l10n_ro_edi_document
StockPickingBatch --|> l10n_ro_edi_document : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


