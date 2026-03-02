<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Withholding Tax on Payment

- Scope: Community Addons
- Source: odoo/addons/l10n_account_withholding_tax
- Dependencies: [[docs/Community Addons/account/account|account]]

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountPayment`
- `account.payment.withholding.line`
- `AccountTax`
- `ProductTemplate`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Withholding Tax on Payment - Models and Relations
class AccountPayment
class "account.payment.withholding.line" as account_payment_withholding_line
class AccountTax
class ProductTemplate
class ResCompany
AccountPayment --|> account_payment_withholding_line : one2many
class "account.payment" as account_payment
account_payment_withholding_line --> account_payment : many2one
class "ir.sequence" as ir_sequence
AccountTax --> ir_sequence : many2one
class "account.account" as account_account
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





