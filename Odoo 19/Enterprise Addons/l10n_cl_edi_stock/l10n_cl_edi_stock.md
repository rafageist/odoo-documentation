<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Chile - E-Invoicing Delivery Guide

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_cl_edi_stock
- Dependencies: [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 19/Enterprise Addons/l10n_cl_edi/l10n_cl_edi|l10n_cl_edi]], [[Odoo 19/Community Addons/stock_account/stock_account|stock_account]]

## XML Artifacts (detected)

- Views: 3
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `L10n_ClEdiReference`
- `ResPartner`
- `StockMove`
- `stock.picking`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Chile - E-Invoicing Delivery Guide - Models and Relations
class AccountMove
class L10n_ClEdiReference
class ResPartner
class StockMove
class "stock.picking" as stock_picking
L10n_ClEdiReference --> stock_picking : many2one
class "l10n_latam.document.type" as l10n_latam_document_type
stock_picking --> l10n_latam_document_type : many2one
class "ir.attachment" as ir_attachment
stock_picking --> ir_attachment : many2one
stock_picking --> ir_attachment : many2one
class "l10n_cl.edi.reference" as l10n_cl_edi_reference
stock_picking --|> l10n_cl_edi_reference : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

