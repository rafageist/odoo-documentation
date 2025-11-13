<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Account Transfers

- Version: v19
- Category: enterprise
- Source: enterprise19/account_transfer
- Dependencies: [[Odoo 19/Enterprise Addons/account_accountant/account_accountant|account_accountant]]
## XML Artifacts (detected)

- Views: 4
- Actions: 2
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 6

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `account.transfer.model`
- `account.transfer.model.line`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Account Transfers - Models and Relations
class AccountJournal
class AccountMove
class AccountMoveLine
class "account.transfer.model" as account_transfer_model
class "account.transfer.model.line" as account_transfer_model_line
AccountMove --> account_transfer_model : many2one
class "account.journal" as account_journal
account_transfer_model --> account_journal : many2one
class "res.company" as res_company
account_transfer_model --> res_company : many2one
class "account.account" as account_account
account_transfer_model .. account_account : many2many
account_transfer_model --|> account_transfer_model_line : one2many
class "account.move" as account_move
account_transfer_model --|> account_move : one2many
account_transfer_model_line --> account_transfer_model : many2one
account_transfer_model_line --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
