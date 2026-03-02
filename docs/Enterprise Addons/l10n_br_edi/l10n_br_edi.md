<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Brazilian Accounting EDI

- Scope: Enterprise Addons
- Source: enterprise/l10n_br_edi
- Dependencies: [[docs/Enterprise Addons/l10n_br_avatax/l10n_br_avatax|l10n_br_avatax]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



