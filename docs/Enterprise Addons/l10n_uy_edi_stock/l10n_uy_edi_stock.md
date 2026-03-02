<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Uruguay - E-Remitos

- Scope: Enterprise Addons
- Source: enterprise/l10n_uy_edi_stock
- Dependencies: [[docs/Enterprise Addons/l10n_uy_edi/l10n_uy_edi|l10n_uy_edi]], [[docs/Community Addons/stock_account/stock_account|stock_account]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



