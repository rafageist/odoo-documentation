<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Brazilian Accounting EDI

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_br_edi
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_br_avatax/l10n_br_avatax|l10n_br_avatax]]

## XML Artifacts (detected)

- Views: 7
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `L10n_BrOperationType`
- `PaymentMethod`
- `ResCountry`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Brazilian Accounting EDI - Models and Relations
class AccountMove
class AccountMoveLine
class L10n_BrOperationType
class PaymentMethod
class ResCountry
class "res.partner" as res_partner
AccountMove --> res_partner : many2one
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

