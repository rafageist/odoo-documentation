<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Online Bank Statement Synchronization

- Version: v18
- Category: enterprise
- Source: enterprise18/account_online_synchronization
- Dependencies: [[Odoo 18/Enterprise Addons/account_accountant/account_accountant|account_accountant]]

## Summary

This module is used for Online bank synchronization.

## XML Artifacts (detected)

- Views: 12
- Actions: 1
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 11

## Detected Models

- `AccountBankStatementLine`
- `AccountJournal`
- `account.online.account`
- `account.online.link`
- `BankRecWidget`
- `ResCompany`
- `MailActivityType`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Online Bank Statement Synchronization - Models and Relations
class AccountBankStatementLine
class AccountJournal
class "account.online.account" as account_online_account
class "account.online.link" as account_online_link
class BankRecWidget
class ResCompany
class MailActivityType
class ResPartner
AccountBankStatementLine --> account_online_account : many2one
AccountBankStatementLine --> account_online_link : many2one
AccountJournal --> account_online_account : many2one
AccountJournal --> account_online_link : many2one
account_online_account --> account_online_link : many2one
class "account.journal" as account_journal
account_online_account --|> account_journal : one2many
class "res.company" as res_company
account_online_account --> res_company : many2one
class "res.currency" as res_currency
account_online_account --> res_currency : many2one
account_online_link --|> account_online_account : one2many
account_online_link --> res_company : many2one
account_online_link --|> account_journal : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
