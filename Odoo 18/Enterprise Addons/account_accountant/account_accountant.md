<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Invoicing

- Version: v18
- Category: enterprise
- Source: enterprise18/account_accountant
- Dependencies: [[Odoo 18/Community Addons/account/account|account]], [[Odoo 18/Enterprise Addons/mail_enterprise/mail_enterprise|mail_enterprise]], [[Odoo 18/Community Addons/web_tour/web_tour|web_tour]]

## Summary

Invoices, Payments, Follow-ups & Bank synchronization (Enterprise)

## XML Artifacts (detected)

- Views: 31
- Actions: 11
- Menus: 5
- Rules (ir.rule): 0
- Access CSV entries: 11

## Detected Models

- `AccountAccount`
- `account.bank.statement`
- `AccountBankStatementLine`
- `account.fiscal.year`
- `account_journal`
- `AccountMove`
- `account.move.line`
- `AccountPayment`
- `AccountReconcileModel`
- `AccountReconcileModelLine`
- `AccountTax`
- `bank.rec.widget`
- `bank.rec.widget.line`
- `Digest`
- `IrModel`
- `IrUiMenu`
- `ResCompany`
- `ResCurrency`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Invoicing - Models and Relations
class AccountAccount
class "account.bank.statement" as account_bank_statement
class AccountBankStatementLine
class "account.fiscal.year" as account_fiscal_year
class account_journal
class AccountMove
class "account.move.line" as account_move_line
class AccountPayment
class AccountReconcileModel
class AccountReconcileModelLine
class AccountTax
class "bank.rec.widget" as bank_rec_widget
class "bank.rec.widget.line" as bank_rec_widget_line
class Digest
class IrModel
class IrUiMenu
class ResCompany
class ResCurrency
class "res.company" as res_company
account_fiscal_year --> res_company : many2one
class "account.move" as account_move
AccountMove .. account_move : many2many
AccountMove .. account_move : many2many
class "res.users" as res_users
AccountMove --> res_users : many2one
class "ir.attachment" as ir_attachment
account_move_line --|> ir_attachment : one2many
class "account.bank.statement.line" as account_bank_statement_line
bank_rec_widget --> account_bank_statement_line : many2one
class "res.currency" as res_currency
bank_rec_widget --> res_currency : many2one
bank_rec_widget --> res_currency : many2one
class "res.partner" as res_partner
bank_rec_widget --> res_partner : many2one
bank_rec_widget --|> bank_rec_widget_line : one2many
class "account.reconcile.model" as account_reconcile_model
bank_rec_widget .. account_reconcile_model : many2many
bank_rec_widget --> account_reconcile_model : many2one
bank_rec_widget --> res_company : many2one
bank_rec_widget .. account_move_line : many2many
bank_rec_widget_line --> bank_rec_widget : many2one
class "account.account" as account_account
bank_rec_widget_line --> account_account : many2one
bank_rec_widget_line --> res_partner : many2one
bank_rec_widget_line --> res_currency : many2one
bank_rec_widget_line --> account_move_line : many2one
bank_rec_widget_line --> account_move : many2one
class "account.tax.repartition.line" as account_tax_repartition_line
bank_rec_widget_line --> account_tax_repartition_line : many2one
class "account.tax" as account_tax
bank_rec_widget_line .. account_tax : many2many
class "account.account.tag" as account_account_tag
bank_rec_widget_line .. account_account_tag : many2many
bank_rec_widget_line --> account_tax : many2one
bank_rec_widget_line --> account_reconcile_model : many2one
bank_rec_widget_line --> res_currency : many2one
bank_rec_widget_line --> account_account : many2one
bank_rec_widget_line --> account_account : many2one
ResCompany --> res_users : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
ResCompany --> account_account : many2one
ResCompany --> account_journal : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
