<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Ecuadorian Delivery Guide

- Scope: Enterprise Addons
- Source: enterprise/l10n_ec_edi_stock
- Dependencies: [[docs/Community Addons/stock_account/stock_account|stock_account]], [[docs/Enterprise Addons/l10n_ec_edi/l10n_ec_edi|l10n_ec_edi]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




