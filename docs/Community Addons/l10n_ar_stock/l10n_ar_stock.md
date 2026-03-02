<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Argentinean - Stock

- Scope: Community Addons
- Source: odoo/addons/l10n_ar_stock
- Dependencies: [[docs/Community Addons/l10n_ar/l10n_ar|l10n_ar]], [[docs/Community Addons/stock_account/stock_account|stock_account]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





