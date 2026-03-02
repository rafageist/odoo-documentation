
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# EFT Batch Payment

- Scope: Enterprise Addons
- Source: enterprise/l10n_nz_eft
- Dependencies: [[docs/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[docs/Community Addons/l10n_nz/l10n_nz|l10n_nz]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

