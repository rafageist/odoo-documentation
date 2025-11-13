<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# India ENet Batch Payment CSV Generator

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_in_enet_batch_payment
- Dependencies: [[Odoo 18/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[Odoo 18/Community Addons/l10n_in/l10n_in|l10n_in]]

## Summary

Export batch payments as ENet files

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountBatchPayment`
- `AccountJournal`
- `AccountPayment`
- `AccountPaymentMethod`
- `enet.bank.template`
- `enet.template`
- `IrAttachment`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title India ENet Batch Payment CSV Generator - Models and Relations
class AccountBatchPayment
class AccountJournal
class AccountPayment
class AccountPaymentMethod
class "enet.bank.template" as enet_bank_template
class "enet.template" as enet_template
class IrAttachment
AccountJournal --> enet_bank_template : many2one
AccountJournal --|> enet_template : one2many
class "account.journal" as account_journal
enet_template --> account_journal : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
