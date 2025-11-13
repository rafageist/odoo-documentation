<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Indonesia - Point of Sale

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_id_pos
- Dependencies: [[Odoo 19/Community Addons/l10n_id/l10n_id|l10n_id]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
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
!include ../../../Templates/DiagramStyles.puml
title Indonesia - Point of Sale - Models and Relations
class PosOrder
class PosPaymentMethod
class L10n_IdQrisTransaction
class "l10n_id.qris.transaction" as l10n_id_qris_transaction
PosOrder .. l10n_id_qris_transaction : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
