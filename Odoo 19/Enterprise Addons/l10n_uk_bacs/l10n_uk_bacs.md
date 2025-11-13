<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# UK BACS Payment Files

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_uk_bacs
- Dependencies: [[Odoo 19/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[Odoo 19/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 19/Community Addons/l10n_uk/l10n_uk|l10n_uk]]

## Summary

Export payments as BACS Direct Debit and Direct Credit files

## XML Artifacts (detected)

- Views: 7
- Actions: 2
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountBatchPayment`
- `AccountJournal`
- `AccountMove`
- `AccountPayment`
- `AccountPaymentMethod`
- `bacs.ddi`
- `ResCompany`
- `ResPartnerBank`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title UK BACS Payment Files - Models and Relations
class AccountBatchPayment
class AccountJournal
class AccountMove
class AccountPayment
class AccountPaymentMethod
class "bacs.ddi" as bacs_ddi
class ResCompany
class ResPartnerBank
AccountMove --> bacs_ddi : many2one
AccountPayment --> bacs_ddi : many2one
class "res.partner" as res_partner
bacs_ddi --> res_partner : many2one
class "res.company" as res_company
bacs_ddi --> res_company : many2one
class "res.partner.bank" as res_partner_bank
bacs_ddi --> res_partner_bank : many2one
class "account.journal" as account_journal
bacs_ddi --> account_journal : many2one
class "account.payment" as account_payment
bacs_ddi --|> account_payment : one2many
class "account.move" as account_move
bacs_ddi --|> account_move : one2many
bacs_ddi .. account_journal : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
