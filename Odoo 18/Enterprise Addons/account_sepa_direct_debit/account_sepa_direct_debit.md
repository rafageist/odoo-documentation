<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# SEPA Direct Debit

- Version: v18
- Category: enterprise
- Source: enterprise18/account_sepa_direct_debit
- Dependencies: [[Odoo 18/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 18/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[Odoo 18/Community Addons/account/account|account]]

## Summary

Collect payments from your customers through SEPA direct debit.

## XML Artifacts (detected)

- Views: 18
- Actions: 4
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 4

## Detected Models

- `AccountBatchPayment`
- `AccountMove`
- `AccountJournal`
- `AccountPartialReconcile`
- `AccountPayment`
- `AccountPaymentMethod`
- `ResCompany`
- `Partner`
- `ResPartnerBank`
- `sdd.mandate`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title SEPA Direct Debit - Models and Relations
class AccountBatchPayment
class AccountMove
class AccountJournal
class AccountPartialReconcile
class AccountPayment
class AccountPaymentMethod
class ResCompany
class Partner
class ResPartnerBank
class "sdd.mandate" as sdd_mandate
class "account.payment" as account_payment
AccountBatchPayment --|> account_payment : one2many
AccountPayment --> sdd_mandate : many2one
Partner --|> sdd_mandate : one2many
class "res.partner" as res_partner
sdd_mandate --> res_partner : many2one
sdd_mandate --> res_partner : many2one
class "res.company" as res_company
sdd_mandate --> res_company : many2one
class "res.partner.bank" as res_partner_bank
sdd_mandate --> res_partner_bank : many2one
class "account.move" as account_move
sdd_mandate --|> account_move : one2many
sdd_mandate --|> account_payment : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
