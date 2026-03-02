<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Avatax Brazil Sale

- Scope: Enterprise Addons
- Source: enterprise/l10n_br_avatax_sale
- Dependencies: [[docs/Enterprise Addons/l10n_br_avatax/l10n_br_avatax|l10n_br_avatax]], [[docs/Community Addons/sale/sale|sale]]

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
!include ../../../templates/DiagramStyles.puml
title Avatax Brazil Sale - Models and Relations
class SaleOrder
class SaleOrderLine
class "l10n_br.operation.type" as l10n_br_operation_type
SaleOrderLine --> l10n_br_operation_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



