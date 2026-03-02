<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Uruguay - E-Remitos

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_uy_edi_stock
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_uy_edi/l10n_uy_edi|l10n_uy_edi]], [[Odoo 19/Community Addons/stock_account/stock_account|stock_account]], [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]]

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `L10nLatamDocumentType`
- `L10nUyEdiDocument`
- `StockMove`
- `StockPicking`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Uruguay - E-Remitos - Models and Relations
class L10nLatamDocumentType
class L10nUyEdiDocument
class StockMove
class StockPicking
class "stock.picking" as stock_picking
L10nUyEdiDocument --> stock_picking : many2one
class "l10n_uy_edi.addenda" as l10n_uy_edi_addenda
StockMove .. l10n_uy_edi_addenda : many2many
class "l10n_latam.document.type" as l10n_latam_document_type
StockPicking --> l10n_latam_document_type : many2one
StockPicking .. l10n_latam_document_type : many2many
class "l10n_uy_edi.document" as l10n_uy_edi_document
StockPicking --> l10n_uy_edi_document : many2one
StockPicking .. l10n_uy_edi_addenda : many2many
StockPicking --> l10n_uy_edi_document : many2one
class "ir.attachment" as ir_attachment
StockPicking --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

