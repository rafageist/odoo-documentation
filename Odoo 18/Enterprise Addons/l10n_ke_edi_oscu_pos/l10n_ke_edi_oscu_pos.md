<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Kenya - Point of Sale

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_ke_edi_oscu_pos
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_ke_edi_oscu_stock/l10n_ke_edi_oscu_stock|l10n_ke_edi_oscu_stock]], [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
## XML Artifacts (detected)

- Views: 6
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `L10nKeOSCUCode`
- `PosConfig`
- `PosOrder`
- `PosSession`
- `ProductProduct`
- `ProductTemplate`
- `ProductCode`
- `StockMove`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Kenya - Point of Sale - Models and Relations
class AccountMove
class L10nKeOSCUCode
class PosConfig
class PosOrder
class PosSession
class ProductProduct
class ProductTemplate
class ProductCode
class StockMove
class StockPicking
class "l10n_ke_edi_oscu.code" as l10n_ke_edi_oscu_code
PosOrder --> l10n_ke_edi_oscu_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
