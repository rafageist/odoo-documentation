<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Kenya - Point of Sale

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_ke_edi_oscu_pos
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_ke_edi_oscu_stock/l10n_ke_edi_oscu_stock|l10n_ke_edi_oscu_stock]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
## XML Artifacts (detected)

- Views: 6
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `l10n_ke_edi_oscu.code`
- `PosConfig`
- `PosOrder`
- `PosSession`
- `ProductProduct`
- `ProductTemplate`
- `product.unspsc.code`
- `StockMove`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Kenya - Point of Sale - Models and Relations
class AccountMove
class "l10n_ke_edi_oscu.code" as l10n_ke_edi_oscu_code
class PosConfig
class PosOrder
class PosSession
class ProductProduct
class ProductTemplate
class "product.unspsc.code" as product_unspsc_code
class StockMove
class StockPicking
PosOrder --> l10n_ke_edi_oscu_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
