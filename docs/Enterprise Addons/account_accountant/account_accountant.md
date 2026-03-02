<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Invoicing

- Scope: Enterprise Addons
- Source: enterprise/account_accountant
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Enterprise Addons/mail_enterprise/mail_enterprise|mail_enterprise]], [[docs/Community Addons/web_tour/web_tour|web_tour]]

## Summary

Invoices, Payments, Follow-ups & Bank synchronization (Enterprise)

## XML Artifacts (detected)

- Views: 33
- Actions: 14
- Menus: 5
- Rules (ir.rule): 0
- Access CSV entries: 8

## Detected Models

- `AccountAccount`
- `account.bank.statement`
- `account.bank.statement.line`
- `account.fiscal.year`
- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `AccountPayment`
- `AccountReconcileModel`
- `AccountReconcileModelLine`
- `AccountTax`
- `DigestDigest`
- `IrUiMenu`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Invoicing - Models and Relations
class AccountAccount
class "account.bank.statement" as account_bank_statement
class "account.bank.statement.line" as account_bank_statement_line
class "account.fiscal.year" as account_fiscal_year
class AccountJournal
class AccountMove
class AccountMoveLine
class AccountPayment
class AccountReconcileModel
class AccountReconcileModelLine
class AccountTax
class DigestDigest
class IrUiMenu
class ResCompany
class "ir.attachment" as ir_attachment
account_bank_statement_line --|> ir_attachment : one2many
account_bank_statement_line --|> ir_attachment : one2many
class "res.company" as res_company
account_fiscal_year --> res_company : many2one
class "account.move" as account_move
AccountMove .. account_move : many2many
AccountMove .. account_move : many2many
class "res.users" as res_users
AccountMove --> res_users : many2one
AccountMoveLine --|> ir_attachment : one2many
ResCompany --> res_users : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_journal : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




