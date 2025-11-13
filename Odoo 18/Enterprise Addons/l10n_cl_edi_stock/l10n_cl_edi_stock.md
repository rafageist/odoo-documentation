<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Chile - E-Invoicing Delivery Guide

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_cl_edi_stock
- Dependencies: [[Odoo 18/Community Addons/sale_stock/sale_stock|sale_stock]], [[Odoo 18/Enterprise Addons/l10n_cl_edi/l10n_cl_edi|l10n_cl_edi]], [[Odoo 18/Community Addons/stock_account/stock_account|stock_account]]
## XML Artifacts (detected)

- Views: 3
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `ResPartner`
- `stock.picking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Chile - E-Invoicing Delivery Guide - Models and Relations
class AccountMove
class ResPartner
class "stock.picking" as stock_picking
class "l10n_latam.document.type" as l10n_latam_document_type
stock_picking --> l10n_latam_document_type : many2one
class "ir.attachment" as ir_attachment
stock_picking --> ir_attachment : many2one
stock_picking --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
