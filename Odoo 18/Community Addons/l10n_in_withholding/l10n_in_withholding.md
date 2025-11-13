<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Indian - TDS and TCS

- Version: v18
- Category: community
- Source: odoo/addons/l10n_in_withholding
- Dependencies: [[Odoo 18/Community Addons/l10n_in/l10n_in|l10n_in]]
## XML Artifacts (detected)

- Views: 10
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `AccountAccount`
- `AccountMove`
- `AccountMoveLine`
- `AccountPayment`
- `AccountTax`
- `l10n_in.section.alert`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - TDS and TCS - Models and Relations
class AccountAccount
class AccountMove
class AccountMoveLine
class AccountPayment
class AccountTax
class "l10n_in.section.alert" as l10n_in_section_alert
class ResCompany
AccountAccount --> l10n_in_section_alert : many2one
class "account.move" as account_move
AccountMove --> account_move : many2one
AccountMove --|> account_move : one2many
class "account.move.line" as account_move_line
AccountMove --|> account_move_line : one2many
AccountTax --> l10n_in_section_alert : many2one
class "account.tax" as account_tax
l10n_in_section_alert --|> account_tax : one2many
class "account.account" as account_account
ResCompany --> account_account : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
