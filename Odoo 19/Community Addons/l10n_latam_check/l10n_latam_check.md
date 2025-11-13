<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Third Party and Deferred/Electronic Checks Management

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_latam_check
- Dependencies: [[Odoo 19/Community Addons/account/account|account]], [[Odoo 19/Community Addons/base_vat/base_vat|base_vat]]

## Summary

Checks Management

## XML Artifacts (detected)

- Views: 11
- Actions: 3
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `AccountPayment`
- `AccountPaymentMethod`
- `l10n_latam.check`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Third Party and Deferred/Electronic Checks Management - Models and Relations
class AccountJournal
class AccountMove
class AccountMoveLine
class AccountPayment
class AccountPaymentMethod
class "l10n_latam.check" as l10n_latam_check
AccountMoveLine --|> l10n_latam_check : one2many
AccountPayment --|> l10n_latam_check : one2many
AccountPayment .. l10n_latam_check : many2many
class "account.payment" as account_payment
l10n_latam_check --> account_payment : many2one
l10n_latam_check .. account_payment : many2many
class "account.journal" as account_journal
l10n_latam_check --> account_journal : many2one
class "res.bank" as res_bank
l10n_latam_check --> res_bank : many2one
class "account.move.line" as account_move_line
l10n_latam_check --> account_move_line : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
