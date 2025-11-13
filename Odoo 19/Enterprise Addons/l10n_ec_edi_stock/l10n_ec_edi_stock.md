<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Ecuadorian Delivery Guide

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_ec_edi_stock
- Dependencies: [[Odoo 19/Community Addons/stock_account/stock_account|stock_account]], [[Odoo 19/Enterprise Addons/l10n_ec_edi/l10n_ec_edi|l10n_ec_edi]]
## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `IrAttachment`
- `StockPicking`
- `StockWarehouse`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Ecuadorian Delivery Guide - Models and Relations
class IrAttachment
class StockPicking
class StockWarehouse
class "res.partner" as res_partner
StockPicking --> res_partner : many2one
class "ir.sequence" as ir_sequence
StockWarehouse --> ir_sequence : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
