<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Indonesia - Point of Sale

- Scope: Community Addons
- Source: odoo/addons/l10n_id_pos
- Dependencies: [[docs/Community Addons/l10n_id/l10n_id|l10n_id]], [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PosOrder`
- `PosPaymentMethod`
- `L10n_IdQrisTransaction`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Indonesia - Point of Sale - Models and Relations
class PosOrder
class PosPaymentMethod
class L10n_IdQrisTransaction
class "l10n_id.qris.transaction" as l10n_id_qris_transaction
PosOrder .. l10n_id_qris_transaction : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





