<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Avatax Brazil Sale

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_br_avatax_sale
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_br_avatax/l10n_br_avatax|l10n_br_avatax]], [[Odoo 19/Community Addons/sale/sale|sale]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Avatax Brazil Sale - Models and Relations
class SaleOrder
class SaleOrderLine
class "l10n_br.operation.type" as l10n_br_operation_type
SaleOrderLine --> l10n_br_operation_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
