<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Assets Management

- Version: v18
- Category: enterprise
- Source: enterprise18/account_asset
- Dependencies: [[Odoo 18/Enterprise Addons/account_reports/account_reports|account_reports]]
## XML Artifacts (detected)

- Views: 14
- Actions: 6
- Menus: 4
- Rules (ir.rule): 2
- Access CSV entries: 6

## Detected Models

- `AccountAccount`
- `account.asset`
- `AssetsReport`
- `account.asset.group`
- `AccountMove`
- `AccountMoveLine`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Assets Management - Models and Relations
class AccountAccount
class "account.asset" as account_asset
class AssetsReport
class "account.asset.group" as account_asset_group
class AccountMove
class AccountMoveLine
class ResCompany
AccountAccount .. account_asset : many2many
class "res.company" as res_company
account_asset --> res_company : many2one
class "res.currency" as res_currency
account_asset --> res_currency : many2one
class "account.account" as account_account
account_asset --> account_account : many2one
account_asset --> account_asset_group : many2one
account_asset --> account_account : many2one
account_asset --> account_account : many2one
class "account.journal" as account_journal
account_asset --> account_journal : many2one
class "account.move" as account_move
account_asset --|> account_move : one2many
class "account.move.line" as account_move_line
account_asset .. account_move_line : many2many
account_asset --> account_asset : many2one
account_asset --> account_asset : many2one
account_asset --|> account_asset : one2many
account_asset --|> account_asset : one2many
account_asset_group --> res_company : many2one
account_asset_group --|> account_asset : one2many
AccountMove --> account_asset : many2one
AccountMove --|> account_asset : one2many
AccountMoveLine .. account_asset : many2many
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
