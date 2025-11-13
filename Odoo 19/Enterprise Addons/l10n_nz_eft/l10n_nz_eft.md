<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# EFT Batch Payment

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_nz_eft
- Dependencies: [[Odoo 19/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[Odoo 19/Community Addons/l10n_nz/l10n_nz|l10n_nz]]

## Summary

Export payments as EFT files

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountBatchPayment`
- `AccountJournal`
- `AccountPayment`
- `AccountPaymentMethod`
- `AccountPaymentMethodLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title EFT Batch Payment - Models and Relations
class AccountBatchPayment
class AccountJournal
class AccountPayment
class AccountPaymentMethod
class AccountPaymentMethodLine
class "res.partner.bank" as res_partner_bank
AccountBatchPayment --> res_partner_bank : many2one
AccountPayment .. res_partner_bank : many2many
AccountPayment --> res_partner_bank : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
