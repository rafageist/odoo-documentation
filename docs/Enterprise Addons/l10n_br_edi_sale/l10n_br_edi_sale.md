<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Brazilian Accounting EDI For Sale

- Scope: Enterprise Addons
- Source: enterprise/l10n_br_edi_sale
- Dependencies: [[docs/Enterprise Addons/sale_external_tax/sale_external_tax|sale_external_tax]], [[docs/Enterprise Addons/l10n_br_edi/l10n_br_edi|l10n_br_edi]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SaleOrder`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Brazilian Accounting EDI For Sale - Models and Relations
class SaleOrder
class "res.partner" as res_partner
SaleOrder --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



