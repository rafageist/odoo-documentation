<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Argentinean - Stock

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_ar_stock
- Dependencies: [[Odoo 19/Community Addons/l10n_ar/l10n_ar|l10n_ar]], [[Odoo 19/Community Addons/stock_account/stock_account|stock_account]]

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `StockPicking`
- `StockPickingType`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Argentinean - Stock - Models and Relations
class StockPicking
class StockPickingType
class "l10n_latam.document.type" as l10n_latam_document_type
StockPickingType --> l10n_latam_document_type : many2one
class "ir.sequence" as ir_sequence
StockPickingType --> ir_sequence : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


