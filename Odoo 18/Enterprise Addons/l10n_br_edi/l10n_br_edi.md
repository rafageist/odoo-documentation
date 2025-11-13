<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Brazilian Accounting EDI

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_br_edi
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_br_avatax/l10n_br_avatax|l10n_br_avatax]]
## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `PaymentMethod`
- `ResCountry`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Brazilian Accounting EDI - Models and Relations
class AccountMove
class PaymentMethod
class ResCountry
class "res.partner" as res_partner
AccountMove --> res_partner : many2one
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
