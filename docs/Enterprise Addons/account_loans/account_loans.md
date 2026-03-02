<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Loans Management

- Scope: Enterprise Addons
- Source: enterprise/account_loans
- Dependencies: [[docs/Enterprise Addons/account_asset/account_asset|account_asset]], [[docs/Community Addons/base_import/base_import|base_import]]

## XML Artifacts (detected)

- Views: 15
- Actions: 4
- Menus: 2
- Rules (ir.rule): 2
- Access CSV entries: 6

## Detected Models

- `AccountAsset`
- `AccountAssetGroup`
- `AccountJournal`
- `account.loan`
- `account.loan.line`
- `AccountMove`
- `AccountReturn`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Loans Management - Models and Relations
class AccountAsset
class AccountAssetGroup
class AccountJournal
class "account.loan" as account_loan
class "account.loan.line" as account_loan_line
class AccountMove
class AccountReturn
AccountAssetGroup --|> account_loan : one2many
class "res.company" as res_company
account_loan --> res_company : many2one
class "account.account" as account_account
account_loan --> account_account : many2one
account_loan --> account_account : many2one
account_loan --> account_account : many2one
class "account.journal" as account_journal
account_loan --> account_journal : many2one
class "account.asset.group" as account_asset_group
account_loan --> account_asset_group : many2one
account_loan --|> account_loan_line : one2many
class "account.asset" as account_asset
account_loan --|> account_asset : one2many
account_loan_line --> account_loan : many2one
class "account.move" as account_move
account_loan_line --|> account_move : one2many
AccountMove --> account_loan_line : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




