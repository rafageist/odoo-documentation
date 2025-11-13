<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Indian - TDS For Payment

- Version: v18
- Category: community
- Source: odoo/addons/l10n_in_withholding_payment
- Dependencies: [[Odoo 18/Community Addons/l10n_in_withholding/l10n_in_withholding|l10n_in_withholding]]
## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountPayment`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - TDS For Payment - Models and Relations
class AccountMove
class AccountPayment
class "account.payment" as account_payment
AccountMove --> account_payment : many2one
class "account.move" as account_move
AccountPayment --|> account_move : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
