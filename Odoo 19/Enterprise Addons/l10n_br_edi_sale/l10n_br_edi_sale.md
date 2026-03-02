<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Brazilian Accounting EDI For Sale

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_br_edi_sale
- Dependencies: [[Odoo 19/Enterprise Addons/sale_external_tax/sale_external_tax|sale_external_tax]], [[Odoo 19/Enterprise Addons/l10n_br_edi/l10n_br_edi|l10n_br_edi]]

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
!include ../../../Templates/DiagramStyles.puml
title Brazilian Accounting EDI For Sale - Models and Relations
class SaleOrder
class "res.partner" as res_partner
SaleOrder --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

